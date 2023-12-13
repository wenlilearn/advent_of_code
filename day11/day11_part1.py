# inputs = [
# "...#......",
# ".......#..",
# "#.........",
# "..........",
# "......#...",
# ".#........",
# ".........#",
# "..........",
# ".......#..",
# "#...#....."]

import os
inputs = []
dir = os.path.dirname(__file__)

with open(os.path.join(dir, 'input.txt'), 'r') as file:
    inputs = [line.strip() for line in file]

m, n = len(inputs), len(inputs[0])
for i in range(m):
  inputs[i] = [c for c in inputs[i]]
i = 0
# 1. expand the rows if it doesn't have '#'
while i < len(inputs):
  expandible = True
  for j in range(n):
    if inputs[i][j] == '#':
      expandible = False
      break
  if expandible:
    new_row = ['.'] * n
    inputs.insert(i, new_row)
    i += 2
  else:
    i += 1
# 2. expand the cols if it doesn't have '#'
m, n = len(inputs), len(inputs[0])
i = 0
while i < len(inputs[0]):
  expandible = True
  for j in range(m):
    if inputs[j][i] == '#':
      expandible = False
      break
  if expandible:
    for j in range(m):
      inputs[j].insert(i, '.')
    i += 2
  else:
    i += 1
# 3. Find shortest path between pairs
m, n = len(inputs), len(inputs[0])
points = []
for i in range(m):
  for j in range(n):
    if inputs[i][j] == '#':
      points.append((i, j)) 
print(points)

# BFS: workable but slow
# from collections import deque
# steps_sum = 0
# for i in range(len(points) - 1):
#   for j in range(i + 1, len(points)):
#     start = points[i]
#     end = points[j]
#     queue = deque()
#     queue.append(start)
#     visited = set()
#     steps = 0
#     while queue:
#       size = len(queue)
#       for _ in range(size):
#         cur = queue.popleft()
#         if cur in visited:
#           continue
#         visited.add(cur)
#         if cur == end:
#           steps_sum += steps
#           print(f"i: {i} j: {j} steps_sum: {steps_sum} steps: {steps}")
#           break
#         for d in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
#           nxt = (cur[0] + d[0], cur[1] + d[1])
#           if nxt[0] < 0 or nxt[0] >= m or nxt[1] < 0 or nxt[1] >= n or nxt in visited:
#             continue
#           queue.append(nxt)
#       steps += 1
# print(steps_sum)    
# 10033566

steps_sum = 0
for i in range(len(points) - 1):
  for j in range(i + 1, len(points)):
    start = points[i]
    end = points[j]
    steps_sum += abs(start[0] - end[0]) + abs(start[1] - end[1])
print(steps_sum)