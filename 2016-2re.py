data = {"a":0, "b":1, "c":2, "d":3, "e":4, "f":5, "g":6, "h":7}

x = input()
y = ''
ans = 0
for i in range(len(x)):
    ans += int(data[x[i]]) * (8 ** int(len(x)-i-1) )

print(ans)
print(data['a'])
