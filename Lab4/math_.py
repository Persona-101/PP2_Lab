#exrcise 1
import math
degree = float(input())
def degree_to_radian(num):
    radian = num * math.pi / 180
    print(radian)
degree_to_radian(degree)

#exercise 2
height_input = float(input())
base1_input = float(input())
base2_input = float(input())
def trapezoid(height, base1, base2):
    area = (base1 + base2) * height * 0.5
    print(area)
trapezoid(height_input, base1_input, base2_input)

#exercise 3
import math
def polygon_area(n, side_length):
    return (n * side_length ** 2) / (4 * math.tan(math.pi / n))
n = int(input("Input number of sides: "))
side_length = float(input("Input the length of a side: "))
area = polygon_area(n, side_length)
print("The area of the polygon is:", round(area, 2))

#exercise 4
def parallelogram_area(base, height):
    return base * height
base = float(input("Length of base: "))
height = float(input("Height of parallelogram: "))
area = parallelogram_area(base, height)
print("The area of the parallelogram is:", area)
