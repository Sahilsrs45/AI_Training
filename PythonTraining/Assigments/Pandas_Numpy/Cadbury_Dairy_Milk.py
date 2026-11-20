import pandas as pd
import numpy as np
 
# Load the datasets
sales = pd.read_csv(r"C:\Users\Sahil.Ranawade\Downloads\Cadbury_Dairy_Milk_Sales_2025_Synthetic.csv")
product = pd.read_csv(r"C:\Users\Sahil.Ranawade\Downloads\Cadbury_Product_Master.csv")
store = pd.read_csv(r"C:\Users\Sahil.Ranawade\Downloads\Cadbury_Store_Master.csv")
 

# PANDAS A: DATA LOADING AND INSPECTION
# ============================================================
 
# P01. Load the sales CSV into a DataFrame.
sales = pd.read_csv(r"C:\Users\Sahil.Ranawade\Downloads\Cadbury_Dairy_Milk_Sales_2025_Synthetic.csv")
print(sales)
 
 
# P02. Display the first 10 records.
print(sales.head(10))
 
 
# P03. Display the last 10 records.
print(sales.tail(10))
 
 
# P04. Find the number of rows and columns.
print("Rows:", sales.shape[0])
print("Columns:", sales.shape[1])
 
 
# P05. List all column names.
print(sales.columns.tolist())
 
 
# P06. Inspect column data types.
print(sales.dtypes)
 
 
# P07. Generate a concise DataFrame information summary.
sales.info()
 
 
# P08. Calculate descriptive statistics for numeric fields.
print(sales.describe())
 
 
# P09. Calculate descriptive statistics for categorical fields.
print(sales.describe(include="object"))
 
 
# P10. Identify missing values by column.
print(sales.isnull().sum())
 
 
# P11. Count duplicate Order_ID values.
print("Duplicate Order IDs:", sales["Order_ID"].duplicated().sum())
 
 
# P12. Find unique product names and their count.
print("Unique Products:", sales["Product_Name"].unique())
print("Total Products:", sales["Product_Name"].nunique())
 
 
# P13. Find unique cities and regions.
print("Unique Cities:", sales["City"].unique())
print("Unique Regions:", sales["Region"].unique())
 
 
# P14. Convert Order_Date to datetime and verify the result.
sales["Order_Date"] = pd.to_datetime(sales["Order_Date"])
print(sales["Order_Date"].dtype)
 
 
# P15. Create a data dictionary listing every field and its business meaning.
data_dictionary = {
    "Order_ID": "Unique order identification number",
    "Order_Date": "Date of order",
    "Region": "Region of sales",
    "City": "City of sales",
    "Store_ID": "Unique store identification",
    "Sales_Channel": "Sales channel",
    "Product_ID": "Unique product identification",
    "Product_Name": "Name of product",
    "Pack_Size_g": "Product pack size in grams",
    "Unit_MRP_INR": "Maximum retail price per unit",
    "Discount_Pct": "Discount percentage",
    "Unit_Selling_Price_INR": "Actual selling price per unit",
    "Quantity": "Number of units sold",
    "Gross_Sales_INR": "Sales before discount",
    "Net_Revenue_INR": "Revenue after discount",
    "Unit_Cost_INR": "Cost of one unit",
    "Total_Cost_INR": "Total product cost",
    "Delivery_Cost_INR": "Delivery cost",
    "Profit_INR": "Profit earned",
    "Payment_Method": "Payment method",
    "Customer_Age": "Age of customer",
    "Customer_Segment": "Customer category",
    "Customer_Rating": "Customer rating",
    "Promotion_Flag": "Indicates promotion",
    "Returned_Flag": "Indicates returned order"
}
 
for column, meaning in data_dictionary.items():
    print(column, ":", meaning)
 
 
# ============================================================
# PANDAS B: CLEANING AND FEATURE ENGINEERING
# ============================================================
 
# P16. Create a working copy without modifying raw data.
sales = sales.copy()
 
 
# P17. Remove exact duplicate records, if any.
print("Duplicates before removal:", sales.duplicated().sum())
 
sales = sales.drop_duplicates()
 
print("Duplicates after removal:", sales.duplicated().sum())
 
 
# P18. Apply a consistent naming convention to columns.
sales.columns = sales.columns.str.strip()
 
print(sales.columns.tolist())
 
 
# P19. Validate that Quantity is positive.
invalid_quantity = sales[sales["Quantity"] <= 0]
 
print(invalid_quantity)
 
 
# P20. Identify records with Discount_Pct outside 0-100.
invalid_discount = sales[
    (sales["Discount_Pct"] < 0) |
    (sales["Discount_Pct"] > 100)
]
 
