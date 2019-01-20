data = {'I':1,'IV':4,'V':5,'IX':9,
        'X':10,'XL':40,'L':50,'XC':90,
        'C':100,'CD':400,'D':500,'CM':900,
        'M':1000}


x = input()
ans = 0
i = 0
while i < len(x):
    if data[x[i]] < data[x[i+1]]:     
        #print(data[x[i:i+2]])
        ans += int(data[x[i+1]])
        ans -= int(data[x[i]])
        i += 2
    else:
        #print(data[x[i]])
        ans += int(data[x[i]])
        i += 1
print(ans)
