'''
43 44 45 46 47 48 49
42 21 22 23 24 25 26
41 20  7  8  9 10 27
40 19  6  1  2 11 28
39 18  5  4  3 12 29
38 17 16 15 14 13 30
37 36 35 34 33 32 31
'''

class SpiralDiagonalNumbers:
    def __init__(self):
        self.elm = 1
        self.step = 2
        self.ctr = 0

    def next(self):
        if self.ctr % 4 > 0 or self.ctr == 0:
            self.elm = self.elm + self.step
        elif self.ctr % 4 == 0:
            self.step = self.step + 2
            self.elm = self.elm + self.step
        self.ctr = self.ctr + 1
        return self.elm

def solution():
    spiral_diags = SpiralDiagonalNumbers()
    res = 1
    next_elm = spiral_diags.next()
    while next_elm <= 1001 ** 2:
        res += next_elm
        next_elm = spiral_diags.next()
    return res

if __name__ == '__main__':
    print solution()
