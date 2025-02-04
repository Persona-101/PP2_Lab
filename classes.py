#exercise 1
class my_class:
    def __init__(self, text):
        self.text = text
    def getString(self):
        self.text = input()
    def printString(self):
        print(self.text.upper())
x = my_class("sentence")
x.getString()
x.printString()


#exercise 2
class Shape:
    def __init__(self):
        pass
    def area(self):
        print("Area of the shape: ", 0)
class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length
    def area(self):
        print("Area of the square: ", self.length**2)

object1 = Shape()
object2 = Square(10)
object1.area()
object2.area()


#exercise 3
class Shape:
    def __init__(self):
        pass
    def area(self):
        print("Area of the shape: ", 0)
class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width
    def area(self):
        print("Area of the rectangle: ", self.length * self.width)

object3 = Shape()
object4 = Rectangle(10, 2)
object3.area()
object4.area()


#exercise 4
import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def show(self):
        print(f"The x coordinate is {self.x}. The y coordinate is {self.y}")
    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y        
        print(f"The new coordinates are ({self.x}, {self.y})")
    def dist(self, other_point):
        distance = math.sqrt((other_point.x - self.x)**2 + (other_point.y - self.y)**2)
        print(f"The distance is {distance}")
O = Point(0, 0)
A = Point(3, 4)
B = Point(8, 13)
O.show()
A.show()
B.show()
A.move(5, 16)
B.move(10, 15)
A.dist(B)


#exercise 5
class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. New balance is ${self.balance}")
    def withdraw(self, amount):
        if amount > self.balance:
            print("The amount exceeds the available balance")
        else:
            self.balance -= amount
            print(f"Withdrawn ${amount}. New balance is ${self.balance}")
money = Account("Kaspi", 1000)
money.deposit(500)
money.withdraw(1300)
money.withdraw(1800)