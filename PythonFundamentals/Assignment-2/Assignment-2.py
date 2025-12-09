#Question 1:

salary = int(input("Enter your salary: "))

if salary < 30000:
   calculateTax = salary * 0.05
   print(f"The tax is: {calculateTax}")
elif salary >= 30000 and salary <= 70000:
    calculateTax = salary * 0.15
    print(f"The tax is: {calculateTax}")
elif salary > 70000:
    calculateTax = salary * 0.25
    print(f"The tax is: {calculateTax}")

#Question 2:

number = int(input("Enter a number: "))
number_2 = int(input("Enter a number: "))

i = number

while i <= number_2:
    if i % 2 == 0:
        print(i)
    i += 1

#Question 3:

number = int(input("Enter a number: "))

total_digits = -1
while number > 0:
    digit = number % 10
    print(digit)
    number = number // 10
    total_digits += 1
print(f"The number of digits in the number is: {total_digits}")

#Question 4:

def count_digits(number):
    total_digits = 0
    while number > 0:
        digit = number % 10
        print(digit)
        number = number // 10
        total_digits += 1
    return total_digits

number = int(input("Enter a number: "))
print(f"The number of digits in the number is: {count_digits(number)}")


#Question 5:

def sum_of_digits(number):
    total_sum = 0
    while number > 0:
        digit = number % 10
        total_sum += digit
        number = number // 10
    return total_sum

number = int(input("Enter a number: "))
print(f"The sum of the digits in the number is: {sum_of_digits(number)}")

#Question 6:

i = 1
while i <= 1000:
    if i % 3 == 0 or i % 5 == 0:
        print(i)
    i += 1

#Question 7:

while True:
    number = (input("Enter a number: "))
    if number == "QUIT":
        break
    print(number)


#Question 8:

def calculator(number_1, number_2, operation):
    if operation == "+":
        return number_1 + number_2
    elif operation == "-":
        return number_1 - number_2
    elif operation == "*":
        return number_1 * number_2
    elif operation == "/":
        return number_1 / number_2
    else:
        return "Invalid operation"

number_1 = int(input("Enter the first number: "))
number_2 = int(input("Enter the second number: "))
operation = input("Enter the operation: ")
print(calculator(number_1, number_2, operation))


#Question 9:

number = int(input("Enter a number: "))

if number < 2:
    print("Not Prime")
else:
    for i in range(2, number):
        if number % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")

#Question 10:

guess_number = 10
while True:
    number = int(input("Enter a number: "))
    if number == guess_number:
        print("Correct!")
        break
    elif number < guess_number:
        print("Too low!")
    else:
        print("Too high!")
