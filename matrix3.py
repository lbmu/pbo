# matriks tiga kali tiga, ngga tahu harus dipisah
# ngga tahu ngga, nyari invers, determinan, sama transpose nya belum
# ketemu kalau pake logika pengulangan
# lagian juga modul matrix2 nya udah hampir lebih 100 baris
from matrix2 import Matrix, Abstract
from function import unpack


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
        a = self.mainMatrix[1][2]
        self.mainMatrix[1][2] = self.mainMatrix[2][1]
        self.mainMatrix[2][1] = a
        return self.mainMatrix
        pass

    def inverse(self):
        pass

    def determinant(self):

        pass
    pass
