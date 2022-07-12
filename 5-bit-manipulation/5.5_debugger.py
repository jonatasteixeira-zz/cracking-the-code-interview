# Cracking the code interview 
#
# 5.5 - Debugger
# Explain what the following code does:
# ((n & (n-1)) == 0)

def debugger():
    print("A and B == 0 \t: Means that A and B doesn't share any 1 in common")
    print("n and (n-1)  \t: It checking for all 1 in common beetwen a number and you sucessor")

    print(" ((n & (n - 1)) == 0) : This express check if there is no 1 in common between a numnber and your sucessor")
    print("                        This situation only happen when n is power of two")
    print("                        This expression check if N in power of two")


def test():
    debugger()

test()