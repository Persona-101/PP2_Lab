#boolean
print(4 > 1)
print(40 == 23)
print(5 < 0)


x = 50
y = 2
if x > y:
  print("x is greater than y")
else:
  print("x is not greater than y")


print(bool("Abc"))
print(bool(""))
print(bool(15))
print(bool(0))
print(bool(["a", "b", "c"]))
print(bool([]))
print(bool(None))


class myclass():
  def __len__(self):
    return 0
myobj = myclass()
print(bool(myobj))


def myFunction() :
  return True
if myFunction():
  print("YES!")
else:
  print("NO!")


x = 8.8
print(isinstance(x, int))

#python operators
a = 3
b = 5
a += 5
print(a + b)
print(a != b)
print(a < 10 and b > 0)
print(a is b)
print(a << 3)


x = [5, 6, 7]
print(6 in x)


print((2 + 99) * (5 - 24) + 56)


#if else
x = 10
y = 13
z = 50
if x < z and y < z: 
  print("z is greater than x and y")
elif x > z and y > z:
  print("x and y are greater than z")
else:
  print("other option")


age = 40
if age >= 16:
  print("You can get driver's license")
  if age >= 18:
    print("You can take out a loan")
  else:
    print("Not eligible for loan")
else:
  print("Not eligible for driver's license")


a = 1
b = 2
if a != b:
  pass

