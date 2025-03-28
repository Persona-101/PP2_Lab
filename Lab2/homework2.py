#boolean
print(4 > 1)

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

def BoolFunction():
  return True
if BoolFunction():
  print("True")
else:
  print("False")

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

list_1 = [1, 2, 5, 8, 5]
x = list_1.count(5)
y = list_1.index(8)
print(x)
print(y)


#tuples
tuple1 = ("ffjfn", True, "hbhdf", "abab", 12, True)
print(tuple1)
print(len(tuple1))
a = tuple1.count(12)
print(a)
b = tuple1.index(12)
print(b)

tuple2 = ("nana",)
print(type(tuple2))

both_tuples = tuple1 + tuple2
print(both_tuples)

m_tuple = tuple2 * 2
print(m_tuple)

tuple1 += tuple2
print(tuple1)

tuple3 = tuple(("bd", "time", 256))
print(tuple3[0])
print(tuple[:2])
print(tuple[1:])
if "time" in tuple3:
  print("True")

t = (21, 54, 23)
m = list(t)
m[0] = 55
m.append(83)
m.remove(54)
t = tuple(m)
print(t)
del t

books = ("mo dao zu shi", "tian guan ci fu", "Pride and prejudice", "Harry Potter")
(*first, second, third) = books
print(first)
print(second)
print(third)

tuple4 = (1, 2, 3, 4, 5)
for x in tuple4:
  print(x)
for i in range(len(tuple4)):
  print(tuple4[i])
i = 0
while i < len(tuple4):
  print(tuple4[i])
  i += 1


#set
colors = {"red", "green", "blue", "red", True, 1, 0, False}
print(len(colors))
print(type(colors))
print(colors)

colors = set(("red", "green", "blue"))
for x in colors:
  print(x)
print("red" in colors)
print("red" not in colors)

colors = {"red", "green", "blue"}
colors2 = ["orange", "violet"]
colors.update(colors2)
colors.add("white")
colors.remove("red")
colors.discard("orange")
x = colors.pop()
print(x)
print(colors)

games = {"Zelda", "Persona 4", "Ace attorney"}
games2 = {"Persona 5", "Ace attorney"}
games3 = {"Danganronpa", "Resident evil", "Zelda"}
games4 = {"Resident evil", "Mario kart"}
union_set = games.union(games2, games3)
print(union_set)
intrs = games.intersection(games2)
print(intrs)
games2.intersection_update(games)
print(games2)
diff = games.difference(games3)
print(diff)
games.difference_update(games3)
print(games)
sdiff = games3.symmetric_difference(games4)
print(sdiff)
games3.symmetric_difference_update(games4)
print(games3)

a = {"a", "g", "c", "e", "b"}
b = {"a", "b", "c"}
z = a.isdisjoint(b)
print(z)
z = b.issubset(a)
print(z)
z = a.issuperset(b)
print(z)


#dictionary
dict1 = {
  "brand": "Samsung",
  "year": 2015,
  "screen" = "LCD",
  "screen" = "OLED"
  "tech": ["smartphone", "laptop", "charging cable"]
}
print(dict1)
print(len(dict1))
print(dict1["brand"])
x = dict1.get("year")
print(x)
y = dict1.keys()
print(y)
z = dict1.values()
print(z)
i = dict1.items()
print(i)

dict2 = dict(name = "Sabina", age = 20, occupation = "student")
dict2["age"] = 21
dict2.update({"name": "Sabina Khalidullina"})
dict2["university"] = "KBTU"
dict2.update({"major": "Data Science"})
dict2.pop("occupation")
dict2.popitem()
del dict2["age"]

for x in dict2.keys():
  print(x)
for x in dict2.values():
  print(x)
for x, y in dict2.items():
  print(x, y)

dict3 = dict2.copy()
mydict = dict(dict3)
print(dict3)
print(mydict)

studies = {
  "calculus" : {
    "hours per week" : 3,
    "grade" : 81
  },
  "algebra" : {
    "hours per week" : 3,
    "grade" : 89
  },
  "statistics" : {
    "hours per week" : 4,
    "grade" : 77
  }
}

for x, obj in studies.items():
  print(x)

  for y in obj:
    print(y + ':', obj[y])


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














