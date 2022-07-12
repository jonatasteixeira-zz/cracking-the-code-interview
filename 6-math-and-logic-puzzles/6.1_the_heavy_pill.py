# Cracking the code interview 
#
# 6.1 - The heavy pill
# You have 20 bottles of pills. 19 botles have 1.0 gram pills but 1 have pills of weight 1.1 grams
# Given a scale that provides an exact measurment, how would you find the heavy bottle?
# You can only use the scale once




def heavy_bottle(bottles):
    sum = 0
    idx = 0
    while idx < len(bottles):
        sum += bottles[idx] * (idx + 1)
        idx += 1
    return (sum - 210)

def test():
    import random

    for havier in range(20):
        array = [1] * 20
        array[havier] = 1.1

        print(havier == round(heavy_bottle(array) * 10 )-1)

test()


