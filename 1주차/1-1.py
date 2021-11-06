directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
snake = []
commands = []

n = int(input())
board = [[0 for col in range(n)] for row in range(n)]

k = int(input())
for idx in range(k):
    i, j = input().split()
    board[int(i) - 1][int(j) - 1] = 1

L = int(input())
dict = {}
for i in range(L):
    X, C = input().split()
    dict[int(X)] = C

i, j, d = 0, -1, 0
lifeCount = 0, 0

while True:
    if lifeCount in dict.keys():
        if dict[lifeCount] == 'D':
            d += 1
        elif dict[lifeCount] == 'L':
            d -= 1

    i += directions[d % 4][0]
    j += directions[d % 4][1]

    lifeCount += 1

    if i >= n or j >= n or i < 0 or j < 0:
        break

    if [i, j] in snake:
        break
    else:
        snake.append([i, j])

    if board[i][j] != 1 and len(snake) > 1:
        snake.pop(0)


print(lifeCount)
