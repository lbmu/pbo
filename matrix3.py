# matriks tiga kali tiga, ngga tahu harus dipisah
# ngga tahu ngga, nyari invers, determinan, sama transpose nya belum
# ketemu kalau pake logika pengulangan
# lagian juga modul matrix2 nya udah hampir lebih 100 baris
import function
from matrix2 import Matrix, Abstract
from function import unpack, detstep1


class ThreeByThreeMethod(Matrix, Abstract):
    def __init__(self, matrix, sizematrix):
        super().__init__(matrix, sizematrix)
        self.matrox = unpack(self.mainMatrix)
        pass

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
        subproduct = []
        function.detstep1(self.mainMatrix)
        res = 1
        for i in range(3):
            res *= self.mainMatrix[i][i]
        product.append(res)
        res = 1
        for i in range(3):
            res *= self.mainMatrix[i][i + 1]
        product.append(res)
        res = 1
        for i in range(3):
            res *= self.mainMatrix[i][i + 2]
        product.append(res)
        res = 1
        stepdown = 3
        for i in range(3):
            stepdown -= 1
            res *= self.mainMatrix[i][stepdown]
        subproduct.append(res)
        res = 1
        stepdown = 4
        for i in range(3):
            stepdown -= 1
            res *= self.mainMatrix[i][stepdown]
        subproduct.append(res)
        res = 1
        stepdown = 5
        for i in range(3):
            stepdown -= 1
            res *= self.mainMatrix[i][stepdown]
        subproduct.append(res)
        subs = 0
        for x in range(len(subproduct)):
            subs -= subproduct[x]
        pass
        return sum(product) + subs
    pass
