x = 10
y = 10

def A(d):
    ans = (x / d + 1) * (y / d + 1)
    return int(ans)

print(A(1))
ans = 0
d = 1
for x in range(0,11):
    for y in range(0,11):
        ans += 1 / d
print(ans)
