pilih = 'ya'
while pilih != 'tidak':
    # start = int(input('Mulai dari :'))
    # end = int(input('Sampai :'))
    # pilihan = (input('Bilangan Ganjil/Genap/Prima :')).lower()
    def bilanganGanjil(start, end):
        print('Bilangan Ganjil')
        ganjil = []
        for i in range(start, end + 1):
            if i % 2 == 1:
                ganjil.append(i)
                print(i, end=' ')
        return ganjil

    def bilanganGenap(start, end):
        print('Bilangan Genap')
        genap = []
        for i in range(start, end + 1):
            if i % 2 == 0:
                genap.append(i)
                print(i, end=' ')
        return genap

    def bilanganPrima(start, end):
        print('Bilangan Prima')
        prima = []
        for i in range(start, end + 1):
            if i > 1:
                for j in range(2, i):
                    if (i % j) == 0:
                        break
                else:
                    prima.append(i)
                    print(i, end=' ')
        return prima

    def tulisFile(ganjil, genap, prima):
        with open('file.txt', 'w') as file:
            for item in ganjil:
                file.write(str(item) + ' ')
            file.write('\n')
            for item in genap:
                file.write(str(item) + ' ')
            file.write('\n')
            for item in prima:
                file.write(str(item) + ' ')

    print('Bilangan Ganjil')
    ganjilGlobal = bilanganGanjil(int(input('Start : ')), int(input('End : ')))
    print(ganjilGlobal)
    print('\nBilangan Genap')
    genapGlobal = bilanganGenap(int(input('Start : ')), int(input('End : ')))
    print('\nBilangan Prima')
    primaGlobal = bilanganPrima(int(input('Start : ')), int(input('End : ')))
    tulisFile(ganjilGlobal, genapGlobal, primaGlobal)
    pilih = input('\nMasih ingin memilh?(ya/tidak): ')
