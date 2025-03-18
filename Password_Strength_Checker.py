password = "Pass123@"
has_upper = any(char.isupper() for char in password)

has_digit = any(char.isdigit() for char in password)
has_special = any(char in "@#₹&" for char in password)
print(f"Strong Password? {has_upper and has_digit and has_special}")  # True
# 5️⃣ Common Mistakes & Best Practices
