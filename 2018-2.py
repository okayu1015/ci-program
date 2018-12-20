f = open('mat1.txt', 'r')
data = f.read()

print(data)
for n in range(len(data)):
    if data[n] == ',':
        break

n = int((n+1)/2)
data = data.replace(',',' ')
data = data.replace('.','')
data = data.split()
print(data)
m = int(len(data)/n)
print('行 = ' + str(m))
print('列 = ' + str(n))
