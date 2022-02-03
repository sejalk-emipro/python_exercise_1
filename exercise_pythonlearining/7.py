# 7.Write a Python program to get a string which is n (non-negative integer) copies of a given string.
str=input("Enter your name : ")
copy=int(input("How many time copies your name : "))
rtn=""
for r in range(copy):
    rtn+=str

print(rtn)
