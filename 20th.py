N, K = map(int, input().split())
word = input()


def almost_palidrom(word, K):
    if len(word) == 1:
        return True
    first_half = word[:len(word) // 2]
    if len(word) % 2 == 0:
        second_half = word[len(word) // 2:]
    else:
        second_half = word[len(word) // 2 + 1:]
    errorsCount = 0
    for i in range(len(first_half)):
        if first_half[i] != second_half[len(second_half) - i - 1]:
            errorsCount += 1
        if errorsCount > K:
            return False
    return True


count = 0
for size in range(1, len(word)):
    for i in range(len(word) - size + 1):
        sub_word = word[i:i + size]
        if almost_palidrom(sub_word, K):
            count += 1

if almost_palidrom(word, K):
    count += 1


print(str(count))

