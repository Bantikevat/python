# intiger data type
students = 45  # int type
pages = 300

# Operations
total_students = students + 10  # 55
print(total_students)

# Type Check
print(type(students))  # <class 'int'>
print(type(total_students))  # <class 'int'>

# float data type
price = 250.50  # float type
discount = 10.50

# Operations
final_price = price - discount  # 240.0
print(final_price)

# Type Check
print(type(price))  # <class 'float'>
print(type(final_price))  # <class 'float'>

# string data type
name = "Banti"  # str type
surname = "Kevat"
name = "अनिल कुमार"  # str (Double Quotes)
email = 'user@test.com'  # Single Quotes भी चलते हैं

# Multi-line String
address = """123, मुख्य सड़क
मुंबई, 400001"""

# String Operations
full_name = name + " शर्मा"  # Concatenation
print(full_name)  # अनिल कुमार शर्मा

# String Indexing
print(name[0])  # 'अ' (पहला Character)

# Operations
full_name = name + " " + surname  # Concatenation
print(full_name)

# Type Check
print(type(name))  # <class 'str'>
print(type(full_name))  # <class 'str'>

# boolean data type
is_active = True  # bool type
is_admin = False

# Operations
is_logged_in = is_active and is_admin  # False
print(is_logged_in)

# Type Check
print(type(is_active))  # <class 'bool'>
print(type(is_logged_in))  # <class 'bool'>



# List Data Type
shopping_list = ["दूध", "अंडे", "ब्रेड"]  # list
numbers = [1, 2, 3, 4, 5]

# List Modify (Mutable)
shopping_list.append("चीनी")  # ['दूध', 'अंडे', 'ब्रेड', 'चीनी']
shopping_list[1] = "ऑलिव ऑयल"  # Index 1 Update

# Slicing
print(numbers[1:3])  # [2, 3] (Index 1 से 2 तक)

# Type Check
print(type(shopping_list))  # <class 'list'>
print(type(numbers))  # <class 'list'>

# Tuple Data Type
days = ("सोमवार", "मंगलवार", "बुधवार")  # tuple
coordinates = (28.61, 77.23)

# Access Elements
print(days[0])  # सोमवार

# tuples Immutable हैं
# days[0] = "रविवार"  # Error आएगा

# Type Check
print(type(days))  # <class 'tuple'>
print(type(coordinates))  # <class 'tuple'>



# dictionary data type
student = {
    "name": "राजेश",
    "age": 20,
    "courses": ["Math", "Science"]
}

# Dictionary Length

# Access Values
print(student["name"])  # राजेश

# Modify/Add Values
student["age"] = 21  # Update Age
student["city"] = "दिल्ली"  # New Key-Value

# Dictionary Methods
print(student.keys())  # ['name', 'age', 'courses', 'city']
print(student.values())  # ['राजेश', 21, ['Math', 'Science'], 'दिल्ली']
print(student.items())  # dict_items([('name', 'राजेश'), ('age', 21), ('courses', ['Math', 'Science']), ('city', 'दिल्ली')])

# Type Check
print(type(student))  # <class 'dict'>
print(type(student["name"]))  # <class 'str'>
print(type(student["age"]))  # <class 'int'>


# set data type
lottery_numbers = {5, 12, 23, 5, 12}  # Duplicates हट जाएंगे
print(lottery_numbers)  # {5, 12, 23}

# Set Operations
A = {1, 2, 3}
B = {3, 4, 5}
print(A.union(B))  # {1, 2, 3, 4, 5}
print(A.intersection(B))  # {3}

# Type Check
print(type(lottery_numbers))  # <class 'set'>
print(type(A))  # <class 'set'>

# None data type
result = None  # None type
print(result)  # None

# Type Check
print(type(result))  # <class 'NoneType'>
# 3️⃣ Type Conversion
# int to float
x = 10
y = float(x)
print(y)  # 10.0

# float to int

z = 20.5
w = int(z)
print(w)  # 20

# str to int

a = "30"
b = int(a)
print(b)  # 30

# int to str

c = 40
d = str(c)
print(d)  # "40"

# bool to str

e = True
f = str(e)
print(f)  # "True"

# str to bool

g = "True"
h = bool(g)
print(h)  #

# 4️⃣ Common Mistakes & Best Practices
# 1. Indentation Error
# if True:
# print("Hello")  # Error: Indentation

# 2. Indentation Error




