# Cracking the code interview 
#
# 5.3 - Flip bit to win
# You have an integer and you can flip exactly on bit from 0 to 1.
# Write a code to find length of the longest sequence of 1s you could create
# EXAMPLE
# Input: 1775
# Output: 8

def count_log_sequence(string):
    binary = [int(n) for n in string]

    idx = 1
    bigger = binary[idx-1]
    while idx < len(binary):
        if binary[idx] == 1:
            binary[idx] = binary[idx-1] + 1

        if binary[idx] > bigger:
            bigger = binary[idx]
        idx += 1

    return bigger

def flip_bit(string):
    idx = 0
    bigger = 0
    while idx < len(string):
        if string[idx] == '0':
            test_string = string[0:idx] + '1' + string[idx+1:]
            long = count_log_sequence(test_string)
            if long > bigger:
                bigger = long
        idx += 1
    return bigger


def test():
    print(flip_bit(bin(1775)[2:]))
    print(flip_bit("000010000100011101110000"))
    print(flip_bit("11011101111"))


test()