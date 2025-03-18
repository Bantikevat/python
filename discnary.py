# **Python Dictionaries In Depth**

# ## 1. Dictionary Kya Hai? (Real-Life Analogy)
# **Definition:**
# - Dictionary ek key-value pair ka collection hota hai.
# - Mutable hota hai, yani update kar sakte hain.
# - Unique keys hoti hain, lekin values duplicate ho sakti hain.
# - Unordered hota hai (Python 3.6+ me ordered behavior aaya hai).

# **Real-Life Example:**
# - Ek Phone Book jisme name (key) aur phone number (value) store hota hai.
# - Ek Student Record jisme Roll Number (key) aur details (value) hoti hain.

# #
# Example: Student Record
student = {
    "name": "Rahul",
    "age": 21,
    "marks": 85,
    "subjects": ["Math", "Science", "English"]
}
print(student)
#

#
## 2. Dictionary Kaise Banaye?
### a. Basic Dictionary
#
details = {"name": "Amit", "age": 25, "city": "Delhi"}
#
### b. dict() Constructor
#
info = dict(name="Rohit", age=30, city="Mumbai")
#
### c. Nested Dictionary
#
students = {
    "101": {"name": "Aman", "age": 20},
    "102": {"name": "Riya", "age": 22}
}
#

#
## 3. Dictionary Elements Access Karna
### a. Using Key
#
print(details["name"])  # Amit
#
### b. get() Method (Error Avoid Karne Ke Liye)
#
print(details.get("age"))  # 25
print(details.get("gender", "Not Found"))  # Default Value
#
### c. Looping Through Dictionary
#
for key, value in details.items():
    print(key, "->", value)
#

#
## 4. Dictionary Modify Karna
### a. Add/Update Items
#
details["gender"] = "Male"  # Add
print(details)
details["city"] = "Mumbai"  # Update

### b. Remove Items

details.pop("age")  # Specific Item Delete
print(details)

del details["city"]  # Another Way

details.clear()  # Empty Dictionary

## 5. Dictionary Methods (Real-World Use Cases)
# | Method         | Example | Use Case |
# |#####|###|###-|
# | keys()       | dict.keys() | Sabhi keys lena |
# | values()     | dict.values() | Sabhi values lena |
# | items()      | dict.items() | Sabhi key-value pairs lena |
# | pop()        | dict.pop(key) | Item remove karna |
# | popitem()    | dict.popitem() | Last item delete karna |
# | update()     | dict.update(new_dict) | Merge karna |
# | copy()       | dict.copy() | Duplicate banana |

# Example:
#
student_info = {"name": "Ravi", "age": 21, "city": "Bhopal"}
print(student_info.keys())
print(student_info.values())
print(student_info.items())
#

#
## 6. Dictionary Comprehension (Advanced Technique)
#
squares = {x: x*x for x in range(1, 6)}
print(squares)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
#

#
## 7. Real-World Projects (Practice Karein)
### a. Contact Book
#
contacts = {
    "Rahul": "9876543210",
    "Anjali": "8765432109"
}
print(contacts.get("Rahul"))
#
### b. Student Marks Analyzer
#
marks = {"Amit": 85, "Neha": 90, "Raj": 78}
print(max(marks, key=marks.get))  # Max Marks Ka Student
#
### c. Inventory Management
#
inventory = {"Apples": 10, "Bananas": 5}
inventory["Apples"] += 5
print(inventory)
#

#
## 8. Common Mistakes & Debugging
### a. KeyError (Key Not Found)
#
print(details["gender"])  # Error
#
# **Solution:** `details.get("gender", "Not Found")`

### b. Copy vs Reference Issue
#
original = {"a": 1, "b": 2}
copy_dict = original.copy()
copy_dict["a"] = 100
print(original)  # No Change
#

#
# ## 9. Cheat Sheet
# | Operation | Example | Result |
# |###--|###|##--|
# | Length | len(dict) | Dictionary ki size |
# | Check Existence | "key" in dict | True/False |
# | Merge | dict1.update(dict2) | Combine Dictionaries |
# | Remove | dict.pop("key") | Key delete karein |
# | Clear | dict.clear() | Empty dictionary |

# #
# ## 10. Memory Tricks & Best Practices
# - **Unique Keys Use Karein**: Duplicate keys avoid karein.
# - **Comprehension for Efficiency**: Large datasets ke liye dictionary comprehension use karein.
# - **`get()` Method Use Karein**: Errors avoid karne ke liye.
# - **Shallow Copy vs Deep Copy**: `copy()` ka difference samjhein.

# Final Challenge:
# #
info = {"x": 10, "y": 20}
info["x"], info["z"] = 50, 30
print(info)
# #
# **Answer:** `{"x": 50, "y": 20, "z": 30}`

# Aap ab Dictionary Pro ban chuke hain! 🚀 Agla Step: Sets, Tuples ya Real-World Projects par kaam karein. 😊

