# Not working!
import os
inputs = []
dir = os.path.dirname(__file__)
with open(os.path.join(dir, 'input.txt'), 'r') as file:
    inputs = [line.strip() for line in file]
inputs = [list(map(lambda i: int(i), input)) for input in inputs]

D, R, U, L = 0, 1, 2, 3
DS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
res = float('inf')
m, n = len(inputs), len(inputs[0])
visited = set()

def dfs(x, y, dir, dir_steps, heat, visited):
  global inputs, m, n, res, DS

  if x == m - 1 and y == n - 1:
    res = min(res, heat)
    print(res)
    return

  if (x, y) in visited:
    return

  heat += int(inputs[x][y])
  visited.add((x, y)) 
  
  for i in range(4):
    if dir == D and i == U:
      continue
    
    if dir == U and i == D:
      continue

    if dir == R and i == L:
      continue

    if dir == L and i == R:
      continue

    nx, ny = x + DS[i][0], y + DS[i][1]
    if nx < 0 or nx >= m or ny < 0 or ny >= n or (nx, ny) in visited:
      continue
    if i == dir:
      if dir_steps - 1 == 0:
        continue
      dfs(nx, ny, i, dir_steps - 1, heat, visited)
    else:
      dfs(nx, ny, i, 3, heat, visited)
  visited.remove((x, y))
  heat -= int(inputs[x][y])

# visited = set()
# dfs(0, 1, R, 3, 0, visited)
visited = set()
dfs(1, 0, D, 3, 0, visited)
print(res)
    

  