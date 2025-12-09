# Python Fundamentals - Assignment 2

This assignment focuses on control structures in Python, including conditional statements (if-elif-else), loops (while and for), and functions. It builds upon the basics learned in Assignment 1.

## 📋 Overview

This assignment contains 10 questions that demonstrate control flow and function concepts in Python:

1. **Conditional Statements (Tax Calculation)** - Calculate tax based on salary ranges using if-elif-else
2. **While Loop (Even Numbers)** - Print all even numbers in a given range
3. **While Loop (Digit Counting)** - Count and display digits of a number
4. **Functions (Digit Counter)** - Create a function to count digits in a number
5. **Functions (Sum of Digits)** - Create a function to calculate the sum of digits
6. **While Loop (Multiples)** - Print all numbers divisible by 3 or 5 up to 1000
7. **Infinite Loop with Break** - Continuously take input until "QUIT" is entered
8. **Functions (Calculator)** - Build a simple calculator function
9. **For Loop (Prime Number Check)** - Check if a number is prime
10. **While Loop (Number Guessing Game)** - Implement a number guessing game with hints

## 🚀 How to Run

1. Make sure you have Python 3 installed on your system
2. Navigate to this directory:
   ```bash
   cd PythonFundamentals/Assignment-2
   ```
3. Run the Python script:
   ```bash
   python Assignment-2.py
   ```
   or
   ```bash
   python3 Assignment-2.py
   ```

**Note:** The script contains multiple questions that will execute sequentially. You'll be prompted for inputs for each question.

## 📝 Questions Breakdown

### Question 1: Tax Calculation
- Takes salary as input
- Calculates tax based on salary brackets:
  - Salary < 30,000: 5% tax
  - Salary 30,000 - 70,000: 15% tax
  - Salary > 70,000: 25% tax
- Uses if-elif-else conditional statements

### Question 2: Even Numbers in Range
- Takes two numbers as input (range)
- Uses a while loop to iterate through the range
- Prints all even numbers in the given range
- Demonstrates loop control and conditional checks within loops

### Question 3: Count Digits
- Takes a number as input
- Uses a while loop to extract and count digits
- Displays each digit and the total count
- Demonstrates number manipulation using modulo and floor division

### Question 4: Digit Counter Function
- Defines a function `count_digits()` that takes a number as parameter
- Returns the count of digits in the number
- Demonstrates function definition and return statements
- Shows how to use functions to organize code

### Question 5: Sum of Digits Function
- Defines a function `sum_of_digits()` that calculates the sum of all digits
- Uses a while loop to extract digits and accumulate their sum
- Returns the total sum
- Demonstrates function with return values

### Question 6: Multiples of 3 or 5
- Uses a while loop to iterate from 1 to 1000
- Prints numbers divisible by 3 or 5
- Demonstrates logical OR operator in conditions
- Shows loop iteration with a fixed range

### Question 7: Input Until QUIT
- Uses an infinite `while True` loop
- Continuously takes input until user enters "QUIT"
- Uses `break` statement to exit the loop
- Demonstrates loop control with break

### Question 8: Calculator Function
- Defines a `calculator()` function that performs basic arithmetic
- Takes two numbers and an operation (+, -, *, /) as parameters
- Returns the result of the operation
- Handles invalid operations with error message
- Demonstrates function parameters and multiple return paths

### Question 9: Prime Number Check
- Takes a number as input
- Checks if the number is prime using a for loop
- Uses the for-else construct (else executes if loop completes without break)
- Demonstrates prime number algorithm and for-else syntax

### Question 10: Number Guessing Game
- Implements a number guessing game with a fixed target (10)
- Uses a while loop to continuously take guesses
- Provides feedback: "Too low!", "Too high!", or "Correct!"
- Uses break to exit when correct guess is made
- Demonstrates interactive programming and loop control

## 💡 Learning Objectives

- Understanding conditional statements (if, elif, else)
- Working with while loops and loop control
- Understanding for loops and range()
- Creating and using functions
- Function parameters and return values
- Using break and continue statements
- Implementing algorithms (prime checking, digit manipulation)
- Building interactive programs

## 🔑 Key Concepts Covered

### Control Structures
- **Conditional Statements**: if, elif, else
- **Loops**: while, for
- **Loop Control**: break, continue
- **For-Else**: else clause with for loops

### Functions
- Function definition and calling
- Parameters and arguments
- Return statements
- Function organization

### Algorithms
- Digit extraction and manipulation
- Prime number checking
- Range iteration
- Input validation

## 📚 Prerequisites

- Completion of Assignment 1 (Python Fundamentals basics)
- Understanding of:
  - Variables and data types
  - Input/output operations
  - Basic arithmetic operations

## 🛠️ Requirements

- Python 3.x

No external libraries or packages are required for this assignment.

## 📖 Course Information

This assignment is part of the **Prime AI:ML Learning** course by Apna College, focusing on Python Fundamentals - Control Structures and Functions.

---

**Note:** When running the script, you'll be prompted to enter values for each question sequentially. Make sure to provide valid inputs as requested by each question. For Question 7, type "QUIT" (in uppercase) to exit the loop.

