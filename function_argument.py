# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# Assignment: Functions
# Positional arguments are arguments that need to be included in the proper position or order.
# The first positional argument always needs to be listed first when the function is called.
# The second positional argument needs to be listed second and the third positional argument listed third, etc.
# First, positional-only arguments make sense when you have arguments that have a natural order but are hard to give good,
# descriptive names to. Another possible benefit of using positional-only arguments is that you can more easily refactor your functions.
# To solve the error, pass positional arguments in the right order and pass any keyword arguments after the positional ones.

def NameAge(name,age):
    print('Hi I am',name)
    print('My age is',age)
NameAge('vijay',32)

def show(a,b):
    print('a:',a)
    print('b:',b)
show(10,20)

def getgrade(names,score):
    if score > 80:
        grade = 'A'
    elif 80 > score > 70:
        grade = 'B'
    elif 70 > score > 60:
        grade = 'C'
    else:
        grade = 'D'
    print(names + " has grade " + grade)
getgrade('vijay',87)

    # keyword argument:
    # A keyword argument is where you provide a name to the variable as you pass it into the function.
    #  If there is a function with many parameters and we want to specify only a few from them,
    #  then this can be done by naming the arguments .
    #  These arguments are called keyword arguments.
    # There are two advantages - one, using the function is easier since we do not need to worry about the order of the arguments.
    # Two, we can give values to only those parameters which we want, provided that the other parameters have default argument values.

def my_function(child3, child2, child1):
        print("The youngest child is " + child3 )
my_function(child1='Amit', child2='Sumit', child3='Namit')

def display_info(first_name,last_name):
    print('First Name:',first_name)
    print('Last Name:',last_name)
display_info(last_name='Shinde',first_name='Vijay')

# Default Argument:
# In Python, a default parameter is defined with a fallback value as a default argument.
# Such parameters are optional during a function call. If no argument is provided,
# the default value is used, and if an argument is provided,
# it will overwrite the default value.

def add_numbers(a=25,b=45,c=75):
    sum = a+b+c
    print('Sum:',sum)
add_numbers(2,3,4)
add_numbers(2,3)
add_numbers()

def my_place(country='INDIA'):
    print("I am from " + country)
my_place()
my_place("USA")
my_place("ENGLAND")

# Variable Length Arguments:
# In Python, Variable-Length Arguments (or varargs) are a way to pass a variable number of arguments to a function.
# This means that you can pass any number of arguments to a function, and the function will handle them all.


def add_num(*args):
    sum = 0
    for num in args:
        sum += num
        return sum
result = add_num(1,2,3)
print('Sum is',result)
result = (10, 20, 30, 40)
print('Sum is',result)
22
result = add_num(5,6,7,8,9)
print('Sum is',result)
#

def multiply(*args):
    y = 1
    for num in args:
        y *= num
        print(y)
multiply(3, 7)
multiply(9, 8)
multiply(3, 4, 7)
multiply(5, 6, 10, 8)


#
def my_function(**kid):
    print("His last name is " + kid["lname"])
my_function(fname = "Aseet", lname = "Shinde")

# Positional Argument vs Keyword Argument:
# 1. Positional Argument:
# Order of positional argument matters.
# The number of arguments during function call should be equal to the Parameters passed
# in the function definition.

2. Keyword Argument:
# Order of the argument doesn't matter.
# In the case of Keyword Arguments, you pass the argument value along with the keyword
# during the function call.


# *args vs *kwargs:
# 1. *args (Non Keyword Arguments)
# Python has *args which allow us to pass the variable number of non keyword arguments
# to function.
# In the function, we should use an asterisk * before the parameter name to pass variable length arguments.
# The arguments are passed as a tuple and these passed arguments make tuple inside the function
# with same name as the parameter excluding asterisk *.
# for ex.
def adder(*num):
    sum = 0
    for n in num:
        sum = sum + n
    print('Sum:',sum)
adder(5,7)
adder(6,5,7,8)

2. *kwargs (Keyword Arguments)
# It allows us to pass the variable length of keyword arguments to the function.
# In the function, we use the double asterisk ** before the parameter name to denote this type of argument.
# The arguments are passed as a dictionary and these arguments make a dictionary inside function with name same as
# the parameter excluding double asterisk **.
# for ex.
def intro(**data):
    print("\nData type of argument:",type(data))
    for key, value in data.items():
        print("{} is {}".format(key,value))
intro(Firstname="Anita", Lastname="Sharma", Age=22, Phone=1234567890)
intro(Firstname="John", Lastname="Wood", Email="johnwood@nomail.com", Country="Wakanda", Age=25, Phone=9876543210)












