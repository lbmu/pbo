# from main import size

def unpack(mat):
    unpackedMat = [element for row in mat for element in row]
    # print()
    return unpackedMat
    pass


def inputMain(size):
    matrixDef = []
    print('Matrix A\n-----')
    for i in range(size):
        rowValue = []
        for j in range(size):
            rowValue.append(float(input(f'Entry {i} {j} = ')))
        matrixDef.append(rowValue)
    return matrixDef
    pass


def inputAux(size):
    matrixOp = []
    print(f'Matrix B')
    for i in range(size):
        rowValue = []
        for j in range(size):
            rowValue.append(float(input(f'Entry {i} {j} = ')))
        matrixOp.append(rowValue)
    return matrixOp
    pass
