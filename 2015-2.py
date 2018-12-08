f1 = open('program.txt', 'r')
data = f1.read()
data1 = data.split('\n')
match = "main"

k = 0
for i in data1:
    if match in i != True:
        print(str(k) + ':' + str(i))
    k += 1
