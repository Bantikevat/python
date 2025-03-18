# Comparison Operators in Python
# =========================================
# Yeh operators do values ko compare karne ke liye use hote hain.
# Inka result hamesha True ya False hota hai.

# Operators:
# 1. ==  (Equal to)
# 2. !=  (Not equal to)
# 3. >   (Greater than)
# 4. <   (Less than)
# 5. >=  (Greater than or equal to)
# 6. <=  (Less than or equal to)

# Example 1: Age Verification System
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

# Example 2: Exam Passing Criteria
marks = int(input("Enter your marks: "))
if marks >= 40:
    print("Congratulations! You have passed the exam.")
else:
    print("Sorry, you have failed. Better luck next time.")

# Example 3: Product Price Comparison
price1 = 500
price2 = 700
if price1 < price2:
    print("The first product is cheaper.")
else:
    print("The second product is cheaper.")

# Example 4: Minimum Balance Requirement in Bank
balance = float(input("Enter your bank balance: "))
if balance >= 500:
    print("Your account is active.")
else:
    print("Your balance is low! Please deposit money.")

# Example 5: Height Comparison for Roller Coaster Ride
height = int(input("Enter your height in cm: "))
if height >= 120:
    print("You can go on the roller coaster ride.")
else:
    print("Sorry, you are not tall enough for this ride.")

# Example 6: Employee Salary Comparison
salary1 = 40000
salary2 = 55000
if salary1 > salary2:
    print("Employee 1 has a higher salary.")
else:
    print("Employee 2 has a higher salary.")

# Example 7: Number Comparison
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if num1 == num2:
    print("Both numbers are equal.")
elif num1 > num2:
    print("The first number is greater.")
else:
    print("The second number is greater.")

# Example 8: Sports Team Selection Based on Age
player_age = int(input("Enter player's age: "))
if player_age < 16:
    print("You are eligible for the junior team.")
elif player_age < 25:
    print("You are eligible for the senior team.")
else:
    print("You are eligible for the veterans' team.")

# Example 9: Shopping Discount Eligibility
shopping_amount = float(input("Enter shopping amount: "))
if shopping_amount >= 5000:
    print("You get a 20% discount!")
else:
    print("No discount available. Shop more!")

# Example 10: Comparing Two Strings
str1 = "Python"
str2 = "Java"
if str1 != str2:
    print("The strings are different.")
else:
    print("The strings are the same.")
