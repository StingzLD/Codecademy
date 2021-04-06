"""
1. Word Length Dict

Write a function named word_length_dictionary that takes a list of strings named words as a parameter.
The function should return a dictionary of key/value pairs where every key is a word in words and every value is the length of that word.
"""
# Write your word_length_dictionary function here:
def word_length_dictionary(words):
    word_dict = {}
    for word in words:
        word_dict[word] = len(word)
    return word_dict

# Uncomment these function calls to test your  function:
print(word_length_dictionary(["apple", "dog", "cat"]))
# should print {"apple":5, "dog": 3, "cat":3}
print(word_length_dictionary(["a", ""]))
# should print {"a": 1, "": 0}


"""
2. Frequency Count

Write a function named frequency_dictionary that takes a list of elements named words as a parameter.
The function should return a dictionary containing the frequency of each element in words.
"""
# Write your frequency_dictionary function here:
def frequency_dictionary(words):
    word_freq = {}
    for word in words:
        if word not in word_freq:
            word_freq[word] = 0
        word_freq[word] += 1
    return word_freq

# Uncomment these function calls to test your  function:
print(frequency_dictionary(["apple", "apple", "cat", 1]))
# should print {"apple":2, "cat":1, 1:1}
print(frequency_dictionary([0,0,0,0,0]))
# should print {0:5}


"""
3. Unique Values

Create a function named unique_values that takes a dictionary named my_dictionary as a parameter.
The function should return the number of unique values in the dictionary.
"""
# Write your unique_values function here:
def unique_values(my_dictionary):
    list = []
    for value in my_dictionary.values():
        if value not in list:
            list.append(value)
    return len(list)

# Uncomment these function calls to test your  function:
print(unique_values({0:3, 1:1, 4:1, 5:3}))
# should print 2
print(unique_values({0:3, 1:3, 4:3, 5:3}))
# should print 1


"""
4. Count First Letter

Create a function named count_first_letter that takes a dictionary named names as a parameter.
names should be a dictionary where the key is a last name and the value is a list of first names.

For example, the dictionary might look like this:
names = {"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}

The function should return a new dictionary where each key is the first letter of a last name,
and the value is the number of people whose last name begins with that letter.
So in example above, the function would return: {"S" : 4, "L": 3}
"""
# Write your count_first_letter function here:
def count_first_letter(names):
    letter_dict = {}
    for key, value in names.items():
        if key[0] not in letter_dict:
            letter_dict[key[0]] = 0
        letter_dict[key[0]] += len(value)
    return letter_dict

# Uncomment these function calls to test your  function:
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 4, "L": 3}
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Sannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 7}
