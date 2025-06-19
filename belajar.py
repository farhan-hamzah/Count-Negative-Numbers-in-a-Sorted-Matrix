import numpy as np
row = int(input())
data = []
for i in range (row):
    baris = list(map(int, input().split()))
    data.append(baris)
panjang = len(data)
neg = 0
for i in range(panjang):
    for j in range(len(data[i])):
        if data[i][j] < 0:
            neg+=1
print(neg)

