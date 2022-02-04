# Write a Python program to check if all values are the same in a dictionary.
# Original Dictionary:{'Cierra Vega': 23, 'Alden Cantrell': 23, 'Kierra Gentry': 23, 'Pierre Cox': 23}
# Check all are 23 in the dictionary.
# True
# Check all are 10 in the dictionary.
# False
# Check if any one value in the dictionary is 25
# False

d={'Cierra Vega': 23, 'Alden Cantrell': 23, 'Kierra Gentry': 23, 'Pierre Cox': 23}

def check_value(n):
    print(all(x == n for x in d.values()))
print('Check all are 23 in the dictionary.')
check_value(23)
print('Check all are 10 in the dictionary.')
check_value(10)
print('Check if any one value in the dictionary is 25')
check_value(25)
