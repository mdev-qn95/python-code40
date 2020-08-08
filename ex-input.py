# The input() function

your_name = input("Please enter your name: ")
print("Hello " + your_name.upper() + '!')

number = input("Please enter your number: ")
print("Your number: " + number)
print("Type of " + str(number) + " is " + str(type(number)))

print("Give me any two number and I'll multiply them together.")
num_1 = int(input("First number: "))
num_2 = int(input("Second number: "))
product = num_1*num_2
print("The product of " + str(num_1) + " and " + str(num_2) + " is " + str(product) + ".")

print("Give me any two number and I'll sum them together.")
num_1 = float(input("First number: "))
num_2 = float(input("Second number: "))
sum_result = num_1 + num_2
print("The sum of " + str(num_1) + " and " + str(num_2) + " is " + str(sum_result))