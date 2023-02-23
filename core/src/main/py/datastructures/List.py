# list data structure
# list is an ordered items collection. items can be duplicated in the list.
# list can be used as Stack data structure: it contains pop() method + append() method

# how to create a list
# create a list using literal:
fruits = ["apple", "banana", "cherry"]
print(type(fruits))  # -><type 'list'>

# create a list using constructor.
thisList2 = list(("apple", "banana", "cherry"))
print(thisList2)  # ->['apple', 'banana', 'cherry']

# How to access a list
# visit through index. this is the Array data structure
print(fruits[1])  # ->"banana"

# add item to the list: append
fruits.append("orange")
print(fruits)  # ->['apple', 'banana', 'cherry', 'orange']

# sort api
days = ["SUNDAY", "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY"]
days.sort()
print(days)  # ->['FRIDAY', 'MONDAY', 'SATURDAY', 'SUNDAY', 'THURSDAY', 'TUESDAY', 'WEDNESDAY']
