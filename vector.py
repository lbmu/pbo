# vektor cuman pake list 1D, semoga ngga impor dari modul matriks
import math
import function


class Vector:
    def __init__(self, value1, value2):
        self.vectorA = value1
        self.vectorB = value2
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
    def __init__(self, value1, value2):
        super().__init__(value1, value2)
        pass

    def dotProduct(self):
        dot = 0
        for x in range(3):
            dot += self.vectorA[x]*self.vectorB[x]
        return dot
        pass

    '''def crossProduct(self):
        i = []
        j = []
        k = []

        pass'''

    def cosAngle(self):
        num = self.dotProduct()
        den = function.notation(self.vectorA) * function.notation(self.vectorB)
        return math.acos(num / den)  # ini gimana biar bentuknya derajat ya
        pass

    pass
