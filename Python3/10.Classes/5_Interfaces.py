class InsurancePolicy:
  def __init__(self, price_of_item):
    self.price_of_insured_item = price_of_item

# Subclass of InsurancePolicy that defines the rate for its subclass.
class VehicleInsurance(InsurancePolicy):
  def get_rate(self):
    return self.price_of_insured_item * .001

# Subclass of InsurancePolicy that uses the same Interface as the previous policy, but with a different rate.
class HomeInsurance(InsurancePolicy):
  def get_rate(self):
    return self.price_of_insured_item * .00005