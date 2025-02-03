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
my_list = [1, 2, 6, 11, 12, 13]
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
my_str = str(input())
def rev_func(str1):
    list1 = str1.split()
    list1.reverse()
    str2 = " ".join(list1)
    print(str2)
rev_func(my_str)


#exercise 7
given_list = [1, 3, 3, 5, 0]
def has_33(g_list):
    for i in range(len(g_list) - 1):
        if g_list[i] == 3 and g_list[i + 1] == 3:
            state = True
            break
        else:
            state = False
    print(state)
has_33(given_list)


#exercise 8
given_list = [0, 0, 7, 3, 5, 6]
def spy_game(g_list):
    for i in range(len(g_list) - 1):
        if g_list[i] == 0 and g_list[i + 1] == 0 and g_list[i + 2] == 7:
            state = True
            break
        else:
            state = False
    print(state)
spy_game(given_list)


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
e_list = [1, 3, 5, 5, 8, 8]
uniq_func(e_list)


#exercise 11
word = str(input())
def palindrome(input_w):
    rev_word = input_w[::-1]
    if rev_word == input_w:
        print(True)
    else:
        print(False)
palindrome(word)


#exercise 12
def histogram(n):
    for y in n:
        print("*" * y)
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

