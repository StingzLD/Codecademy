class LawFirm:
  def __init__(self, practice, lawyers):
    self.practice = practice
    self.lawyers = lawyers

  # Return the number of lawyers in LawFirm
  def __len__(self):
    return len(self.lawyers)

  # Check to see if lawyer is in self.lawyers
  def __contains__(self, lawyer):
    return lawyer in self.lawyers

d_and_p = LawFirm("Injury", ["Donelli", "Paderewski"])
print(d_and_p.lawyers)
print(d_and_p.practice)