# Turn up the Temperature
#1
def f_to_c(f_temp):
  c_temp = (f_temp - 32) * 5 / 9
  return c_temp

#3
def c_to_f(c_temp):
  f_temp = c_temp * (9 / 5) + 32
  return f_temp

#2
f100_in_celsius = f_to_c(100)
print("100 *F = " + str(f100_in_celsius) + " *C")

#4
c0_in_fahrenheit = c_to_f(0)
print("0 *C = " + str(c0_in_fahrenheit) + " *F \n")

# Use the Force
train_mass = 22680
train_accel = 10
train_dist = 100
bomb_mass = 1

#5
def get_force(mass, accel):
  force = mass * accel
  return force

#8
def get_energy(mass, c = 3 * 10 ** 8):
  energy = mass * c ** 2
  return energy

#6-7
train_force = get_force(train_mass, train_accel)
print("The GE train supplies " + str(train_force) + " Newtons of force. 
\n")

#9-10
bomb_energy = get_energy (bomb_mass)
print("A 1kg bomb supplies " + str(bomb_energy) + " Joules. \n")

# Do the Work
#11
def get_work(mass, accel, dist):
  force = get_force(mass, accel) * dist
  return force

#12-13
train_work = get_work(train_mass, train_accel, train_dist)
print("The GE train does " + str(train_work) + " Joules of work over" + 
str(train_dist) + " meters.")

