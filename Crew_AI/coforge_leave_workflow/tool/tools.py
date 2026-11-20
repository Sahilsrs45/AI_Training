import json
from crewai.tools import tool
 
employees = [
    {
        "employee_id":101,
        "employee_name":"Hitesh Patwal",
        "leave_balance":12
    },
    {
        "employee_id":102,
        "employee_name":"Sahil",
        "leave_balance":13
    },
    {
        "employee_id":103,
        "employee_name":"Prince kumar",
        "leave_balance":15
    },
    {
        "employee_id":104,
        "employee_name":"shiv",
        "leave_balance":16
    }
]


@tool("check_level_balance")
def check_leave_balance(employee_id:int)->str:
    """Find an employee and return their leave balance."""
    
    for employee in employees:
        if employee["employee_id"]==employee_id:
            return json.dumps(employee)
        
    return json.dumps({
        "status":"not_found",
        "message":"Employee does not exist"
    })    