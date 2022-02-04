# 15.Write a Python program to count the number occurrences of a specific character in a string.

str=input("Enter string : ")
# count=input("Enter Specific Character in a above enter string : ")
# print(str.count(count))
#Using set and count Individule charactore in string
print({i : str.count(i) for i in set(str)})
#Using Dict
res={}
for keys in str:
    res[keys] = res.get(keys, 0) + 1
print(res)
