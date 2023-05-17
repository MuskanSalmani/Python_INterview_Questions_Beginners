"""
Author = Muskan
date = 17/may/2023
"""


dicti1 = {1:"One",2:"Two",3:"Three",4:"Four",5:"Five"}


# Way-1
keys_list = list(dicti1.keys())
print(keys_list)

# Way-2 (Shortcut of above way-1)
dict_list = list(dicti1)
print(dict_list)

# Way-3
iter_list = [*dicti1.keys()]  # Using Iterable unpacking operator
print(iter_list)

# Way -4 (Shortcut to way-3)
x = [*dicti1]  # Using Iterable unpacking operator
print(x)

# Way-5
a = dicti1.keys()
print([i for i in a])

# Way-6
*c, = dicti1.keys()  # Using Iterable unpacking operator
print(c)

# Way -7
*d, = dicti1   # Using Iterable unpacking operator
print(d)