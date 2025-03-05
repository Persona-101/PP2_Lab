import re
txt = "The sun dipped below the horizon, painting the sky in shades of orange and pink. A gentle breeze rustled the leaves, whispering secrets of the coming night."

#exercise 1
x = re.findall("ab*", txt)
print(x)

#exercise 2
y = re.findall("ab{2,3}", txt)
print(y)

#exercise 3
z = re.findall("[a-z]+_[a-z]+" ,txt)
print(z)

#exercise 4
a = re.findall("[A-Z]{1}[a-z]+", txt)
print(a)

#exercise 5
b = re.findall("a.*b", txt)
print(b)

#exercise 6
c = re.sub(r"[ ,.]", ":", txt)
print(c)

#exercise 7
f = re.sub(r'_([a-z])', lambda match: match.group(1).upper(), txt)
print(f)

#exercise 8
d = re.split("[A-Z]", txt)
print(d)

#exercise 9
e = re.sub(r"([a-z])([A-Z])", r"\1 \2", txt)
print(e)

#exercise 10
g = re.sub(r'([a-z])([A-Z])', r'\1_\2', txt).lower()
print(g)
