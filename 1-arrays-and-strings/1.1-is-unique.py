# Cracking the code interview 
#
# 1.1 - Is unique
# Implement an algorithm to determine if a string has all unique character. What if you cannot use additional data structure?

# without data sctructure
def is_unique1(test_string):
    if (isinstance(test_string, str) == False):
        return None

    for idx1, val1 in enumerate(test_string):
        for idx2, val2 in enumerate(test_string[(idx1+1):]):
            if (val1 == val2):
                return False
    return True

# with data structure - only with ASCII
def is_unique2(test_string):
    if (isinstance(test_string, str) == False):
        return None

    char_set = [False] * 128 # ASCII is 128
    for char in test_string:
        if (char_set[ord(char)] == True ):
            return False
        char_set[ord(char)] = True
    return True

def test_is_unique():
    print(is_unique1("abcdefghijklmnopqrstuvxz") == True)
    print(is_unique1("abcdefghijklmnopqrstuvxza") == False)
    print(is_unique1("abcdefghijklmnopqrstuvxzz") == False)
    print(is_unique1("") == True)
    print(is_unique1("1um2dois") == True)
    print(is_unique1(None) == None)
    print(is_unique1(111) == None)
    print(is_unique1(123) == None)

test_is_unique()