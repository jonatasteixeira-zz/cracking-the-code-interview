# Cracking the code interview 
#
# 1.8 - Zero Matrix
# Problem: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to 0

def print_matrix(matrix, n, m):
    for i in range(n):
        for j in range(m):
            print(matrix[i][j]),
        print('')
    print("---")

def zero_matrix(matrix, n, m):
    zeros=[]
    for i in range(n):
        for j in range(m):
            if (matrix[i][j] == 0):
                zeros.append([i,j])
    for pair in zeros:
        for i in range(n):
            matrix[i][pair[1]] = 0
        for j in range(m):
            matrix[pair[0]][j] = 0
#    print_matrix(matrix, n, m)
    return matrix

def test_zero_matrix():
    res = zero_matrix([[1,0],[3,4]], 2, 2)
    print (res == [[0, 0], [3, 0]])

    res = zero_matrix([[1,2,3],[4,0,6],[7,8,9]], 3, 3)
    print (res == [[1, 0, 3], [0, 0, 0], [7, 0, 9]])
test_zero_matrix()