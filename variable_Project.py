#  using variables in python project add decoration in program 


# Student Details (Variables)

student_name = "अर्जुन सिंह"
math_marks = 95
science_marks = 89
hindi_marks = 78
# Calculations
total_marks = math_marks + science_marks + hindi_marks
percentage = (total_marks / 300) * 100  # 300 total marks
# Report Print करें
print(f"नाम: {student_name}")    # Name of Student
print(f"कुल अंक: {total_marks}/300") # /300 → Total Marks
print(f"प्रतिशत: {percentage:.2f}%")  # .2f → 2 Decimal Places
# Output
# नाम: अर्जुन सिंह
# कुल अंक: 262/300
# प्रतिशत: 87.33%
# इस तरह से आप अपने Python Project में Variables का उपयोग कर सकते हैं।

# Expression Evaluate करके Result Variable में Store करें
total = (5 * 20) + (10 / 2)  # 100 + 5 = 105
print(total)  # Output: 105.0

# Real-Life Example: Electricity Bill Calculation
units_consumed = 150
rate_per_unit = 8.5
bill = units_consumed * rate_per_unit  # 150 * 8.5 = 1275
print(f"Bill: ₹{bill}")  # Output: Bill: ₹1275.0


# Path: variable_Project.py
# Python Variables Quiz
a = [1, 2, 3]
b = a
b.append(4)
print(a)  # ?


# 7️⃣ Global vs Local Variables

count = 10  # Global int (Immutable)

def update_count():
    # count += 1  # Error: 'count' is Local (Without 'global')
    # Solution: Use 'global' or Return New Value
    global count
    count += 1

update_count()
print(count)  # Output: 11