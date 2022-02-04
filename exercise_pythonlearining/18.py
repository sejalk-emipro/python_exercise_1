# 18.Write a Python program to print out a set containing all the colors from color_list_1 which are not present in color_list_2. Also find which values are common in both the lists.
# Test Data :
# color_list_1 = set(["White", "Black", "Red"])
# color_list_2 = set(["Red", "Green"])
# Expected Output :
# {'Black', 'White'}
color_list_1 = set(["Sejal", "Hardik", "Harsh"])
color_list_2 = set(["Harsh", "Shankar"])
print("The colors from color_list_1 which are not present in color_list_2 :",color_list_1.difference(color_list_2))
print("The colors from color_list_2 which are not present in color_list_1 :",color_list_2.difference(color_list_1))
print("common in both the lists : ",color_list_2.intersection(color_list_1))


