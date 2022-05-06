# Cracking the code interview 
#
# 1.2 - Check permutation
# Given two strings, write a method to decide if one is a permutation of the other


# With datastructure and string with ASCII
def is_permutation(string1, string2):
    if ((isinstance(string1, str) == False) or (isinstance(string2, str) == False)) :
        return None

    if (len(string1) != len(string2)):
        return False

    char_set1 = [0] * 128
    char_set2 = [0] * 128

    for char in string1:
        char_set1[ord(char)] += 1

    for char in string2:
        char_set2[ord(char)] += 1

    for i in range(128):
        if char_set1[i] != char_set2[i]:
            return False

    return True

def test():
    print(is_permutation("abc", "cba") == True)
    print(is_permutation("aabbcc", "abc") == False)
    print(is_permutation("abcdefghijklmnopqrstuvxz", "zxvutsrqponmlkjihgfedcba") == True)
    print(is_permutation("", "") == True)
    print(is_permutation("123", "321") == True)
    print(is_permutation(None, None) == None)
    print(is_permutation(111, 111) == None)
    print(is_permutation(123, 123) == None)

test()