print(invalid_discount)
 
 
# P21. Detect negative revenue, cost, or profit values and explain their meaning.
negative_records = sales[
    (sales["Net_Revenue_INR"] < 0) |
    (sales["Total_Cost_INR"] < 0) |
    (sales["Profit_INR"] < 0)
]
 
print(negative_records)
 
# Negative profit means the business has incurred a loss.
# Negative revenue or cost values should be investigated.
 
 
# P22. Recalculate Net_Revenue_INR from Quantity and Unit_Selling_Price_INR.
sales["Net_Revenue_INR"] = (
    sales["Quantity"] * sales["Unit_Selling_Price_INR"]
)
 
print(sales[["Order_ID", "Net_Revenue_INR"]].head())
 
 
# P23. Compare recorded and recomputed revenue with a tolerance.
sales["Revenue_Match"] = np.isclose(
    sales["Gross_Sales_INR"] * (1 - sales["Discount_Pct"] / 100),
    sales["Net_Revenue_INR"],
    atol=0.01
)
 
print(sales["Revenue_Match"].value_counts())
 
 
# P24. Recalculate Profit_INR using revenue, costs, and delivery.
sales["Profit_INR"] = (
    sales["Net_Revenue_INR"]
    - sales["Total_Cost_INR"]
    - sales["Delivery_Cost_INR"]
)
 
print(sales[["Order_ID", "Profit_INR"]].head())
 
 
# P25. Create Profit_Margin_Pct with safe division.
sales["Profit_Margin_Pct"] = np.where(
    sales["Net_Revenue_INR"] != 0,
    (sales["Profit_INR"] / sales["Net_Revenue_INR"]) * 100,
    0
)
 
print(sales[["Order_ID", "Profit_Margin_Pct"]].head())
 
 
# P26. Create Year, Month, and Month_Name fields from Order_Date.
sales["Order_Date"] = pd.to_datetime(sales["Order_Date"])
 
sales["Year"] = sales["Order_Date"].dt.year
sales["Month"] = sales["Order_Date"].dt.month
sales["Month_Name"] = sales["Order_Date"].dt.month_name()
 
print(sales[["Order_Date", "Year", "Month", "Month_Name"]].head())
 
 
# P27. Create Quarter and Weekday fields.
sales["Quarter"] = sales["Order_Date"].dt.quarter
sales["Weekday"] = sales["Order_Date"].dt.day_name()
 
print(sales[["Order_Date", "Quarter", "Weekday"]].head())
 
 
# P28. Create Weekend_Flag from Order_Date.
sales["Weekend_Flag"] = sales["Order_Date"].dt.dayofweek >= 5
 
print(sales[["Order_Date", "Weekend_Flag"]].head())
 
 
# P29. Create Discount_Band categories (none, low, medium, high).
sales["Discount_Band"] = pd.cut(
    sales["Discount_Pct"],
    bins=[-0.01, 0, 5, 15, 100],
    labels=["None", "Low", "Medium", "High"]
)
 
print(sales[["Discount_Pct", "Discount_Band"]].head())
 
 
# P30. Create Order_Value_Band using quantiles or defined thresholds.
sales["Order_Value_Band"] = pd.qcut(
    sales["Net_Revenue_INR"],
    q=3,
    labels=["Low", "Medium", "High"],
    duplicates="drop"
)
 
print(sales[["Net_Revenue_INR", "Order_Value_Band"]].head())
 
 
# ============================================================
# PANDAS C: SELECTION, FILTERING AND SORTING
# ============================================================
 
# P31. Select Order_ID, Product_Name, City, Quantity and Net_Revenue_INR.
print(sales[[
    "Order_ID",
    "Product_Name",
    "City",
    "Quantity",
    "Net_Revenue_INR"
]])
 
 
# P32. Filter transactions from Mumbai.
mumbai_orders = sales[sales["City"] == "Mumbai"]
 
print(mumbai_orders)
 
 
# P33. Filter orders for Dairy Milk Silk.
silk_orders = sales[
    sales["Product_Name"] == "Dairy Milk Silk"
]
 
print(silk_orders)
 
 
# P34. Filter transactions with Quantity >= 10.
quantity_orders = sales[sales["Quantity"] >= 10]
 
print(quantity_orders)
 
 
# P35. Filter orders with Discount_Pct >= 15.
discount_orders = sales[sales["Discount_Pct"] >= 15]
 
print(discount_orders)
 
 
# P36. Find loss-making orders where Profit_INR < 0.
loss_orders = sales[sales["Profit_INR"] < 0]
 
print(loss_orders)
 
 
# P37. Find orders from North region placed in Q4.
north_q4_orders = sales[
    (sales["Region"] == "North") &
    (sales["Order_Date"].dt.quarter == 4)
]
 
print(north_q4_orders)
 
 
# P38. Filter e-commerce orders paid by UPI.
ecommerce_upi = sales[
    (sales["Sales_Channel"] == "E-commerce") &
    (sales["Payment_Method"] == "UPI")
]
 
