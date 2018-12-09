#x = int(input())

#10進数をn進数へ
def change(i, n):
    if (int(i / n)):
        return change(int(i/n), n)+str(i%n)
    return str(i%n)

#n進数を10進数へ
def change_to_10(i, n):
    x = 0
    for j in range(1, len(i)+1):
        x += int(i[-j]) * (n ** (j-1))
    return x

y = 123
print(change_to_10(str(y), 4))
