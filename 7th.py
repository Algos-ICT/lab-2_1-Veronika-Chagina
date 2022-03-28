with open('input.txt') as file:
    K, n = map(int, file.readline().split())
    t = list(map(int, file.readline().split()))

t = sorted(t)

i = 0
cur_sum = 0

while i < len(t) and cur_sum + t[i] <= K:
    cur_sum += t[i]
    i += 1

print(i)
