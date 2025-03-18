# This file contains all the fixed data in the form of tuple
# सप्ताह के दिन (Fixed Data)
days = ("सोमवार", "मंगलवार", "बुधवार", "गुरुवार", "शुक्रवार", "शनिवार", "रविवार")

# महीने (Fixed Data)
months = ("जनवरी", "फरवरी", "मार्च", "अप्रैल", "मई", "जून", "जुलाई", "अगस्त", "सितम्बर", "अक्टूबर", "नवम्बर", "दिसम्बर")

# रंग (Fixed Data)
colors = ("लाल", "नीला", "हरा", "पीला", "काला", "गुलाबी", "सफेद")

# दिशाएँ (Fixed Data)
directions = ("उत्तर", "दक्षिण", "पूर्व", "पश्चिम")

# फल (Fixed Data)
fruits = ("आम", "सेब", "केला", "संतरा", "अंगूर", "अनार", "अमरूद", "चेरी", "खजूर", "नाशपाती", "नारियल", "अदरक खाना")

# making a tuple of fruits in English language 
fruits = ("Apple", "Mango", "Banana")  
coordinates = (28.61, 77.23)  # Latitude, Longitude

# b. Single Element Tuple (Comma जरूरी):
single_item = ("Hello",)  # Comma नहीं होगा तो String माना जाएगा!
single_number = (5,)  # Comma जरूरी है।
single_boolean = (True,)  # Comma जरूरी है।
single_float = (3.14,)  # Comma जरूरी है।
single_list = ([1, 2, 3],)  # Comma जरूरी है।

# tuple() Constructor:
numbers = tuple(range(1, 6))  # (1, 2, 3, 4, 5)
print(numbers)
print(type(numbers))

# tuple() Constructor:
ays = ("Mon", "Tue", "Wed")
print(days[0])   # "Mon" (First Item)
print(days[-1])  # "Wed" (Last Item)

# Slicing (Range Access) (एक Range को Access करना)
# [start:end:step] (start: Start Index, end: End Index (Not Included), step: Step Value)
print(days[1:3])  # ["Tue", "Wed"] (Index 1 से 2 तक)
print(days[0:2])  # Index 0 से 1 तक
print(days[::2])  # ["Mon", "Wed", "Fri", "Sun"] (Step 2)
print(days[::-1])  # ["Sun", "Sat", "Fri", "Thu", "Wed", "Tue", "Mon"] (Reverse)

#  Tuples के साथ Operations
# Concatenation (जोड़ना)
tuple1 = (1, 2)
tuple2 = (3, 4)
combined = tuple1 + tuple2  # (1, 2, 3, 4)
print(combined)

# Repetition (दोहराना)
repeated = tuple1 * 3  # (1, 2, 1, 2, 1, 2)
print(repeated)

# Membership Test (शामिलता परीक्षण)
print(1 in tuple1)  # True
print(3 in tuple1)  # False

# Length (लंबाई)
print(len(tuple = (1, 2, 3, 4, 5)))  # 5

# Unpacking (अनपैकिंग)
student = ("राहुल", 25, "Delhi")
name, age, city = student  # Variables में Assign
print(f"{name} ({age}), {city} से")  # राहुल (25), Delhi से

# Swapping (बदलाव)
a = 5
b = 10
a, b = b, a
print(a)  # 10
print(b)  #

# Tuple to List (Tuple को List में Convert करना)
numbers = (1, 2, 3, 4, 5)
numbers_list = list(numbers)
print(numbers_list)  # [1, 2, 3, 4, 5]

# List to Tuple (List को Tuple में Convert करना)
numbers = [1, 2, 3, 4, 5]
numbers_tuple = tuple(numbers)
print(numbers_tuple)  # (1, 2, 3, 4, 5)


# Nested Tuples (Matrix): एक Tuple में एक Tuple हो सकता है।
matrix = ((1, 2), (3, 4), (5, 6))
print(matrix[1][0])  # 3 (Second Row, First Column)


# dictionary with tuple keys (ट्यूपल कुंजी वाला शब्दकोश)

location_coords = {
    (28.61, 77.23): "Delhi",
    (19.07, 72.87): "Mumbai"
}
print(location_coords[(28.61, 77.23)])  # "Delhi"
