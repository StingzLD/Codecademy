# Create a class that inherits from List, but modify Append to sort the list after appending the new value.
class SortedList(list):
  def append(self, value):
    super().append(value)
    self.sort()
