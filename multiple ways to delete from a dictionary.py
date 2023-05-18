"""
Author = Muskan
date = 18/may/2023
"""

diction1 = {
  "brand": "Ford",
  "model": "Mustang",
  "launch_year": 1964,
  "current_year": 2023
}

#way-1
d1 = diction1.clear()
print(d1)  # all key,value pair deleted


#way-2

diction2 = {
  "brand": "Ford",
  "model": "Mustang",
  "launch_year": 1964,
  "current_year": 2023
}

d2 = diction2.pop('brand')
print(d2)


#way-3

diction3 = {
  "brand": "Ford",
  "model": "Mustang",
  "launch_year": 1964,
  "current_year": 2023
}
del diction3['model']
print(diction3)