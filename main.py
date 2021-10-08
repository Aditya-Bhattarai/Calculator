from addition import addition
from subtraction import subtract

print('Welcome to one of the worst calculator app where we dont even have a gui!')

action = input('''

What action would you like to perform?
- Addition
-Subtraction
-multiplication
-division
-Power
-Percentage

> ''')

if action == 'addition' or action == 'add':
    addition()
elif action == 'subtraction'.lower or action == 'subtract'.lower:
    subtract()
""" elif action == 'multiply'.lower or action == 'multiplication'.lower:
    multiply()
 """
