# Incorrect!
import os
inputs = []
dir = os.path.dirname(__file__)

with open(os.path.join(dir, 'input.txt'), 'r') as file:
    inputs = [line.strip() for line in file]

patterns = []
pattern = []

for input in inputs:
  if input == "":
      patterns.append(pattern)
      pattern = []
      continue
  pattern.append(list(input))

total = 0
rows = 0
cols = 0

for pattern in patterns:
  rows_found = False
  cols_found = False
  m, n = len(pattern), len(pattern[0])
  # First reflect on rows
  for i in range(1, m):
    if pattern[i] == pattern[i - 1]:
      x, y = i - 1, i
      while x >= 0 and y < m:
        if pattern[x] != pattern[y]:
          break
        x -= 1
        y += 1
      if x == -1 or y == m:
        rows += i
        rows_found = True 
  # if rows_found:
  #   break
     
  # Transpose the matrix
  tranposed = list(map(list, zip(*pattern)))
  tranposed = [row[::-1] for row in tranposed]

  # Then reflect on cols
  m, n = len(tranposed), len(tranposed[0])
  for i in range(1, m):
    if tranposed[i] == tranposed[i - 1]:
      x, y = i - 1, i
      while x >= 0 and y < m:
        if tranposed[x] != tranposed[y]:
          break
        x -= 1
        y += 1
      if x == -1 or y == m:
         cols += i

total = rows * 100 + cols
print(total)       
     
