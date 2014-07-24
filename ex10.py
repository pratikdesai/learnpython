tabby_cat = "\t I'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = " I'm \\ a \\ cat."

fat_cat = '''
I'll do a list:
\t* Cat Food
\t* Fishies
\t* Catnip \n\t* Grass
'''

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

# \t ASCII horizontal tab (TAB)
# \b ASCII backspace (BS)
# \f ASCII formfeed (FF)
# \n ASCII linefeed (LF)
# \v ASCII vertical tab (VT)
# \r ASCII carriage return (CR)
# \n New Line character
# \ = Escape character

# Escape sequences don't work with %r. Use %s
