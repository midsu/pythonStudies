
# variable name
message = "Hello Python Crash Course reader!"
print(message)

# this gives error cuz of spelling
''' message = "Hello Python Crash Course reader!"
print(mesage) '''

# changing case in string with methods. The dot tells title() to act on variable name
name = "ada lovelace"
print(name.title())

# change case to uppercase or lowercase
name = "Ada Lovelace"
print(name.upper())
print(name.lower())

# using variables in strings
# These strings are called f-strings. The f is for format, 
# because Python formats the string by replacing the name of any variable in braces with its value.
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(f"Hello, {full_name.title()}!")

# You can also use f-strings to compose a message, and then assign the entire message to a variable:
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
message = f"Hello, {full_name.title()}!"
print(message)

# You can use whitespace to organize your output so it’s easier for users to read.
print("Python")
print("\tPython")
print("Languages:\nPython\nC\nJavaScript")
print("Languages:\n\tPython\n\tC\n\tJavaScript")

# stripping whitespaces
# To programmers, 'python' and 'python ' look pretty much the same. 
# But to a program, they are two different strings. For right side of a string, use the rstrip(). 
# It is only removed temporarily
favorite_language = 'python '
favorite_language
#'python '
favorite_language.rstrip()
#'python'
favorite_language
#'python '

# To remove the whitespace from the string permanently, you have to associate the stripped value with the variable name:
favorite_language = 'python '
favorite_language = favorite_language.rstrip()
favorite_language
#'python'

# You can also strip whitespace from the left side of a string using the lstrip() method, 
# or from both sides at once using strip():
favorite_language = ' python '
favorite_language.rstrip()
#' python'
favorite_language.lstrip()
#'python '
favorite_language.strip()
#'python'