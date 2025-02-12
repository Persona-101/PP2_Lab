#exercise 1
n = int(input())
class MyNumbers:
  def __init__(self, limit):
    self.limit = limit

  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= self.limit:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers(n)
myiter = iter(myclass)

for x in myiter:
  print(x)


#exercise 2
m = int(input())
class Numbers:
  def __init__(self, limit):
    self.limit = limit
  def __iter__(self):
    self.a = 1
    return self
  def __next__(self):
    while self.a <= self.limit:
      x = self.a
      self.a += 1
      if x % 2 == 0:
        return x 
    raise StopIteration

myclass2 = Numbers(m)
myiter2 = iter(myclass2)

for x in myiter2:
  print(x)


#exercise 3
k = int(input())
class NNumbers:
  def __init__(self, limit):
    self.limit = limit
  def __iter__(self):
    self.a = 1
    return self
  def __next__(self):
    while self.a <= self.limit:
      x = self.a
      self.a += 1
      if x % 3 == 0 and x % 4 == 0:
        return x 
    raise StopIteration

myclass3 = NNumbers(k)
myiter3 = iter(myclass3)

for x in myiter3:
  print(x)


#exercise 4
a = int(input())
b = int(input())

class squares:
  def __init__(self, begin, end):
    self.begin = begin
    self.end = end
  def __iter__(self):
    self.a = self.begin
    return self
  def __next__(self):
    while self.a <= self.end:
      x = self.a
      self.a += 1
      return x**2
    raise StopIteration

myclass4 = squares(a, b)
myiter4 = iter(myclass4)

for x in myiter4:
  print(x)


#exercise 5
h = int(input())

class num:
  def __init__(self, limit):
    self.limit = limit
  def __iter__(self):
    self.a = self.limit
    return self
  def __next__(self):
    while self.a >= 0:
      x = self.a
      self.a -= 1
      return x
    raise StopIteration

myclass5 = num(h)
myiter5 = iter(myclass5)

for x in myiter5:
  print(x)
