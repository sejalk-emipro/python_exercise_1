#12.Define a global dictionary with key & values. Iterate through it and print the key and value of it separately in the following format.
#Key is <key> and Value is <value>
Emps = {"Emp1":"Sejal", "Emp2":"Hardik", "Emp3":"Harsh"}
# inputEmpNames=input("Enter Comma-separate Employees Name: ")

EmpNames=inputEmpNames.split(',')
for key in Emps:
    print("Key is " + key + " and Value is " + Emps[key])