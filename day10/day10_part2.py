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
  'S': [(-1, 0), (0, 1), (0, -1), (1, 0)]
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

inputs = [
  "..........",
  ".S------7.",
  ".|F----7|.",
  ".||....||.",
  ".||....||.",
  ".|L-7F-J|.",
  ".|..||..|.",
  ".L--JL--J.",
  ".........."
]

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
print(start)
loop = []
def dfs(i, j, inputs, visited, path):
  global m, n, dirs, start, loop
  if i < 0 or i >= m or j < 0 or j >= n or inputs[i][j] == '.' or (i, j) in visited:
    if (i, j) == start:
      loop.append(path[::])
    return
  visited.add((i, j))
  cur_char = inputs[i][j]
  for d in dirs[cur_char]:
    path.append((i + d[0], j + d[1]))
    dfs(i + d[0], j + d[1], inputs, visited, path)
    path.pop()

visited = set()
path = []
dfs(start[0], start[1], inputs, visited, path)
print(loop)
for i in loop[0]:
  inputs[i[0]][i[1]] = 'X'
for input in inputs:
  print(''.join(input))
# def is_surrounded(i, j):
#   global m, n, inputs
  
#   i1, j1 = i, j
#   while i1 >= 0:
#     if i1 != i and (inputs[i1][j1] == 'X'):
#       break
#     i1 -= 1
  
#   i2, j2 = i, j
#   while i2 < m:
#     if i2 != i and (inputs[i2][j2] == 'X'):
#       break 
#     i2 += 1
  
#   i3, j3 = i, j
#   while j3 >= 0:
#     if j3 != j and (inputs[i3][j3] == 'X'):
#       break
#     j3 -= 1
  
#   i4, j4 = i, j
#   while j4 < n:
#     if j4 != j and (inputs[i4][j4] == 'X'):
#       break
#     j4 += 1
  
#   return (
#     (i1 >= 0 and inputs[i1][j1] == 'X') and
#     (i2 < m and inputs[i2][j2] == 'X') and
#     (j3 >= 0 and inputs[i3][j3] == 'X') and
#     (j4 < n and inputs[i4][j4] == 'X')
#   )
# tiles = 0
# for i in range(m):
#   for j in range(n):
#     if inputs[i][j] == '#' or inputs[i][j] == 'X':
#       continue
#     if is_surrounded(i, j):
#       tiles += 1

# print(tiles)


