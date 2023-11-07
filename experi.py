# kalo stuck waktu bikin fungsi atau program coba disini sekalian sama outputnya
# atau kalo lagi coba

import function

# m = [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 'A', 'B'], ['C', 'D', 'E', 'F']]
a, b = [0, 1, 2], [3, 4, 5]
# m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# m = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

cross = function.detVector(a, b)
for x in cross:
    print(x)
# print(len(cross[0]))
res = 1
det = []
for x in range(2):
    if x < len(cross):
        # print(cross[x][x+1], end=' ')
        res *= cross[x][x+1]
det.append(res)
res = 1
for x in range(2):
    if x < len(cross):
        # print(res, cross[x][x+2], end=' ')
        res *= cross[x][x+2]
det.append(res)
res = 1
for x in range(2):
    if x < len(cross):
        # print(cross[x][x+1], end=' ')
        res *= cross[x][x+3]
det.append(res)
# print(res)
pass
print(det)
