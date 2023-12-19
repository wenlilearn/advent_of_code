import os
inputs = []
dir = os.path.dirname(__file__)
with open(os.path.join(dir, 'input.txt'), 'r') as file:
    inputs = [line.strip() for line in file]
inputs = [list(input) for input in inputs]


U, D, L, R = 0, 1, 2, 3
DS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
visited = set()
all_visited = set()
max_steps = 0

# need stackless python
# import sys
# # Set the stack size to 10000.
# sys.setrecursionlimit(100000)
# def dfs(cur, steps):
#   global DS, visited, max_steps, inputs
#   x, y, dir = cur
#   if cur in visited or y == len(inputs[0]):
#     max_steps = max(max_steps, steps)
#     return
#   visited.add(cur)
#   all_visited.add((x, y)) 
#   cur_char = inputs[x][y]
#   if cur_char == '.':
#     x, y = x + DS[dir][0], y + DS[dir][1]
#     if x < 0 or x >= len(inputs) or y < 0 or y > len(inputs[0]) or (x, y, dir) in visited:
#       return
#     dfs((x, y, dir), steps + 1)
#   elif cur_char == '/':
#     if dir == L:
#       dir = D
#       x, y = x + DS[dir][0], y + DS[dir][1]
#       if x < 0 or x >= len(inputs) or y < 0 or y > len(inputs[0]) or (x, y, dir) in visited:
#         return
#       dfs((x, y, dir), steps + 1)
#     elif dir == R:
#       dir = U
#       x, y = x + DS[dir][0], y + DS[dir][1]
#       if x < 0 or x >= len(inputs) or y < 0 or y > len(inputs[0]) or (x, y, dir) in visited:
#         return
#       dfs((x, y, dir), steps + 1)
#     elif dir == U:
#       dir = R
#       x, y = x + DS[dir][0], y + DS[dir][1]
#       if x < 0 or x >= len(inputs) or y < 0 or y > len(inputs[0]) or (x, y, dir) in visited:
#         return
#       dfs((x, y, dir), steps + 1)
#     elif dir == D:
#       dir = L
#       x, y = x + DS[dir][0], y + DS[dir][1]
#       if x < 0 or x >= len(inputs) or y < 0 or y > len(inputs[0]) or (x, y, dir) in visited:
#         return
#       dfs((x, y, dir), steps + 1)
#   elif cur_char == '\\':
#     if dir == L:
#       dir = U
#       x, y = x + DS[dir][0], y + DS[dir][1]
#       if x < 0 or x >= len(inputs) or y < 0 or y > len(inputs[0]) or (x, y, dir) in visited:
#         return
#       dfs((x, y, dir), steps + 1)
#     elif dir == R:
#       dir = D
#       x, y = x + DS[dir][0], y + DS[dir][1]
#       if x < 0 or x >= len(inputs) or y < 0 or y > len(inputs[0]) or (x, y, dir) in visited:
#         return
#       dfs((x, y, dir), steps + 1)
#     elif dir == U:
#       dir = L
#       x, y = x + DS[dir][0], y + DS[dir][1]
#       if x < 0 or x >= len(inputs) or y < 0 or y > len(inputs[0]) or (x, y, dir) in visited:
#         return
#       dfs((x, y, dir), steps + 1)
#     elif dir == D:
#       dir = R
#       x, y = x + DS[dir][0], y + DS[dir][1]
#       if x < 0 or x >= len(inputs) or y < 0 or y > len(inputs[0]) or (x, y, dir) in visited:
#         return
#       dfs((x, y, dir), steps + 1)
#   elif cur_char == '|':
#     x, y, dir = cur
#     if dir == U or dir == D:
#       x, y = x + DS[dir][0], y + DS[dir][1]  
#       if not(x < 0 or x >= len(inputs) or y < 0 or y > len(inputs[0]) or (x, y, dir) in visited):
#         dfs((x, y, dir), steps + 1)
#     else:
#       x, y, dir = cur
#       dir = U
#       x, y = x + DS[dir][0], y + DS[dir][1]  
#       if not(x < 0 or x >= len(inputs) or y < 0 or y > len(inputs[0]) or (x, y, dir) in visited):
#         dfs((x, y, dir), steps + 1)
#       x, y, dir = cur
#       dir = D
#       x, y = x + DS[dir][0], y + DS[dir][1]  
#       if x < 0 or x >= len(inputs) or y < 0 or y > len(inputs[0]) or (x, y, dir) in visited:
#         return
#       dfs((x, y, dir), steps + 1)
#   elif cur_char == '-':
#     x, y, dir = cur
#     if dir == 'L' or dir == 'R':
#       x, y = x + DS[dir][0], y + DS[dir][1]  
#       if not(x < 0 or x >= len(inputs) or y < 0 or y > len(inputs[0]) or (x, y, dir) in visited):
#         dfs((x, y, dir), steps + 1)
#     else:
#       x, y, dir = cur
#       dir = L
#       x, y = x + DS[dir][0], y + DS[dir][1]  
#       if not (x < 0 or x >= len(inputs) or y < 0 or y > len(inputs[0]) or (x, y, dir) in visited):
#         dfs((x, y, dir), steps + 1)
#       x, y, dir = cur
#       dir = R
#       x, y = x + DS[dir][0], y + DS[dir][1]  
#       if x < 0 or x >= len(inputs) or y < 0 or y > len(inputs[0]) or (x, y, dir) in visited:
#         return
#       dfs((x, y, dir), steps + 1)
#   visited.remove(cur)
# dfs((0, 0, R), 0)
# print(max_steps)
# print(len(all_visited))
import os
inputs = []
dir = os.path.dirname(__file__)
with open(os.path.join(dir, 'input.txt'), 'r') as file:
    inputs = [line.strip() for line in file]
