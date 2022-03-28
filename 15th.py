import math

with open('input.txt') as file:
    s = file.readline()
n = len(s)
#создаем два массива 0
dp = [[0 for l in range(n)] for k in range(n)]
ep = [[0 for l in range(n)] for k in range(n)]

#массив dp = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
for i in range(n):
    for j in range(n):
        if i == j:
            dp[i][j] = 1


for right in range(n):
    for left in range(right, -1, -1):
        if left == right:
            dp[left][right] = 1
        else:
            minimal = math.inf
            mink = -1
            if s[left] == '(' and s[right] == ')' \
                    or s[left] == '[' and s[right] == ']' \
                    or s[left] == '{' and s[right] == '}':
                minimal = dp[left + 1][right - 1]

            for k in range(left, right):
                if minimal > dp[left][k] + dp[k + 1][right]:
                    minimal = dp[left][k] + dp[k + 1][right]
                    mink = k
            dp[left][right] = minimal
            ep[left][right] = mink



def restoring_response(left1, right1):
    temp = right1 - left1 + 1
    if dp[left1][right1] == temp:
        return

    if dp[left1][right1] == 0:
        print(s[left1:right1 + 1], end="")
        return

    if ep[left1][right1] == -1:
        print(s[left1], end="")
        restoring_response(left1 + 1, right1 - 1)
        print(s[right1], end="")
        return
    restoring_response(left1, ep[left1][right1])
    restoring_response(ep[left1][right1] + 1, right1)


restoring_response(0, n - 1)
