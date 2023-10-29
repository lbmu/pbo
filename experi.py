# kalo stuck waktu bikin fungsi atau program coba disini sekalian sama outputnya
# atau kalo lagi coba
# m = [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 'A', 'B'], ['C', 'D', 'E', 'F']]
import function

i = 0
m = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
# a = m[0][i+1]
# print(len(m))
det = 0
res = 1
for i in range(len(m)):
    for j in range(2):
        m[i].append(m[i][j])  # ganggu (asalnya ada error ganggu yang ga ngaruh ke program)

for i in range(len(m)):
    for j in range(len(m)):
        if j < len(m):
            res *= m[i][i]
            pass
        pass
    print(res)
for x in m:
    print(x)
print(det)
