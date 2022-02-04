# 33.Write a Python program to match key values in two dictionaries.
# Sample dictionary: {'key1': 1, 'key2': 3, 'key3': 2}, {'key1': 1, 'key2': 2}
# Expected output: key1: 1 is present in both x and y
a= {'key1': 1, 'key2': 3, 'key3': 2}
b={'key1': 1, 'key2': 2}

for (key, value) in set(a.items()) & set(b.items()):
    print('%s: %s is present in both x and y' % (key, value))

