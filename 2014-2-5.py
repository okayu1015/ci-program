
#data = str(input())
data = '12345678901234567890123456789012 04'
x = data.split()
print(x)
#data = str(input())
data = '98765432109876543210987654321098 09'
y = data.split()
print(y)

n = 10**(int(x[1])+int(y[1]) - 31*2)

def times(x, y):
    if len(x) <= 2 and len(x) <= 2:
        return int(x) * int(y)
    else:
        a = int(x[0:int(len(x)/2)])
        b = int(x[int(len(x)/2):len(x)])
        c = int(y[0:int(len(y)/2)])
        d = int(y[int(len(y)/2):len(y)])

        return times(str(a),str(c))*(10**int(len(x))) + ((times(str(a),str(c))+times(str(b),str(d)))-((a-b)*(c-d))) * (10**int(len(x)/2)) + times(str(b),str(d))

print('======')
ans = times(x[0],y[0])*n
print('ans = ' + str(ans)) ##通常表記
ans = str("{:.32f}".format(ans))
#print(ans)

for i in range(32): ##有効数字32桁
    if ans[i] == '.':
        break

ans = ans.replace('.','')
print(str(ans[0:32]) + ' ' + str(i-1))
