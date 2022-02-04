#25. Write a Python program to count the number of strings in a list where
# the string length is 2 or more
# and the first and last character are the same from a given list of strings.
list=['abc','asa','010','xyz']

def rtnCount(list):

    c=0
    for l in list:
        if len(l)>2 and l[0]==l[-1]:
            c+=1
    return c

print(rtnCount(list))