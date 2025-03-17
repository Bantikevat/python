# # Variable Declaration
# x = 10      # x नाम का एक Variable, जिसमें Integer Value 10 Store है
# name = "Banti"  # name नाम का एक Variable, जिसमें String Value 'Banti' Store है
# pi = 3.14   # pi नाम का एक Variable, जिसमें Float Value 3.14 Store है

# # Output Print करने के लिए print() Function का उपयोग करते हैं
# print(x)    # Output: 10
# print(name) # Output: Banti
# print(pi)   # Output: 3.14

# # ✅ Valid Names
# student_name = "Rahul"  # Underscore allowed
# totalAmount = 1000      # CamelCase (common in Java, but Python में lowercase_preferred)
# age4 = 25               # Number अंत में है (valid)

# # ❌ Invalid Names
# 4age = 25               # Error: Number से शुरू नहीं हो सकता
# student-name = "Riya"   # Error: Hyphen (-) allowed नहीं
# class = "Python"        # Error: 'class' एक Keyword है

# # Variable Types
# # Python में Variables का Type बदला जा सकता है (Dynamic Typing)

# my_var = 10       # अभी यह Integer है
# print(type(my_var))  # <class 'int'>

# my_var = "Hello"  # अब यह String हो गया
# print(type(my_var))  # <class 'str'>



# # Mutable vs Immutable Variables
# # Mutable Example: List (बदला जा सकता है)
# shopping_list = ["Apple", "Milk"]
# shopping_list[1] = "Banana"  # Milk को Banana से बदल दिया
# print(shopping_list)  # Output: ['Apple', 'Banana']

# # Immutable Example: String (बदला नहीं जा सकता)
# name = "Riya"
# # name[0] = "P"  # Error: Strings are immutable
# new_name = "Priya"  # नया Variable बनाना पड़ेगा


# # Local vs Global Variables

# # Global Variable
# global_score = 95  # पूरे Program में accessible

# def calculate_grade():
#     # Local Variable (सिर्फ इस Function में)
#     passing_marks = 40
#     if global_score >= passing_marks:
#         print("Pass")

# calculate_grade()
# print(passing_marks)  # Error: NameError (Local Variable बाहर नहीं मिलेगा)


# # Multiple Variables Assign

# # एक Line में Multiple Variables Assign करना
# x, y, z = 10, 20, 30

# # Swap Variables (बिना Temporary Variable के)
# a = 5
# b = 10
# a, b = b, a  # a=10, b=5


# # Type Conversion

# # String को Integer में बदलना
# age = "25"
# age_int = int(age)  # अब यह Integer है (25)

# # Float को Integer में (Decimal हट जाता है)
# price = 99.95
# price_int = int(price)  # 99

# # Integer को String में बदलना
# year = 2024
# year_str = str(year)  # "2024"

# # 10. Common Mistakes & Best Practices

# # 1. Indentation Error
# # if True:
# # print("Hello")  # Error: Indentation Error

# # 2. NameError
# # print(age)  # Error: age Variable
# # not defined

# # 3. TypeError
# # print("Age: " + 25)  # Error: Can't concatenate str and
# # int

# # 1. Undefined Variable Use
# print(score)  # Error: 'score' Define नहीं किया गया

# # 2. Case Sensitivity
# Name = "Rahul"
# print(name)  # Error: 'name' और 'Name' अलग हैं

# # 3. Reserved Keywords Use
# class = "Python"  # Error: 'class' एक Keyword है

# # 4. Naming Conventions
# # CamelCase (common in Java, but Python में lowercase_preferred)
# totalAmount = 1000

# # snake_case
# student_name = "Rahul"

# # PascalCase
# StudentName = "Rahul"

# # kebab-case
# student-name = "Rahul"  # Error: Hyphen (-) allowed नहीं
# Python Variables - Full Concept with Examples

# 1️⃣ Basic Variable Declaration
x = 10  # Integer Variable
y = 20.5  # Float Variable
name = "Banti"  # String Variable
is_active = True  # Boolean Variable

# Printing values
print(x)  # Output: 10
print(y)  # Output: 20.5
print(name)  # Output: Banti
print(is_active)  # Output: True

# Checking data types
print(type(x))  # Output: <class 'int'>
print(type(y))  # Output: <class 'float'>
print(type(name))  # Output: <class 'str'>
print(type(is_active))  # Output: <class 'bool'>

# 2️⃣ Variable Reassignment
x = 50
print(x)  # Output: 50
x = "Hello"
print(x)  # Output: Hello

# 3️⃣ Multiple Variable Assignment
a, b, c = 5, 10, 15  # Assigning multiple values
print(a, b, c)  # Output: 5 10 15
x = y = z = 100  # Assigning same value to multiple variables
print(x, y, z)  # Output: 100 100 100

# 4️⃣ String Concatenation
first_name = "Banti"
last_name = "Kevat"
full_name = first_name + " " + last_name  # Concatenation
print(full_name)  # Output: Banti Kevat

# 5️⃣ Mathematical Operations using Variables
price_item1 = 250
price_item2 = 450
total_bill = price_item1 + price_item2
print("Total Bill:", total_bill)  # Output: Total Bill: 700

# 6️⃣ Constants in Python
PI = 3.14159  # Conventionally written in uppercase
g = 9.8  # Gravity Constant
print(PI, g)  # Output: 3.14159 9.8

# 7️⃣ Global and Local Variables
global_var = "I am Global"
def my_function():
    local_var = "I am Local"
    print(local_var)  # Output: I am Local
print(global_var)  # Output: I am Global
my_function()

# 8️⃣ Deleting Variables
del x  # Deleting variable
# print(x)  # ❌ Will cause NameError as x is deleted

# 9️⃣ Using Variables in a Function
def add_numbers():
    num1 = 5
    num2 = 10
    return num1 + num2
print(add_numbers())  # Output: 15

# 10️⃣ Using Variables in a Class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
person = Person("Rahul", 25)

person.display()
# Output:
# Name: Rahul
# Age: 25

# 11️⃣ Using Variables in a List
fruits = ["Apple", "Banana", "Mango"]
print(fruits[0])  # Output: Apple
a = 10
print(id(a))  # Output: 140735783267904 (a का Memory Address)

a = 20  # अब 'a' नए Address को Point करता है
print(id(a))  # Output: 140735783268224 (नया Address)
