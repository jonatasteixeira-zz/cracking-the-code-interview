# Cracking the code interview 
#
# 5.2 - Binary to String
# Given a real number between 1 and 0 (e.g., 0.72) that is passed in as a double, print
# the binary representation. If the number cannot be represented accurately in binary with at most
# 32 characters, print ERROR.

def float_to_bin(number):
    #if number < 0 or number > 1:
    #    return "ERROR"

    integer = bin(int(number.split(".")[0]))[2:]
    decimal = float("0." + number.split(".")[1])

    res = str(integer)
    res += "."

    while decimal > 0:
        if len(res) > 64:
            return "ERROR"

        r = (decimal * 2)
        if r >= 1:
            res += '1'
            decimal = r - 1
        else:
            res += '0'
            decimal = r
    return res

def test():
    print(float_to_bin("15.72"))

test()