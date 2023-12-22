# Incorrect!!!
import os
inputs = []
dir = os.path.dirname(__file__)
with open(os.path.join(dir, 'input.txt'), 'r') as file:
    inputs = [line.strip() for line in file]
inputs = [input.split(' ')[2] for input in inputs]

tmp = []
for input in inputs:
  input = input[1:-1]
  meter = int(input[1:6], 16)
  dir = int(input[6])
  print(f'{meter} -> {dir}')

  if dir == 0:
    tmp.append(('R', meter))
  elif dir == 1:
    tmp.append(('D', meter))
  elif dir == 2:
    tmp.append(('L', meter))
  elif dir == 3:
    tmp.append(('U', meter))

inputs = tmp
matrix = [['.' for _ in range(10000000)] for _ in range(10000000)]

def print_matrix(matrix):
  for i in range(len(matrix)):
    print(''.join(matrix[i]))
# print_matrix(tmp)
# print_matrix(inputs)
# print_matrix(matrix)

curx, cury = 500000, 500000
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
print_matrix(matrix)
# print(total)

from collections import deque
i, j = 500000, 500000
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
# print(total)
# 162800 too high 
# 90720 is too high
# 90719 wrong
# 63242 wrong
# 1054 too low
# 67891 Right