from collections import deque

# Part 2 is wrong!!!
# inputs = [
#   ".....",
#   ".S-7.",
#   ".|.|.",
#   ".L-J.",
#   "....."
# ]

# inputs = [
#   "..F7.",
#   ".FJ|.",
#   "SJ.L7",
#   "|F--J",
#   "LJ..."
# ]
# ..##.
# .###.
# ##.##
# #####
# ##...

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

inputs = [
  ".F----7F7F7F7F-7....",
  ".|F--7||||||||FJ....",
  ".||.FJ||||||||L7....",
  "FJL7L7LJLJ||LJ.L-7..",
  "L--J.L7...LJS7F-7L7.",
  "....F-J..F7FJ|L7L7L7",
  "....L7.F7||L7|.L7L7|",
  ".....|FJLJ|FJ|F7|.LJ",
  "....FJL-7.||.||||...",
  "....L---J.LJ.LJLJ..."
]

# inputs = [
#   "..........",
#   ".S------7.",
#   ".|F----7|.",
#   ".||....||.",
#   ".||....||.",
#   ".|L-7F-J|.",
#   ".|..||..|.",
#   ".L--JL--J.",
#   ".........."
# ]

# Find S in the inputs
m, n = len(inputs), len(inputs[0])
for i in range(m):
  inputs[i] = list(inputs[i])

start = (-1, -1)
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
    cur_char = inputs[cur[0]][cur[1]]
    inputs[cur[0]][cur[1]] = '#'
    if cur in visited:
      continue
    visited.add(cur)

    for d in dirs[cur_char]:
      nxt = (cur[0] + d[0], cur[1] + d[1])
      if nxt[0] < 0 or nxt[0] >= m or nxt[1] < 0 or nxt[1] >= n or inputs[nxt[0]][nxt[1]] == '.' or inputs[nxt[0]][nxt[1]] == '#' or nxt in visited:
        continue
      queue.append(nxt)

# for input in inputs:
#   print("".join(input))
  
def is_outer_valid(i, j):
  global m, n, inputs
  
  i1, j1 = i, j
  while i1 >= 0:
    if i1 != i and (inputs[i1][j1] == '#' or inputs[i1][j1] == 'X'):
      break
    i1 -= 1
  
  i2, j2 = i, j
  while i2 < m:
    if i2 != i and (inputs[i2][j2] == '#' or inputs[i2][j2] == 'X'):
      break 
    i2 += 1
  
  i3, j3 = i, j
  while j3 >= 0:
    if j3 != j and (inputs[i3][j3] == '#' or inputs[i3][j3] == 'X'):
      break
    j3 -= 1
  
  i4, j4 = i, j
  while j4 < n:
    if j4 != j and (inputs[i4][j4] == '#' or inputs[i4][j4] == 'X'):
      break
    j4 += 1
  
  return i1 == -1 or i2 == m or j3 == -1 or j4 == n

# print(is_outer_valid(2, 2))
for i in range(m):
  for j in range(n):
    if inputs[i][j] == '#':
      if is_outer_valid(i, j):
        inputs[i][j] = 'X'
for input in inputs:
  print("".join(input)) 

print('-----------------------')

def is_inner_valid(i, j):
  global m, n, inputs
  
  i1, j1 = i, j
  while i1 >= 0:
    if i1 != i and (inputs[i1][j1] == '#'):
      break
    i1 -= 1
  
  i2, j2 = i, j
  while i2 < m:
    if i2 != i and (inputs[i2][j2] == '#'):
      break 
    i2 += 1
  
  i3, j3 = i, j
  while j3 >= 0:
    if j3 != j and (inputs[i3][j3] == '#'):
      break
    j3 -= 1
  
  i4, j4 = i, j
  while j4 < n:
    if j4 != j and (inputs[i4][j4] == '#'):
      break
    j4 += 1
  
  return i1 == -1 or i2 == m or j3 == -1 or j4 == n

for i in range(m):
  for j in range(n):
    if inputs[i][j] == '#' or inputs[i][j] == 'X':
      continue
    visited = set()
    if not is_inner_valid(i, j):
      inputs[i][j] = '#' 
for input in inputs:
  print("".join(input)) 

def is_surrounded(i, j):
  global m, n, inputs
  
  i1, j1 = i, j
  while i1 >= 0:
    if i1 != i and (inputs[i1][j1] == 'X'):
      break
    i1 -= 1
  
  i2, j2 = i, j
  while i2 < m:
    if i2 != i and (inputs[i2][j2] == 'X'):
      break 
    i2 += 1
  
  i3, j3 = i, j
  while j3 >= 0:
    if j3 != j and (inputs[i3][j3] == 'X'):
      break
    j3 -= 1
  
  i4, j4 = i, j
  while j4 < n:
    if j4 != j and (inputs[i4][j4] == 'X'):
      break
    j4 += 1
  
  return (
    (i1 >= 0 and inputs[i1][j1] == 'X') and
    (i2 < m and inputs[i2][j2] == 'X') and
    (j3 >= 0 and inputs[i3][j3] == 'X') and
    (j4 < n and inputs[i4][j4] == 'X')
  )
tiles = 0
for i in range(m):
  for j in range(n):
    if inputs[i][j] == '#' or inputs[i][j] == 'X':
      continue
    if is_surrounded(i, j):
      tiles += 1

print(tiles)


