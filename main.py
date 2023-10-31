import menu

# opt buat yang paling luar (keinginan user untuk masih ingin menginput)
opt = None
while opt != 'n':
    vmopt = int(input('Input\n'
                      '[1] Vector\n'
                      '[2] 2 x 2 Matrix\n'
                      '[3] 3 x 3 Matrix\n'
                      ))
    # ini buat vector
    if vmopt == 1:
        menu.menuVector()
    # ini buat matrix 2 x 2
    elif vmopt == 2:
        menu.menuMatrix2()
        pass
        # ini buat matrix 3 x 3
    elif vmopt == 3:
        pass
    opt = input('Reinput from main Matrix and Vector?(y/n) : ').lower()
    pass
