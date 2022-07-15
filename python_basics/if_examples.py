### Verious examples of IF ELSE in python
x = 5

if (x > 3):
    print(f"{x} is grater than 3")

# parentheses are optional

if x > 3:
    print(f"{x} is grater than 3")

x = 10

if x > 3 and x < 6:
    print(f"{x} is between than 3 and 6 ")
else:
    print(f"{x} is not between 3 and 6")

######################################################
number = 5
if number%2 == 0:
    isEven = True
else:
    isEven = False

print(f"isEven is {isEven}")

# above can be written as

number = 4
isEven = True if number%2==0 else False
print(f"isEven is {isEven}")

############################################
x_string = input("Enter a Number")
x = int(x_string)
if x==2:
    print(f"x is {x}")
elif x==3:
    print (f"x is {x}")
else:
    print(f"x is {x}")

############################################

number_one = int(input("Enter Number 1"))
number_two = int(input("Enter Number 2"))

print("Available choices are ")
print("1 - Add")
print("2 - Subtract")
print("3 - Divide")
print("4 - Multiply")

choice = int(input("Enter your choice"))
print(f"Your choice is {choice}")

if choice==1:
    print(f"Result is {number_one+number_two}")
elif choice==2:
    print(f"Result is {number_one-number_two}")
elif choice==3:
    print(f"Result is {number_one/number_two}")
elif choice==4:
    print(f"Result is {number_one*number_two}")
else:
    print("Invalid option selected , please choose from above options")

################################################################################

# int float and str in if conditions
# any non zero numbers results to True , non empty string results to true

if 45:
    print("Yes")

if 0:
    print("if")
else:
    print("else")

if 0.0:
    print("0.0")

if "Test":
    print("Test")

if '':
    print("Empty")

i = 10

if i%2:
    print ("Even")
else:
    print ("Odd")









