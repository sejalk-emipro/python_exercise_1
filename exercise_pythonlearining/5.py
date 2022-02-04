# 5.Write a Python program to get the difference between a given number and 17,
# if the number is greater than 17 return double the absolute difference.
print("if the number is greater than 17 return double the absolute difference.")
val1 = int(input("Enter number:"))
d=17-val1
if val1 > 17:
    print("Double ",abs(d)*2)
else:
    print("Difference ",abs(d))
