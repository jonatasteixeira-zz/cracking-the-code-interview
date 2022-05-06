# Cracking the code interview 
#
# 1.5 - One away
# Problem: One Away: There are three types of edits that can be performed on strings: insert a character, remove a character, or replace a character.
# Given two strings, write a function to check if they are one edit (or zero edits) away.
# EXAMPLES
# pale, ple -> true
# pales, pale -> true
# pale, bale -> true
# pale, bake -> false

def count_differences(string1, string2):
    if ( not (isinstance(string1,  str)) or not (isinstance(string2, str)) ):
        return None
    len_string1 = len(string1)
    len_string2 = len(string2)
    if  (abs(len_string1 - len_string2) > 1): 
        return False
    
    diff = 0
    pivot1 = 0
    pivot2 = 0

    while (pivot1 < len_string1 and pivot2 < len_string2):
        if string1[pivot1] != string2[pivot2]:
            diff+=1
            if (diff >= 2):
                return False
            if (pivot2 < len_string2-1) and (string1[pivot1] == string2[pivot2+1]):
                pivot2+=1
            elif (pivot1 < len_string1-1) and (string1[pivot1+1] == string2[pivot2]):
                pivot1+=1
            else:
                pivot1 += 1
                pivot2 += 1
        else:
            pivot1 += 1
            pivot2 += 1

    return (diff <= 1)


def test():
    print(count_differences("pale", "ple") == True)
    print(count_differences("pales", "pale") == True)
    print(count_differences("pale", "bale") == True)
    print(count_differences("pale", "bake") == False)
    print(count_differences("jonatas teixeira", "jonatas teixeiraaaa") == False)
    print(count_differences("jonatas teixeira", "j1natas teixeira") == True)
    print(count_differences("", "") == True)
    print(count_differences("123", "") == False)
    print(count_differences("aaaaaaaa", "a") == False)
    print(count_differences(111, 111) == None)
    print(count_differences(123, 321) == None)
    
test()