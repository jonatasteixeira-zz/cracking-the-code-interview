# Cracking the code interview 
#
# 5.4 - Next Number
# Given a positive integer, print the next smallest and the next largest number
# that have the same number of 1 bit in the binary representation


def int_to_bin(number):
    return bin(number)[2:]

def count_char(string, char='1'):
    count = 0
    for c in string:
        if c == char:
            count += 1
    return count

def next_number(number):
    binary = int_to_bin(number)
    count_bits = count_char(binary, '1')

    found = False
    next_largest = number + 1
    while not found:
        if count_char(int_to_bin(next_largest)) == count_bits:
            found = True
        else:
            next_largest += 1
    
    found = False
    next_smallest = number - 1
    while not found:
        if count_char(int_to_bin(next_smallest)) == count_bits:
            found = True
        else:
            next_smallest -= 1

    print(binary, int_to_bin(next_smallest), int_to_bin(next_largest))
    return (number, next_smallest, next_largest)

def test():
    print(next_number(1000))


test()