# Arithmetic Operators in Python (गणितीय ऑपरेटर्स)
# =====================================================
# यह ऑपरेटर्स गणितीय गणनाओं के लिए उपयोग होते हैं।
# इनसे हम जोड़, घटाव, गुणा, भाग जैसी संख्याओं से संबंधित गणनाएँ कर सकते हैं।
#
# Operators: + (Addition), - (Subtraction), * (Multiplication), / (Division),
#            % (Modulus), ** (Exponentiation), // (Floor Division)

# 1️⃣ Addition (+) - जोड़
# Example: दो संख्याओं का जोड़
num1 = 10
num2 = 20
sum_result = num1 + num2
print(f"Addition: {num1} + {num2} = {sum_result}")

# 2️⃣ Subtraction (-) - घटाव
# Example: बैंक अकाउंट बैलेंस से पैसे निकालना
balance = 5000
withdraw = 1200
remaining_balance = balance - withdraw
print(f"Remaining Balance: {balance} - {withdraw} = {remaining_balance}")

# 3️⃣ Multiplication (*) - गुणा
# Example: किसी सामान की कुल कीमत निकालना
price_per_item = 50
quantity = 5
total_price = price_per_item * quantity
print(f"Total Price: {price_per_item} * {quantity} = {total_price}")

# 4️⃣ Division (/) - भाग
# Example: टीम में समान रूप से चॉकलेट बाँटना
total_chocolates = 10
members = 3
chocolates_per_member = total_chocolates / members
print(f"Each member gets: {chocolates_per_member} chocolates")

# 5️⃣ Modulus (%) - शेषफल निकालना
# Example: किसी संख्या को जाँचना कि यह सम (even) है या विषम (odd)
num = 7
if num % 2 == 0:
    print(f"{num} is Even")
else:
    print(f"{num} is Odd")

# 6️⃣ Exponentiation (**) - घातांक
# Example: किसी संख्या का स्क्वायर या क्यूब निकालना
base = 2
power = 3
result = base ** power
print(f"{base} raised to power {power} = {result}")

# 7️⃣ Floor Division (//) - भागफल का पूर्णांक भाग
# Example: किसी संख्या को ग्रुप में बाँटना और पूर्ण ग्रुप निकालना
students = 27
group_size = 5
total_groups = students // group_size
print(f"Total full groups: {total_groups}")

# ========== Real-World Problems (10 Examples) ===========
# 1. किसी स्कूल में टोटल स्टूडेंट्स को बराबर टीम में बाँटना
# 2. डिस्काउंट सिस्टम लागू करना
# 3. EMI कैलकुलेशन
# 4. रेस्टोरेंट में बिल स्प्लिट करना
# 5. किसी फैक्ट्री में मशीनों का आउटपुट कैलकुलेट करना
# 6. किसी स्पोर्ट्स टीम में खिलाड़ियों की जरूरत निकालना
# 7. किसी ई-कॉमर्स साइट पर टोटल कार्ट वैल्यू निकालना
# 8. बैंक का इंटरेस्ट कैलकुलेशन
# 9. किसी लॉटरी सिस्टम में शेष भाग्यशाली नंबर निकालना
# 10. ट्रेन या बस में सीटों का वितरण

# 🔹 अगले ऑपरेटर (Comparison Operators) के लिए तैयार रहिए! 🚀
# =====================================================
