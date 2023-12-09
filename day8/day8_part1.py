dirs = "LRRLLRLLRRRLRRLRLRRRLRLLRLRRLRRRLRRRLRRLRRRLRLRRRLRLRRLRLRRRLRRLLRRLLLRRLRLRRRLRLRRRLRRLRRRLRLLRRLRRLRLRRRLRRRLRRLRRLLRLLRRRLRLRRLRRRLRRLRRRLRRRLLLLRRLRLRRRLRRRLLRRLLRRLRRRLRRRLRLRLLRRLRLRLRLRLRRLRLRLRRRLRRLRRLRRLRRRLRLRRRLRLRRLRLLLLRRRLLRRRLRLLRRRLRLLRRRLLRRLRLRLRLRLLLLRRLRRRLRLLRRLRRRLRRRLRLRRLRRLRLLRRRR"

import os
inputs = []
dir = os.path.dirname(__file__)

with open(os.path.join(dir, 'input.txt'), 'r') as file:
    steps = [line.strip() for line in file]
ds = []
for dir in dirs:
  ds.append(0) if dir == 'L' else ds.append(1)

def steps2map(steps):
  steps_map = {}
  for step in steps:
    source_dests = step.split(" = ")
    steps_map[source_dests[0]] = [i.replace('(','').replace(')', '').strip() for i in source_dests[1].split(",")]
  return steps_map

steps_map = steps2map(steps)
# print(steps_map)

steps_cnt = 0
# DFS will stackoverflow
# def dfs(steps_map, cur_step, ds, cur_dir_index):
#   global steps_cnt

#   steps_cnt += 1
#   if steps_map[cur_step][ds[cur_dir_index]] == 'ZZZ':
#     return

#   return dfs(steps_map, steps_map[cur_step][ds[cur_dir_index]] , ds, (cur_dir_index + 1) % len(ds))

# cur_dir_index = ds[0]
# res = dfs(steps_map, 'AAA', ds, cur_dir_index)
# print(res)
# print(steps_cnt)

steps_cnt = 0
cur_step = 'AAA'
cur_dir_index = ds[0]
while True:
  steps_cnt += 1
  if steps_map[cur_step][ds[cur_dir_index]] == 'ZZZ':
    break
  cur_step = steps_map[cur_step][ds[cur_dir_index]]
  cur_dir_index = (cur_dir_index + 1) % len(ds)

print(steps_cnt)
  