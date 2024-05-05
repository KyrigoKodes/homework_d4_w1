# Lesson 5: Assignments | Python Functions
# 1. The Calculator App
# Objective:
# The aim of this assignment is to build a basic calculator that can perform addition, subtraction, multiplication, and division.
# Task 1: Create functions for each arithmetic operation.
# Task 2: Implement user input to receive numbers and an operation choice.
# Task 3: Ensure your program can handle division by zero and other potential errors.
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
operator = input("Enter an operator (+, -, *, /, %): ")  # Asking the user to enter an operator
def arithmetic_operations(num1, num2, operator):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        return num1 / num2
    elif operator == "%":
        return num1 % num2
    else:
        return "Invalid operator"
result = arithmetic_operations(num1, num2, operator)  # Calculating the result
print(f"{num1} {operator} {num2} = {result}")


# 2. The Shopping List Maker
# Objective:
def shopping_list_maker():
    shopping_list = []  # Initialize an empty list to store items
        
    def add_item(item):
            shopping_list.append(item)  # Add item to the shopping list
        
    def remove_item(item):
        if item in shopping_list:
            shopping_list.remove(item)  # Remove item from the shopping list
            print(f"You no longer need {item}.")
        else:
            print(f"{item} is not in the shopping list.")
        
    def print_list():
        if len(shopping_list) == 0:
            print("Your shopping list is empty.")
        else:
            print("Your shopping list:")
            for item in shopping_list:
                print(item)
        
        # Allow an input from the user to add, remove, or finish adding items to a list
    while True:
        action = int(input("Enter '1' to add an item, '2' to remove an item, '3' to see your list, or '4' to finish: "))
            
        if action == 1:
            item = input("Enter an item to add: ")
            add_item(item)
            print(f"You added {item} to your list.")
        elif action == 2:
            item = input("Enter an item to remove: ")
            remove_item(item)
        elif action == 3:
            print_list()
        elif action == 4:
            print_list()
            break
        else:
            print("Invalid action. Please try again. Your number must be between 1 and 4.")
shopping_list_maker()