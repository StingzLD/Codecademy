# Make some pizzas
toppings = ['pepperoni', 'pineapple', 'cheese', 'sausage', 'olives', 'anchovies', 'mushrooms']
prices = [2, 6, 1, 3, 2, 7, 2]

num_pizzas = len(toppings)
print("We sell "+str(num_pizzas)+" kinds of pizza!\n")

pizzas = list(zip(prices, toppings))
print(pizzas)


# Sorting and slicing pizzas
pizzas.sort()
print('', pizzas, sep='\n')
cheapest_pizza = pizzas[0]
#print(cheapest_pizza)
priciest_pizza = pizzas[-1]
#print(priciest_pizza)
three_cheapest = pizzas[:3]
#print(three_cheapest)
num_two_dollar_slices = prices.count(2)
print('', num_two_dollar_slices, sep='\n')