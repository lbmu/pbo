# matriks dua kali dua
# kelas MatrixOperations bisa dipindah ke kelas Matrix kayanya
import function
from abc import ABC, abstractmethod


class Matrix(ABC):
    def __init__(self, matrix, sizematrix):
        self.mainMatrix = matrix
        self.size = sizematrix
        self.matrox = function.unpack(self.mainMatrix)

    @abstractmethod
    def printMatrix(self):
        pass

    @abstractmethod
    def determinant(self):
        pass

    @abstractmethod
    def inverse(self):
        pass

    @abstractmethod
    def transpose(self):
        pass

    @abstractmethod
    def writeToTxt(self):
        pass

    pass


class TwoByTwoMethod(Matrix):

    def printMatrix(self):
        for entry in self.mainMatrix:
            print(entry)
        pass

    def determinant(self):
        entry = self.matrox
        det = entry[0] * entry[3] - entry[1] * entry[2]
        return det
        pass

    def inverse(self):
        entry = self.matrox
        div = 1 / self.determinant()
        inv = [[entry[3], -entry[1]], [-entry[2], entry[0]]]
        # print(len(inv))
        for x in range(len(inv)):
            for y in range(len(inv)):
                # print(f'{div} * {inv[x][y]} = ', end=' ')
                inv[x][y] = div * inv[x][y]
                # print(inv[x][y])
        return inv
        pass

    def transpose(self):
        trans = self.matrox
        temp = trans[2]
        trans[2] = trans[1]
        trans[1] = temp
        # print(trans)
        transpose = [trans[:2], trans[2:]]
        return transpose

    def writeToTxt(self):
        pass


class MatrixOperations(Matrix, ABC):
    def __init__(self, matrix, newMatrix, matrixsize):
        super().__init__(matrix, matrixsize)
        self.matrixB = newMatrix

    def printMatrix(self):
        for entry in self.matrixB:
            print(entry)
        pass

    def addition(self, stat):
        """print('Mat A')
        for x in matA:
            print(x)
        print('Mat B')
        for x in matB:
            print(x)"""
        self.matrox = []
        for x in range(self.size):
            row = []
            for y in range(self.size):
                if stat == 'a':
                    row.append(self.mainMatrix[x][y] + self.matrixB[x][y])
                elif stat == 's':
                    row.append(self.mainMatrix[x][y] - self.matrixB[x][y])
            self.matrox.append(row)
        return self.matrox
        pass

    def multiplication(self, stat):
        if stat == 'd':
            print(self.matrox)
            pass
        elif stat == 'c':
            pass
        pass
