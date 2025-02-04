#exercise 1
num = float(input())
def func_convert(grams):
    print(grams * 28.3495231)
func_convert(num)


#exercise 2
temp = float(input())
def func_temp(F):
    C = (5 / 9) * (F - 32)
    print(C)
func_temp(temp)


#exercise 3
heads = int(input())
legs = int(input())
def solve(numheads, numlegs):
    r = (numlegs - 2 * numheads) // 2
    c = numheads - r
    print(str(r) + " rabbits")
    print(str(c) + " chickens")
solve(heads, legs)


#exercise 4
def is_prime(the_list):
    for x in the_list:
        i = 1
        cnt = 0
        while i <= x:
            if x % i == 0:
                cnt += 1
            i += 1
        if cnt == 2:
            print(x)
my_list = [1, 2, 6, 11, 12, 13]
is_prime(my_list)


#exercise 5
from itertools import permutations
def the_permutations(inp):
    p_list = permutations(inp)
    for x in p_list:
        print("".join(x)) 
user_input = input()
the_permutations(user_input)


#exercise 6
my_string = str(input())
def reverse_func(string1):
    mylist = string1.split()
    mylist.reverse()
    string2 = " ".join(mylist)
    print(string2)
reverse_func(my_string)


#exercise 7
def has_33(given_list):
    for i in range(len(given_list) - 1):
        if given_list[i] == 3 and given_list[i + 1] == 3:
            state = True
            break
        else:
            state = False
    print(state)
has_33([1, 3, 3]) 
has_33([1, 3, 1, 3]) 
has_33([3, 1, 3]) 


#exercise 8
def spy_game(given_list):
    find = [0, 0, 7]
    i = 0
    for num in given_list:
        if num == find[i]:
            i += 1
        if i == 3:
            state = True
            break
        state = False
    print(state)
spy_game([1,2,4,0,0,7,5])
spy_game([1,0,2,4,0,5,7])
spy_game([1,7,2,0,4,5,0])


#exercise 9
import math
x = int(input())
def volume(radius):
    V = (4 / 3) * math.pi * (radius ** 3)
    print(V)
volume(x)


#exercise 10
def uniq_func(exist_list):
    newlist = []
    for x in exist_list:
        if x in newlist:
            continue
        else:
            newlist.append(x)
    print(newlist)
example_list = [1, 3, 5, 5, 8, 8]
uniq_func(example_list)


#exercise 11
my_word = str(input())
def palindrome(word):
    rev_word = word[::-1]
    if rev_word == word:
        print(True)
    else:
        print(False)
palindrome(my_word)


#exercise 12
def histogram(n):
    for i in n:
        print("*" * i)
My_list = [4, 9, 7]
histogram(My_list)


#exercise 13
import random
rand_num = random.randrange(1, 21)

def rand_func(x):
    print("Hello! What is your name?")
    name = input()
    print("Well, " + name + ", I am thinking of a number between 1 and 20.")
    print("Take a guess.")
    guess = int(input())
    cnt = 0
    while True:
        if guess < x:
            cnt += 1
            print("Your guess is too low. Take a guess.")
            guess = int(input())
        elif guess > x:
            cnt += 1
            print("Your guess is too high. Take a guess.")
            guess = int(input())
        elif guess == x:
            cnt += 1
            print("Good job, " + name + "! You guessed my number in " + str(cnt) + " guesses!")
            break

rand_func(rand_num)

