# 9.Write a Program which takes a statement as input from the user and counts occurrences of each vowel in it.
str=input("Enter a string : ")
vowels="aeiouAEIOU"
print(len([v for v in str if v in vowels]))
