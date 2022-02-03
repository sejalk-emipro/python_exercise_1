#Write a Python program which accepts a sequence of comma-separated numbers from the user and generates a list and a tuple with those numbers.
inputValue=input("Enter Comma-separate number:")
#list=inputValue.split(',')
print('List :',inputValue.split(','))
print('Tuple : ',tuple(inputValue))
print('Set : ',set(inputValue))
print('Dictionary : ',tuple(inputValue))

