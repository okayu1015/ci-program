def g(n):
    g = {}
    g[0] = 1
    for i in range(1,n+1):
        g[i] = (1103515245 * g[i-1] + 12345) % 2**26
    return g[n]

n = k = m = 0
flag = 0
n = {}
m = {}
num = 1000
for i in range(1, num):
    for j in range(i+1, num):
        print("(i,j) =" + str(i) + "," + str(j))
        if g(i) == g(j):
            n[m] = i
            k[m] = j
            flag = 1
            break
    if flag == 1:
        break
print(n[0])
print(k[0])
