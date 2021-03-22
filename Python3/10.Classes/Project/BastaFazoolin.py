class Business:
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises
  
  def __repr__(self):
    return "The {business} business contains the following franchises: {franchises}.".format(business=self.name, franchises=self.franchises)

class Franchise:
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus
  
  def __repr__(self):
    return "The store is located at {}.".format(self.address)
  
  def available_menus(self, time):
    available_menus = []
    for menu in self.menus:
      if (menu.start_time <= time) and (time <= menu.end_time):
        available_menus.append(menu)
    return available_menus

  def available_items(self, time):
    available_items = []
    for menu in self.menus:
      if (menu.start_time <= time) and (time <= menu.end_time):
        for item in menu.items:
          available_items.append(item)
    return available_items

class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time
  
  def __repr__(self):
    return "The {menu} Menu is available from {start} to {end}.".format(menu=self.name, start=self.start_time, end=self.end_time)
  
  def calculate_bill(self, purchased_items):
    total = 0
    for item in purchased_items:
      if item in self.items:
        total += self.items[item]
    return total




### Menus
# Brunch Menu
brunch_items = {
  'pancakes': 7.50,
  'waffles': 9.00,
  'burger': 11.00,
  'home fries': 4.50,
  'coffee': 1.50,
  'espresso': 3.00,
  'tea': 1.00,
  'mimosa': 10.50,
  'orange juice': 3.50
}
brunch = Menu("Brunch", brunch_items, 1100, 1600)
#print(brunch)
#print(brunch.calculate_bill(['pancakes', 'home fries', 'coffee']))

# Early-Bird Dinner Menu
early_bird_items = {
  'salumeria plate': 8.00,
  'salad and breadsticks (serves 2, no refills)': 14.00,
  'pizza with quattro formaggi': 9.00,
  'duck ragu': 17.50,
  'mushroom ravioli (vegan)': 13.50,
  'coffee': 1.50,
  'espresso': 3.00
}
early_bird = Menu("Early Bird", early_bird_items, 1500, 1800)
#print(early_bird)
#print(early_bird.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)']))

# Dinner Menu
dinner_items = {
  'crostini with eggplant caponata': 13.00,
  'ceaser salad': 16.00,
  'pizza with quattro formaggi': 11.00,
  'duck ragu': 19.50,
  'mushroom ravioli (vegan)': 13.50,
  'coffee': 2.00,
  'espresso': 3.00
}
dinner = Menu("Dinner", dinner_items, 1700, 2300)
#print(dinner)
#print(dinner.calculate_bill(['pizza with quattro formaggi', 'duck ragu', 'espresso']))

# Kids Menu
kids_items = {
  'chicken nuggets': 6.50,
  'fusilli with wild mushrooms': 12.00,
  'apple juice': 3.00
}
kids = Menu("Kids", kids_items, 1100, 2100)

menus = [brunch, early_bird, dinner, kids]
#print(kids)
#print(kids.calculate_bill(['chicken nuggets', 'applejuice']))

# Arepas' Menu
arepa_items = {
  'arepa pabellon': 7.00,
  'pernil arepa': 8.50,
  'guayanes arepa': 8.00,
  'jamon arepa': 7.50
}
arepas = Menu("Take a’ Arepa", arepa_items, 1000, 2000)
arepas_menu = [arepas]
#print(arepas)
#print(arepas.calculate_bill(['arepa pabellon', 'jamon arepa']))




### Franchises
flagship_store = Franchise("1232 West End Road", menus)
#print(flagship_store)
#print(flagship_store.available_menus(1200))
#print(flagship_store.available_items(1200))

new_installment = Franchise("12 East Mulberry Street", menus)
#print(new_installment)
#print(new_installment.available_menus(1200))
#print(new_installment.available_items(1200))

first_franchises = [flagship_store, new_installment]

arepas_place = Franchise("189 Fitzgerald Avenue", arepas_menu)
#print(arepas_place)
#print(arepas_place.available_menus(1200))
#print(arepas_place.available_items(1200))
arepas_franchises = [arepas_place]




### Businesses
first_business = Business("Basta Fazoolin' with my Heart", first_franchises)
#print(first_business)

arepas_business = Business("Take a' Arepa", arepas_franchises)
#print(arepas_business)
