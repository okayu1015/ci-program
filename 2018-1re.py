m = 12
n = 10
i = 0
cnt = 0
while i < m:
    j = 0
    while j < m:
        d = 0
        k = 0
        while k < n:
            #d += a[i][k] * b [k][j]
            k += 1
            cnt += 1
        #c[i][j] = d
        j += 1
    i += 1

print(cnt)
