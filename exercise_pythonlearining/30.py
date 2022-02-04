# 30.Define a global dictionary. Iterate through it and print the key and value of it separately in the following format.
# Key is <key> and Value is <value>.
# The loop statement should be enough to extract key and value,
# so don't use the "get" method or [] to extract the value from the dictionary.
student={1:'Sejal',2:'Hardik',3:'Harsh',4:'Yash'}

for key, value in student.items():
    print("Key is {} and Value is {}".format(key,value))