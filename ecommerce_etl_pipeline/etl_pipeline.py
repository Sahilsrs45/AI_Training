# data engineering ->
from pathlib import Path
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
 
# project folder locations
BASE_DIR= Path(__file__).resolve().parent  #BASE_DIR is the path object . __file__ = gives location of currently executing py file      
print(f"Base Directory: {BASE_DIR}")
 
DATA_DIR=BASE_DIR/"data"
REPORT_DIR=BASE_DIR/"reports"
DATABASE_DIR=BASE_DIR/"database"
 
print(f"Data Directory: {DATA_DIR}")
print(f"Report Directory: {REPORT_DIR}")
print(f"Database Directory: {DATABASE_DIR}")
 
DATABASE_PATH=DATABASE_DIR/"ecommerce_warehouse.db"
print(f"Database Path: {DATABASE_PATH}")
 
# create required folders
def create_folder() -> None:
    """Create report and database folders if they do not exist."""
 
    REPORT_DIR.mkdir(exist_ok=True)
    DATABASE_DIR.mkdir(exist_ok=True)
 
# create_folder() -> creates folder because we called this function
 
# Extract
def extract_data() -> tuple[
    pd.DataFrame,
    pd.DataFrame,
    pd.DataFrame,
    pd.DataFrame
]:
    """Read Data from csv files."""
 
    customers=pd.read_csv(DATA_DIR/"customers.csv",encoding="utf-8-sig")
    orders=pd.read_csv(DATA_DIR/"orders.csv",encoding="utf-8-sig")
    deliveries=pd.read_csv(DATA_DIR/"deliveries.csv",encoding="utf-8-sig")
    payments=pd.read_csv(DATA_DIR/"payments.csv",encoding="utf-8-sig")
 
    # clean all columns
    for dataframe in [
        customers,orders,deliveries,payments
    ]:
        dataframe.columns=(
            dataframe.columns.astype(str).str.replace("\ufeff","",regex=False)
            .str.strip()
            .str.lower()
        )
 
    print("Customer columns: ", customers.columns.tolist())
    print("Order columns: ", orders.columns.tolist())
    print("Payment columns: ", payments.columns.tolist())
    print("Delivery columns: ", deliveries.columns.tolist())
 
    return customers,orders,payments,deliveries
extract_data()
 
# transform : clean customer data
def clean_customers(customers: pd.DataFrame) -> pd.DataFrame:
    """Remove Duplicates customers and clean customer fields"""
 
    customers=customers.copy()
 
    customers=customers.drop_duplicates(
        subset=["customer_id"]
    )
 
    customers["customer_name"]=(
        customers["customer_name"].fillna("Unknown Customer")
        .astype(str)
        .str.strip()
        .str.title()
    )
 
    customers["email"]=(
        customers["email"].fillna("unknown@gmail.com")
        .astype(str)
        .str.strip()
        .str.title()
    )
 
    customers["city"]=(
        customers["city"].fillna("Unknown")
        .astype(str)
        .str.strip()
        .str.title()
    )
 
    return customers
 
# transform : clean deliveries data
def clean_deliveries(deliveries: pd.DataFrame) -> pd.DataFrame:
    """Remove Duplicates customers and clean customer fields"""
 
    deliveries=deliveries.copy()
 
    deliveries=deliveries.drop_duplicates(
        subset=["delivery_id"]
    )
 
    deliveries["delivery_status"]=(
        deliveries["delivery_status"].fillna("Unknown")
        .astype(str)
        .str.strip()
        .str.title()
    )
 
    deliveries["delivery_city"]=(
        deliveries["delivery_city"].fillna("Unknown")
        .astype(str)
        .str.strip()
        .str.title()
    )
 
    return deliveries
 
# transform : clean Orders data
def clean_orders(orders: pd.DataFrame) -> pd.DataFrame:
    """Remove Duplicates customers and clean customer fields"""
 
    orders=orders.copy()
 
    orders=orders.drop_duplicates(
        subset=["order_id"]
    )
 
    orders["product_name"]=(
        orders["product_name"].fillna("Unknown")
        .astype(str)
        .str.strip()
        .str.title()
    )
 
    orders["quantity"]=pd.to_numeric(
        orders["quantity"],
        errors="coerce"
    ).fillna(0)
 
    orders["unit_price"]=pd.to_numeric(
        orders["unit_price"],
        errors="coerce"
    ).fillna(0)
 
    orders["order_date"]=pd.to_datetime(
        orders["order_date"],
        errors="coerce"
    )
 
    orders["total_amount"]=(
        orders["quantity"] * orders["unit_price"]
    )
 
    return orders
 
