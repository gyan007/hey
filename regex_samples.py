# 1. Check if a string contains only alphabets

pattern = r"^[A-Za-z]+$"

# 2. Check if a string contains only digits

pattern = r"^\d+$"

# 3. Validate a mobile number (10 digits only)

pattern = r"^[0-9]{10}$"

# 4. Check if a string starts with a vowel

pattern = r"^[AEIOUaeiou]"

# 5. Find all vowels in a string

import re
vowels = re.findall(r"[AEIOUaeiou]", "Beautiful day")
print(vowels)   # ['e', 'a', 'u', 'i', 'u', 'a']

# 6. Replace all vowels with *

import re
text = "Hello World"
new_text = re.sub(r"[AEIOUaeiou]", "*", text)
print(new_text)  # H*ll* W*rld

# 7. Extract all words starting with capital letters

import re
text = "Ravi and John went to New York"
names = re.findall(r"\b[A-Z][a-z]*\b", text)
print(names)  # ['Ravi', 'John', 'New', 'York']

# 8. Find all numbers in a string

text = "The price is 120 and discount is 10%"
numbers = re.findall(r"\d+", text)
print(numbers)  # ['120', '10']

# 9. Replace all spaces with underscores

text = "Python is fun"
new_text = re.sub(r"\s", "_", text)
print(new_text)  # Python_is_fun

# 10. Check if a string ends with “ing”

pattern = r".*ing$"

# 🔹 11. Extract domain from an email address

email = "user@example.com"
match = re.search(r"@([A-Za-z0-9.-]+)", email)
print(match.group(1))   # example.com

# 🔹 12. Find all words of 4 or more letters

text = "This is a simple regex practice session"
words = re.findall(r"\b[a-zA-Z]{4,}\b", text)
print(words)  # ['This', 'simple', 'regex', 'practice', 'session']

# 🔹 13. Remove all digits from a string

text = "Room number 404 at floor 7"
cleaned = re.sub(r"\d", "", text)
print(cleaned)  # Room number  at floor 

# 🔹 14. Check if a string is a valid variable name

pattern = r"^[a-zA-Z_]\w*$"


# 🔹 15. Split text by commas or semicolons

text = "apple,banana;grape;orange,kiwi"
fruits = re.split(r"[,;]", text)
print(fruits)