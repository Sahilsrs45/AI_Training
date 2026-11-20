import json
import sqlglot
from sqlglot import exp
from crewai.tools import tool
from database.sql_database import get_connection
 
 
def validate_sql(query: str) -> str:
    statements = sqlglot.parse(
        query.strip(),
        read="mysql"
    )
 
    if len(statements) != 1:
        raise ValueError("Only one SQL statement allowed")
 
    statement = statements[0]
 
    if not isinstance(statement, exp.Select):
        raise ValueError("Only SELECT queries allowed")
 
    if statement.find(exp.Into):
        raise ValueError("SELECT INTO is not allowed")
 
    # Reject nested statements and unsupported operations
    forbidden = (
        exp.Insert, exp.Update, exp.Delete,
        exp.Drop, exp.Create, exp.Alter,
        exp.Command, exp.Union, exp.Subquery,
        exp.With, exp.Join, exp.Lock
    )
 
    for node in statement.walk():
        if isinstance(node, forbidden):
            raise ValueError("Unsupported SQL operation")
 
    tables = list(statement.find_all(exp.Table))
 
    if len(tables) != 1:
        raise ValueError("Exactly one table required")
 
    if tables[0].name.lower() != "employees":
        raise ValueError("Only employees table allowed")
 
    if tables[0].db or tables[0].catalog:
        raise ValueError("Qualified table names not allowed")
 
    allowed_columns = {
        "employee_id", "employee_name",
        "department", "salary", "city"
    }
 
    for col in statement.find_all(exp.Column):
        if col.name.lower() not in allowed_columns:
            raise ValueError("Invalid column: " + col.name)
 
    # Disallow functions other than these aggregates
    for func in statement.find_all(exp.Func):
        if not isinstance(
            func, (exp.Count, exp.Sum, exp.Avg,
                   exp.Min, exp.Max)
        ):
            raise ValueError("Unsupported SQL function")
 
    return statement.sql(dialect="mysql")
 
 
@tool("execute_employee_sql")
def execute_employee_sql(query: str) -> str:
    """Execute a validated read-only employee SQL query."""
 
    try:
        safe_query = validate_sql(query)
 
        connection = get_connection()
 
        try:
            cursor = connection.cursor(dictionary=True)
 
            try:
                cursor.execute(
                    "SET SESSION MAX_EXECUTION_TIME=5000"
                )
                cursor.execute(
                    "SET TRANSACTION READ ONLY"
                )
                cursor.execute(
                    "START TRANSACTION READ ONLY"
                )
                cursor.execute(safe_query)
 
                rows = cursor.fetchmany(101)
 
                if len(rows) > 100:
                    return json.dumps({
                        "status": "failed",
                        "message": "Result exceeds 100 rows"
                    })
 
                return json.dumps({
                    "status": "success",
                    "rows": rows
                }, default=str)
 
            finally:
                connection.rollback()
                cursor.close()
 
        finally:
            connection.close()
 
    except Exception as error:
        return json.dumps({
            "status": "failed",
            "message": str(error)
        })