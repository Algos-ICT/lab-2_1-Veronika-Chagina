with open('input.txt') as file:
    n = int(file.readline())


ans = []
cur_sum = 0
i = 1

#начиная с 1 подбираем все числа, на которые можно разбить n, увеличивая 1 после каждой операции
while cur_sum + i <= n:
    ans.append(i)
    cur_sum += i
    i += 1
#если конечная сумма не равна n, то прибавляем в ответ разность n и конечной суммы
if cur_sum != n:
    print(ans[-1])
    ans[-1] += n - cur_sum

print(len(ans))
print(*ans)
