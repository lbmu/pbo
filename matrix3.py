# matriks tiga kali tiga, ngga tahu harus dipisah
# ngga tahu ngga, nyari invers, determinan, sama transpose nya belum
# ketemu kalau pake logika pengulangan
# lagian juga modul matrix2 nya udah hampir lebih 100 baris
import function
from matrix2 import Matrix
from function import unpack


class ThreeByThreeMethod(Matrix):
    def __init__(self, matrix, sizematrix):
        super().__init__(matrix, sizematrix)
        self.matrox = unpack(self.mainMatrix)
        pass

    def printMatrix(self):
        for entry in self.mainMatrix:
            print(entry)

    def transpose(self):
        for x in range(len(self.mainMatrix[0])):  # range dari suatu baris atau kolom, bukan matriks secara keseluruhan
            if x < len(self.mainMatrix):  # cek kondisi agar index dari list tidak melebihi batas
                a = self.mainMatrix[0][x]
                self.mainMatrix[0][x] = self.mainMatrix[x][0]
                self.mainMatrix[x][0] = a
        # ya
        a = self.mainMatrix[1][2]
        self.mainMatrix[1][2] = self.mainMatrix[2][1]
        self.mainMatrix[2][1] = a
        return self.mainMatrix
        pass

    def inverse(self):
        pass

    def determinant(self):
        product = []
        function.detstep1(self.mainMatrix)
        for x in self.mainMatrix:
            print(x)
        i = 0
        while i < 3:    # Jujur ngga pake ChatGPT
            j = i       # Cuman bengong abis makan indomie ayam bawang
            res = 1
            for x in range(3):
                # print(q[x][j], end=' | ')
                res *= self.mainMatrix[x][j]
                j += 1
            i += 1
            product.append(res)
        i = 2           # tiba-tiba logikanya dapet
        while i < 5:    # lumayan hemat 8 baris
            j = i       # probably
            res = 1
            for x in range(3):
                # print(q[x][j], end=' | ')
                res *= self.mainMatrix[x][j]
                j -= 1
            i += 1
            product.append(res)
        total = 0
        for x in range(3):
            total += product[x]
        for x in range(3, 6):
            total -= product[x]
        return total

    def writeToTxt(self):
        pass

    pass
