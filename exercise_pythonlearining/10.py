# Write a Python program to check whether a specified value is contained in a group of values.
# Test Data :
# B. 3 -> [1, 5, 8, 3] : True
# C. -1 -> [1, 5, 8, 3] : False

def group_data(list,n):
    return n in list

print(group_data([1, 5, 8, 3,8,9,4],5))
print(group_data(['A', 'C','D','E','F','G','H',],'K'))