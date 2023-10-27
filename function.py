# from main import size


def unpack(mat):
    unpackedMat = [element for row in mat for element in row]
    # print()
    return unpackedMat
    pass


def inputOp(size):
    matrixOp = []
    print(f'Matrix B')
    for i in range(size):
        rowValue = []
        for j in range(size):
            rowValue.append(float(input(f'Entry {i} {j} = ')))
        matrixOp.append(rowValue)
    return matrixOp
    pass
