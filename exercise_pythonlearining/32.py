# 32.students = {'Aex':{'class':'V', 'roll_id':2}, 'Puja':{'class':'V',’roll_id':3}}
# Using the above dictionary, print the following output.
# Aex
# class : V
# roll_id : 2
# Puja
# class : V
# roll_id : 3

students = {'Aex':
                {'class':'V', 'roll_id':2},
            'Puja':
                {'class':'V','roll_id':3}}

for k, v in students.items():
    print(k)
    for key,value in v.items():
        print('{} : {}'.format(key,value))


