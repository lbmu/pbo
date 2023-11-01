# di sini bakal banyak while sama if, ngasih variabelnya juga jangan asal
import function as f
import vector as v
import matrix3 as m3
import matrix2 as m2


def menuVector():
    opt = None
    while opt != 'n':
        sizeV = int(input('Size of The Vector dimensions : '))
        vectorA = f.inputVector(sizeV)
        vectorB = f.inputVector(sizeV)
        if sizeV > 5:
            print('No')
            break
        vect = v.VectorOperations(vectorA, vectorB)
        vectorOpt = None
        while vectorOpt != 'e':
            vectorOpt = input('Choose Vector Op\n'
                              '[P]rint Vector\n'
                              '[D]ot Product\n'
                              '[C]ross Product\n'
                              'Cos [A]ngle\n'
                              '[E]xit').lower()
            if vectorOpt == 'p':
                vect.printVector()
                pass
            elif vectorOpt == 'd':
                print(vect.dotProduct(sizeV))
                pass
            elif vectorOpt == 'c':
                print(vect.crossProduct())
                pass
            elif vectorOpt == 'a':
                print(vect.cosAngle(sizeV))
                pass
            pass
        opt = input('Input New Vector? (y/n)').lower()
        pass
    pass


def menuMatrix2():
    opt = None
    while opt != 'n':
        mTwo = m2.TwoByTwoMethod(f.inputMain(2), 2)
        m2Opt = input('Method\n'
                        '[P]rint Matrix | '
                        '[D]eterminant | '
                        '[I]nverse | '
                        '[T]transpose | '
                        '[O]perations | '
                        '[E]xit | '
                        ' = '
                        ).lower()
        while m2Opt != 'e':
            pass
        opt = input('Input New Matrix? (y/n)').lower()
        pass
    pass
