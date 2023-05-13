"""
Author = Muskan
date = 13/may/2023


#1. use of  break statement
The break statement is used to terminate the loop or statement in which it is present.
After that, the control will pass to the statements that are present after the break statement, if available.

"""

for i in range(100):
    if i ==10:
        break
    print(i)


#2. use of continue statement: Continue is also a loop control statement just like the break statement.
# continue statement is opposite to that of break statement, instead of terminating the loop,
# it forces to execute the next iteration of the loop.

for i in range(100):
    if i%2 ==0:
        continue
    print(i)


# 3use of pass statement:As the name suggests pass statement simply does nothing
def test():
    pass