# create a bar plot of the US data
plt.bar(range(len(us_data_2010)), [d["Price"] for d in us_data_2010])
plt.xlabel("Days of 2010")
plt.ylabel("Price of gold in USD")
plt.title("Gold price trend in US in 2010")
plt.show()