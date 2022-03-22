with open('input.txt') as file:
    W, n = map(int, file.readline().split())
    A = list(map(int, file.readline().split()))


F = [1] + [0] * W
F_new = F[:]

for j in range(len(A)):
    for i in range(A[j], W + 1):
        if F[i - A[j]] == 1:
            F_new[i] = 1
    F = F_new[:]

i = W
while F[i] == 0:
    i -= 1
print(i)
