# 4.Write a Python program to get the volume of a sphere with radius 15.
# Formula - 4/3 πr3

pi=22/7
radius = float(input('Radius of sphere: '))
volume = (4/3) * (pi * radius ** 3)
print("Volume is: ", volume)