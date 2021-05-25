class Node:
    def __init__(self, value, link_node=None):
        self.value = value
        self.link_node = link_node
      
    def set_link_node(self, link_node):
        self.link_node = link_node
      
    def get_link_node(self):
        return self.link_node
    
    def get_value(self):
        return self.value

# Add your code below:
# Instantiate the nodes
yacko = Node("likes to yak")
wacko = Node("has a penchant for hoarding snacks")
dot = Node("enjoys spending time in movie lots")

# Update the nodes' links
yacko.set_link_node(dot)
dot.set_link_node(wacko)

# Get dot's data from yacko and wacko's data from dot
dots_data = yacko.get_link_node().get_value()
wackos_data = dot.get_link_node().get_value()
print(dots_data)
print(wackos_data)