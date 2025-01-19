#home
print("Hello, World!")

#version 
import sys
print(sys.version)

#syntax
if 5 > 2:
    print("Five is greater than two!")

#This is a comment

"""
This is a comment
written in
more than just one line
"""

#variables
x, y = 5, "John"
print(x)
print(y)

x = "Sally"
print(x)

#casting
x = str(3)    
y = int(3)    
z = float(3)

#type
print(type(x))
print(type(y))
print(type(z))

#unpacking
fruits = ['apple', 'banana', 'cherry']
x, y, z = fruits
print(x, y, z)

#output
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

x = 5
y = 10
print(x + y)

#global and local variables
x = "awesome"
def myfunc():
  x = "fantastic"
  print("Python is " + x)
myfunc()
print("Python is " + x)

#global keyword
def myfunc():
  global x
  x = "fantastic"
myfunc()
print("Python is " + x)

#random number
import random
print(random.randrange(1, 10))

#type conversion
x = 1    
y = 2.8  
z = 1j  

a = float(x)
b = int(y)
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))
