# 5.Write a Python program to get the difference between a given number and 17,
# if the number is greater than 17 return double the absolute difference.
print("if the number is greater than 17 return double the absolute difference.")
val1 = int(input("Enter number:"))

if val1 > 17:
    print("Double ",val1 * 2)
else:
    print("Difference ",17 - val1)
