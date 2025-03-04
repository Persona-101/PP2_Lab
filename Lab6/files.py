#exerice 1
import os
path = r"C:\Users\user\OneDrive\Рабочий стол\PP1-PP2\PP2\Lab6"
print("Only directories:")
print([ name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name)) ])
print("Only files:")
print([ name for name in os.listdir(path) if not os.path.isdir(os.path.join(path, name)) ])
print("All directories and files :")
print([ name for name in os.listdir(path)])

#exerice 2
print("\n")
f = open(r"C:\Users\user\OneDrive\Рабочий стол\PP1-PP2\PP2\Lab6\practicef.txt", "a")
f.write("Now the file has more content!")
f.close()
f = open(r"C:\Users\user\OneDrive\Рабочий стол\PP1-PP2\PP2\Lab6\practicef.txt", "r")
print(f.read())

#exerice 3
import os
print("\n")
print("Test a path exists or not:")
path = r"C:\Users\user\OneDrive\Рабочий стол\PP1-PP2\PP2\Lab6\practicef.txt"
print(os.path.exists(path))
print("\nFile name of the path:")
print(os.path.basename(path))
print("\nDir name of the path:")
print(os.path.dirname(path))


#exerice 4
f = open(r"C:\Users\user\OneDrive\Рабочий стол\PP1-PP2\PP2\Lab6\practicef.txt", "r")
lines = len(f.readlines())
print(lines)

#exerice 5
my_list = [1, 2, 3, 4, 5]
f = open(r"C:\Users\user\OneDrive\Рабочий стол\PP1-PP2\PP2\Lab6\practicef.txt", "w")
for i in my_list:
    f.write(str(i))
f.close()
f = open(r"C:\Users\user\OneDrive\Рабочий стол\PP1-PP2\PP2\Lab6\practicef.txt", "r")
print(f.read())

#exerice 6
import string
if not os.path.exists("letters"):
   os.makedirs("letters")
for letter in string.ascii_uppercase:
   with open(letter + ".txt", "w") as f:
       f.writelines(letter)

#exerice 7
with open(r"C:\Users\user\OneDrive\Рабочий стол\PP1-PP2\PP2\Lab6\practicef.txt",'r') as firstfile, open(r"C:\Users\user\OneDrive\Рабочий стол\PP1-PP2\PP2\Lab6\file2.txt",'a') as secondfile:
    for line in firstfile:
        secondfile.write(line)

#exerice 8
if os.path.exists(r"C:\Users\user\OneDrive\Рабочий стол\PP1-PP2\PP2\Lab6\file2.txt"):
  os.remove(r"C:\Users\user\OneDrive\Рабочий стол\PP1-PP2\PP2\Lab6\file2.txt")
else:
  print("The file does not exist")
