"""
1. Divisible By Ten

Create a function named divisible_by_ten() that takes a list of numbers named nums as a parameter.

Return the count of how many numbers in the list are divisible by 10.
"""
#Write your function here
def divisible_by_ten(nums):
    counter = 0
    for num in nums:
        if num % 10 == 0:
            counter += 1
    return counter

#Uncomment the line below when your function is done
print(divisible_by_ten([20, 25, 30, 35, 40]))


"""
2. Greetings

Create a function named add_greetings() which takes a list of strings named names as a parameter.

In the function, create an empty list that will contain each greeting. Add the string 'Hello, '
in front of each name in names and append the greeting to the list.

Return the new list containing the greetings.
"""
#Write your function here
def add_greetings(names):
    lst = []
    for name in names:
        lst.append('Hello, ' + name + '!')
    return lst

#Uncomment the line below when your function is done
print(add_greetings(["Owen", "Max", "Sophie"]))


"""
3. Delete Starting Even Numbers

Write a function called delete_starting_evens() that has a parameter named lst.

The function should remove elements from the front of lst until the front of the list is not even.
The function should then return lst.

For example if lst started as [4, 8, 10, 11, 12, 15], then delete_starting_evens(lst) should return [11, 12, 15].

Make sure your function works even if every element in the list is even!
"""
#Write your function here
def delete_starting_evens(lst):
    while len(lst) > 0 and lst[0] % 2 == 0:
        lst = lst[1:]
    return lst

#Uncomment the lines below when your function is done
print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))


"""
4. Odd Indices

Create a function named odd_indices() that has one parameter named lst.

The function should create a new empty list and add every element from lst that has an odd index.
The function should then return this new list.

For example, odd_indices([4, 3, 7, 10, 11, -2]) should return the list [3, 10, -2].
"""
#Write your function here
def odd_indices(lst):
    new_lst = []
    for index in range(1, len(lst), 2):
        new_lst.append(lst[index])
    return new_lst

#Uncomment the line below when your function is done
print(odd_indices([4, 3, 7, 10, 11, -2]))


"""
5. Exponents

Create a function named exponents() that takes two lists as parameters named bases and powers.
Return a new list containing every number in bases raised to every number in powers.

For example, consider the following code: exponents([2, 3, 4], [1, 2, 3])

The result would be the list [2, 4, 8, 3, 9, 27, 4, 16, 64]. It would first add two to the first.
Then two to the second. Then two to the third, and so on.
"""
#Write your function here
def exponents(bases, powers):
    lst = []
    for base in bases:
        for power in powers:
            lst.append(base ** power)
    return lst

#Uncomment the line below when your function is done
print(exponents([2, 3, 4], [1, 2, 3]))
