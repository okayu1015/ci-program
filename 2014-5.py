import math

def AR0(d):
    ans = 0
    for x in range(0,11,d):
        for y in range(0,11,d):
            ans += 1
    return ans

def AR1(d):
    ans = 0
    for x in range(0,11,d):
        for y in range(0,11,d):
            if (x-5)*(x-5) + (y-5)*(y-5) <= 25:
                ans += 1
    return ans

def AR2(d):
    ans = 0
    for x in range(0,11,d):
        for y in range(0,11,d):
            if (x <= 5 and y <= 2 * x) or (x >= 5 and y <= -2 * x + 20):
                ans += 1
    return ans    


##コッホ切片面積
a = math.sqrt(3) * 5 * 5 #最初の三角形の面積
b = 3                    #辺の個数
c = 10                   #辺のながさ


def koch(a, b, c, n):
    for i in range(1,n):
        a = a + (3*math.sqrt(3)/16)*c*c*((4/9)**i)
        b = 4 * b
    return a             #面積を返す



print('K2 =' + str(koch(a,b,c,2)))

k2 = koch(a,b,c,2)
##ピックの定理を使うのかもしれない？
