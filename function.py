# blok fungsi santai dulu ga sih
import math


def unpack(mat):
    # list comprehension
    unpackedMat = [element for row in mat for element in row]
    # print()
    return unpackedMat
    pass


def inputMain(size):
    value = []
    print('Matrix A\n-----')
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



