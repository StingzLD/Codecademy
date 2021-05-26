'''
1. Two Pointers Moving in Parallel

Complete the nth_last_node() function so that it returns the correct Node instance
(or None if the linked_list is shorter than n elements). Do this without creating
any additional new data structures (such as a list). You can assume that the
linked list has no cycles.

You can use the generate_test_linked_list() function to test it yourself. It
returns a linked list with values from 1 -> 2 -> ... -> 49 -> 50.
'''
from LinkedList import LinkedList

# Complete this function:
def nth_last_node(linked_list, n):
    nth_pointer = None
    tail_pointer = linked_list.head_node
    count = 1

    while tail_pointer:
        tail_pointer = tail_pointer.get_next_node()
        count += 1
        if count >= n + 1:
            if nth_pointer == None:
                nth_pointer = linked_list.head_node
            else:
                nth_pointer = nth_pointer.get_next_node()
    return nth_pointer

def generate_test_linked_list():
    linked_list = LinkedList()
    for i in range(50, 0, -1):
        linked_list.insert_beginning(i)
    return linked_list

# Use this to test your code:
test_list = generate_test_linked_list()
print(test_list.stringify_list())
nth_last = nth_last_node(test_list, 4)
print(nth_last.value)

'''
2. Pointers at Different Speeds

Complete the find_middle() function and return the middle node of linked_list.
You can assume that the linked list has no cycles.

Return the right-weighted middle for even-length linked lists. For example, in
a linked list of 4 elements it should return the element at the third position.

Use generate_test_linked_list(length) to generate linked lists with values from
 1 -> 2 -> .. -> length to test out your function. For instance, 
 generate_test_linked_list(4) results in 1 -> 2 -> 3 -> 4.
'''
from LinkedList import LinkedList

# Complete this function:
def find_middle(linked_list):
    fast_pointer = linked_list.head_node
    slow_pointer = linked_list.head_node
    while fast_pointer:
        fast_pointer = fast_pointer.get_next_node()
        if fast_pointer:
            fast_pointer = fast_pointer.get_next_node()
            slow_pointer = slow_pointer.get_next_node()
    return slow_pointer

def generate_test_linked_list(length):
    linked_list = LinkedList()
    for i in range(length, 0, -1):
        linked_list.insert_beginning(i)
    return linked_list

# Use this to test your code:
test_list = generate_test_linked_list(7)
print(test_list.stringify_list())
middle_node = find_middle(test_list)
print(middle_node.value)
