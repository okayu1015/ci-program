#data = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000,"IV":4, "IX":9, "XL":40, "XC":90, "CD":400, "CM":900}

data = {"I":"1", "V":"5", "X":"10", "L":"50", "C":"100", "D":"500", "M":"1000","IV":"4", "IX":"9", "XL":"40", "XC":"90", "CD":"400", "CM":"900"}

#ローマ数字からアラビア数字へ
def change_to_romen(rome):
    ara = 0 
    #for i in range(0,len(rome)):
    i = 1
    while i <= len(rome):
        if i < len(rome) and rome[-i-1]+rome[-i] in data:
            #print(data[str(rome[-i-1]) + str(rome[-i])])
            ara += data[str(rome[-i-1]) + str(rome[-i])]
            i += 2
        else:
            #print(data[str(rome[-i])])
            ara += data[str(rome[-i])]
            i += 1
    return ara


#アラビア数字からローマ数字へ
def change_to_ara(ara):
    rome = ''
    data1 = {}
    for k,v in data.items(): #dataのkey,valueを反転
        data1[v] = k
        
    i = 1
    while i <= len(ara):
        if ara[-i] == '4' or ara[-i] == '9':
            print(str( data1[ str(int(ara[-i]) * (10**(i-1))) ] ))
            rome = str( data1[ str(int(ara[-i]) * (10**(i-1))) ] ) + rome
        if ara[-i] != '4' and ara[-i] != '9' and ara[-i] != '0':
            if ara[-i] == '5':
                print(str( data1[ str(int(ara[-i]) * (10**(i-1))) ] ))
                rome = str( data1[ str(int(ara[-i]) * (10**(i-1))) ] ) + rome
            else:
                for j in range(int(ara[-i])):
                     print(str( data1[ str(10**(i-1)) ] ))
                     rome = str( data1[ str(10**(i-1)) ] ) + rome
        i += 1
    return rome
     
num = input()
#num = 1904 #MCMIV

print(change_to_ara(str(num)))
