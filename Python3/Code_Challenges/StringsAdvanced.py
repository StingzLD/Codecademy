"""
1. Check Name

Write a function called check_for_name that takes two strings as parameters named sentence and name.
The function should return True if name appears in sentence in all lowercase letters, all uppercase letters,
or with any mix of uppercase and lowercase letters. The function should return False otherwise.

For example, the following three calls should all return True:
check_for_name("My name is Jamie", "Jamie")
check_for_name("My name is jamie", "Jamie")
check_for_name("My name is JAMIE", "Jamie")
"""
# Write your check_for_name function here:
def check_for_name(sentence, name):
    if name.lower() in sentence.lower():
        return True
    return False

# Uncomment these function calls to test your  function:
print(check_for_name("My name is Jamie", "Jamie"))
# should print True
print(check_for_name("My name is jamie", "Jamie"))
# should print True
print(check_for_name("My name is Samantha", "Jamie"))
# should print False


"""
2. Every Other Letter

Create a function named every_other_letter that takes a string named word as a parameter.
The function should return a string containing every other letter in word.
"""
# Write your every_other_letter function here:
def every_other_letter(word):
    new_string = ''
    for i in range(0, len(word), 2):
        new_string += word[i]
    return new_string

# Uncomment these function calls to test your function:
print(every_other_letter("Codecademy"))
# should print Cdcdm
print(every_other_letter("Hello world!"))
# should print Hlowrd
print(every_other_letter(""))
# should print 


"""
3. Reverse

Write a function named reverse_string that has a string named word as a parameter. The function should return word in reverse.
"""
# Write your reverse_string function here:
def reverse_string(word):
    new_word = ''
    for i in range(len(word)-1, -1, -1):
        new_word += word[i]
    return new_word

# Uncomment these function calls to test your  function:
print(reverse_string("Codecademy"))
# should print ymedacedoC
print(reverse_string("Hello world!"))
# should print !dlrow olleH
print(reverse_string(""))
# should print


"""
4. Make Spoonerism

Write a function called make_spoonerism that takes two strings as parameters named word1 and word2.
Finding the first syllable of a word is a difficult task, so for our function, we’re going to switch the first letters of each word.
Return the two new words as a single string separated by a space.
"""
# Write your make_spoonerism function here:
def make_spoonerism(word1, word2):
    new_word1 = word2[0] + word1[1:]
    new_word2 = word1[0] + word2[1:]
    return new_word1 + " " + new_word2

# Uncomment these function calls to test your function:
print(make_spoonerism("Codecademy", "Learn"))
# should print Lodecademy Cearn
print(make_spoonerism("Hello", "world!"))
# should print wello Horld!
print(make_spoonerism("a", "b"))
# should print b a


"""
5. Add Exclamation

Create a function named add_exclamation that has one parameter named word.
This function should add exclamation points to the end of word until word is 20 characters long.
If word is already at least 20 characters long, just return word.
"""
# Write your add_exclamation function here:
def add_exclamation(word):
    while len(word) < 20:
        word += "!"
    return word

# Uncomment these function calls to test your function:
print(add_exclamation("Codecademy"))
# should print Codecademy!!!!!!!!!!
print(add_exclamation("Codecademy is the best place to learn"))
# should print Codecademy is the best place to learn
