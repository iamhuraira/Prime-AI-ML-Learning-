
#Question 1; 
name = input("Enter your Name: ")
age = input("Enter your Age: ")
print("Hello, " + name + "! You are " + age + " years old.")

#Question 2;
number_1 = int(input("Enter the first number: "))
number_2 = int(input("Enter the second number: "))
sum = number_1 + number_2

print(f"The sum of the two numbers is: {sum}")
difference = number_1 - number_2
print(f"The difference of the two numbers is: {difference}")
product = number_1 * number_2
print(f"The product of the two numbers is: {product}")
quotient = number_1 / number_2
print(f"The quotient of the two numbers is: {quotient}")

#Question 3;
number_int_1 = float(input("Enter the first Integer number: "))
number_int_2 = float(input("Enter the second Integer number: "))
number_float_1 = float(input("Enter the first Float number: "))

average = (number_int_1 + number_int_2 + number_float_1) / 3
print(f"The average of the three numbers is: {average}")  

#Question 4;
str_num = input("Enter a number: ")
int_num = int(str_num)
float_num = float(str_num)
str_num = str(int_num)
print(f"The integer number is: {int_num} and the type is: {type(int_num)}")
print(f"The float number is: {float_num} and the type is: {type(float_num)}")
print(f"The string number is: {str_num} and the type is: {type(str_num)}")

#Question 5;
x = 10+3*2**2
print(x)
# By Using The BODMAS Rule, First we will solve the exponentiation, then multiplication, then addition.
# So, the result will be 22.

#Question 6;
number_1 = int(input("Enter the first number: "))
number_2 = int(input("Enter the second number: "))

temp = number_1
number_1 = number_2
number_2 = temp

print(f"The first number is: {number_1} and the second number is: {number_2}")

#Question 7; 
temprature = float(input("Enter the temprature in Celsius: "))
fahrenheit = (temprature * 9/5) + 32
print(f"The temprature in Fahrenheit is: {fahrenheit}")

#Question 8;
radius = float(input("Enter the radius of the circle: "))
PI = 3.14
area = PI * radius**2
print(f"The area of the circle is: {area}")

#Question 9:
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time period: "))
simple_interest = (principal * rate * time) / 100
print(f"The simple interest is: {simple_interest}")

#Question 10:
number_decimal = float(input("Enter a decimal number: "))
integer_part = int(number_decimal)
decimal_part = number_decimal - integer_part
print(f"The integer part is: {integer_part}")
print(f"The decimal part is: {decimal_part}")