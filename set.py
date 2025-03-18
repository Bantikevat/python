# Python Sets - Complete Guide with Real-World Examples

## 1. Set क्या है? (Real-Life Analogy)
### **Definition:**
# - **Set** एक **unordered collection** होता है, जिसमें **unique elements** होते हैं।
# - इसमें **duplicate values नहीं हो सकते**।
# - यह **mutable (modifiable)** होता है, लेकिन इसके **elements immutable** होने चाहिए।

# ### **Real-Life Example:**
# - **Classroom Attendance** – एक **set** में सिर्फ **unique students** होंगे, कोई नाम दो बार नहीं होगा।
# - **Unique Colors in a Palette** – किसी भी **painting app** में **हर color** सिर्फ **एक बार** होगा।

# ---
## 2. Set बनाने के तरीके
### a) **Basic Set** (Curly Braces `{}` से)

colors = {"red", "blue", "green"}
print(colors)  # {'red', 'blue', 'green'}


### b) **set() Constructor से**

numbers = set([1, 2, 3, 4, 2, 3])  # Duplicates हट जाएँगे
print(numbers)  # {1, 2, 3, 4}


### c) **Empty Set बनाने का सही तरीका**

empty_set = set()  # ✅ सही तरीका
wrong_set = {}      # ❌ गलत तरीका (यह Dictionary बनेगी)


## 3. Set के Operations (Basic Operations)
### a) **Add Elements** (`add()`)

fruits = {"apple", "banana"}
fruits.add("orange")
print(fruits)  # {'apple', 'banana', 'orange'}


### b) **Remove Elements** (`remove()` & `discard()`)

numbers = {1, 2, 3, 4}
numbers.remove(2)  # 2 को हटा देगा
numbers.discard(5)  # Error नहीं देगा, अगर 5 मौजूद नहीं है
print(numbers)  # {1, 3, 4}


### c) **Pop Elements** (`pop()` – Randomly कोई एक Element हटाएगा)
 
items = {"pen", "pencil", "eraser"}
removed_item = items.pop()
print(items)  # Random element हट जाएगा


### d) **Clear Set** (`clear()` – पूरा Set खाली कर देगा)
 #
cars = {"BMW", "Audi", "Tesla"}
cars.clear()
print(cars)  # set()


### e) **Check Element Presence** (`in` operator)
 #
cities = {"Delhi", "Mumbai", "Kolkata"}
print("Delhi" in cities)  # True
print("Chennai" in cities)  # False


## 4. Set Operations (Mathematical Operations)
### a) **Union (`|` या `union()`)**
 #
A = {1, 2, 3}
B = {3, 4, 5}
print(A | B)  # {1, 2, 3, 4, 5}
print(A.union(B))  # {1, 2, 3, 4, 5}


### b) **Intersection (`&` या `intersection()`)**
#
print(A & B)  # {3}
print(A.intersection(B))  # {3}


### c) **Difference (`-` या `difference()`)**
#
print(A - B)  # {1, 2} (जो सिर्फ A में हैं)
print(B - A)  # {4, 5} (जो सिर्फ B में हैं)


### d) **Symmetric Difference (`^` या `symmetric_difference()`)**
#
print(A ^ B)  # {1, 2, 4, 5} (जो केवल एक में हैं)



## 5. Set Methods (Advanced Techniques)
# | Method | Use Case |
# |--------|---------|
# | `add(x)` | Set में `x` Add करता है |
# | `remove(x)` | `x` Remove करता है, Error देगा अगर `x` नहीं मिला |
# | `discard(x)` | `x` Remove करता है, Error नहीं देगा |
# | `pop()` | Random element Remove करता है |
# | `clear()` | पूरा Set Empty कर देता है |
# | `union(set2)` | दो Sets को जोड़ता है |
# | `intersection(set2)` | Common elements देता है |
# | `difference(set2)` | सिर्फ पहले Set के Unique Elements देता है |
# | `symmetric_difference(set2)` | दोनों में Unique Elements देता है |
# | `issubset(set2)` | चेक करता है कि पहला Set दूसरे का Subset है या नहीं |
# | `issuperset(set2)` | चेक करता है कि पहला Set दूसरे का Superset है या नहीं |


## 6. Real-World Examples
### a) **Duplicate-Free Student Names List**
#
students = ["Aman", "Rahul", "Priya", "Aman", "Rahul"]
unique_students = set(students)
print(unique_students)  # {'Aman', 'Rahul', 'Priya'}


### b) **Common Ingredients in Two Recipes**

recipe1 = {"tomato", "onion", "salt"}
recipe2 = {"onion", "garlic", "salt"}
common_ingredients = recipe1 & recipe2
print(common_ingredients)  # {'onion', 'salt'}


### c) **Movies Watched by Two Friends**

john_movies = {"Inception", "Avengers", "Interstellar"}
doe_movies = {"Interstellar", "Titanic", "Avengers"}
common_movies = john_movies.intersection(doe_movies)
print(common_movies)  # {'Avengers', 'Interstellar'}

### d) **Banned Words Filter in Chat Application**
#
banned_words = {"spam", "fake", "scam"}
message = "This is not a scam!"
words = set(message.lower().split())
if words & banned_words:
    print("Warning: Message contains banned words!")


## 7. Common Mistakes & Debugging
### a) **Mutable Elements Error** (Set में List नहीं डाल सकते)
#
my_set = {1, 2, [3, 4]}  # ❌ TypeError: unhashable type: 'list'

# **✅ सही तरीका:**
#
my_set = {1, 2, tuple([3, 4])}  # ✅ Tuple को Use करें


### b) **Duplicate Values अपने आप हट जाते हैं**
#
nums = {1, 2, 2, 3, 3, 4}
print(nums)  # {1, 2, 3, 4}


## 🎯 **Final Challenge**
#
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
A.difference_update(B)
print(A)

# **Output:** `{1, 2}` (A में से B के Common Elements हट गए)

# अब आप **Python Sets Master** बन चुके हैं! 🚀 अगला कदम: **Tuples & Dictionaries** सीखें या **Real-World Projects** बनाना शुरू करें! 😊

