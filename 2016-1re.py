x = input()
ans = 0
for i in range(len(x)):
    ans += int(x[i]) * (4 ** int(len(x)-i-1) )

print(ans)
