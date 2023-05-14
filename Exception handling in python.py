
try:
    exp = 2 / 0
except ZeroDivisionError:
    print("Division by 0 error")
else:
    print("If there is no exception then this block will be executed")
finally:
    print("This block will get executed either exception is generated or not")