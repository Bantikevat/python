
# 
# String Object की उदाहरण
name = "Alice"  # Memory में एक String Object बनता है
name = "Bob"    # नया Object बनता है, पुराना नहीं बदलता
print(name
      )  # Output: Bob

# Single/Double Quotes: आप Single या Double Quotes दोनों Use कर सकते हैं।
s1 = 'Single Quotes में "Double Quotes" Use कर सकते हैं।'
s2 = "Double Quotes में 'Single Quotes' Use कर सकते हैं।"
print(s1)  # Output: Single Quotes में "Double Quotes" Use कर सकते हैं।
print(s2)  # Output: Double Quotes में 'Single Quotes' Use कर सकते हैं।

# Multi-line String: आप Triple Quotes (""" या ''') Use करके Multi-line String Declare कर सकते हैं।
address = """123, Main Road
Mumbai, 400001"""
print(address)
# Output:
# 123, Main Road
# Mumbai,

# Escape Characters: आप Escape Characters का Use करके विभिन्न Characters को Print कर सकते हैं।
# \n: New Line
# \t: Tab
# \": Double Quote
# \': Single Quote
# \\: Backslash
print("Hello\nWorld")
# Output:
# Hello
# World


# d. Raw Strings (Escape Ignore):
# आप Raw Strings Declare करके Escape Characters को Ignore कर सकते हैं।
# उदाहरण: r"Hello\nWorld"
print(r"Hello\nWorld")
raw_path = r"C:\Users\Desktop"  # 'r' Prefix → \ को Escape नहीं करता
print(raw_path)  # Output: C:\Users\Desktop
# Output: Hello\nWorld

# String Operations & Indexing
# Concatenation: आप + Operator का Use करके Strings को Concatenate कर सकते हैं।
first_name = "Alice"
last_name = "Bob"
full_name = first_name + " " + last_name
print(full_name)  # Output: Alice Bob

#  Repetition (दोहराना):
# आप * Operator का Use करके String को दोहरा सकते हैं।
print("Hello " * 3)  # Output: Hello Hello Hello

#  Indexing (Position Access):
# आप [] Bracket का Use करके String के Characters को Access कर सकते हैं।
# Indexing: 0 से Start होता है
# -1: Last Character
# -2: Second Last Character
name = "Alice"
print(name[0])  # Output: A
print(name[-1])  # Output: e

# Slicing (Range Access):
# आप [:] Colon का Use करके Range Access कर सकते हैं।
# [start:end:step]
# start: Start Index
# end: End Index (Not Included)
# step: Step Value
name = "Alice"
print(name[0:3])  # Output: Ali
print(name[1:])  # Output: lice
print(name[:3])  # Output: Ali
print(name[::2])  # Output: Ac
print(name[::-1])  # Output: ecilA



# String Methods
# String Methods: आप String Methods का Use करके String को Modify कर सकते हैं।
# Method: एक Function होता है जो Object को Modify करता है।

# Upper Case: आप upper() Method का Use करके String को Upper Case कर सकते हैं।
name = "Alice"
print(name.upper())  # Output: ALICE

# Lower Case: आप lower() Method का Use करके String को Lower Case कर सकते हैं।
name = "Alice"
print(name.lower())  # Output: alice

# Title Case: आप title() Method का Use करके String को Title Case कर सकते हैं।
name = "alice bob"
print(name.title())  # Output: Alice

# Replace: आप replace() Method का Use करके String को Replace कर सकते हैं।
name = "Alice"
print(name.replace("A", "B"))  # Output: Blice

# Split: आप split() Method का Use करके String को Split कर सकते हैं।   # आपको एक Separator देना होगा।
name = "Alice Bob"
print(name.split(" "))  # Output: ['Alice', 'Bob']

# Join: आप join() Method का Use करके String को Join कर सकते हैं। आपको List को Join करने के लिए Use करें।
name = ["Alice", "Bob"]
print(" ".join(name))  # Output: Alice Bob

