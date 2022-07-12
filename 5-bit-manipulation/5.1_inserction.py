# Cracking the code interview 
#
# 5.1 - Inserction
# You are given two 32-bit numbers, N and M, and two bit positions, i and j. 
# Write a method to set all bits between i and j in N equal to M 
# (e.g., M becomes a substring of N located at i and starting at j).
# 
# EXAMPLE: Input: N = 10000000000, M = 10101, i = 2, j = 6 Output: N = 10001010100

def set_bits(bin1_str, bin2_str, idx1, idx2):
    res = bin1_str[0:idx1] + bin2_str + bin1_str[idx2:]
    res = res[0:32]
    res = (32 - len(res)) * '0' + res
    return (res)


def test():
    bin1_str = '11111111111111111111111111111111'
    bin2_str = '00000000'

    print(set_bits(bin1_str, bin2_str, 2, 10) ==  '11000000001111111111111111111111')
    print(set_bits(bin1_str, bin2_str, 0, 8) ==   '00000000111111111111111111111111')
    print(set_bits(bin1_str, bin2_str, 30, 38) == '11111111111111111111111111111100')
    print(set_bits(bin1_str, bin2_str, 0, 0) ==   '00000000111111111111111111111111')

test()