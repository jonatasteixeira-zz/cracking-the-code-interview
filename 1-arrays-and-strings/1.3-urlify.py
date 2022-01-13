# Cracking the code interview 
#
# 1.3 - URLify
# Wrrite a method to replace all space in a string with '%20'. You may assume that the string has sufficient space at the end to hold adictional characters,  and that you are given the "true" length of the string.
# Note: if implement in Java, please use a character array so that you can perform this operation in place.
# EXAMPLE
# Input: "Mr  John Smith      ", 13
# Output: "Mr%20John%20Smith"

def urlify(string):
    if (isinstance(string, str) == False):
        return None

    restring = ""
    last_char = ''
    for char in string:
        if (char != ' ' or last_char != ' '):
            if (char == ' '): 
                restring += '%20'
            else:
                restring += char
        last_char = char

    if (last_char == ' '):
        restring = restring[:len(restring)-3]
   # print("\"" + restring + "\"")
    return restring

def test_urlify():
    print(urlify("abc") == "abc")
    print(urlify("aa      bb      cc") == "aa%20bb%20cc") 
    print(urlify("abc         ") == "abc")
    print(urlify("") == "")
    print(urlify("123") == "123")
    print(urlify(None) == None)
    print(urlify(111) == None)
    print(urlify(123) == None)

test_urlify()

