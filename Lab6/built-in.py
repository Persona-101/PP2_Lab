#exerice 1
import math
my_list = [1, 2, 5, 10]
mult = math.prod(my_list)
print(mult)

#exercise 2
def upper_lower(sentence):
    upper_cnt = 0
    lower_cnt = 0
    for i in sentence:
        if i.isupper() == True:
            upper_cnt += 1
        else:
            lower_cnt += 1
    print(upper_cnt, lower_cnt)
upper_lower("The cat sleeps peacefully")

#exercise 3
txt = str(input())
def is_palindrome(txt):
    rev_txt = "".join(reversed(txt))
    if txt == rev_txt:
        print("Palindrome")
    else:
        print("Not a palindrome")
is_palindrome(txt)

#exercise 4
import time
x = 25100
y = 2123
time.sleep(y / 1000)
print("Square root of ", x, " after ", y, " miliseconds is ", math.sqrt(x))

#exercise 5
my_tuple = (True, 1, 22)
x = all(my_tuple)
print(x)
