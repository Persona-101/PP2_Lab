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

def BoolFunction():
  return True
if BoolFunction():
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


#list
subjects = ["calculus", "PP2", "algebra", "econ", "PE", "PE"]
subjects[4] = "statistics"
print(subjects)
print(len(subjects))
print(type(subjects))
print(subjects[0])
print(subjects[-1])
print(subjects[1:4])
if "PP2" in subjects:
  print("Yes, it's in the list")

schedule = list(("calculus", "PP2", "algebra", "econ", "PE", "statistics"))
extra = ["finance", "banking"]
schedule[1:3] = ["data science", "advanced statistics"]
schedule.insert(4, "python")
schedule.append("business analytics")
schedule.extend(extra)
print(schedule)

mylist = [50, 20, 3, 6, 20]
mylist.remove(20)
mylist.pop(2)
del mylist[0]
print(mylist)
mylist.clear()
print(mylist)

list1 = ["phone number", "ID", "code"]
for x in list1:
  print(x)
list2 = ["USA", "UK", "Australia"]
for i in range(len(list2)):
  print(list2[i])
list3 = [1, 5, 8, 9]
i = 0
while i < len(list3):
  print(list3[i])
  i = i + 1

list4 = ["54", "21", "45", "8"]
newlist = [x for x in list4 if "4" in x]
print(newlist)
newlist2 = [x if x != "45" else "55" for x in list4]
print(newlist2)

fruits = ["Orange", "mango", "Kiwi", "pineapple", "Banana"]
fruits.sort()
print(fruits)
fruits.sort(reverse = True)
print(fruits)
fruits.sort(key = str.lower)
print(fruits)

numbers = [100, 50, 65, 82, 23]
numbers.sort()
print(numbers)
numbers.sort(reverse = True)
print(numbers)
numbers.reverse()
print(numbers)

code = [210, 526, 234, 847]
code2 = code.copy()
code3 = list(code)
code4 = code[:]
print(code2)
print(code3)
print(code4)

list1 = ["h", "e", "l", "l", "o"]
list2 = [" ", "c", "a", "t"]
list3 = list1 + list2
print(list3)

list1 = ["h", "e", "l", "l", "o"]
list2 = [" ", "c", "a", "t"]
for x in list2:
  list1.append(x)
print(list1)

list1 = ["h", "e", "l", "l", "o"]
list2 = [" ", "c", "a", "t"]
list1.extend(list2)
print(list1)


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


#while loop
i == 10
while i > 0:
  if i % 2 != 0:
    continue
  print(i)
  i -= 1
else:
  print("i is no longer a positive number")

i = 0
while i < 10:
  print(i)
  if i == 8:
    break
  i += 1
  

#for loop
shopping_list = ["carrot", "cucumber", "rice"]
for x in shopping_list:
  if x == "rice":
    break
  if x == "cucumber":
    continue
  print(x)

for x in range(1, 10, 2):
  print(x)
else:
  print("No more numbers")

subject = ["calculus", "algebra", "PP2"]
time = ["8am", "1pm", "3pm"]
for x in subject:
  for y in time:
    print(x, y)














