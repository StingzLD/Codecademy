# Turn up the Temperature
def f_to_c(f_temp):
  return (f_temp - 32) * 5/9

def c_to_f(c_temp):
  return c_temp * 9/5 + 32

f100_in_celsius = f_to_c(100)
# print(f100_in_celsius)
c0_in_fahrenheit = c_to_f(0)
# print(c0_in_fahrenheit)


# Use the Force
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1

def get_force(mass,acceleration):
  return mass * acceleration

def get_energy(mass,c=3*10**8):
  return mass * c

train_force = get_force(train_mass,train_acceleration)
print("The GE train supplied "+str(train_force)+" Newtons of force.")
bomb_energy = get_energy(bomb_mass)
print("A 1kg bomb supplies "+str(bomb_energy)+" Joules.")


# Do the Work
def get_work(mass,acceleration,distance):
  return get_force(mass,acceleration) * distance

train_work = get_work(train_mass,train_acceleration,train_distance)
print("The GE train does "+str(train_work)+" Joules of work over "+str(train_distance)+" meters.")
