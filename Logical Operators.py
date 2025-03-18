# Logical Operators in Python (AND, OR, NOT) with Real-Life Examples
# ================================================================
# Logical operators ka use decision making aur conditions check karne ke liye hota hai.
# Python me 3 logical operators hote hain:
# 1. and  -> Dono conditions True honi chahiye
# 2. or   -> Koi ek condition True hone par bhi True hoga
# 3. not  -> Condition ko ulta kar deta hai (True ko False aur False ko True)

# 1️⃣ AND Operator Example: University Admission Criteria
# Student ka admission tabhi hoga jab uske marks 80+ hon aur uski attendance 75% se upar ho.
marks = int(input("Enter your marks: "))
attendance = int(input("Enter your attendance percentage: "))

if marks >= 80 and attendance >= 75:
    print("Congratulations! You are eligible for admission.")
else:
    print("Sorry, you do not meet the admission criteria.")

# 2️⃣ OR Operator Example: Job Eligibility Criteria
# Candidate ko job tab milegi agar uske paas 5+ years experience ho ya uske paas special certification ho.
experience = int(input("Enter your years of experience: "))
certification = input("Do you have a special certification? (yes/no): ").lower()

if experience >= 5 or certification == "yes":
    print("You are eligible for the job interview!")
else:
    print("You do not meet the job criteria.")

# 3️⃣ NOT Operator Example: Library Membership Check
# User ke paas valid membership honi chahiye warna access nahi milega.
membership = input("Do you have a valid library membership? (yes/no): ").lower()

if not membership == "yes":
    print("Access Denied! Please get a valid membership.")
else:
    print("Access Granted! You can enter the library.")

# 4️⃣ AND, OR, NOT Combined Example: Online Shopping Discount
# Agar user ke paas coupon ho ya uski total shopping 5000+ ho aur membership ho toh discount milega.
coupon = input("Do you have a discount coupon? (yes/no): ").lower()
total_amount = int(input("Enter total shopping amount: "))
membership = input("Are you a premium member? (yes/no): ").lower()

if (coupon == "yes" or total_amount >= 5000) and membership == "yes":
    print("Congratulations! You got a discount.")
else:
    print("Sorry, you are not eligible for a discount.")

# 5️⃣ Security System Example (NOT Operator)
# Agar user "admin" nahi hai toh usko access nahi milega.
username = input("Enter your username: ")

if not username == "admin":
    print("Access Denied! Only admin can enter.")
else:
    print("Welcome, Admin!")

# 🔹 Ye sirf 5 examples hain. Aap khud aur examples likh kar practice karein!
# 🔹 Logical operators programming me decision making aur AI-based systems ke liye bahut useful hote hain! 🚀
