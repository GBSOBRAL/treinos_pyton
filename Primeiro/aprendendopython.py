import sys
import math
import random
import threading
import time
from functools import reduce

# Comment
'''Comm
    ent'''

str1 = "Escape Sequences \' \" \t \\ \n hi"
age = 25
str3 = "Crazy Monkey"
div = "\n-------------------------\n"

#Básico

print("Cast", type(int(5.4)))
print("Cast", type(str(5.4)))
print("Cast", type(chr(97)))
print("Cast", type(ord('a')))
print("\n")

print(22, 11, 2000, sep="/")
print("No Newline", end="")
print("\n%04d %s %.2f %c" % (1, "Gustavo", 1.234, "A"))
print("\n")

print(3**2)

#Condições
print(div)

canVote = True if age >= 18 else False
print(canVote)

#Strings
print(div)

print(str3)
str4 = str3.replace("Monkey", "Dog")
print(str4)
str3 = str3[:6] + "m" + str3[7:]
print(str3)
print("Crazy" in str3)
print("Crazy" not in str3)
print("\n")

print(" ".join(["Some", "Words"]))
print("\n")

print("A String".split(" "))
print("\n")

int1 = int2 = 5
print(f"{int1} + {int2} = {int1 + int2}")
print("\n")

print(str4.upper())
print("\n")

print("A String 123".isalnum())
print("A String 123".isalpha())
print("A String 123".isdigit())
print("\n")

print("AString123".isalnum())
print("AString".isalpha())
print("123".isdigit())

#Listas
print(div)
print("LISTA")

l1 = [1, 3.14, "Derek", True]

print("Length", len(l1))
print("1st", l1[0])
print("Last", l1[-1])
print("\n")

l1[0] = 2
l1[2:4] = ["Bob", False]
l1[2:2] = ["Paul", 9]
l2 = l1 + ["Egg", 4]
l2.remove("Paul")
l2.pop(0)
print("l2", l2)
print("\n")
l2 = ["Egg", 4] + l1
print("\n")

l3 = [[1,2], [3,4]]
print("[1,1]", l3[1][1])
print("\n")

print("1 Exists", (1 in l1))
print("\n")
print("Min", min([1, 2, 3]))
print("\n")
print("Max", max([1, 2, 3]))
print("\n")
print(l1)
print("\n")
print("1dt 2", l1[0:2])
print("\n")
print("Every Other", l1[0:-1:2])
print("\n")
print("Reverse", l1[::-1])

#Loops
print(div)

w1 = 1
while w1 < 5:
    print(w1)
    w1 += 1

w2 = 0
while w2 <= 20:
    if w2 % 2 == 0:
        print(w2)
    elif w2 == 9:
        break
    else:
        w2 += 1
        continue
    w2 += 1
print("\n")

l4 = [1, 3.14, "Derek"]
while len(l4):
    print(l4.pop(0))
print("\n")

for x in range(0, 10):
    print(x, " ", end="")
print("\n")

l4 = [1, 3.14, "Derek"]
for x in l4:
    print(x)
print("\n")

for x in [2, 4, 6]:
    print(x)
print("\n")

#Iterators
print(div)

l5 = [6, 9, 12]
itr = iter(l5)
print(next(itr))
print(next(itr))
print(next(itr))
print("\n")

#Ranges
print(div)

print(list(range(0, 10)))
print(list(range(0, 10, 2)))
print("\n")

num_list = [[1, 2, 3], [10, 20, 30], [100, 200, 300]]
for x in range(0,3):
    for y in range(0,3):
        print(num_list[x][y])

#Tuple
#Listas que não podem ser editadas
print(div)

t1 = (1, 3.14, "Derek")
print("Length", len(t1))
print("1st", t1[0])
print("Last", t1[-1])
print("1st 2", t1[0:2])
print("Every Other", t1[0:-1:2])
print("Reverse", t1[::-1])

#Dictionaries
print(div)

heroes = {
    "Superman": "Clark Kent",
    "Batman": "Bruce Wayne"
}

print("Length", len(heroes))
print(heroes["Superman"])
heroes["Flash"] = "Barry Allan"
heroes["Flash"] = "Barry Allen"
print(list(heroes.items()))
print(list(heroes.keys()))
print(list(heroes.values()))

del heroes["Flash"]
print(heroes.pop("Batman"))
print("Superman" in heroes)
for k in heroes:
    print(k)

for v in heroes.values():
    print(v)

d1 = {"name": "Bread", "price": .88}
print("%(name)s costs $%(price).2f" % d1)

#sets
print(div)

s1 = set(["Derek", 1])
s2 = {"Paul", 1}

print("Length", len(s2))
s3 = s1 | s2
print(s3)
s3.add("Doug")
s3.discard("Derek")
print("Random", s3.pop())
s3 |= s2
print(s1.intersection(s2))
print(s1.symmetric_difference(s2))
print(s1.difference(s2))
s3.clear()
s4 = frozenset(["Paul", 7])

#Functions
print(div)

def get_sum(num1, num2):
    return num1 + num2

print(get_sum(5, 4))

def get_sum2(*args):
    sum = 0
    for arg in args:
        sum += arg
    return sum
print(get_sum2(1, 2, 3, 4, 5))

def next_2(num):
    return num + 1, num + 2

i1, i2 = next_2(5)
print(i1, i2)

def mult_by(num):
    return lambda x: x * num
print("3 * 5 =", mult_by(3)(5))

def mult_list(list, func):
    for x in list:
        print(func(x))
mult_by_4 = mult_by(4)
mult_list(list(range(0, 5)), mult_by_4)

power_list = [lambda x: x ** 2,
              lambda x: x ** 3]

#map
print(div)

one_to_4 = range(1, 5)
times2= lambda x: x * 2
print(list(map(times2, one_to_4)))

#filter
print(div)

print(list(filter(lambda x: x % 2 == 0, range(1,11))))

#reduce
print(div)

print(reduce((lambda x, y: x + y), range(1, 6)))

#exception handling
print(div)

'''while True:
    try:
        number= int(input("Digite um numero: "))
        break
    except ValueError:
        print("Voce não colocou um numero")
    except:
        print("Um erro inesperado aconetecu")
print("Obrigado")
'''
#file i/o
print(div)

with open("mydata.txt", mode="w", encoding="utf-8") as my_file:
    my_file.write("Some random text\nMore random text\nand more")

with open("mydata.txt", encoding="utf-8") as my_file:
    print(my_file.read())

print(my_file.closed)

#classes e objects
print(div)

class Square:
    def __init__(self, height="0", width="0"):
        self.height = height
        self.width = width

    @property
    def height(self):
        print("Retrieving the height")
        return self.__height

    @height.setter
    def height(self, value):
        if value.isdigit():
            self.__height = value
        else:
            print("Please enter only number for height")

    @property
    def width(self):
        print("Retrieving the height")
        return self.__height

    @width.setter
    def width(self, value):
        if value.isdigit():
            self.__width = value
        else:
            print("Please enter only number for width")

    def get_area(self):
        return int(self.__height) * int(self.__width)

square = Square()
square.height = "10"
square.width = "10"

print("Area", square.get_area())