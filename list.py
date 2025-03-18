#  List Data Type
# एक Playlist (List of Songs)
playlist = ["Lut Gaye", "Kesariya", "Tum Hi Ho", "Raataan Lambiyan"]
print(playlist)

# Access Elements
print(playlist
[0])  # Lut
print(playlist[1])  # Kesariya

# List Modify (Mutable)
playlist.append("Dil Diyan Gallan")  # Add Song
playlist[0] = "Dil Diyan Gallan"  # Update Song
print(playlist)


#  List Data Type (एक List में एक से ज्यादा Data Types हो सकते हैं)
numbers = [1, 2, 3, 4, 5]  # Integers
fruits = ["Apple", "Mango", "Banana"]  # Strings
mixed_list = [1, "Hello", True, 3.14]  # Mixed Data Types
print(numbers)
print(fruits)
print(mixed_list)

# Access Elements

# list() Constructor: आप list() Constructor का Use करके List बना सकते हैं।
# आपको एक Iterable Object देना होगा।
numbers = list(range(1, 6))  # [1, 2, 3, 4, 5]

# Slicing (Range Access) (एक Range को Access करना)
# [start:end:step] (start: Start Index, end: End Index (Not Included), step: Step Value)
print(numbers[1:3])  # [2, 3] (Index 1 से 2 तक)
print(playlist[0:2])  # Index 0 से 1 तक



# Nested Lists (Matrix): एक List में एक List हो सकती है।
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix)
print(matrix[0][1])  # 2 (Row 0, Column 1)

# 4. List Modify करना (Mutable Operations)
# Add Elements
playlist.append("Tum Hi Ho")  # Add Song
playlist.insert(1, "Kesariya")  # Insert Song at Index 1

# b. Remove Items:
# Remove by Value
playlist.remove("Tum Hi Ho")  # Remove Song by Value

# Remove by Index
del playlist[0]  # Remove Song by Index

# Remove by Slice
del playlist[0:2]  # Remove Songs by Slice

# Remove Last Element
playlist.pop()  # Remove Last Song

# Remove First Element
playlist.pop(0)  # Remove First Song

# Remove All Elements
playlist.clear()  # Remove All Songs
print(playlist)



# 5. List Methods (हर Method का Real-World Use)
# Student Marks Sorting
marks = [85, 92, 78, 90]
marks.sort()  # [78, 85, 90, 92]
marks.reverse()  # [92, 90, 85, 78]
print(marks)

# List Comprehension
numbers = [1, 2, 3, 4, 5]
squared_numbers = [num ** 2 for num in numbers]
print(squared_numbers)  # [1, 4, 9, 16, 25]

# 6. List Functions (हर Function का Real-World Use)
# Length of List
print(len(playlist))  # 4

# Max and Min of List
numbers = [10, 20, 30, 40, 50]
print(max(numbers))  # 50
print(min(numbers))  # 10

# Sum of List
print(sum(numbers))  # 150

# Count of Element in List
numbers = [1, 2, 3, 1, 2, 1]
print(numbers
.count(1))  # 3

# Index of Element in List
numbers = [10, 20, 30, 40, 50]
print(numbers
.index(30))  # 2

# Copy of List
numbers = [1, 2, 3]
numbers_copy = numbers.copy()
print(numbers_copy)  # [1, 2, 3]

# Concatenation of Lists
numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
numbers = numbers1 + numbers2
print(numbers)  # [1, 2, 3, 4, 5, 6]

# Repetition of Lists
numbers = [1, 2, 3]
print(numbers * 2)  # [1, 2, 3, 1, 2, 3]

# Membership Check
numbers = [1, 2, 3]
print(1 in numbers)  # True
print(4 in numbers)  # False

# 7. List Unpacking (Multiple Variables Assign)
# Multiple Variables Assign
x, y, z = [10, 20, 30]
print(x)  # 10
print(y)  # 20
print(z)  # 30


# Swap Variables (बिना Temporary Variable के)
a = 5
b = 10
a, b = b, a  # a=10, b=5
print(a, b)  # 10 5

# 8. List vs Array
# List: हम List में Different Data Types के Elements Store कर सकते हैं।
# Array: हम Array में Same Data Type के Elements Store कर सकते हैं।


# iltering & Mapping:
# Filter: आप filter() Function का Use करके List को Filter कर सकते हैं। आपको Function देना होगा। जो True या False Return करेगा।
numbers = [1, 2, 3, 4, 5]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

# Map: आप map() Function का Use करके List को Map कर सकते हैं। हर Element को Transform करने के लिए।
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(even_numbers)  # [2, 4]
print(squared_numbers)  # [1, 4, 9, 16, 25]

# 10. List vs Tuple
# List: हम List में Different Data Types के Elements Store कर सकते हैं।
# Tuple: हम Tuple में Same Data Type के Elements Store कर सकते हैं।

# 11. List vs Dictionary
# List: हम List में Different Data Types के Elements Store कर सकते हैं।

