# blok fungsi santai dulu ga sih
import math


def unpack(mat):
    # list comprehension
    unpackedMat = [element for row in mat for element in row]
    # print()
    return unpackedMat
    pass


def pack(mat):
    M = []
    root = int(math.sqrt(len(mat)))
    for x in range(root):
        M.append(mat[:root])
        for y in range(root):
            mat.pop(0)
    return M


def inputMain(size):
    value = []
    print(f'Matrix A ({size} x {size})\n-----')
    for i in range(size):
        rowValue = []
        for j in range(size):
            rowValue.append(float(input(f'Entry {i} {j} = ')))
        value.append(rowValue)
    return value
    pass


def inputAux(size):
    value = []
    print(f'Matrix B')
    for i in range(size):
        rowValue = []
        for j in range(size):
            rowValue.append(float(input(f'Entry {i} {j} = ')))
        value.append(rowValue)
    return value
    pass


def inputVector(size):
    if size > 3:
        print('4D vector currently unavailable')
    else:
        vector = []
        print('Input : ')
        for i in range(size):
            vector.append(int(input()))
        return vector
    pass


def notation(vect):
    value = 0
    for x in range(len(vect)):
        value += vect[x] ** 2
        pass
    return math.sqrt(value)
    pass


def detstep1(m):
    for i in range(len(m)):
        for j in range(2):
            m[i].append(m[i][j])  # ganggu (asalnya ada error ganggu yang ga ngaruh ke program)
            pass
        pass
    return m


def detVector(v1, v2):
    for y in range(2):
        v1.append(v1[y])
        v2.append(v2[y])
    cross = [v1, v2]
    return cross
