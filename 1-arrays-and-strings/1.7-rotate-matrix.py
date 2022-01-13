# Cracking the code interview 
#
# 1.7 - Rotate Matrix
# Given an image represented by nxn matrix, where each pixel in image is 4 bytes, write a method to rotate the image by 90 degrees. (In place)
# EXAMPLE
# A | B | C      G | D | A
# - + - + -      - + - + -
# D | E | F  =>  H | E | B
# - + - + -      - + - + -
# G | H | I      I | F | C

# A (0,0) => A (0,2)
# B (0,1) => B (1,2)
# C (0,2) => C (2,2)
# 
# D (1,0) => D (0,1)
# E (1,1) => E (1,1)
# F (1,2) => f (2,1)
# 
# G (2,0) => G (0,0)
# H (2,1) => H (1,0)
# I (2,2) => I (2,0)

# In other place # Using an auxiliar matrix
# def rotate_matrix(matrix, n):
#    dest = [[0 for _ in range(n)] for _ in range(n)] 
#    for i in range(n):
#        for j in range(n):
#            print("(" + str(i) + "," + str(j) + ") => (" + str(j) + "," + str((n-1)-i) + ")" )
#            dest[j][(n-1)-i]=matrix[i][j]
#     print(dest)


def print_matrix(matrix, n):
    for i in range(n):
        for j in range(n):
            print(matrix[i][j]),
        print('')
    print("---")

def rotate_matrix(matrix, n):
    level = 0 
    while (level <= (n-1)/2 ):
        low = level
        high = (n - 1) - level

        # first run:
        #     prev  <-  0,0
        #     0,0   <-  3,0
        #     3,0   <-  3,3
        #     3,3   <-  0,3
        #     0,3   <-  prev
        # 
        # second run:
        #     prev  <-  0,1
        #     0,1   <-  2,0
        #     2,0   <-  3,2
        #     3,2   <-  1,3
        #     1,3   <-  prev
        # 
        # third run:
        #     prev  <-  0,2
        #     0,2   <-  1,0
        #     1,0   <-  3,1
        #     3,1   <-  2,3
        #     2,3   <-  prev
        for i in range(low, high):
            prev = matrix[low][i]
            matrix[low][i] = matrix[(n - 1)-i][low]
            matrix[(n - 1)-i][low] = matrix[(n - 1)-low][(n - 1)-i]
            matrix[(n - 1)-low][(n - 1)-i] = matrix[i][(n - 1)-low]
            matrix[i][(n - 1)-low] = prev
        level +=1
#    print_matrix(matrix, n)
    return matrix


def test_rotate_matrix():
    res = rotate_matrix([[1,2],[3,4]], 2)
    print (res == [[3, 1, ], [4, 2]])

    res = rotate_matrix([[1,2,3],[4,5,6],[7,8,9]], 3)
    print (res == [[7, 4, 1], [8, 5, 2], [9, 6, 3]])

    res = rotate_matrix([['a','b','c','d'],['e','f','g','h'],['i','j','k','l'],['m','n','o','p']], 4)
    print (res == [['m', 'i', 'e', 'a'], ['n', 'j', 'f', 'b'], ['o', 'k', 'g', 'c'], ['p', 'l', 'h', 'd']])

    res = rotate_matrix([['a','b','c','d','e'],['f','g','h','i','j'],['k','l','m','n','o'],['p','q','r','s','t'],['u','v','w','x','y']], 5)
    print (res == [['u', 'p', 'k', 'f', 'a'], ['v', 'q', 'l', 'g', 'b'], ['w', 'r', 'm', 'h', 'c'], ['x', 's', 'n', 'i', 'd'], ['y', 't', 'o', 'j', 'e']]
)
test_rotate_matrix()
