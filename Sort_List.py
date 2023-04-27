"""
Author:Muskan Salmani, Date: 11/MArch/2023

1.Sorting a list in python without using pre-defined sort() function

Uncomment code to use
"""

list = [9,8,7,4,1,2]
n = len(list)
for i in range(n):
    for j in range (i+1,n):
      if list[i] > list[j]:
        list[i], list[j] = list[j], list[i]

print(list)
# output : [1, 2, 4, 7, 8, 9]


# 2.Sorting a list in python with  sort() function

l = [9,7,4,3]
l.sort()
print(l)

# output: [3, 4, 7, 9]

