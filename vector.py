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
        for x in cross:
            print(x)
        # print(len(cross[0]))
        res = 1
        det = []
        detnet = []
        for x in range(2):
            if x < len(cross):
                # print(cross[x][x+1], end=' ')
                res *= cross[x][x + 1]
        det.append(res)
        res = 1
        for x in range(2):
            if x < len(cross):
                # print(res, cross[x][x+2], end=' ')
                res *= cross[x][x + 2]
        det.append(res)
        res = 1
        for x in range(2):
            if x < len(cross):
                # print(cross[x][x+1], end=' ')
                res *= cross[x][x + 3]
        det.append(res)
        # print(res)
        pass
        print(det)
        res = 1
        stepdown = 2
        for x in range(2):
            if x < len(cross):
                # print(res, cross[x][x+2], end=' ')
                stepdown -= 1
                res *= cross[x][stepdown]
        detnet.append(res)
        res = 1
        stepdown = 3
        for x in range(2):
            if x < len(cross):
                # print(res, cross[x][x+2], end=' ')
                stepdown -= 1
                res *= cross[x][stepdown]
        detnet.append(res)
        res = 1
        stepdown = 4
        for x in range(2):
            if x < len(cross):
                # print(res, cross[x][x+2], end=' ')
                stepdown -= 1
                res *= cross[x][stepdown]
        detnet.append(res)
        finalProduct = []
        for x in range(3):
            # print(det[x])
            opera = det[x] + detnet[x]
            print(opera)
            finalProduct.append(opera)
        print(detnet)
        print(f'({finalProduct[0]})i + '
              f'({finalProduct[1]})j + '
              f'({finalProduct[2]})k')
        pass

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