# transform : clean payments data
def clean_payments(payments: pd.DataFrame) -> pd.DataFrame:
    """Remove Duplicates customers and clean customer fields"""
 
    payments=payments.copy()
 
    payments=payments.drop_duplicates(
        subset=["payment_id"]
    )
 
    payments["payment_status"]=(
        payments["payment_status"].fillna("Unknown")
        .astype(str)
        .str.strip()
        .str.title()
    )
 
    payments["payment_method"]=(
        payments["payment_method"].fillna("Unknown")
        .astype(str)
        .str.strip()
        .str.title()
    )
 
    payments["payment_date"]=pd.to_datetime(
        payments["payment_date"],
        errors="coerce"
    )
 
    return payments

def join_data(
    customers: pd.DataFrame,
    orders: pd.DataFrame,
    payments: pd.DataFrame,
    deliveries: pd.DataFrame
) -> pd.DataFrame:

    combined_data = orders.merge(
        customers,
        on = "customer_id",
        how = "left"
    )

    combined_data = combined_data.merge(
        payments,
        on="order_id",
        how="left"
    )

    combined_data = combined_data.merge(
        deliveries,
        on="order_id",
        how="left"
    )

    combined_data["customer_name"] = (
        combined_data["customer_name"]
        .fillna("Unknown customer")
    )

    combined_data["city"] = (
            combined_data["city"]
            .fillna("Unknown")
    )

    combined_data["payment_status"] = (
            combined_data["payment_status"]
            .fillna("Unknown")
    )

    combined_data["delivery_status"] = (
            combined_data["delivery_status"]
            .fillna("Unknown")
    )

    return combined_data

# Generate total orders report

def generate_total_orders_report(combined_data: pd.DataFrame) -> pd.DataFrame:
    """Calculate total number of unique orders."""

    total_orders = combined_data["order_id"].nunique()

    return pd.DataFrame(
        {
            "metric": ["Total Orders"],
            "value": [total_orders]
        }
    )

# Generate total revenue report

def generate_total_revenue_report(combined_data: pd.DataFrame) -> pd.DataFrame:
    """Calculate revenue from successful payments."""

    successful_orders = combined_data[
        combined_data["payment_status"] == "Success"
    ]

    total_revenue = successful_orders["total_amount"].sum()

    return pd.DataFrame(
        {
            "metric": ["Total Revenue"],
            "value": [total_revenue]
        }
    )    

#generate top products report

def generate_top_products(
        combined_data: pd.DataFrame
) -> pd.DataFrame:
    """Find the top 10 selling products."""

    successful_orders = combined_data[
        combined_data["payment_status"] == "Success"
    ]

    top_products = (
        successful_orders
        .groupby("product_name",as_index = False)  #as_index = False will not include index column
        .agg(
            total_quantity_sold = ("quantity","sum"),
            total_product_revenue = ("total_amount","sum")
        )
        .sort_values(
            by = "total_quantity_sold",
            ascending = False
        )
        .head(10)
    )
    return top_products

#generate top customers
def generate_top_customers_report(
        combined_data: pd.DataFrame
)-> pd.DataFrame:
    """Find the top 10 customers by total spending."""

    successful_orders = combined_data[
        combined_data["payment_status"] == "Success"
    ]

    top_customers = (
        successful_orders
        .groupby(
            ["customer_id","customer_name"],
            as_index = False
        )
        .agg(
            total_orders = ("order_id","nunique"),
            total_spent = ("total_amount","sum")
        )
        .sort_values(
            by="total_spent",
            ascending = False
        )
        .head(10)
    )
    return top_customers

#generate failed payments report
def generate_failed_payment_report(
    combined_data: pd.DataFrame
)-> pd.DataFrame:
    """create a report containing failed payments"""

    failed_payments = combined_data[
        combined_data["payment_status"] == "Failed"
    ]

    required_columns = [
        "payment_id",
        "order_id",
        "customer_id",
        "customer_name",
        "product_name",
        "total_amount",
        "payment_method",
        "payment_status"
    ]

    return failed_payments[required_columns]

