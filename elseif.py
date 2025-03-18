# If-Else, Else-If (elif) & Nested If-Else Programs with Real-Life Examples
# ================================================================
# Yeh programs real-world problems ko solve karne ke liye bane hain.
# Har ek example ke sath proper explanation aur comments diye gaye hain.

# 1️⃣ ATM Withdrawal System
# User ko ATM se paise nikalne hain, lekin balance check bhi hona chahiye.

balance = 5000  # User ke account ka balance
withdraw_amount = int(input("Enter amount to withdraw: "))

if withdraw_amount <= balance:
    print("Transaction successful! Please collect your cash.")
else:
    print("Insufficient balance! Please enter a valid amount.")


# 2️⃣ Traffic Signal System
# Agar signal red hai toh rukna hai, yellow hai toh prepare hona hai, green hai toh chalna hai.

signal = input("Enter traffic signal color (red/yellow/green): ").lower()

if signal == "red":
    print("Stop! Wait for the green light.")
elif signal == "yellow":
    print("Get ready to go.")
elif signal == "green":
    print("Go ahead, but drive safely.")
else:
    print("Invalid signal input!")


# 3️⃣ Movie Ticket Price System
# Baccho ke liye discount milta hai, adults full price dete hain.

age = int(input("Enter your age: "))

if age < 12:
    print("Your ticket price is Rs. 100.")
elif age < 60:
    print("Your ticket price is Rs. 250.")
else:
    print("Your ticket price is Rs. 150 (senior citizen discount).")


# 4️⃣ Login Authentication System
# User ka username aur password check kiya jayega.

username = "admin"
password = "12345"

input_username = input("Enter username: ")
input_password = input("Enter password: ")

if input_username == username and input_password == password:
    print("Login successful!")
else:
    print("Invalid credentials! Please try again.")


# 5️⃣ Electricity Bill Calculation
# Units ke basis par bill charge hoga.

units = int(input("Enter electricity units consumed: "))

if units <= 100:
    bill = units * 5  # Rs. 5 per unit
elif units <= 300:
    bill = 100 * 5 + (units - 100) * 7  # Rs. 7 per unit after 100 units
else:
    bill = 100 * 5 + 200 * 7 + (units - 300) * 10  # Rs. 10 per unit after 300 units

print(f"Total electricity bill: Rs. {bill}")


# 6️⃣ Scholarship Eligibility Check
# Agar student ke marks 90+ hain toh full scholarship milegi, 75+ par half scholarship.

marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Congratulations! You got a full scholarship.")
elif marks >= 75:
    print("You got a half scholarship.")
else:
    print("Sorry, you are not eligible for a scholarship.")


# 7️⃣ Cab Fare Calculation
# Distance ke basis par cab fare calculate hoga.

distance = int(input("Enter distance in km: "))

if distance <= 5:
    fare = 50  # Minimum charge
elif distance <= 20:
    fare = 50 + (distance - 5) * 10
else:
    fare = 50 + 15 * 10 + (distance - 20) * 8

print(f"Your cab fare is Rs. {fare}")


# 8️⃣ Online Shopping Discount
# Shopping ke total amount ke basis par discount milega.

total_amount = float(input("Enter total shopping amount: "))

if total_amount >= 5000:
    discount = total_amount * 0.2  # 20% discount
elif total_amount >= 3000:
    discount = total_amount * 0.1  # 10% discount
else:
    discount = 0

final_amount = total_amount - discount
print(f"Final amount to pay after discount: Rs. {final_amount}")


# 9️⃣ Student Grade System
# Marks ke basis par grade assign kiya jayega.

marks = int(input("Enter marks: "))

if marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 50:
    grade = "D"
else:
    grade = "Fail"

print(f"Your grade is: {grade}")


# 🔟 Weather Advice System
# Temperature ke basis par user ko weather advice di jayegi.

temp = float(input("Enter temperature in Celsius: "))

if temp < 10:
    print("It's very cold! Wear warm clothes.")
elif temp < 25:
    print("The weather is pleasant.")
elif temp < 35:
    print("It's warm outside. Stay hydrated!")
else:
    print("It's too hot! Stay indoors if possible.")

# 🔹 Yeh sirf 10 examples hain, baki 10 aur real-world programs aap practice ke liye khud likhiye!
# 🔹 Aise hi aur examples chahiye toh batao! 😃
