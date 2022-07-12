# Cracking the code interview 
#
# 5.7 - Pairwise swap
# Write a program to swap odd and even bits in a integer with a few instruction as
# possible (e.g., bit 0 and bit 1 are swapped, bit 2 and bit 3 are swaped and so on)
# EXAMPLE: 
# Input: 23     (00010111)
# Output : 43   (00101011)


def pairwise_swap(number):
    #binary = bin(number)[2:]
    #binary = (32 - len(binary)) * '0' + binary

    # Get all even bits of x with the mask
    even_bits = number & 0xAAAAAAAA
 
    # Get all odd bits of x with the mask
    odd_bits = number & 0x55555555
     
    # Right shift even bits
    even_bits >>= 1
     
    # Left shift odd bits
    odd_bits <<= 1
 
    # Combine even and odd bits
    return (even_bits | odd_bits)


def test():
    print(pairwise_swap(23))


test()