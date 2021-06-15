"""
1. Move items to the end of a list

Define a function called move_to_end() that accepts two arguments: lst and val.

The function should return a copy of lst with every instance of val moved to the end of the list.

Example:
Input: move_to_end(["Amber", "Sapphire", "Amber", "Jade"], “Amber”)
Output: ["Sapphire", "Jade", "Amber", "Amber"]

Hint: Use Python list slicing to quickly generate sub-lists.
For example: lst[1:] is the sublist of lst containing every item except the first.
"""
# define move_to_end() here
def move_to_end(lst, val):
    result = []

    if len(lst) == 0:
        return []
    
    if lst[0] == val:
        result += move_to_end(lst[1:], val)
        result.append(lst[0])
    else:
        result.append(lst[0])
        result += move_to_end(lst[1:], val)
    
    return result

# Test code - do not edit
gemstones = ["Amber", "Sapphire", "Amber", "Jade"]
print(move_to_end(gemstones, "Amber"))

"""
2. Delete i-th node from a linked list

Define a function called remove_node() that takes in the following parameters:

head - a node that acts as the head of a linked list
i - an integer
The function should remove the ith node of the linked list (index from 0) and return the modified head.

Example:

Input: remove_node(head = "Amber"->"Sapphire"->"Jade"->"Pearl", 1)
Output: head = "Amber"->"Jade"->"Pearl"
The LinkedList class has been implemented for you. You do not need to modify it.
"""
import LinkedList

# Definition for singly-linked list node.
# class ListNode:
#     def __init__(self, value, next_node=None):
#         self.value = value
#         self.next_node = next_node

# define remove_node() here
def remove_node(head, i):
    if i < 0:
        return head
    
    if head is None:
        return None
    
    if i == 0:
        return head.next_node

    head.next_node = remove_node(head.next_node, i - 1)
    
    return head

# Test code - do not edit
gemstones = LinkedList.LinkedList(["Amber", "Sapphire", "Jade", "Pearl"])
head = remove_node(gemstones.head, 1)
print(head.flatten())

"""
3. Prepend and append to a string

Define the function called wrap_string() that accepts two arguments: string str and int n.

The function should return a copy of str with n number of '<' and '>' prepended and appended to it, respectively.

Example:

Input: wrap_string("Pearl", 3)
Output: "<<<Pearl>>>"
"""
# define wrap_string() here
def wrap_string(str, n):
    result = ""

    if n <= 0:
        return str
    
    result = f"<{wrap_string(str, n - 1)}>"

    return result

# Test code - do not edit
wrapped = wrap_string("Pearl", 3)
print(wrapped)