print(ecommerce_upi)
 
 
# P39. Find orders between two user-selected dates.
start_date = input("Enter start date (YYYY-MM-DD): ")
end_date = input("Enter end date (YYYY-MM-DD): ")
 
date_orders = sales[
    sales["Order_Date"].between(
        pd.to_datetime(start_date),
        pd.to_datetime(end_date)
    )
]
 
print(date_orders)
 
 
# P40. Find orders where Product_Name contains Dairy Milk.
dairy_milk_orders = sales[
    sales["Product_Name"].str.contains(
        "Dairy Milk",
        case=False,
        na=False
    )
]
 
print(dairy_milk_orders)
 
 
# P41. Find transactions with Customer_Rating <= 2.
low_rating_orders = sales[
    sales["Customer_Rating"] <= 2
]
 
print(low_rating_orders)
 
 
# P42. Sort orders by Net_Revenue_INR descending.
sorted_revenue = sales.sort_values(
    by="Net_Revenue_INR",
    ascending=False
)
 
print(sorted_revenue)
 
 
# P43. Show the top 20 orders by Profit_INR.
top_20_orders = sales.nlargest(
    20,
    "Profit_INR"
)
 
print(top_20_orders)
 
 
# P44. Sort by Region ascending then Quantity descending.
sorted_region_quantity = sales.sort_values(
    by=["Region", "Quantity"],
    ascending=[True, False]
)
 
print(sorted_region_quantity)
 
 
# P45. Select transactions meeting three simultaneous business conditions.
# Conditions: West region, quantity >= 10 and discount >= 10%.
filtered_orders = sales[
    (sales["Region"] == "West") &
    (sales["Quantity"] >= 10) &
    (sales["Discount_Pct"] >= 10)
]
 
print(filtered_orders)
 
 
# ============================================================
# PANDAS D: AGGREGATION AND BUSINESS METRICS
# ============================================================
 
# P46. Calculate total net revenue.
total_revenue = sales["Net_Revenue_INR"].sum()
 
print("Total Revenue:", total_revenue)
 
 
# P47. Calculate total profit.
total_profit = sales["Profit_INR"].sum()
 
print("Total Profit:", total_profit)
 
 
# P48. Calculate total quantity sold.
total_quantity = sales["Quantity"].sum()
 
print("Total Quantity Sold:", total_quantity)
 
 
# P49. Calculate overall profit margin percentage.
profit_margin = (total_profit / total_revenue) * 100
 
print("Overall Profit Margin:", profit_margin)
 
 
# P50. Calculate average order value.
average_order_value = sales["Net_Revenue_INR"].mean()
 
print("Average Order Value:", average_order_value)
 
 
# P51. Count orders by Sales_Channel.
channel_orders = sales["Sales_Channel"].value_counts()
 
print(channel_orders)
 
 
# P52. Calculate revenue by Product_Name.
product_revenue = sales.groupby("Product_Name")[
    "Net_Revenue_INR"
].sum()
 
print(product_revenue)
 
 
# P53. Calculate profit by Region.
region_profit = sales.groupby("Region")[
    "Profit_INR"
].sum()
 
print(region_profit)
 
 
# P54. Calculate units sold by City.
city_quantity = sales.groupby("City")[
    "Quantity"
].sum()
 
print(city_quantity)
 
 
# P55. Find the top five products by revenue.
top_products = product_revenue.nlargest(5)
 
print(top_products)
 
 
# P56. Find the bottom five cities by profit.
city_profit = sales.groupby("City")[
    "Profit_INR"
].sum()
 
bottom_cities = city_profit.nsmallest(5)
 
print(bottom_cities)
 
 
# P57. Calculate mean and median discount by channel.
discount_analysis = sales.groupby("Sales_Channel")[
    "Discount_Pct"
].agg(["mean", "median"])
 
print(discount_analysis)
 
 
# P58. Calculate revenue and profit grouped by Region and Product_Name.
region_product = sales.groupby(
    ["Region", "Product_Name"]
).agg(
    Total_Revenue=("Net_Revenue_INR", "sum"),
    Total_Profit=("Profit_INR", "sum")
)
 
print(region_product)
 
 
# P59. Calculate order count, revenue, and average rating by Customer_Segment.
customer_analysis = sales.groupby("Customer_Segment").agg(
    Order_Count=("Order_ID", "count"),
    Total_Revenue=("Net_Revenue_INR", "sum"),
    Average_Rating=("Customer_Rating", "mean")
)
 
print(customer_analysis)
 
 
# P60. Calculate return rate by product using Returned_Flag.
return_rate = sales.groupby("Product_Name")[
    "Returned_Flag"
].mean() * 100
 
print(return_rate)
 
 
# ============================================================
# PANDAS E: ADVANCED ANALYTICS AND JOINS
# ============================================================
 
