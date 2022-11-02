import sys
import logging
import numpy as np
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s')

def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if (b == 0):
        logging.error("Not division by zero!")
    else:
        return a / b

print(f"""
Which action do you want to perform? 
Choose: 
1. Addition
2. Subtraction
3. Multiplication
4. Division
""")
choice = input("Your choice: ")
result = None
action = None
if (choice != '1' and choice != '2' and choice != '3' and choice != '4'):
    logging.warning("Not choose correct option")
else:
    arg = input("Give number and separate it by comma (if you chose addition or multiplication you can give more then two numbers): ")
    arg_list = arg.split(',')
    try: arg_list_numbers = [float(item) for item in arg_list]
    except: ValueError: logging.error("Given elements not numbers")
    else:
        if (len(arg_list_numbers) < 2):
            logging.warning("Too less numbers, cannot calculate, result will be a given number")
        if ((choice == '2' or choice == '4' ) and len(arg_list_numbers) > 2):
            logging.warning("Only two first numbers will be taken to action")
        if (choice == '2'):
            result = arg_list_numbers[0] - arg_list_numbers[1]
            action = "subtraction"
        elif (choice == '4'):
            action = "division"
            if (arg_list_numbers[1] == 0.0):
                logging.error("Cannot division by zero!")
            else:
                result = arg_list_numbers[0] / arg_list_numbers[1]
        elif (choice == '1'):
            result = sum(arg_list_numbers)
            action = "addition"
        else:
            result = np.prod(arg_list_numbers)
            action = "multiplication"
        print(f"You chose {action} for numbers {arg_list_numbers}, result is {result}")
        
