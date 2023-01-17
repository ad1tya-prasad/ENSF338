import json
import matplotlib.pyplot as plt

# open the dataset
with open("assign-1/q6/golddata.json", "r") as f:
    data = json.load(f)

# extract the data for US in 2010
us_data_2010 = [d for d in data if d["Date"][-4:] == "2010" and d["United States(USD)"] is not None]

# extract the data for South Africa in 2010
sa_data_2010 = [d for d in data if d["Date"][-4:] == "2010" and d["South Africa(ZAR)"] is not None]

# create a bar plot of the US data
plt.bar(range(len(us_data_2010)), [d["United States(USD)"] for d in us_data_2010])
plt.xlabel("Date")
plt.xticks(range(len(us_data_2010)), [d["Date"] for d in us_data_2010], rotation = 90)
plt.ylabel("Price of gold in USD")
plt.title("Gold price trend in US in 2010")
plt.show()

# create a bar plot of the South Africa data
plt.bar(range(len(sa_data_2010)), [d["South Africa(ZAR)"] for d in sa_data_2010])
plt.xlabel("Date")
plt.xticks(range(len(sa_data_2010)), [d["Date"] for d in sa_data_2010], rotation = 90)
plt.ylabel("Price of gold in ZAR")
plt.title("Gold price trend in South Africa in 2010")
plt.show()
