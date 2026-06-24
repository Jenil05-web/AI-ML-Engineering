import math
import random
import time

# This is my first Python Code
print("Hello i am Python !")
print("Hello my name is Jenil !")

#strings 
first_name = "Jenil"
food = "Pizza"

print(first_name)
print(f"i love {food}")

#Integers 

age = 18
quantity = 3


print(f"My age is {age}")
print(f"i like {quantity} pizzas!")

# Float

price = 10.12
gpa = 8.34
distance = 4.32

print(f"the price is ${price}")
print(f"My gpa is {gpa} in college")
print(f"I run {distance}km every day!")

# Boolean it has either true or false

is_student = True

print(f"Are you a student ?: {is_student}")

# Type casting : process of converting one variable into another data type
# str(), int() , float() , bool()

name = "Jenil"
age = 19
gpa = 8.9
is_student = True

gpa = int(gpa) # here we converted gpa in integer so in output we got 8

print(gpa)

age = float(age) # similar case for this also 

print(age)

# input() =  A Function that prompts the user to enter data Returns the entered data as a string


name = input('What is your name : ')

age = input("How old are you ?")

age = int(age)

age = age + 1


print(f"Hello{name}")
print("Happy Birthday")
print(f"You are {age}years old")

#Exercise 1 : Rectangle area

Length = input("Enter Length : ")

Breadth = input("Enter Breadth : ")

Height = input("Enter Height")

Height = float(Height)
Length = float(Length)
Breadth = float(Breadth)

area = Length * Breadth * Height
print(f"The are of rectangle is {area}m")

# Word Game

adjective1 = input("enter an adjective(description)")
noun1 = input("Enter a noun (person , place , thing)")
adjective2 = input("Enter an adjective (description)")
verb1 = input("Enter an verb ending with 'ing")
adjective3 =("Enter an description")

print(f"Today is went to a {adjective1}Zoo")
print(f"In an exibit , i saw a {noun1}")
print(f"{noun1} was {adjective2} and {verb1}")
print(f"i was {adjective3}")

# arithmetic operations : + , - , / , * , %


x = 3.14
y = 4
z = 5

result = round(x) # round() function will roundoff the value

result = abs(y) # it give absolute value , distance away from zero but whole number

result = pow(4 , 3) # it means 4 to the power 3 which is 64 !

result = max(x,y,z) # it will give as maximum value among numbers

# import math --> this will import library so that we can use more ready made math functions
# so after importing : go back to line 1 

# print(math.pi)
x = 9
result = math.sqrt(x)

#  Question :circumference of circle calculation

radius = int(input("Enter radius:"))

circumference = 2  * math.pi * radius
print(f"The circumference is :{round(circumference ,2)}")

# if = Do some code only if some conditon is true
# else do something else

#Logical Operators  evaluate multiple conditions (or , not , not)
# or = at least one condition mmust be true
# and = both conditions should be true
# not = invert the condition (not False , not True)

temp = 25
is_raining = False

if temp > 35 or temp<0 or is_raining:
    print("The outdoor event is cancelled!")

else :
    print("The outdoor event continues")

#conditional expression = A one-line shortcut foor the if-else statement (ternary operator)
# Print or assign one of two values based on condition 
# x if conditoin else y

# num = 5 
# a = 6
# b = 7
# age = 17

# print ("Positive" if num>0 else "Negative") 

name = input("Enter your full name :")

# len(value) it will give length of a string 
# find()  we can find any word using this but it will start finding from staring 
# rfind() it will find it from end
#name.capitalize() it will capitalize our name or word anything
# name.upper() it will convert the variable in uppercase 
# lower() it will convert in lower case
# result = name.isdigit() it will return number of digits only if the string is full of numbers
# 
# result = len(name)

result = name.find("")

print(result)


# Exercise
# 

username =  input("Enter  username :")

if len(username)<12:
    print("your username should dbe less then 12 char")

elif '' in username:
    print("username should not contain space")

elif not username.isalpha():
    print("username should not havve digit")

else : 
    print("valid username")

# String Indexing : accessing elements of a sequence using [] (indexing operator)

credit_number = "123-456-7890"
# 0 , 1 , 2 etc .. numbering just like an array 

print(credit_number[2])

#[start : end : step]
credit_number[0:4] # it will give first four digits of string / number

# format specifiers = {value"flags} format a value based on what flags are inserted

price1 = 3.123
price2 = -782.31
price3 = 12.35

print(f"price 1 is {price1 : .2f}") # it will give decimal values till 2 decimals
print(f"price 2 is {price2 : 0}") # each number will precede with zero
print(f"price 3 is {price3: .2f}")

# While loop  = execute some code WHILE some condition remains true

name = input("Enter your name:")


while  name == "":     #Meaning : while this conditon remains true execcute this below code foreever until the condition is not met
    print("You did not enter your name :")
else:
    print(f"Hello {name}")


food = input("Enter a food you like(q to quit)")

while not food == "q":
    print(f"you like this {food}")

food = input("Enter another food you like (q to quit):")
print("bye")

# for loops = execute a block of code a fixed number of times. you can iterate over a range , string , sequence etc...
for x in  range(1,11): # it will print numbers from 1 to 10 using range function 
    print(x)

