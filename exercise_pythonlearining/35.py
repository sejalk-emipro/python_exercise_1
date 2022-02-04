# 35.Write a Python program to drop empty(None) Items from a given Dictionary.
# Original Dictionary - {'c1': 'Red', 'c2': 'Green', 'c3': None}
# New Dictionary after dropping empty items: {'c1': 'Red', 'c2': 'Green'}
a={'c1': 'Red', 'c2': 'Green', 'c3': None}
# res = dict(filter(None, ({key : val for key, val in sub.items() if val} for sub in a)))
print({key:value for (key, value) in a.items() if value is not None})