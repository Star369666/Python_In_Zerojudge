import random

# Q1
odd_or_even = int(input("Enter a number to check if it is a odd number: "))

print(f"If this is a odd number: {bool(odd_or_even % 2)}\n")

# Q2
toRoot = float(input("Enter a number to find it's root: "))

print(f"{toRoot**(1/2)} is the root of {toRoot}\n")

# Q3
print(f"The random result is {random.randrange(1, 6)}\n")

# Q4
list_check = ["1", "True", "2", "star", "3", "False", "aaa"]
Target = input("Enter a string to find if it exist: ")

def to_check(find, list):
    return(list.index(find))
    
print(f"If the input exists in the list: {to_check(Target, list_check)}")