account_number = "1-2345-6789-0"

for x in account_number :

    print(x)

    # nested loop 

    # identation : In simple terms, indentation is the empty space at the beginning of a line of code.

for x in range (3): # outer loop 


    for x in range (1,10): # inner loop 
        print(x , end="")

        # collections = single variables used to store multiple values

        # List = [] ordered and changeable. Duplicates OK
    # Set = {} unordered and immutable , but Add/Remove OK . No Duplicates
    # Tuple = () ordered and unchangeable . Duplicates OK . Faster

fruits = ["Apple , banana ,coconut"] # list 
fruits = {"Apple , banana ,coconut"} # set
print(fruits[0])

for fruit in fruits:
    print(fruit)

    # fruits.append -- to add eelements 
    # fruits.sort() it will sort the list{array}
    # fruits.reverse it will reverse the array 

    # 2D lists

    fruits =    ["Apple" , "orange" , "Berry"]
    vegetables =["Carrots" ,"Potatoes" , "celery"]
    meats =     ["chicken" , "fish" , "turkey"]

groceries = [fruits , vegetables , meats]

print(groceries[0]) # it will print fruits row j
# just imagine it like an matrix 

groceries = [["Apple" , "orange" , "Berry"] ,["Carrots" ,"Potatoes" , "celery"] ,["chicken" , "fish" , "turkey"] ]

for collection in groceries :
    for food in collection :
        print(food , end="")
        print()

        # dictionary = a collection of {key:value}pairs ordered and changeable . NO duplicates

        capitals = {"USA": "Washington D.C",
                    "India":"New Delhi",
                    "China": "beijing"}
        
        print(capitals.get("USA"))
    
    # capitals.update({"USA : L.A"})
    # capitals.pop("China")
    # capitals.popitem()
    # capitals.clear()
    keys = capitals.keys()
    print(capitals)

    items = capitals.items()
    for key , value in capitals.items():
        print(f"{key}:{value}")

# import random 

max_num = int(input("Enter maximum number :"))
min_num = int(input("Enter minimum number:"))


for range in max :
    number =  random.max(max_num,min_num)
print(max)
for min in number :
    num = random.min(max_num,min_num)
    print(number)

    # print("")
 # Function = A Block of reusable code  place () after the function name to invoke it
 
def happy_birthday(name,age ):
    print(f"Happy birthday {name}")
    print(f"You are old !{age}")
    print()

    happy_birthday("Jay",10)

# return = statement used to end a function 
# and send a result back to caller

def add(x,y):
    z = x+y
    return z

def divide(x,y):
    z = x/y
    return z

def multiply(x,y):
    z = x*y
    return z

print(multiply(1,2))
print(divide(1,2))

# default arguments = A default value for certain parameters
# default is used when that argument is omitted
# make your functions more flexible , reduces # of arguments
# 1. positional 2. DEFAULT 3. keyword, 4. arbitrary

# DEFAULT ARGUMENTS
def net_price(list_price , discount=0 , tax=0.05): # we gave default value to this Default argument
    return list_price *(1-discount)* (1+tax)

print(net_price(500))
print(net_price(500,0.1))


def count(end , start=0):
 for x in range(start,end+1):
        print(x)
        time.sleep(1)
        print("DONE!")

        count(10)

        # Keyword arguments = an argument preceded by an identifier order of arguments does'nt matter

def hello(greeting , title , first , last):
    print(f"{greeting}{title}{first}{last}")

    hello("Hello" , "Mr." ,"ram","Shyam")

#  *args = allows you to pass multiple non-key arguments
#  **kwargs = allows you to pass multiple keyword-arguments



# Iterables

numbers = [1,2,3,4,5,6]

for number in reversed(numbers):
    print(number)

# List comprehenison = A concise way to create lists in Python
# Compact and easier to read than traditional loops
# [expression for value in iterable if condition]

doubles = []

for x in range(1,11):
    doubles.append(x*2)
    print(doubles)


    doubles = [x*2 for x in range(1,11)] # list comprehension

    print(doubles) 

    triples = [ y*3 for y in range(1,11)] # in 
    # in sentence : for every y in range(1,11) multiply y*3

    print(triples)

numbers = [1,-2,3,-4,5,-6]
positive_nums = [num for num in numbers if num>=0]

print(positive_nums)

# scope resolution  = (LEGB) Local -> enclosed -> Global -> Built-in

def func1(): # its like our home 
    a = 1 # hhere 'a' is defined locally inside an function you cant use a in the function2
    # functions cant see each others value 
    print(a)

    def func2(): # neighbours home
        b = 2
        print(b)

        

class Food :
   def __init__(self , burgers , pizzas ,coldrinks) : # Parameterised Constructor ( because we passed values in it )
       self.burgers = burgers,
       self.pizzas = pizzas,
       self.coldrinks = coldrinks

       def restaurant(self):
           print("Welcome foodie")

f1 = Food("Bigmac" , "Cheesepizza" , "Coke")
f2 = Food("Macmaharaja" , "Italianpizza" , "Fanta")

print(f1.burgers , f2.pizzas , f1.coldrinks),
print(f2.burgers , f1.pizzas)


f1.restaurant()

del f1.burgers # delete method















    










