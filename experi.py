# kalo stuck waktu bikin fungsi atau program coba disini sekalian sama outputnya
# atau kalo lagi coba
# import function
# import vector

# p = [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 'A', 'B'], ['C', 'D', 'E', 'F']]
# q = [[0, 1, 2], [3, -4, 5], [6, 7, 8]]
# r = [[0, 1], [2, 3]]
s = [[0, 1], [2, 3], [4, 5]]
t = [[0, 1, 2], [3, 4, 5]]
# a, b = [1, 2, 3], [1, 3, -4]

for x in s:
    print(x)

print(len(s[0]), 'X', len(s))
print(len(t[0]), 'X', len(t))

if len(s) == len(t[0]):
    print('lets go')
else:
    print(':(')
