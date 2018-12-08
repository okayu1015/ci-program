def AR0(d):
    ans = 0
    for x in range(0,11):
        for y in range(0,11):
            ans += 1 / d
    return ans

def AR1(d):
    ans = 0
    for x in range(0,11):
        for y in range(0,11):
            if (x-5)*(x-5) + (y-5)*(y-5) <= 25:
                ans += 1 / d
    return ans

print(AR0(1))
print(AR1(1))

print((AR0(1)/AR1(1))/4)
