# 9.Write a Program which takes a statement as input from the user and counts occurrences of each vowel in it.
str=input("Enter a string : ")
vowels="aeiouAEIOU"
print("Total vowel",len([v for v in str if v in vowels]))

count = {x:sum([1 for char in str if char == x]) for x in vowels}
print(count)#print  Direct Dictionary
for key, value in count.items():
  print(key, '->', value)#print key and value
