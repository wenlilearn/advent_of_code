import os
inputs = []
dir = os.path.dirname(__file__)
with open(os.path.join(dir, 'input.txt'), 'r') as file:
    inputs = [line.strip() for line in file]
inputs = [input.split(' ') for input in inputs]

matrix = [['.' for _ in range(650)] for _ in range(400)]

def print_matrix(matrix):
  for i in range(len(matrix)):
    print(''.join(matrix[i]))

print_matrix(inputs)
# print_matrix(matrix)

curx, cury = 250, 250
matrix[curx][cury] = '#'
DS = {
   'L': (0, -1),
   'R': (0, 1),
   'U': (-1, 0),
   'D': (1, 0),
}

total = 0
for input in inputs:
  dir = input[0]
  steps = int(input[1])
  
  for i in range(steps):
    curx += DS[dir][0]
    cury += DS[dir][1]
    if curx < 0 or curx >= len(matrix) or cury < 0 or cury >= len(matrix[0]):
      print(f'{curx} -> {cury}')
      raise ValueError('Out of bounds')
    matrix[curx][cury] = '#'
    total += 1
# print_matrix(matrix)
# print(total)

from collections import deque
i, j = 167, 398
# i, j = 253, 255
queue = deque()
visited = set()
queue.append((i, j))
DS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

while queue:
  cur = queue.popleft() 
  if cur in visited:
    continue
  total += 1
  visited.add(cur)

  for D in DS:
    nx, ny = cur[0] + D[0], cur[1] + D[1]
    if nx < 0 or nx >= len(matrix) or ny < 0 or ny >= len(matrix[0]):
      continue
    if matrix[nx][ny] == '#':
      continue
    queue.append((nx, ny))

# print_matrix(matrix)
print(total)
# 162800 too high 
# 90720 is too high
# 90719 wrong
# 63242 wrong
# 1054 too low
# 67891 Right