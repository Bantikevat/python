'''
what is if-else in python?
using hindi language
🔥 If-Else क्या है? (What is If-Else in Hindi?)
If-Else एक Conditional Statement है जो किसी निर्णय को लेने के लिए उपयोगी है। इसका उपयोग किसी भी प्रोग्राम में एक निर्दिष्ट शर्त के आधार पर कोड को चलाने के लिए किया जाता है। यदि शर्त सत्य है तो एक निर्दिष्ट एक्शन को चलाया जाता है, अन्यथा दूसरा एक्शन चलाया जाता है।
🔥 If-Else क्यों ज़रूरी है? (Why If-Else is Important?.)
If-Else का उपयोग किसी भी प्रोग्राम को सही निर्णय लेने के लिए किया जाता है। यह उपयोगी है जब आपको किसी निर्दिष्ट शर्त के आधार पर कोड को चलाना हो। इसके अलावा, यह गलत इनपुट को रोकने, यूज़र इनपुट को हैंडल करने, सुरक्षा जाँच करने और ऑटोमेशन के लिए भी उपयोगी है।



🔥 Why If-Else is Important? (क्यों ज़रूरी है?)
Decision Making – किसी भी प्रोग्राम को सही निर्णय लेने के लिए चाहिए।
User Input Handling – यूज़र से डेटा लेने के बाद उसके हिसाब से सही एक्शन लेना।
Error Handling – गलत इनपुट को रोकने में मदद करता है।
Security Checks – पासवर्ड चेकिंग, लॉगिन सिस्टम वगैरह में उपयोगी।
Automation – बैकग्राउंड में कोई भी टास्क तभी होना चाहिए जब कोई कंडीशन पूरी हो।
🔥 If-Else Syntax (इफ-एल्स का सिंटैक्स)
'''














# 1️⃣ Check if a number is positive or negative
num = int(input("Enter a number: "))
if num >= 0:
    print("Positive number")
else:
    print("Negative number")

# 2️⃣ Check if a person is eligible to vote
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote!")
else:
    print("You are not eligible to vote!")

# 3️⃣ Check if a number is even or odd
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")

# 4️⃣ Find the greatest of two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a > b:
    print(f"{a} is greater than {b}")
else:
    print(f"{b} is greater than {a}")

# 5️⃣ Check if a number is divisible by 5
num = int(input("Enter a number: "))
if num % 5 == 0:
    print("Divisible by 5")
else:
    print("Not divisible by 5")

# 6️⃣ Check if a year is a leap year
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap year")
else:
    print("Not a leap year")

# 7️⃣ Simple login system
correct_password = "python123"
password = input("Enter password: ")
if password == correct_password:
    print("Access granted!")
else:
    print("Access denied!")

# 8️⃣ Check if a character is a vowel or consonant
char = input("Enter a character: ").lower()
if char in 'aeiou':
    print("Vowel")
else:
    print("Consonant")

# 9️⃣ Check if a number is single-digit or multi-digit
num = int(input("Enter a number: "))
if num >= -9 and num <= 9:
    print("Single-digit number")
else:
    print("Multi-digit number")

# 🔟 Temperature check (Cold, Warm, Hot)
temp = int(input("Enter temperature: "))
if temp < 15:
    print("Cold Weather")
else:
    print("Normal Weather")

# 1️⃣1️⃣ ATM withdrawal system
balance = 5000
amount = int(input("Enter withdrawal amount: "))
if amount <= balance:
    print(f"Withdrawal successful! Remaining balance: {balance - amount}")
else:
    print("Insufficient balance")

# 1️⃣2️⃣ Check if a string is empty or not
text = input("Enter a string: ")
if text:
    print("String is not empty")
else:
    print("String is empty")

# 1️⃣3️⃣ Check if a number is a perfect square
import math
num = int(input("Enter a number: "))
if math.sqrt(num).is_integer():
    print("Perfect Square")
else:
    print("Not a Perfect Square")

# 1️⃣4️⃣ Check if a person is eligible for a senior citizen discount
age = int(input("Enter your age: "))
if age >= 60:
    print("Eligible for senior citizen discount")
else:
    print("Not eligible")

# 1️⃣5️⃣ Check if an email contains '@'
email = input("Enter your email: ")
if "@" in email:
    print("Valid email")
else:
    print("Invalid email")

# 1️⃣6️⃣ Check if a number is in a given range
num = int(input("Enter a number: "))
if 10 <= num <= 50:
    print("Number is within range 10-50")
else:
    print("Number is out of range")

# 1️⃣7️⃣ Simple traffic light system
signal = input("Enter traffic light color (red/yellow/green): ").lower()
if signal == "red":
    print("Stop")
else:
    print("Go")

# 1️⃣8️⃣ Discount on shopping
amount = float(input("Enter shopping amount: "))
if amount > 500:
    print("Congratulations! You get a 10% discount.")
else:
    print("No discount available.")

# 1️⃣9️⃣ Check if a user entered a prime number
num = int(input("Enter a number: "))
if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print("Not a prime number")
            break
    else:
        print("Prime number")
else:
    print("Not a prime number")

# 2️⃣0️⃣ Check if a person is a teenager
age = int(input("Enter your age: "))
if 13 <= age <= 19:
    print("You are a teenager!")
else:
    print("You are not a teenager.")

