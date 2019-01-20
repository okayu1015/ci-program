def num0(a):
    a[0] += '****'
    a[1] += '|  |'
    a[2] += '*  *'
    a[3] += '|  |'
    a[4] += '****'
    for i in range(5):
        a[i] += '  '

def num1(a):
    a[0] += '*'
    a[1] += '|'
    a[2] += '*'
    a[3] += '|'
    a[4] += '*'
    for i in range(5):
        a[i] += '  '

def num2(a):
    a[0] += '****'
    a[1] += '   |'
    a[2] += '****'
    a[3] += '|   '
    a[4] += '****'
    for i in range(5):
        a[i] += '  '

def num3(a):
    a[0] += '****'
    a[1] += '   |'
    a[2] += '****'
    a[3] += '   |'
    a[4] += '****'
    for i in range(5):
        a[i] += '  '

def num4(a):
    a[0] += '*  *'
    a[1] += '|  |'
    a[2] += '****'
    a[3] += '   |'
    a[4] += '   *'
    for i in range(5):
        a[i] += '  '

def num5(a):
    a[0] += '****'
    a[1] += '|   '
    a[2] += '****'
    a[3] += '   |'
    a[4] += '****'
    for i in range(5):
        a[i] += '  '

def num6(a):
    a[0] += '*   '
    a[1] += '|   '
    a[2] += '****'
    a[3] += '|  |'
    a[4] += '****'
    for i in range(5):
        a[i] += '  '

def num7(a):
    a[0] += '****'
    a[1] += '   |'
    a[2] += '   *'
    a[3] += '   |'
    a[4] += '   *'
    for i in range(5):
        a[i] += '  '

def num8(a):
    a[0] += '****'
    a[1] += '|  |'
    a[2] += '****'
    a[3] += '|  |'
    a[4] += '****'
    for i in range(5):
        a[i] += '  '

def num9(a):
    a[0] += '****'
    a[1] += '|  |'
    a[2] += '****'
    a[3] += '   |'
    a[4] += '   *'
    for i in range(5):
        a[i] += '  '


f = open('out1.txt', 'w')
x = input()
a = ['' for i in range(5)]


for i in range(len(x)):
    if x[i] == '0':
        num0(a)
    elif x[i] == '1':
        num1(a)
    elif x[i] == '2':
        num2(a)
    elif x[i] == '3':
        num3(a)
    elif x[i] == '4':
        num4(a)
    elif x[i] == '5':
        num5(a)
    elif x[i] == '6':
        num6(a)
    elif x[i] == '7':
        num7(a)
    elif x[i] == '8':
        num8(a)
    elif x[i] == '9':
        num9(a)

for i in range(5):
    print(a[i])
    f.write(a[i] + '\n')
f.close()