inputs = [list(input) for input in inputs]
m, n = len(inputs), len(inputs[0])

def run(sx, sy, sd):
  import os
  inputs = []
  dir = os.path.dirname(__file__)
  with open(os.path.join(dir, 'input.txt'), 'r') as file:
      inputs = [line.strip() for line in file]
  inputs = [list(input) for input in inputs]
  orig_inputs = [list(input) for input in inputs]

  U, D, L, R = 0, 1, 2, 3
  DS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
  visited = set()

  from collections import deque
  queue = deque()
  queue.append((sx, sy, sd))
  while queue:
    # print(queue)
    cur = queue.popleft()
    x, y, dir = cur
    inputs[x][y] = '#'
    if (x, y, dir) in visited:
      continue
    visited.add(cur)
    cur_char = orig_inputs[x][y]

    if cur_char == '.':
      x, y = x + DS[dir][0], y + DS[dir][1]
      if x < 0 or x >= len(inputs) or y < 0 or y >= len(inputs[0]) or (x, y, dir) in visited:
        continue
      queue.append((x, y, dir))
    elif cur_char == '/':
      if dir == L:
        dir = D
        x, y = x + DS[dir][0], y + DS[dir][1]
        if x < 0 or x >= len(inputs) or y < 0 or y >= len(inputs[0]) or (x, y, dir) in visited:
          continue
        queue.append((x, y, dir))
      elif dir == R:
        dir = U
        x, y = x + DS[dir][0], y + DS[dir][1]
        if x < 0 or x >= len(inputs) or y < 0 or y >= len(inputs[0]) or (x, y, dir) in visited:
          continue
        queue.append((x, y, dir))
      elif dir == U:
        dir = R
        x, y = x + DS[dir][0], y + DS[dir][1]
        if x < 0 or x >= len(inputs) or y < 0 or y >= len(inputs[0]) or (x, y, dir) in visited:
          continue
        queue.append((x, y, dir))
      elif dir == D:
        dir = L
        x, y = x + DS[dir][0], y + DS[dir][1]
        if x < 0 or x >= len(inputs) or y < 0 or y >= len(inputs[0]) or (x, y, dir) in visited:
          continue
        queue.append((x, y, dir))
    elif cur_char == '\\':
      if dir == L:
        dir = U
        x, y = x + DS[dir][0], y + DS[dir][1]
        if x < 0 or x >= len(inputs) or y < 0 or y >= len(inputs[0]) or (x, y, dir) in visited:
          continue
        queue.append((x, y, dir))
      elif dir == R:
        dir = D
        x, y = x + DS[dir][0], y + DS[dir][1]
        if x < 0 or x >= len(inputs) or y < 0 or y >= len(inputs[0]) or (x, y, dir) in visited:
          continue
        queue.append((x, y, dir))
      elif dir == U:
        dir = L
        x, y = x + DS[dir][0], y + DS[dir][1]
        if x < 0 or x >= len(inputs) or y < 0 or y >= len(inputs[0]) or (x, y, dir) in visited:
          continue
        queue.append((x, y, dir))
      elif dir == D:
        dir = R
        x, y = x + DS[dir][0], y + DS[dir][1]
        if x < 0 or x >= len(inputs) or y < 0 or y >= len(inputs[0]) or (x, y, dir) in visited:
          continue
        queue.append((x, y, dir))
    elif cur_char == '|':
      x, y, dir = cur
      if dir == U or dir == D:
        x, y = x + DS[dir][0], y + DS[dir][1]  
        if not(x < 0 or x >= len(inputs) or y < 0 or y >= len(inputs[0]) or (x, y, dir) in visited):
          queue.append((x, y, dir))
      else:
        x, y, dir = cur
        dir = U
        x, y = x + DS[dir][0], y + DS[dir][1]  
        if not(x < 0 or x >= len(inputs) or y < 0 or y >= len(inputs[0]) or (x, y, dir) in visited):
          queue.append((x, y, dir))
        x, y, dir = cur
        dir = D
        x, y = x + DS[dir][0], y + DS[dir][1]  
        if x < 0 or x >= len(inputs) or y < 0 or y >= len(inputs[0]) == 0 or (x, y, dir) in visited:
          continue
        queue.append((x, y, dir))
    elif cur_char == '-':
      x, y, dir = cur
      if dir == 'L' or dir == 'R':
        x, y = x + DS[dir][0], y + DS[dir][1]  
        if not(x < 0 or x >= len(inputs) or y < 0 or y >= len(inputs[0]) or (x, y, dir) in visited):
          queue.append((x, y, dir))
      else:
        x, y, dir = cur
        dir = L
        x, y = x + DS[dir][0], y + DS[dir][1]  
        if not (x < 0 or x >= len(inputs) or y < 0 or y >= len(inputs[0]) or (x, y, dir) in visited):
          queue.append((x, y, dir))
        x, y, dir = cur
        dir = R
        x, y = x + DS[dir][0], y + DS[dir][1]  
        if x < 0 or x >= len(inputs) or y < 0 or y >= len(inputs[0]) or (x, y, dir) in visited:
          continue
        queue.append((x, y, dir))
          
  visited_cnt = 0
  m, n = len(inputs), len(inputs[0])
  for i in range(m):
    for j in range(n):
      if inputs[i][j] == '#':
        visited_cnt += 1
  return visited_cnt

max_cnt = 0
# top row
for i in range(n):
  max_cnt = max(max_cnt, run(0, i, D))
  max_cnt = max(max_cnt, run(m - 1, i, U))

for j in range(m):
  max_cnt = max(max_cnt, run(j, 0, L))
  max_cnt = max(max_cnt, run(j, n - 1, R))
print(max_cnt)