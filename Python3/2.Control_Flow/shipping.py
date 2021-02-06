weight = 4.8

# Ground Shipping
ground = 0
if weight > 10:
  ground = weight * 4.75 + 20
elif weight > 6:
  ground = weight * 4.00 + 20
elif weight > 2:
  ground = weight * 3.00 + 20
else:
  ground = weight * 1.50 + 20
print("Ground Shipping: $" + "{:.2f}".format(ground))

# Premium Ground Shipping
premium_ground = 125
print("Premium Ground Shipping: $" + str(premium_ground))

# Drone Shipping
drone = 0
if weight > 10:
  drone = weight * 14.25
elif weight > 6:
  drone = weight * 12.00
elif weight > 2:
  drone = weight * 9.00
else:
  drone = weight * 4.50
print("Drone Shipping: $" + "{:.2f}".format(drone))