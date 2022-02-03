# 6.Write a Python program to calculate the sum of three given numbers,
# if the values are equal then return three times of their sum.

def sum_of_number(x,y,z):
        sum=x+y+z
        if x==y==z:
            sum=sum*3
        return sum
print(sum_of_number(2,3,4))
print(sum_of_number(5,5,5))

Num1=int(input("Enter First Number : "))
Num2=int(input("Enter Second Number : "))
Num3=int(input("Enter Third Number : "))

if Num1==Num2==Num3:
    print("three times : ",(Num3+Num2+Num1)*3)
else:
    print("Simple Sum Of There Number : " ,(Num3+Num2+Num1))

