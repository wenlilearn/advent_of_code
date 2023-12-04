inputs = [
"467..114..",
"...*......",
"..35..633.",
"......#...",
"617*......",
".....+.58.",
"..592.....",
"......755.",
"...$.*....",
".664.598.."
]

import os
inputs = []
dir = os.path.dirname(__file__)

with open(os.path.join(dir, 'input.txt'), 'r') as file:
    inputs = [line.strip() for line in file]

DS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

m = len(inputs) 
res = 0
for i in range(m):
  n = len(inputs[i])
  for j in range(n):
    if inputs[i][j] == '.':
      continue

    if inputs[i][j] >= '0' and inputs[i][j] <= '9':
      continue

    for D in DS:
      ni, nj = i + D[0], j + D[1]
      if ni < 0 or ni >= m or nj < 0 or nj >= n:
        continue
    
      if inputs[ni][nj] < '0' or inputs[ni][nj] > '9':
        continue
    
      local = f"{inputs[ni][nj]}"
      left, right = nj - 1, nj + 1
      while left >= 0 and inputs[ni][left] >= '0' and inputs[ni][left] <= '9':
        local = f"{inputs[ni][left]}{local}"
        inputs[ni] = inputs[ni][:left] + '.' + inputs[ni][left + 1:]
        left -= 1

      while right < n and inputs[ni][right] >= '0' and inputs[ni][right] <= '9':
        local = f"{local}{inputs[ni][right]}"
        inputs[ni] = inputs[ni][:right] + '.' + inputs[ni][right + 1:]
        right += 1
      res += int(local)

print(res)