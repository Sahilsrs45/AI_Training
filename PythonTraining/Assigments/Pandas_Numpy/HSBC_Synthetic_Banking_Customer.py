import numpy as np
import pandas as pd

#21. Read the supplied CSV using pd.read_csv. 
df=pd.read_csv(r"C:\Users\Sahil.Ranawade\Downloads\HSBC_Synthetic_Banking_Customers.csv")
print(df)


print(df.head())
print(df.tail())

#1 Convert account balance into numpy array
balance=df["Account_Balance"].to_numpy()
print(balance)

#2 Inspect array ndim, shape, size and dtype.

print("Dimension :",balance.ndim)
print("Shape :",balance.shape)
print("Size :",balance.size)
print("Data Type : ",balance.dtype)

#3. Calculate minimum and maximum balances. 
min_balance=balance.min()
max_balance=balance.max()

print("Minimum balance: ",min_balance)
print("Maximum Balance: ",max_balance)

#4. Calculate sum, mean, median and standard deviation of balances. 
sum_balance=balance.sum()
print("sum : ",sum_balance)

mean_balance=balance.mean()
print("Mean of Balance : ",mean_balance)

median_balance=np.median(balance)
print("median of balance",median_balance)

std_balance=np.std(balance)
print("Standard deviation of balance: ",std_balance)

#5 Find the 25th, 50th and 75th balance percentiles

balance_percentile=np.percentile(balance,[25,50,75])

print("25th :",balance_percentile[0])
print("50th :",balance_percentile[1])
print("75th :",balance_percentile[2])

#6. Filter balances above INR 500,000. 
filter_balance=balance[balance>500000]

print(filter_balance)
print(len(filter_balance))

#7 Identify credit scores below 650 using boolean masking

credit_scores=df[df["Credit_Score"]<650]

print("Credit scores below 650 are :",credit_scores)

#8.Sort balances ascending and descending

balance_ascending=df.sort_values(by="Account_Balance")
print("In ascending order :",balance_ascending)

balance_descending=df.sort_values(by="Account_Balance" ,ascending=False)
print("In Descending order :",balance_descending)

#9Compute total monthly deposits and total monthly withdrawals.
total_deposits=df["Monthly_Income"].sum() 
total_withdrawls=df["Monthly_Withdrawal"].sum()

print("Total deposits :",total_deposits)
print("Total Withdrawls :",total_withdrawls)

#10 Use vectorization to calculate hypothetical balances after a 5% increase.
hypothetical_balance=balance*1.05
print("Hypothetical balance: ",hypothetical_balance)

#11  Use np.where to classify balances as High (> INR 500,000) or Low
result=np.where(balance > 500000 , "High","Low")
print(result)

#12. Use np.select to categorize balances into Low (< INR 100,000), Medium (INR 100,000–500,000) and High (> INR 500,000). 

condition=[
    balance<100000,
    (balance>=100000) & (balance<=500000),
    balance>500000
]

choices=["Low","Medium","High"]

df["Balance_Category"]=np.select(condition,choices,default="High")
print(df[["Account_Balance","Balance_Category"]])

#13. Compute deposit-to-income ratio; handle zero income safely. 

df["Ratio"]=df["Monthly_Deposit"]/df["Monthly_Income"].replace(0,np.nan)

print(df["Ratio"])

# 14. Identify records where monthly withdrawals exceed monthly deposits. 
record=df[df["Monthly_Withdrawal"] >df["Monthly_Deposit"]]

print(record)

#15. Use np.unique to summarize credit-score frequencies.
print("******************************")
credit_score_freq=np.unique(df["Credit_Score"],return_counts=True)

print(credit_score_freq)

#16. Use np.argsort to locate the five largest balances. 
sorted_balance=np.argsort(balance)[-5:][::-1]
print(sorted_balance)

print("---------------------------")
#17. Perform min-max normalization of balances; handle constant arrays safely.
if balance.max() != balance.min():
    normalized = (balance - balance.min()) / (
        balance.max() - balance.min()
    )
