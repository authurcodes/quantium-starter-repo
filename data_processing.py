import pandas as pd

daily_sales_files = [
    "data/daily_sales_data_0.csv",
    "data/daily_sales_data_1.csv",
    "data/daily_sales_data_2.csv"
]

processed_files =[]

for file in daily_sales_files:
    data = pd.read_csv(file)
    data = data[data["product"] == "pink morsel"]
    data["price"] = data["price"].str.strip('$').astype(float)
    data["sales"] = data["price"] * data["quantity"]
    data = data[['sales', 'date', 'region']]
    processed_files.append(data)

    combined_data_files = pd.concat(processed_files, ignore_index=True)
    combined_data_files.to_csv('pink_morsel_sales.csv', index=False)
