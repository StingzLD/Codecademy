def ground_shipping(weight):
  if weight <= 2:
    cost = 20 + (1.5 * weight)
  elif weight <= 6:
    cost = 20 + (3 * weight)
  elif weight <= 10:
    cost = 20 + (4 * weight)
  else:
    cost = 20 + (4.75 * weight)
  return cost

prem_shipping = 125

def drone_shipping(weight):
  if weight <= 2:
    cost = 4.5 * weight
  elif weight <= 6:
    cost = 9 * weight
  elif weight <= 10:
    cost = 12 * weight
  else:
    cost = 14.25 * weight
  return cost

def cheapest_shipping(weight):
  ground = ground_shipping(weight)
  prem = prem_shipping
  drone = drone_shipping(weight)
  if ground < prem and drone:
    option = "Standard Ground Shipping"
    cost = ground
  elif prem < ground and drone:
    option = "Premium Ground Shipping"
    cost = prem
  else:
    option = "Drone Shipping"
    cost = drone
  print("The cheapest option is " + option + " for $" + str(cost) + ".")

cheapest_shipping(41.5)
