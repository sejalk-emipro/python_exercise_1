# Write a Python program to check if all values are the same in a dictionary.
# Original Dictionary:{'Cierra Vega': 23, 'Alden Cantrell': 23, 'Kierra Gentry': 23, 'Pierre Cox': 23}
# Check all are 23 in the dictionary.
# True
# Check all are 10 in the dictionary.
# False
# Check if any one value in the dictionary is 25
# False

d={'Cierra Vega': 23, 'Alden Cantrell': 23, 'Kierra Gentry': 25, 'Pierre Cox': 23}

def check_value_all(n):
    print(all(x == n for x in d.values()))

def check_value_any(n):
    print(any(n for v in d.values()))
# print('Check all are 23 in the dictionary.')
check_value_all(int(input('Check all are 23 in the dictionary:')))
# print('Check all are 10 in the dictionary.')
check_value_all(input('Check all are 10 in the dictionary:'))
# print('Check if any one value in the dictionary is 25')
check_value_any(input('Check if any one value in the dictionary is 25:'))
