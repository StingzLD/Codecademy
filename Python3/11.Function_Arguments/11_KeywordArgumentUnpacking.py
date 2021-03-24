# Checkpoint 1
print("My name is {name} and I'm feeling {feeling}.".format(
	name = "Iceman",
  feeling = "Colder than cold. ICE COLD"
))

# Checkpoint 2
from products import create_product

# Update create_products() to take arbitrary keyword arguments
def create_products(**products_dict):
  for name, price in products_dict.items():
    create_product(name, price)

# Checkpoint 3
# Update the call to `create_products()` to pass in this dictionary as a series of keyword
create_products(
  baseball = '3',
  shirt = '14',
  guitar = '70',
)
