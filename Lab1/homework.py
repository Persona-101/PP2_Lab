#home
print("Hello, World!")

#version 
import sys
print(sys.version)

#syntax
if 4 > 3:
    print("Four is greater than three")

#This is a comment

"""
This is a comment
written in
more than just one line
"""

#variables
x, y = 10, "Cat"
print(x)
print(y)

#casting
x = str(9)    
y = int(9)    
z = float(9)

#type
print(type(x))
print(type(y))
print(type(z))

#unpacking
fruits = ['kiwi', 'pineapple', 'lemon']
x, y, z = fruits
print(x, y, z)

#output
x = "Today "
y = "is "
z = "Sunday"
print(x + y + z)

x = 7
y = 11
print(x + y)

#global and local variables
x = "Sunday"
def myfunc():
  x = "Tuesday"
  print("Today is " + x)
myfunc()
print("Today is " + x)

#global keyword
def myfunc():
  global x
  x = "Bob"
myfunc()
print("His name is " + x)

#random number
import random
print(random.randrange(1, 100))

#type conversion
x = 8    
y = 3.3  
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

#strings
print("I am learning 'python'")

a = """Gbfbfknaj
fhbfhkfb
fjnfskjfeklkamm
kjfflksefk"""
print(a)

a = "I'm 20 years old"
print(a[1])

for x in "apple":
  print(x)

a = "I'm 20 years old"
print(len(a))

txt = "Chinese language is difficult"
if "language" in txt:
  print("Yes, 'language' is present.")

txt = "Chinese language is difficult"
if "Korean" not in txt:
  print("No, 'Korean' is NOT present.")

b = "Smartphone"
print(b[2:5])
print(b[:5])
print(b[2:])
print(b[-5:-2])

a = "Smartphone"
print(a.upper())
print(a.lower())
print(a.strip())
print(a.replace("p", "c"))
print(a.split(","))

a = "My"
b = "name"
c = a + " " + b
print(c)

age = 20
txt = f"My name is Sabina, I am {age}"
print(txt)

price = 22000
txt = f"The price is {price:.2f} tenge"
print(txt)

txt = "I a \"second\" year student"
