# vektor cuman pake list 1D, semoga ngga impor dari modul matriks
import math
import function


class Vector:
    def __init__(self, value1, value2, dimensions):
        self.vectorA = value1
        self.vectorB = value2
        self.dimensions = dimensions
        pass

    def printVector(self):
        print('< ', end='')
        for x in self.vectorA:
            print(x, end=', ')
        print('>')

        print('< ', end='')
        for x in self.vectorB:
            print(x, end=', ')
        print('>')
    pass


class VectorOperations(Vector):
    def __init__(self, value1, value2, dimensions):
        super().__init__(value1, value2, dimensions)
        pass

    def dotProduct(self, size):
        dot = 0
        for x in range(size):
            dot += self.vectorA[x]*self.vectorB[x]
        return dot
        pass

    def crossProduct(self):
        cross = function.detVector(self.vectorA, self.vectorB)
        # print(cross)
        for x in cross:
            print(x)
        res = 1
        det = []
        detnet = []
        i = 1
        while i <= 3:
            for x in range(2):
                # print(cross[x][x+i], end=' ')
                res *= cross[x][x + i]
            det.append(res)
            i += 1
            res = 1
            pass
        print(det)
        i = 1
        while i <= 3:
            y = i
            for x in range(2):
                # print(cross[x][y], end=' ')
                res *= cross[x][y]
                y -= 1
            detnet.append(res)
            i += 1
            res = 1
            pass
        print(detnet)
        finalProduct = (det[0] - detnet[1],
                        det[1] - detnet[2],
                        det[2] - detnet[0],
                        )
        print(f'({finalProduct[0]})i + '
              f'({finalProduct[1]})j + '
              f'({finalProduct[2]})k')

    def cosAngle(self, size):
        num = self.dotProduct(size)
        den = function.notation(self.vectorA) * function.notation(self.vectorB)
        return math.acos(num / den)  # ini gimana biar bentuknya derajat ya
        pass

    def orthoProjection(self):
        opt = int(input('1. A to B\n'
                        '2. B to A\n'))
        den = None
        vproj = None
        if opt == 1:
            den = function.notation(self.vectorB)
            vproj = self.vectorB
        elif opt == 2:
            den = function.notation(self.vectorA)
            vproj = self.vectorA
        product = self.dotProduct(self.dimensions) / den ** 2
        ortho = []
        for x in vproj:
            x = x * product
            print(x)
            ortho.append(x)
            pass
        return ortho

    pass
