from collections import deque

inputs = [
  ".....",
  ".S-7.",
  ".|.|.",
  ".L-J.",
  "....."
]

inputs = [
  "..F7.",
  ".FJ|.",
  "SJ.L7",
  "|F--J",
  "LJ..."
]

import os
inputs = []
dir = os.path.dirname(__file__)

with open(os.path.join(dir, 'input.txt'), 'r') as file:
    inputs = [line.strip() for line in file]

dirs = {
  '|': [(1, 0), (-1, 0)],
  '-': [(0, 1), (0, -1)],
  'L': [(0, 1), (-1, 0)],
  'J': [(0, -1), (-1, 0)],
  '7': [(1, 0), (0, -1)],
  'F': [(1, 0), (0, 1)],
  'S': [(-1, 0), (0, 1)]
}

start = (-1, -1)
# Find S in the inputs
m, n = len(inputs), len(inputs[0])
for i in range(m):
  for j in range(n):
    if inputs[i][j] == 'S':
      start = (i, j)
      break
# Then BFS dirs till we can't traverse it anymore.
queue = deque()
queue.append(start)
visited = set()
steps = 0

while queue:
  size = len(queue)
  for _ in range(size):
    cur = queue.popleft()
    if cur in visited:
      continue
    visited.add(cur)

    for d in dirs[inputs[cur[0]][cur[1]]]:
      nxt = (cur[0] + d[0], cur[1] + d[1])
      if nxt[0] < 0 or nxt[0] >= m or nxt[1] < 0 or nxt[1] >= n or inputs[nxt[0]][nxt[1]] == '.' or nxt in visited:
        continue
      queue.append(nxt)
  steps += 1
print(steps - 1)