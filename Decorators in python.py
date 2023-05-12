# Without decorator

def school(func):
    def work():
        print("School work done")
        return func
    print("In the school of school")
    return work()

def M_home():
    print("at home,HomeWork Done")

var1 = school(M_home)

var1()

#-------------------------------------------------------------------------------

# With Decorator

print("After Using Decorator ---->")
@school
def holiday():
    print("Yay! Finally Holidays........")

holiday()
