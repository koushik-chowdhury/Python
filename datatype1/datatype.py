# This cell demonstrates basic arithmetic operations
print(12 + 12)
print(2.5 * 5)
print(2 ** 100)
print(10/5)
print(10//5) # floor division : rounds the result down to the nearest whole number

# This cell imports the math library and demonstrates its usage
import math # module
print(math.pi)

# This cell demonstrates using the random library
import random

print(random.random())
print(random.choice([1, 2, 3, 4]))

# This cell shows string manipulation
username = "koushikchowdhury"

print(len(username))
print(username[0])
print(username[-1])
print(username[1:3])

# This cell demonstrates list creation and access
mylist = [123, "koushik", 3.14]

print(mylist)
print(len(mylist))
print(mylist[0])
print(mylist[2])

# This cell demonstrates dictionary creation and access
myd = {"one": "lemon", "two": "ginger", "comic": "ironman"}

print(myd)
print(myd["comic"])

# This cell demonstrates creating a tuple and accessing its element
mytp = (1, 2, 3, 4)

print(mytp)
print(mytp[0])

# This cell demonstrates boolean 
a = 10
b = 4

print(a < b)
print(b < a)