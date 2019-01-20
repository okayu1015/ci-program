#s スタート，k　間隔 ,l
def num0(a,s,k,l):
    a[s+0] += '****'
    a[s+1] += '|  |'
    a[s+2] += '*  *'
    a[s+3] += '|  |'
    a[s+4] += '****'
    for i in range(l):
        for j in range(k):
            a[i] += ' '
        if i < s or i > s+4:
            for j in range(4):
                a[i] += ' '
            

def num1(a,s,k,l):
    a[s+0] += '*'
    a[s+1] += '|'
    a[s+2] += '*'
    a[s+3] += '|'
    a[s+4] += '*'
    for i in range(l):
        for j in range(k):
            a[i] += ' '
        if i < s or i > s+4:
            for j in range(1):
                a[i] += ' '

def num2(a,s,k,l):
    a[s+0] += '****'
    a[s+1] += '   |'
    a[s+2] += '****'
    a[s+3] += '|   '
    a[s+4] += '****'
    for i in range(l):
        for j in range(k):
            a[i] += ' '
        if i < s or i > s+4:
            for j in range(4):
                a[i] += ' '

def num3(a,s,k,l):
    a[s+0] += '****'
    a[s+1] += '   |'
    a[s+2] += '****'
    a[s+3] += '   |'
    a[s+4] += '****'
    for i in range(l):
        for j in range(k):
            a[i] += ' '
        if i < s or i > s+4:
            for j in range(4):
                a[i] += ' '

def num4(a,s,k,l):
    a[s+0] += '*  *'
    a[s+1] += '|  |'
    a[s+2] += '****'
    a[s+3] += '   |'
    a[s+4] += '   *'
    for i in range(l):
        for j in range(k):
            a[i] += ' '
        if i < s or i > s+4:
            for j in range(4):
                a[i] += ' '

def num5(a,s,k,l):
    a[s+0] += '****'
    a[s+1] += '|   '
    a[s+2] += '****'
    a[s+3] += '   |'
    a[s+4] += '****'
    for i in range(l):
        for j in range(k):
            a[i] += ' '
        if i < s or i > s+4:
            for j in range(4):
                a[i] += ' '

def num6(a,s,k,l):
    a[s+0] += '*   '
    a[s+1] += '|   '
    a[s+2] += '****'
    a[s+3] += '|  |'
    for i in range(l):
        for j in range(k):
            a[i] += ' '
        if i < s or i > s+4:
            for j in range(4):
                a[i] += ' '

def num7(a,s,k,l):
    a[s+0] += '****'
    a[s+1] += '   |'
    a[s+2] += '   *'
    a[s+3] += '   |'
    a[s+4] += '   *'
    for i in range(l):
        for j in range(k):
            a[i] += ' '
        if i < s or i > s+4:
            for j in range(4):
                a[i] += ' '

def num8(a,s,k,l):
    a[s+0] += '****'
    a[s+1] += '|  |'
    a[s+2] += '****'
    a[s+3] += '|  |'
    a[s+4] += '****'
    for i in range(l):
        for j in range(k):
            a[i] += ' '
        if i < s or i > s+4:
            for j in range(4):
                a[i] += ' '
                
def num9(a,s,k,l):
    a[s+0] += '****'
    a[s+1] += '|  |'
    a[s+2] += '****'
    a[s+3] += '   |'
    a[s+4] += '   *'
    for i in range(l):
        for j in range(k):
            a[i] += ' '
        if i < s or i > s+4:
            for j in range(4):
                a[i] += ' '


f = open('out2.txt', 'w')
#x = input()
x = '813,0,4,1,3,2'
x = x.split(',')
x.append(0)
print(x)
l = 5
max = 0
for i in range(1,len(x),2):
    if max < int(x[i]):
        max = int(x[i])
l += max

print(l)
a = ['' for i in range(l)]


for i in range(len(x[0])):
    if x[0][i] == '0':
        num0(a,int(x[i*2+1]),int(x[i*2+2]), l)
    elif x[0][i] == '1':
        num1(a,int(x[i*2+1]),int(x[i*2+2]), l)
    elif x[0][i] == '2':
        num2(a,int(x[i*2+1]),int(x[i*2+2]), l)
    elif x[0][i] == '3':
        num3(a,int(x[i*2+1]),int(x[i*2+2]), l)
    elif x[0][i] == '4':
        num4(a,int(x[i*2+1]),int(x[i*2+2]), l)
    elif x[0][i] == '5':
        num5(a,int(x[i*2+1]),int(x[i*2+2]), l)
    elif x[0][i] == '6':
        num6(a,int(x[i*2+1]),int(x[i*2+2]), l)
    elif x[0][i] == '7':
        num7(a,int(x[i*2+1]),int(x[i*2+2]), l)
    elif x[0][i] == '8':
        num8(a,int(x[i*2+1]),int(x[i*2+2]), l)
    elif x[0][i] == '9':
        num9(a,int(x[i*2+1]),int(x[i*2+2]), l)

for i in range(l):
    print(a[i])
    f.write(a[i] + '\n')
f.close()
