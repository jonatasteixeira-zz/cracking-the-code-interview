# Cracking the code interview 
#
# 1.6 - String compreesion
# Implement a method to perform basic string compression using the counts of repeated characters. For example, aabcccccaaa would become a2b1c5a3. 
# If the compressed string would not become smaller than the original string, your method should return the original string.

def string_compreesion(string):
    if ( not isinstance(string, str)):
        return None
    if (len(string) <= 1):
        return string

    compressed = ""
    count_letters = ''
    prev = ''

    for letter in string:
        if (letter != prev):
            compressed += str(count_letters)
            compressed += letter
            count_letters = 1
            prev = letter
        else:
            count_letters += 1
    compressed += str(count_letters)

    if len(compressed) >= len(string):
        return string
    return compressed

def test_string_compreesion():
    print (string_compreesion("aabcccccaaa") == "a2b1c5a3")
    print (string_compreesion("") == "")
    print (string_compreesion("abcdefg") == "abcdefg")
    print (string_compreesion("aaaaaaaaa") == "a9")
    print (string_compreesion("a") == "a")
    print (string_compreesion("aaabbbcccaaabbbccc") == "a3b3c3a3b3c3")
    print (string_compreesion("aabbccdd") == "aabbccdd")
    print (string_compreesion(123) == None)
    print (string_compreesion(False) == None)
    print (string_compreesion(True) == None)

test()