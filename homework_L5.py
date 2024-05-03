# Lesson 5: Assignments | Python Functions
# 1. The Calculator App
# Objective:
# The aim of this assignment is to build a basic calculator that can perform addition, subtraction, multiplication, and division.
# Task 1: Create functions for each arithmetic operation.
# Task 2: Implement user input to receive numbers and an operation choice.
# Task 3: Ensure your program can handle division by zero and other potential errors.
# num1 = int(input("Enter a number: "))
# num2 = int(input("Enter another number: "))
# operator = input("Enter an operator (+, -, *, /, %): ")  # Asking the user to enter an operator
# def arithmetic_operations(num1, num2, operator):
#     if operator == "+":
#         return num1 + num2
#     elif operator == "-":
#         return num1 - num2
#     elif operator == "*":
#         return num1 * num2
#     elif operator == "/":
#         return num1 / num2
#     elif operator == "%":
#         return num1 % num2
#     else:
#         return "Invalid operator"
# result = arithmetic_operations(num1, num2, operator)  # Calculating the result
# print(f"{num1} {operator} {num2} = {result}")


# 2. The Shopping List Maker
# Objective:
# The aim of this assignment is to create a program that helps users make a shopping list.
# Task 1: Write a function that lets the user add items to a list.
# Task 2: Include a feature to remove items from the list.
# Task 3: Add a function that prints out the entire list in a formatted way.

def shopping_list_maker():
    shopping_list = []  # Initialize an empty list to store items
    
    def add_item(item):
        shopping_list.append(item)  # Add item to the shopping list
    
    def remove_item(item):
        if item in shopping_list:
            shopping_list.remove(item)  # Remove item from the shopping list
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
        action = input("Enter 'add' to add an item, 'remove' to remove an item, or 'done' to finish: ")
        
        if action == "add":
            item = input("Enter an item to add: ")
            add_item(item)
            print(f"You added {item} to your list.")
        elif action == "remove":
            item = input("Enter an item to remove: ")
            remove_item(item)
            print(f"You no longer need {item}.")
        elif action == "done":
            print_list()
            break
        else:
            print("Invalid action. Please try again.")

shopping_list_maker()