else:
    normalized = np.zeros_like(balance)

print(normalized)

#18. Compute z-scores for balances; handle zero standard deviation safely. 


#19. Build a 2D array with balance, deposit and withdrawal columns and inspect axis-wise totals.

#20. Calculate Pearson correlation between income and account balance. 

#22. Display first and last ten rows. 
print(df.head(10))
print(df.tail(10))

#23. Inspect shape, columns, dtypes and info(). 
print(df.shape)
print(df.columns)
print(df.dtypes)
print(df.info())
#24. Generate numerical descriptive statistics using describe(). 
print(df.describe())

#25. Check missing values and duplicate Customer_ID values. 
print("Missing values",df.isnull().sum())

print("Duplicate customer ids:",df["Customer_ID"].duplicated().sum())

#26. Select customer name, city, balance and credit score columns.

selected = df[
    [
        "Customer_Name",
        "City",
        "Account_Balance",
        "Credit_Score"
    ]
]
print(selected)
#27. Filter customers aged 25 through 40 inclusive.
print(df[(df["Age"] >= 25) &
       (df["Age"] <= 40)
    ]
) 

#28. Find active Savings accounts. 
print(df[(df["Account_Type"] == "Savings") &
        (df["Account_Status"] == "Active")
    ]
)

#29. Sort by balance and monthly income, descending
sorted_df = df.sort_values(by=["Account_Balance", "Monthly_Income"],
    ascending=False
)
print(sorted_df)

#30. Create Net_Monthly_Flow = Monthly_Deposit - Monthly_Withdrawal. 
df["Net_Monthly_Flow"] = (df["Monthly_Deposit"] - df["Monthly_Withdrawal"])

print(df[ ["Customer_Name",
         "Net_Monthly_Flow"]]
)

#31. Group by City and calculate total Account_Balance. 
city_balance = df.groupby("City")["Account_Balance"].sum()

#32. Group by Account_Type and calculate average Monthly_Income. 
avg_income = df.groupby( "Account_Type")["Monthly_Income"].mean()
#33. Compute branch-wise deposit and withdrawal totals. 
branch_summary = df.groupby( "Branch")[
    ["Monthly_Deposit","Monthly_Withdrawal"]
].sum()
#34. Use agg to report minimum, maximum, mean and median balances by branch. 

branch_stats = df.groupby("Branch").agg(
    Min_Balance=("Account_Balance", "min"),
    Max_Balance=("Account_Balance", "max"),
    Mean_Balance=("Account_Balance", "mean"),
    Median_Balance=("Account_Balance", "median")
)

print(branch_stats)

#35. Create a pivot table of total balance by City and Account_Type. 
pivot_tbl = pd.pivot_table(
    df,
    values="Account_Balance",
    index="City",
    columns="Account_Type",
    aggfunc="sum"
)

print(pivot_tbl)

#36. Use pd.cut to create age groups: 18–25, 26–40, 41–60 and 61+. 
df["Age_Group"] = pd.cut(
    df["Age"],
    bins=[18, 25, 40, 60, 100],
    labels=["18-25", "26-40", "41-60", "61+"]
)

print(df[["Age", "Age_Group"]])

#37. Use groupby().transform() to calculate each customer’s balance minus branch average. 
df["Balance_Minus_Branch_Avg"] = (df["Account_Balance"]-
    df.groupby("Branch")["Account_Balance"].transform("mean")
)

print(df[
    ["Customer_Name",
    "Branch",
    "Balance_Minus_Branch_Avg"]
])

#38. Create a separate Branch_Details DataFrame with Branch and Region; merge it on Branch and validate the join. 

#39. Find the top three customers by balance within each City. 
top3 = (df.sort_values("Account_Balance",ascending=False)
    .groupby("City")
    .head(3)
)

print(top3[
    [ "City","Customer_Name","Account_Balance"]
])
#40. Create a branch summary with total balance, mean credit score, counts by account status and total net monthly flow. 

