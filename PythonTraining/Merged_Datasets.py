import pandas as pd
customers = pd.DataFrame({
   "customer_id": [
       "C101", "C102", "C103", "C104", "C105",
       "C106", "C107", "C108", "C109", "C110"
   ],
   "customer_name": [
       "Amit", "Neha", "Rahul", "Priya", "Karan",
       "Sneha", "Rohit", "Anjali", "Vikas", "Pooja"
   ],
   "city": [
       "Delhi", "Mumbai", "Delhi", "Pune", "Noida",
       "Mumbai", "Bangalore", "Delhi", "Noida", "Pune"
   ],
   "segment": [
       "Premium", "Regular", "Premium", "Regular", "Premium",
       "Premium", "Regular", "Premium", "Regular", "Premium"
   ]
})
print(customers)
#Products Dataset
products = pd.DataFrame({
   "product_id": [
       "P101", "P102", "P103", "P104",
       "P105", "P106", "P107", "P108"
   ],
   "product_name": [
       "Laptop",
       "Mouse",
       "Keyboard",
       "Monitor",
       "Headphones",
       "Tablet",
       "Printer",
       "Smartphone"
   ],
   "category": [
       "Electronics",
       "Accessories",
       "Accessories",
       "Electronics",
       "Accessories",
       "Electronics",
       "Electronics",
       "Electronics"
   ],
   "price": [
       65000,
       1200,
       2500,
       18000,
       3500,
       30000,
       15000,
       45000
   ]
})
#Stores Dataset
stores = pd.DataFrame({
   "store_id": [
       "S101", "S102", "S103", "S104"
   ],
   "store_name": [
       "Delhi Central",
       "Mumbai Central",
       "Pune Mall",
       "Bangalore Hub"
   ],
   "city": [
       "Delhi",
       "Mumbai",
       "Pune",
       "Bangalore"
   ]
})
#Sales Dataset
#I am intentionally adding a few invalid references
# so we can demonstrate data-quality problems during merging.
sales = pd.DataFrame({
   "sale_id": [
       1001, 1002, 1003, 1004, 1005,
       1006, 1007, 1008, 1009, 1010,
       1011, 1012, 1013, 1014, 1015
   ],
   "customer_id": [
       "C101", "C102", "C103", "C104", "C105",
       "C106", "C107", "C108", "C109", "C110",
       "C101", "C103", "C106", "C999", "C105"
   ],
   "product_id": [
       "P101", None, "P103", "P104", "P105",
       "P106", "P107", "P108", "P101", "P104",
       "P102", "P106", "P105", None, "P999"
   ],
   "store_id": [
       "S101", "S102", "S101", None, "S101",
       "S102", "S104", "S101", "S101", "S103",
       "S101", "S101", "S102", "S101", "S999"
   ],
   "quantity": [
       1, 3, 2, 1, 4,
       1, 2, 1, 1, 2,
       5, 1, 3, 1, 2
   ],
   "sale_date": [
       "2026-08-01",
       "2026-08-02",
       "2026-08-03",
       "2026-08-04",
       "2026-08-05",
       "2026-08-06",
       "2026-08-07",
       "2026-08-08",
       "2026-08-09",
       "2026-08-10",
       "2026-08-11",
       "2026-08-12",
       "2026-08-13",
       "2026-08-14",
       "2026-08-15"
   ]
})
 
print(customers)
print(products)
print(stores)
print(sales)
 
print("CUSTOMERS")
print(customers.head())
print(customers.shape)
print(customers.columns)
customers.info()
 
print("\nPRODUCTS")
print(products.head())
print(products.shape)
print(products.columns)
products.info()
 
print("\nSTORES")
print(stores.head())
print(stores.shape)
print(stores.columns)
stores.info()
 
print("\nSALES")
print(sales.head())
print(sales.shape)
print(sales.columns)
sales.info()
 
# check missing values
print("Customers Missing values:")
print(customers.isnull().sum())
 
