# 27.Define a global dictionary.
# Define a function which takes 2 values 1st as key and 2nd as value.
# The function should add those key values to the global dictionary.
student={1:'Sejal',2:'Hardik',3:'Harsh',4:'Yash'}

def take_two_value(k,v):
    student[k]=v
    print(student)

take_two_value(4,'Meera')
