import pandas as pd

# file operations
df = pd.read_csv('expert_outreach_metrics_dec.csv')  # read csv
df.to_csv('output.csv', index=False)  # write to csv
df = pd.read_excel('file.xlsx')  # read Excel
df.to_excel('output.xlsx', index=False)  # write Excel
df.to_json("file.json", orient="records")  # export to JSON
df.to_sql("table_name", con=engine, if_exists="replace")  # export to SQL

# display
with pd.option_context("display.max_rows", None, "display.max_columns", None):  # display full data, not truncated
  print(df)

# basic info:
df.head()  # print first 5 rows
df.tail()  # last 5 rows
df.info()  # column names, non-null counts, data types
df.shape  # rows x columns
df.columns  # column names
df.dtypes  # data types
df.isnull().sum()  # total null values per column
df.describe()  # stats like mean/median/min/max for numeric columns

# select/explore data:
df.sample(5)  # show first x rows
df["col_name"]  # single column (Series)
df[["col1", "col2"]]  # multiple columns (DataFrame)
df["project_id"].head(8) # shows given column, x rows
df.iloc[0]  # first row by index
df.loc[df["col_name"] == "value"]  # rows with specific value
df.iloc[0:5, 0:3]  # slice rows/cols by position
df.sort_values(by="project_id", ascending=True).head() # sort
df[df["project_id"] < 10] # filter - note nested df
df["source"].unique() # unique values
df["source"].value_counts() # unique value counts

# modify data
df["new_column"] = df["project_id"] + df["segment_id"] # create a new column
df["new_col"] = df["col1"].apply(lambda x: x * 2)  # transform column
df.rename(columns={"project_id": "new_name"}, inplace=True) # rename columns
df.drop(columns=["col_name"], inplace=True)  # drop column
df.dropna(inplace=True) # drop rows with null value ***inplace mutates original dataframe
df.fillna(value=0, inplace=True) # fill null with default value, inplace mutates the original dataframe
df.replace({"old": "new"}, inplace=True)  # replace values

# aggregations
grouped = df.groupby("col_name")  # group by column
print(grouped.size())  # size of each group
print(grouped.mean())  # mean of each group
print(grouped["col2"].sum())  # sum specific col by group
df.groupby("project_id").mean() # group and aggregate data

# merging/joining
other_df = pd.DataFrame({"key": [1, 2], "val": ["A", "B"]})
merged = pd.merge(df, other_df, on="key", how="inner")  # merge on key
df = pd.concat([df, other_df], axis=0)  # append rows
df = pd.concat([df, other_df], axis=1)  # append cols

# Pivot tables
pivot = df.pivot_table(values="col1", index="col2", columns="col3", aggfunc="sum")  # pivot table

# working with dates
df["date_col"] = pd.to_datetime(df["date_col"])  # convert to datetime
print(df["date_col"].dt.year)  # extract year
print(df["date_col"].dt.month)  # extract month
print(df["date_col"].dt.day_name())  # extract day name

# Advanced filtering
print(df.query('col1 > 100 and col2 == "value"'))  # query using strings

# Working with indexes
df.set_index("col_name", inplace=True)  # set index
df.reset_index(inplace=True)  # reset index
df.sort_index(inplace=True)  # sort by index

# Advanced operations
df["rolling_avg"] = df["col_name"].rolling(window=3).mean()  # rolling avg
df["expanding_sum"] = df["col_name"].expanding().sum()  # expanding sum
df["rank"] = df["col_name"].rank()  # rank values












