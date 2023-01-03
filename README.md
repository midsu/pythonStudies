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
ou learned another object-oriented language before Python, you may find it strange to use len(collection) instead of collection.len(). This apparent oddity is the tip of an iceberg that, when properly understood, is the key to everything we call Pythonic./
The term magic method is slang for special method, but how do we talk about a specific method like __getitem__? I learned to say “dunder-getitem” from author and teacher Steve Holden. “Dunder” is a shortcut for “double underscore before and after.” That’s why the special methods are also known as dunder methods. The “Lexical Analysis” chapter of The Python Language Reference warns that “Any use of __*__ names, in any context, that does not follow explicitly documented use, is subject to breakage without warning.”/
TIP:
One reason to still use my_fmt.format() is when the definition of my_fmt must be in a different place in the code than where the formatting operation needs to happen. For instance, when my_fmt has multiple lines and is better defined in a constant, or when it must come from a configuration file, or from the database. Those are real needs, but don’t happen very often./

