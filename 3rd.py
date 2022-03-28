with open('input.txt') as file:
    n = file.readline()
    a = list(map(int, file.readline().split()))
    b = list(map(int, file.readline().split()))

a.sort()
b.sort()

res = 0

for i in range(len(a)):
    res += a[i] * b[i]

print(res)

