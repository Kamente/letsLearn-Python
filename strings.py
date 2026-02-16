str1 = 'Justin'
str2 = "Kim"
print(f"Hello {str1} How is {str2} doing?")
print("st" in str2)
print(len(str2))

str2_upper = str2.upper()
print(str2_upper)

str2_lower = str2.lower()
print(str2_lower)

# strip and replace
# replace: string.replace("old", "new")
str4 = "   Hello World   "
str_strip = str4.strip()
print(str_strip)

str_replace = str_strip.replace("Hello", "Hi")
print(str_replace)


# startswith & endswith return boolean (true or false)
str_startswith = str_strip.startswith("Hello")
str_endswith = str_strip.endswith("People")
print(str_startswith, str_endswith)


str_count = str_strip.count('o')
print(str_count)


# isupper and islower (checks if all characters are upper or lower cases): returns boolean
str5 = "how are you?"
str_islower = str5.isupper()
str_isupper = str5.islower()
print(str_islower, str_isupper)
