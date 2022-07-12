# Cracking the code interview 
#
# 5.6 - Conversion
# Write a function to deterrmine the number of bits you would need
# to flip to convert integer A to integer B
# EXAMPLE
# Input 29 (11101), 15 (01111)
# Outpur: 2


def convertion1(numberA, numberB):
    binaryA = bin(numberA)[2:]
    binaryB = bin(numberB)[2:]

    bigger = max(len(binaryA), len(binaryB))
    binaryA = ((bigger - len(binaryA)) * '0') + binaryA
    binaryB = ((bigger - len(binaryB)) * '0') + binaryB
    print(binaryA, binaryB)

    idx = 0
    flips = 0
    while idx < bigger:
        if binaryA[idx] != binaryB[idx]:
            flips += 1
        idx += 1
    return flips

def convertion2(numberA, numberB):
    diff = numberA ^ numberB
    total = 0
    for bit in bin(diff)[2:]:
        if bit == '1':
            total += 1

    return total
    
def test():
    print(convertion1(29, 15), convertion2(29,15))
    print(convertion1(27, 13), convertion2(27,13))
    print(convertion1(5012, 1111), convertion2(5012, 1111))

test()