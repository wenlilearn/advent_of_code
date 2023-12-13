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

expand_factor = 1000000

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
    new_row = [expand_factor] * len(inputs[0])
    inputs[i] = new_row
  i += 1

m, n = len(inputs), len(inputs[0])
# for i in range(m):
#   print("".join(f"{inputs[i]}"))
# 2. transpose the matrix
inputs = list(map(list, zip(*inputs)))
# for input in inputs:
#   print("".join([f"{i}" for i in input]))
# 3. expand the rows again
i, j = 0, 0
while i < len(inputs):
  expandible = True
  for j in range(len(inputs[0])):
    if inputs[i][j] == '#':
      expandible = False
      break
  if expandible:
    # print(f"expanding row {i}")
    new_row = [expand_factor] * len(inputs[0])
    inputs[i] = new_row
  i += 1
# for input in inputs:
#   print("".join([f"{i}" for i in input]))
# print("finding shortest distance")
inputs = list(map(list, zip(*inputs)))
# for input in inputs:
#   print("".join([f"{i}" for i in input]))
# 4. Find shortest path between pairs
m, n = len(inputs), len(inputs[0])
i, j = 0, 0
points = []
for i in range(m):
  for j in range(n):
    if inputs[i][j] == '#':
      points.append((i, j)) 
    if inputs[i][j] == '.' or inputs[i][j] == '#':
      inputs[i][j] = 1
print(points)

steps_sum = 0
import heapq
for i in range(len(points) - 1):
  for j in range(i + 1, len(points)):
    print(f"processing {i * (len(points) - 1) + j} / {(len(points) - 1) ** 2}")
    start = (0, points[i])
    queue = []
    heapq.heappush(queue, start)
    visited = set()
    while queue:
      cur_dist, cur_node = heapq.heappop(queue)
      if cur_node in visited:
        continue
      visited.add(cur_node)
      if cur_node == points[j]:
        steps_sum += cur_dist
        break
      for d in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nxt = (cur_node[0] + d[0], cur_node[1] + d[1])
        if nxt[0] < 0 or nxt[0] >= m or nxt[1] < 0 or nxt[1] >= n or nxt in visited:
          continue
        heapq.heappush(queue, (cur_dist + int(inputs[nxt[0]][nxt[1]]), nxt))
print(steps_sum)      