def create_sales_line_chart(combined_data):

    sales = combined_data[
        combined_data["payment_status"] == "Success"
    ].copy()

    sales = sales.dropna(subset=["order_date"])

    daily_sales = (
        sales.groupby("order_date")["total_amount"]
        .sum()
        .sort_index()
    )

    plt.figure(figsize = (10,5))

    plt.plot(
        daily_sales.index,
        daily_sales.values,
        marker = "o",
        color = "blue",
    )

    plt.title("Daily Sales Revenue")
    plt.xlabel("Order Date")
    plt.ylabel("Revenue")
    plt.xticks(rotation = 45)
    plt.grid(True)

    plt.tight_layout()

    plt.savefig(REPORT_DIR / "sales_line_chart.png")
    plt.close()
    
#Pie chart - payment status
#this chart displays the percentage of successful , failed and pending status
def create_payment_pie_chart(combined_data):
 
    payment_counts=(
        combined_data.drop_duplicates(subset=["payment_id"])
        ["payment_status"].value_counts()
    )
 
    payment_counts_1=(
        combined_data["payment_status"].value_counts()
    )
 
    print("Payment Status Counts: \n",payment_counts)
    print("Payment Status Counts: \n",payment_counts_1)
 
    plt.figure(figsize=(7,7))
 
    plt.pie(
        payment_counts.values,
        labels=payment_counts.index,
        autopct="%1.1f%%",
        startangle=90
    )
 
    plt.title("Payment Status Distribution")
 
    plt.tight_layout()
 
    plt.savefig(REPORT_DIR/"payment_pie_chart.png")
    plt.close()
 
 

#Save reports to CSV files
def save_reports(
        total_orders_report: pd.DataFrame,
        total_revenue_report: pd.DataFrame,
        top_products_report: pd.DataFrame,
        top_customers_report: pd.DataFrame,
        failed_payments_report: pd.DataFrame
)-> None:
    """Save all generated reports as CSV files."""   

    total_orders_report.to_csv(
        REPORT_DIR / "total_orders.csv",
        index = False
    )

    total_revenue_report.to_csv(
        REPORT_DIR / "total_revenue.csv",
        index = False
    ) 

    top_products_report.to_csv(
        REPORT_DIR / "top_products.csv",
        index = False
    )

    top_customers_report.to_csv(
        REPORT_DIR / "top_customers.csv"
    )

    failed_payments_report.to_csv(
        REPORT_DIR / "failed_payments.csv"
    )



#------------MAIN ETL PIPELINE-------------

def run_etl_pipeline() -> None:
    """Execute the complete ETL Pipeline."""

    print("Starting E-commerce ETL Pipeline...")
    create_folder()
    print("Step 1: Extracting data...")

    customers, orders,payments,deliveries = extract_data()

    print("Step 2: Cleaning customer data...")
    customers = clean_customers(customers)

    print("Step 3: Cleaning order data...")
    orders = clean_orders(orders)

    print("Step 4: Cleaning payment data...")
    payments = clean_payments(payments)

    print("Step 5: Cleaning delivery data...")
    deliveries = clean_deliveries(deliveries)

    print("Step 6: Joining datasets...")

    combined_data = join_data(
        customers,
        orders,
        payments,
        deliveries
    )

    print("Step 7: Generating reports...")

    total_orders_report = generate_total_orders_report(
        combined_data
    )

    print(total_orders_report)

    total_revenue_report = generate_total_revenue_report(
        combined_data
    )

    print(total_revenue_report)

    top_products = generate_top_products(
            combined_data
        )
    
    print(top_products)

    top_customers = generate_top_customers_report(
                combined_data
            )
        
    print(top_customers)

    failed_payments = generate_failed_payment_report(
                    combined_data
                )
            
    print(failed_payments)

    save_reports(
    total_orders_report,
    total_revenue_report,
    top_products,
    top_customers,
    failed_payments
    )   

    print("Step 8:Visualization by Pie Chart and Line Chart")
    line_chart = create_sales_line_chart(combined_data)
    print(line_chart)

    pie_chart = create_payment_pie_chart(combined_data)
    print(pie_chart)
     
#Program starting point

if __name__ == "__main__":
    run_etl_pipeline()

