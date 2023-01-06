# pythonStudies
Here you will find all studies notes for python language
It will include:
- Notes
- Definitions
- Practice code


# Books used:
- Fluent Python, 2nd Edition (Luciano Ramalho)
- Python Crash Course, 3rd Edition (Eric Matthes)
- Python Workout (Reuven M. Lerner)


## Note:

naming and variables:
-Variable names can contain only letters, numbers, and underscores. They can start with a letter or an underscore, but not with a number. For instance, you can call a variable message_1 but not 1_message.
- Spaces are not allowed in variable names, but underscores can be used to separate words in variable names. For example, greeting_message works but greeting message will cause errors.
- Avoid using Python keywords and function names as variable names. For example, do not use the word print as a variable name;
- Variable names should be short but descriptive.
- Be careful when using the lowercase letter l and the uppercase letter O because they could be confused with the numbers 1 and 0.

running into error:
- A traceback is a record of where the interpreter ran into trouble when trying to execute your code.

Strings:
A string is a series of characters. Anything inside quotes is considered a string in Python, and you can use single or double quotes around your strings
example
'I told my friend, "Python is my favorite language!"'
"The language 'Python' is named after Monty Python, not the snake."
"One of Python's strengths is its diverse and supportive community."

Changing case:
You typically won’t want to trust the capitalization that your users provide, so you’ll convert strings to lowercase before storing them. 
name.title()
name.upper()
name.lower()


Using variablesin string
These strings are called f-strings. The f is for format, because Python formats the string by replacing the name of any variable in braces with its value.
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
message = f"Hello, {full_name.title()}!"
print(message)

Adding Whitespace to Strings with Tabs or Newlines
You can use whitespace to organize your output so it’s easier for users to read.
>>>print("Languages:\nPython\nC\nJavaScript")
>>> print("Languages:\n\tPython\n\tC\n\tJavaScript")
Languages:
    Python
    C
    JavaScript

Stripping whitespace
To programmers, 'python' and 'python ' look pretty much the same. But to a program, they are two different strings. 
But to a program, they are two different strings. For right side of a string, use the rstrip(). It is only removed temporarily

Temporary:
>>> favorite_language = 'python '
>>> favorite_language
'python '
>>> favorite_language.rstrip()
'python'
>>> favorite_language
'python '

Permenant:
>>> favorite_language = 'python '
>>> favorite_language = favorite_language.rstrip()
>>> favorite_language
'python'

You can also strip whitespace from the left side of a string using the lstrip() method, or from both sides at once using strip():
❶ >>> favorite_language = ' python '
❷ >>> favorite_language.rstrip()
' python'
❸ >>> favorite_language.lstrip()
'python '
❹ >>> favorite_language.strip()
'python'




ou learned another object-oriented language before Python, you may find it strange to use len(collection) instead of collection.len(). This apparent oddity is the tip of an iceberg that, when properly understood, is the key to everything we call Pythonic./
The term magic method is slang for special method, but how do we talk about a specific method like __getitem__? I learned to say “dunder-getitem” from author and teacher Steve Holden. “Dunder” is a shortcut for “double underscore before and after.” That’s why the special methods are also known as dunder methods. The “Lexical Analysis” chapter of The Python Language Reference warns that “Any use of __*__ names, in any context, that does not follow explicitly documented use, is subject to breakage without warning.”/
TIP:
One reason to still use my_fmt.format() is when the definition of my_fmt must be in a different place in the code than where the formatting operation needs to happen. For instance, when my_fmt has multiple lines and is better defined in a constant, or when it must come from a configuration file, or from the database. Those are real needs, but don’t happen very often./

