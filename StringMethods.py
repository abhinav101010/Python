# String Methods

# String Methods are built-in functions that allow you to manipulate strings.
# 1. str.upper() - Converts all characters in the string to uppercase.
# 2. str.lower() - Converts all characters in the string to lowercase.
# 3. str.title() - Converts the first character of each word to uppercase and the rest to lowercase.
# 4. str.capitalize() - Converts the first character to uppercase and the rest to lowercase.
# 5. str.replace() - Replaces all occurrences of a substring with another substring.
# 6. str.split() - Splits the string into a list of substrings based on a delimiter.
# 7. str.join() - Joins a list of strings into a single string using a specified delimiter.
# 8. str.find() - Returns the index of the first occurrence of a substring in the string.
# 9. str.count() - Returns the number of occurrences of a substring in the string.
# 10. str.strip() - Removes leading and trailing whitespace from the string.
# 11. str.lstrip() - Removes leading whitespace from the string.
# 12. str.rstrip() - Removes trailing whitespace from the string.
# 13. str.splitlines() - Splits the string into a list of substrings based on line breaks.
# 14. str.partition() - Splits the string into three parts based on a delimiter.
# 15. str.rpartition() - Splits the string into three parts based on a delimiter, starting from the end.
# 16. str.ljust() - Returns a left-justified version of the string with a specified width.
# 17. str.rjust() - Returns a right-justified version of the string with a specified width.
# 18. str.center() - Returns a centered version of the string with a specified width.
# 19. str.zfill() - Returns a zero-filled version of the string with a specified width.
# 20. str.endswith() - Returns True if the string ends with a specified suffix, False otherwise.
# 21. str.startswith() - Returns True if the string starts with a specified prefix, False otherwise.
# 22. str.substr() - Returns a substring of the string based on the specified start and end indices.
# 23. str.isalpha() - Returns True if the string contains only alphabetic characters, False otherwise.
# 24. str.isalnum() - Returns True if the string contains only alphanumeric characters, False otherwise.
# 25. str.isdigit() - Returns True if the string contains only numeric characters, False otherwise.

a = "  Hello, World!  "
print(a.strip())
print(a.strip().lower())
print(a.strip().lower().capitalize())
print(a.strip().lower().capitalize().endswith("!"))
print(a.strip().lower().capitalize().startswith("H"))
print(a.strip().lower().capitalize().replace("H", "h"))
print(a.strip().lower().capitalize().replace("H", "h").zfill(20))
print(a.strip().lower().capitalize().replace("H", "h").zfill(20).partition(" "))
print(a.strip().lower().capitalize().replace("H", "h").zfill(20).rpartition(" ")[0])
print(a[0:2])
print(a)
print(a + "AAA")
print(a[::-1])