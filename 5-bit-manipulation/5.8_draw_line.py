# Cracking the code interview 
#
# 5.8 - Draw Line
# A monochrome screen is stored as singly array of bytes, allowing eight consecutive pixels to be stored in one byte.
# The screen has width w, where w is divisible by 8 (that is, no byte will be split across rows).
# The height of the screen, of course, can be derived from the length of the array and the width.
# Implement a function that draws a horizontal line from (x1, y) to (x2, y)

# The method signature should look something like:
# drawLine(byte[] screen, int width, int x1, int x2, int y)

def print_screen(screen, w):
    idx = 0
    res = ""
    while idx < len(screen):
        if idx % w == 0:
            res += "\n"
        res += screen[idx]
        idx += 1
    return res


#def drawLine(screen, w, x1, x2, y):
#    for idx in range(y*w+x1, y*w+x2):
#        screen[idx] = '1'
#    
#    return screen

def drawLine(screen, w, x1, x2, y):
    print(print_screen(screen, w))
    a = min(x1, x2)
    b = max(x1, x2)

    line = 0
    col = 0
    res = ""
    while (line * w + col) < len(screen):
        idx = line * w + col
        if line == y and col >= a and col <= b:
            res += '1'
        else:
            res += screen[idx]

        col += 1
        if col == w:
            col = 0
            line += 1

    return print_screen(res, w)



def test():
    empty_screen =  '0' * 16 * 16 # 16 x 16
    print(drawLine(empty_screen, 16, 0, 16, 2))
 
test()