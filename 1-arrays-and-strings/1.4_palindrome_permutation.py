# Cracking the code interview 
#
# 1.4 - Palindrome Permutation
# Given a string, write a function to check if it is a permutation of a palindrome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation is a rearrangement of letters.
# The palindrome does not need to be limited to just dictionary words. You can ignore casing and non-letter characters.
# EXAMPLE
# Input: Tact Coa
# Output: True (permutations: "taco cat". "atco cta". etc.)

def is_palindrome_permutation(test_string): # Considering ASCII
    if (isinstance(test_string, str) == False):
        return None
    char_set = [0] * 256 # All the letter must be found in pairs, only one can be odd

    for char in test_string:
        if (char != ' '):
            if (char >= 'A'  and char <= 'Z'):
                char_set[ord(char)+32] += 1 # To lowercase
            else:
                char_set[ord(char)] += 1
    odds = 0 # Can`t be bigger then 1

    for occour in char_set:
        odds +=  (occour % 2)

#    print (char_set)
    return (odds <= 1)

def test():
    print(is_palindrome_permutation("abcDCBA") == True)
    print(is_palindrome_permutation("Tact Coa") == True)
    print(is_palindrome_permutation("atco cta") == True) 
    print(is_palindrome_permutation("taco     cat") == True)
    print(is_palindrome_permutation("A A BBC C dc b a c b a") == True)
    print(is_palindrome_permutation("") == True)
    print(is_palindrome_permutation("123") == False)
    print(is_palindrome_permutation("aaabbbccc d ccc bbb aaa f") == False)
    print(is_palindrome_permutation(111) == None)
    print(is_palindrome_permutation(123) == None)

test()