def f(n):
    f = {}
    f[0] = 1
    for i in range(1, n+1):
        if n < 1:
          f[i] = 1
        else:
            f[i] = (161 * f[i-1] + 2457) % 2**24
    return f[n]

print("f(100) = " + str(f(100)))

cnt = 0
for i in range(0,100):
    if f(i) % 2 == 0:
        cnt += 1
print("i<100かつf(i)が偶数の個数:" + str(cnt))
