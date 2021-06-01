from linkedList import Node, LinkedList
from blossomLib import flower_definitions

class HashMap:
    def __init__(self,size):
        self.array_size = size
        self.array = [LinkedList() for i in range(self.array_size)]

    def hash(self, key):
        return sum(key.encode())

    def compress(self, hash_code):
        return hash_code % self.array_size

    def assign(self, key, value):
        array_index = self.compress(self.hash(key))
        payload = Node([key, value])
        list_at_array = self.array[array_index]

        for lst in list_at_array:
            if lst[0] == key:
                lst[1] = value
                return

        list_at_array.insert(payload)
    
    def retrieve(self, key):
        array_index = self.compress(self.hash(key))
        list_at_index = self.array[array_index]

        for lst in list_at_index:
            if lst[0] == key:
                return lst[1]
        return None


blossom = HashMap(len(flower_definitions))

for key, value in flower_definitions:
    blossom.assign(key, value)

print(blossom.retrieve('daisy'))
