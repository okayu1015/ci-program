#data = {'I':1,'IV':4,'V':5,'IX':9,'X':10,'XL':40,'L':50,'XC':90,'C':100,'CD':400,'D':500,'CM':900,'M':1000}

data = {1:'I',4:'IV',5:'V',9:'IX',
        10:'X',40:'XL',50:'L',90:'XC',
        100:'C',400:'CD',500:'D',900:'CM',
        1000:'M'}

x = input()
y = int(x)
if y >= 4000 and y <= 0:
    print('error')
ans = ''
    
for i in range(len(x)):
    if x[i] == '1' or x[i] == '4' or x[i] == '5' or x[i] == '9':
        ans += data[int(x[i])*(10**(len(x)-i-1))]
    else:
        if int(x[i]) < 5:
            for j in range(int(x[i])):
                ans += data[(10**(len(x)-i-1))]
        else:
            ans += data[5*(10**(len(x)-i-1))]
            for j in range(int(x[i])-5):
                ans += data[(10**(len(x)-i-1))]

print(ans)
