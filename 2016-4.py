data = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000,
        "IV":4, "IX":9, "XL":40, "XC":90, "CD":400, "CM":900}


#10進数をn進数へ
def change(i, n):
    if (int(i / n)):
        return change(int(i/n), n)+str(i%n)
    return str(i%n)

#n進数を10進数へ
def change_to_10(i, n):
    x = 0
    for j in range(1, len(i)+1):
        x += int(data[str(i[-j])]) * (n ** (j-1))
    return x

#ローマ数字からアラビア数字へ
def change_to_romen(rome):
    sum = 0 
    #for i in range(0,len(rome)):
    i = 1
    while i <= len(rome):
        if i < len(rome) and rome[-i-1]+rome[-i] in data:
            #print(data[str(rome[-i-1]) + str(rome[-i])])
            sum += data[str(rome[-i-1]) + str(rome[-i])]
            i += 2
        else:
            #print(data[str(rome[-i])])
            sum += data[str(rome[-i])]
            i += 1
    return sum

num = input()
#num = 'MCMIV' #=1904
print(change_to_romen(num))