print("Products Missing values:")
print(products.isnull().sum())
 
print("Stores Missing values:")
print(stores.isnull().sum())
 
print("Sales Missing values:")
print(sales.isnull().sum())
 
# check duplicate records
print(customers.duplicated().sum())
print(products.duplicated().sum())
print(stores.duplicated().sum())
print(sales.duplicated().sum())
 
# check duplicate primary keys spearately:
print(customers["customer_id"].duplicated().sum())
print(products["product_id"].duplicated().sum())
print(stores["store_id"].duplicated().sum())
print(sales["sale_id"].duplicated().sum())
 
# Merge sales with customers use a inner merge
# because we dont want t o lose sales transactions
 
sales_customers=sales.merge(
    customers,
    on="customer_id",
    how="inner"
)
 
print("Sales with Customers")
print(sales_customers)
 
print(sales_customers.head())
print(sales.shape)
print(sales_customers.shape)
 
invalid_customers=sales_customers[
    sales_customers["customer_name"].isna()
]
 
print("Invalid Customers")
print(invalid_customers)
 
sales_customer_product=sales_customers.merge(
    products,
    on="product_id",
    how="left"
)
 
print("Sales with Customers and Products")
print(sales_customer_product.head())
 
invalid_products=sales_customer_product[
    sales_customer_product["product_name"].isna()
]
 
print(invalid_products)
 
final_df=sales_customer_product.merge(
    stores,
    on="store_id",
    how="left",
    suffixes=("_customer","_store")
)
print(final_df.head())
 
# Find Invalid Stores
invalid_stores=final_df[
    final_df["store_name"].isna()
]
 
print(invalid_stores)
 
invalid_records=final_df[
    final_df["customer_name"].isna()
    | final_df["product_name"].isna()
    | final_df["store_name"].isna()
]
 
print(invalid_records)
 
final_df["revenue"]=(
    final_df["quantity"] * final_df["price"]
)
 
print(
    final_df[
        ["sale_id","product_name","quantity","price","revenue"]
    ]
)
 
# Total Revenue
total_revenue=final_df["revenue"].sum()
print("Total Revenue: ",total_revenue)
 
# Total Quantity Sold
total_quantity=final_df["quantity"].sum()
print("Total Quantity Sold: ",total_quantity)
 
valid_df=final_df[
    final_df["store_name"].notna()
    & final_df["product_name"].notna()
    & final_df["store_name"].notna()
].copy()
print(valid_df.head())
 
# groupby("where we want to groupby")[column name].aggfun()
 
category_revenue=valid_df.groupby("category")["revenue"].sum().reset_index().sort_values(by="revenue",ascending=False)
print(category_revenue)
 
# Revenue by Customer Segment
 
category_revenue=valid_df.groupby("segment")["revenue"].sum().reset_index().sort_values(by="revenue",ascending=True)
print(category_revenue)
 
# Revenue by Store Name
 
category_revenue=valid_df.groupby("store_name")["revenue"].sum().reset_index().sort_values(by="revenue",ascending=False)
print(category_revenue)
 
product_revenue=(
    valid_df.groupby("product_name")["revenue"].sum().sort_values(ascending=False)
)
print(product_revenue)
 
print("Top Product: ",product_revenue.idxmax()) # gives the max id of product_revenue
print("Revenue: ", product_revenue.max())
 
# Top 5 Customers
customer_revenue=(
    valid_df.groupby("customer_name")["revenue"].sum().sort_values(ascending=False).nlargest(5)
)
print(customer_revenue)
 
# Find Customer who purchased more than 2 items and made atleast 2 transactions
 
customer_summary=(
    sales.groupby("customer_id").agg(
        total_quantity=("quantity","sum"),
        total_transactions=("sale_id","count")
    )
    .reset_index()
)
 
result=customer_summary[
    (customer_summary["total_quantity"]>2) &
    (customer_summary["total_transactions"]>=2)
]
 
print(result)