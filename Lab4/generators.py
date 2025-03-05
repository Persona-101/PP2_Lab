#exercise 1
N = int(input())
def square(Num):
    for i in range(Num):
        yield i ** 2
gen1 = square(N)
for i in gen1:
    print(i)

#exercise 2
n = int(input())
def even(num):
    for i in range(num):
        if i % 2 == 0:
            yield i
gen2 = even(n)
print(",".join(map(str, even(n))))

#exercise 3
n = int(input())
def divisible(num):
    for i in range(num):
        if i%3 == 0 and i%4 == 0:
            yield i
gen3 = divisible(n)
for i in gen3:
    print(i)

#exercise 4
a = int(input())
b = int(input())
def squares(min, max):
    for i in range(min, max + 1):
        yield i ** 2
gen4 = squares(a, b)
for i in gen4:
    print(i)

#exercise 5
n = int(input())
def output(num):
    while num >= 0:
        yield num
        num = num - 1
gen5 = output(n)
for i in gen5:
    print(i)
