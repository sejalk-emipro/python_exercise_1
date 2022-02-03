# 8.Write a Python program to test whether a passed letter is a vowel or not.

letter=input("Enter a letter :")
if letter in ('a', 'e', 'i', 'o', 'u'):
        print(letter,"is vowel")
elif letter in ('A', 'E', 'I', 'O', 'U'):
        print(letter,"is vowel")
else:
        print(letter,"is not vowel")