# P61. Build a monthly revenue trend table.
monthly_revenue = sales.groupby(
    sales["Order_Date"].dt.to_period("M")
)["Net_Revenue_INR"].sum()
 
print(monthly_revenue)
 
 
# P62. Compute month-over-month revenue growth percentage.
monthly_growth = monthly_revenue.pct_change() * 100
 
print(monthly_growth)
 
 
# P63. Build a quarterly profit comparison.
quarterly_profit = sales.groupby(
    sales["Order_Date"].dt.to_period("Q")
)["Profit_INR"].sum()
 
print(quarterly_profit)
 
 
# P64. Create a pivot table: Region by Product_Name with revenue totals.
region_product_pivot = pd.pivot_table(
    sales,
    values="Net_Revenue_INR",
    index="Region",
    columns="Product_Name",
    aggfunc="sum",
    fill_value=0
)
 
print(region_product_pivot)
 
 
# P65. Create a pivot table: Sales_Channel by Month with order counts.
channel_month_pivot = pd.pivot_table(
    sales,
    values="Order_ID",
    index="Sales_Channel",
    columns="Month",
    aggfunc="count",
    fill_value=0
)
 
print(channel_month_pivot)
 
 
# P66. Create a cross-tab of Customer_Segment versus Payment_Method.
customer_payment = pd.crosstab(
    sales["Customer_Segment"],
    sales["Payment_Method"]
)
 
print(customer_payment)
 
 
# P67. Calculate a seven-day rolling revenue average on daily totals.
daily_revenue = sales.groupby("Order_Date")[
    "Net_Revenue_INR"
].sum().sort_index()
 
rolling_revenue = daily_revenue.rolling(
    window=7,
    min_periods=1
).mean()
 
print(rolling_revenue)
 
 
# P68. Calculate cumulative revenue over time.
cumulative_revenue = daily_revenue.cumsum()
 
print(cumulative_revenue)
 
 
# P69. Rank products within each region by revenue.
region_product_revenue = sales.groupby(
    ["Region", "Product_Name"]
)["Net_Revenue_INR"].sum()
 
product_rank = region_product_revenue.groupby(
    level="Region"
).rank(ascending=False, method="dense")
 
print(product_rank)
 
 
# P70. Calculate each product share of total revenue.
product_share = (
    product_revenue / total_revenue
) * 100
 
print(product_share)
 
 
# P71. Merge sales with the product master on Product_ID.
sales_product = pd.merge(
    sales,
    product,
    on="Product_ID",
    how="left",
    suffixes=("", "_Master")
)
 
print(sales_product.head())
 
 
# P72. Merge sales with the store master on Store_ID.
sales_store = pd.merge(
    sales_product,
    store,
    on="Store_ID",
    how="left"
)
 
print(sales_store.head())
 
 
# P73. Compare actual unit MRP with standard product master MRP.
mrp_comparison = sales_store[
    ["Product_Name", "Unit_MRP_INR", "Standard_MRP_INR"]
].drop_duplicates().copy()
 
mrp_comparison["MRP_Difference"] = (
    mrp_comparison["Unit_MRP_INR"]
    - mrp_comparison["Standard_MRP_INR"]
)
 
mrp_comparison["MRP_Matches"] = np.isclose(
    mrp_comparison["Unit_MRP_INR"],
    mrp_comparison["Standard_MRP_INR"]
)
 
print(mrp_comparison)
 
 
# P74. Calculate store-level revenue, profit, order count and average order value.
store_analysis = sales_store.groupby("Store_ID").agg(
    Total_Revenue=("Net_Revenue_INR", "sum"),
    Total_Profit=("Profit_INR", "sum"),
    Order_Count=("Order_ID", "count"),
    Average_Order_Value=("Net_Revenue_INR", "mean")
)
 
print(store_analysis)
 
 
# P75. Identify top-performing stores and prepare a five-point management summary.
 
top_stores = store_analysis.sort_values(
    by="Total_Revenue",
    ascending=False
).head(10)
 
print("Top 10 Performing Stores:")
print(top_stores)
 
# Five-point management summary
 
print("\n========== MANAGEMENT SUMMARY ==========")
 
print("1. Top Revenue Product:")
print(product_revenue.idxmax())
 
print("\n2. Highest Profit Region:")
print(region_profit.idxmax())
 
print("\n3. Best Performing Sales Channel by Profit:")
 
channel_profit = sales.groupby("Sales_Channel")["Profit_INR"].sum()
print(channel_profit.idxmax())
 
print("\n4. Highest Revenue City:")
 
city_revenue = sales.groupby("City")["Net_Revenue_INR"].sum()
print(city_revenue.idxmax())
 
print("\n5. Average Customer Rating:")
 
print(round(sales["Customer_Rating"].mean(), 2))