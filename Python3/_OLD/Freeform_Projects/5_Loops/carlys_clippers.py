hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]
prices = [30, 25, 40, 20, 20, 35, 50, 35]
last_week = [2, 3, 5, 8, 4, 4, 6, 2]

# Calculate total price of all haircuts
total_price = 0
for price in prices:
  total_price += price

# Calculate average price of all haircuts
average_price = total_price / len(prices)
print("Average Haircut Price:\n" + str(average_price))

# Calculate new prices of haircuts
new_prices = [price - 5 for price in prices]
print(new_prices)

# Calculate revenue
total_revenue = 0
for i in range(len(hairstyles)):
  total_revenue += prices[1] * last_week[1]
print("Total Revenue:\n" + str(total_revenue))

average_daily_revenue = total_revenue / 7
print("Average Daily Revenue:\n" + str(average_daily_revenue))

# List haircuts under $30
cuts_under_30 = [hairstyles[i] for i in range(len(new_prices) - 1) if new_prices[i] < 30]
print(cuts_under_30)