# Format: Dynamic Values Insert करें। आप {} Placeholder का Use करके Dynamic Values Insert कर सकते हैं।
name = "Alice"
age = 25
print("Name: {}, Age: {}".format(name, age))  # Output: Name
# : Alice,
# Age: 25

# f-Strings (Python 3.6+): आप f-Strings का Use करके Dynamic Values Insert कर सकते हैं।
name = "Alice"
age = 25
print(f"Name: {name}, Age: {age}")  # Output: Name: Alice, Age: 25





# S.strip(): दोनों तरफ के Whitespace हटाएँ (User Input Clean करने के लिए)।
name = " Alice "
print(name.strip())  # Output: Alice

# Lstrip: आप lstrip() Method का Use करके String को Lstrip कर सकते हैं।
name = " Alice "
print(name.lstrip())  # Output: Alice

# Rstrip: आप rstrip() Method का Use करके String को Rstrip कर सकते हैं।
name = " Alice "
print(name.rstrip())  # Output: Alice

# Find: आप find() Method का Use करके String को Find कर सकते हैं।
name = "Alice"
print(name.find("A"))  # Output: 0

# Count: आप count() Method का Use करके String को Count कर सकते हैं।
name = "Alice"
print(name .count("A"))  # Output: 1

# Replace: आप replace() Method का Use करके String को Replace कर सकते हैं।
name = "Alice"
print(name.replace("A", "B"))  # Output: Blice

# Length: आप len() Method का Use करके String की Length प्राप्त कर सकते हैं।
name = "Alice"
print(len(name))  # Output: 5

# Check: आप in Operator का Use करके String को Check कर सकते हैं।
name = "Alice"
print("A" in name)  # Output: True

# Check: आप not in Operator का Use करके String को Check कर सकते हैं।
name = "Alice"
print("A" not in name)  # Output: False

# Check: आप startswith() Method का Use करके String को Check कर सकते हैं।
name = "Alice"
print(name.startswith("A"))  # Output: True

# Check: आप endswith() Method का Use करके String को Check कर सकते हैं।
name = "Alice"
print(name.endswith("e"))  # Output: True

# Check: आप isdigit() Method का Use करके String को Check कर सकते हैं।
name = "123"
print(name.isdigit())  # Output: True

# Check: आप isalpha() Method का Use करके String को Check कर सकते हैं।
name = "Alice"
print(name.isalpha())  # Output: True

# Check: आप isalnum() Method का Use करके String को Check कर सकते हैं।
name = "Alice123"
print(name.isalnum())  # Output: True

# Check: आप islower() Method का Use करके String को Check कर सकते हैं।
name = "alice"
print(name
      .islower())  # Output: True

# Check: आप isupper() Method का Use करके String को Check कर सकते हैं।
name = "ALICE"
print(name.isupper())  # Output: True

# Check: आप isnumeric() Method का Use करके String को Check कर सकते हैं।
name = "123"
print(name.isnumeric())  # Output: True

# Check: आप isidentifier() Method का Use करके String को Check कर सकते हैं।
name = "Alice"
print(name.isidentifier())  # Output
# : True

# Check: आप isprintable() Method का Use करके String को Check कर सकते हैं।
name = "Alice"
print(name.isprintable())  # Output : True

# Unicode & Encoding (Emojis, Hindi Text): आप Unicode का Use करके Emojis और Hindi Text Print कर सकते हैं।
# Unicode: एक Standard है जिसमें हर Character को Unique Code दिया गया है।
# उदाहरण: \u0905 (अ)
print("\u0905")  # Output: अ
print("\U0001F600")  # Output: 😁
emoji = "😊"
hindi = "नमस्ते"
print(len(emoji))  # 1 (Character Count)
print(hindi.encode("utf-8"))  # b'\xe0\xa4\xa8\xe0\xa4\xae...'













