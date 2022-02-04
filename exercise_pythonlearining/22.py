# 22.Create a function which takes a value.
# Define a global dictionary.
# The function should be able to display a statement whether the passed value is in the dictionary or not.

student={1:'Sejal',2:'Hardik',3:'Harsh',4:'Yash'}

def is_value_exit(value):
    if value in student.values():
         print('value exits')
    else:
         print('value is not exist')

is_value_exit(input("Enter a value :"))

