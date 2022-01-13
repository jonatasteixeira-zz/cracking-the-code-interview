# Cracking the code interview 
#
# 1.9 - String rotation
# Problem: Assume you have a method isSubstring which checks if one word is a substring of another. 
# Given two strings, write the code to check if one string is a rotation of the other using only one call to isSubstring (e.g., waterbottle is a rotation of erbottlewat)

# Check is string2 is substring of string1
def isSubstring(string1, string2):
    if ( (not isinstance(string1, str)) and (not isinstance(string2, str)) ):
        return None

    for i in range(len(string1)):
        ctrl=0
        while ( (ctrl < len(string2)) and (ctrl+i < len(string1)) and (string1[i+ctrl] == string2[ctrl])):
            ctrl += 1
        if ctrl == len(string2):
            return True
    return False

def test_isSubstring():
    print (isSubstring("the firt test of string", "test") == True)
    print (isSubstring("the firt test of string", "string") == True)
    print (isSubstring("the firt test of string", "of") == True)
    print (isSubstring("the firt test of string", " t") == True)
    print (isSubstring("the firt test of string", "zambu") == False)
    print (isSubstring("t", "t") == True)
    print (isSubstring("a", "t") == False)
    print (isSubstring("test", "tes") == True)
    print (isSubstring(123, 1) == None)

test_isSubstring()