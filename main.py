import function
import classmethod as matrix
import menu


# masterOptions = None
options = 'y'
# newMatrixStatus = None
while options == 'y':

    size = int(input('Size of square matrix : '))
    matrixValue = function.inputMain(size)
    function.unpack(matrixValue)
    operations = matrix.MatrixMethod(matrixValue, size)
    menu.main(options)
    while options != 'e':
        options = input('Method\n'
                        '[P]rint Matrix | '
                        '[D]eterminant | '
                        '[I]nverse | '
                        '[T]transpose | '
                        '[O]perations | '
                        '[E]xit | '
                        ' = '
                        ).lower()
        if options == 'p':
            operations.printMatrix()
        elif options == 'd':
            if size == 2:
                print('Matrix Determinant : ', operations.determinant())
            else:
                print('2 x 2 Matrix only')
                pass
            pass
        elif options == 'i':
            if size != 2:
                print('Ngawur')
                pass
            else:
                for verse in operations.inverse():
                    print(verse)
            pass
        elif options == 't':
            for pose in operations.transpose():
                print(pose)
        elif options == 'o':
            # Status Operations, sentinel for Main decisions
            statOp = input('[B]asic | [M]ultiplication | [E]xit : ')
            while statOp != 'e':
                calculate = matrix.MatrixOperations(matrixValue, function.inputAux(size), size)
                # calculate Status, sentinel for AM function decisions
                calStatus = input('[A]ddition | [S]ubstraction | [E]xit:').lower()
                while calStatus == 'b':
                    if calStatus == 'a':
                        print(f'Matrix A + B')
                        for i in calculate.addition(calStatus):
                            print(i)
                    elif calStatus == 's':
                        print(f'Matrix A - B')
                        for i in calculate.addition(calStatus):
                            print(i)
                while calStatus == 'm':
                    if calStatus == 'd':
                        print(f'Matrix A + B')
                        for i in calculate.multiplication(calStatus):
                            print(i)
                    elif calStatus == 'c':
                        print(f'Matrix A - B')
                        for i in calculate.multiplication(calStatus):
                            print(i)
                    calStatus = input('[D]ot Product| [C]ross Product | [E]xit:').lower()
    options = input('Input new matrix instead?[y/n] ').lower()
