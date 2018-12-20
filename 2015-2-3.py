def f(n):
    f = {}
    f[0] = 1
    for i in range(1, n+1):
        if n < 1:
          f[i] = 1
        else:
            f[i] = (161 * f[i-1] + 2457) % 2**24
    return f[n]


cnt = 0
for i in range(0,101):
    if f(i) % 2 == 0 and i % 2 == 1:
        cnt += 1
print("i<100かつf(i)が偶数かつ奇数iの個数:" + str(cnt))


