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

# print(patterns)

m = len(patterns)
for pattern in patterns:
  if len(pattern) % 2 == 0:
    print('even!')
  if len(pattern[0]) % 2 == 0:
    print('even!')

total = 0
rows = 0
cols = 0

for pattern in patterns:
  cur = pattern[1:]
  m, n = len(cur), len(cur[0])
  # First reflect on rows
  for i in range(1, m):
    if cur[i] == cur[i - 1]:
      s, e = i - 1, i
      while s >= 0 and e < m and cur[s] == cur[e]:
        s -= 1
        e += 1
      if s == -1 and e == m:
        rows += i + 1
        break
  
  cur = pattern[:-1]
  m, n = len(cur), len(cur[0])
  for i in range(1, m):
    if cur[i] == cur[i - 1]:
      s, e = i - 1, i
      while s >= 0 and e < m and cur[s] == cur[e]:
        s -= 1
        e += 1
      if s == -1 and e == m:
        rows += i + 1
        break
     
  # Transpose the matrix
  tranposed = list(map(list, zip(*pattern)))
  tranposed = [row[::-1] for row in tranposed]

  cur = tranposed[1:]
  # Then reflect on cols
  m, n = len(cur), len(cur[0])
  for i in range(1, m):
    if cur[i] == cur[i - 1]:
      s, e = i - 1, i
      while s >= 0 and e < m and cur[s] == cur[e]:
        s -= 1
        e += 1
      if s == -1 and e == m:
        cols += i + 1

  cur = tranposed[:-1]
  # Then reflect on cols
  m, n = len(cur), len(cur[0])
  for i in range(1, m):
    if cur[i] == cur[i - 1]:
      s, e = i - 1, i
      while s >= 0 and e < m and cur[s] == cur[e]:
        s -= 1
        e += 1
      if s == -1 and e == m:
        cols += i + 1
        break

total = rows * 100 + cols
print(total)       
     
