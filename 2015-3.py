f1 = open('program.txt', 'r')
data = f1.read()
data1 = data.split('\n')
match = "main"

k = 0
for i in range(len(data1)):
    if i > 0 and data1[i] == data1[i-1]:
        print(data1[i])
