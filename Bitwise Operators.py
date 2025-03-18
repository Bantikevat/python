# Bitwise Operators in Python - Detailed Notes & Examples
# =========================================================
# Bitwise operators work at the binary level and perform operations on bits.
# These operators are mainly used in low-level programming, cryptography, compression, etc.

# List of Bitwise Operators in Python:
# 1. &  -> Bitwise AND
# 2. |  -> Bitwise OR
# 3. ^  -> Bitwise XOR
# 4. ~  -> Bitwise NOT
# 5. << -> Bitwise Left Shift
# 6. >> -> Bitwise Right Shift

# =========================================================
# 1️⃣ Bitwise AND (&)
# This operator compares each bit of two numbers and returns 1 if both bits are 1, otherwise 0.
# Example:
a = 5   # Binary: 0101
b = 3   # Binary: 0011
result = a & b  # Binary: 0001 (Decimal: 1)
print("Bitwise AND:", result)

# =========================================================
# 2️⃣ Bitwise OR (|)
# This operator compares each bit of two numbers and returns 1 if at least one of the bits is 1.
result = a | b  # Binary: 0111 (Decimal: 7)
print("Bitwise OR:", result)

# =========================================================
# 3️⃣ Bitwise XOR (^)
# This operator compares each bit of two numbers and returns 1 if the bits are different, otherwise 0.
result = a ^ b  # Binary: 0110 (Decimal: 6)
print("Bitwise XOR:", result)

# =========================================================
# 4️⃣ Bitwise NOT (~)
# This operator inverts all bits. In Python, it returns -(n+1) due to signed integers.
result = ~a  # Binary: -(0101+1) -> -(6)
print("Bitwise NOT:", result)

# =========================================================
# 5️⃣ Bitwise Left Shift (<<)
# This operator shifts the bits to the left by a given number of positions, filling with 0s.
# Equivalent to multiplying by 2^n
result = a << 1  # Binary: 1010 (Decimal: 10)
print("Bitwise Left Shift:", result)

# =========================================================
# 6️⃣ Bitwise Right Shift (>>)
# This operator shifts the bits to the right by a given number of positions, discarding bits.
# Equivalent to dividing by 2^n
result = a >> 1  # Binary: 0010 (Decimal: 2)
print("Bitwise Right Shift:", result)

# =========================================================
# Practical Problems Using Bitwise Operators
# =========================================================

# 1️⃣ Check if a number is even or odd using Bitwise AND
num = 10
if num & 1 == 0:
    print(num, "is Even")
else:
    print(num, "is Odd")

# 2️⃣ Swap two numbers without using a temporary variable
x, y = 5, 10
x = x ^ y
y = x ^ y
x = x ^ y
print("Swapped values:", x, y)

# 3️⃣ Multiply a number by 2 using Left Shift
num = 6
print("6 multiplied by 2 is:", num << 1)

# 4️⃣ Divide a number by 2 using Right Shift
num = 8
print("8 divided by 2 is:", num >> 1)

# 5️⃣ Convert lowercase letter to uppercase using Bitwise AND
char = 'b'
uppercase_char = chr(ord(char) & ~32)
print("Uppercase of 'b':", uppercase_char)

# 6️⃣ Convert uppercase letter to lowercase using Bitwise OR
char = 'D'
lowercase_char = chr(ord(char) | 32)
print("Lowercase of 'D':", lowercase_char)

# 7️⃣ Find if a number is a power of 2
num = 16
if num & (num - 1) == 0 and num != 0:
    print(num, "is a power of 2")
else:
    print(num, "is not a power of 2")

# 8️⃣ Count number of 1s in the binary representation of a number
def count_ones(n):
    count = 0
    while n:
        n &= n - 1  # Removes the rightmost 1 bit
        count += 1
    return count

print("Number of 1s in binary of 13:", count_ones(13))

# =========================================================
# Ye file aap VS Code me paste karke direct use kar sakte ho. 
# Har concept ke sath example aur logic diya gaya hai. 👍
