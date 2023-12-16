inputs = [
  "???.### 1,1,3",
  ".??..??...?##. 1,1,3",
  "?#?#?#?#?#?#?#? 1,3,1,6",
  "????.#...#... 4,1,1",
  "????.######..#####. 1,6,5",
  "?###???????? 3,2,1"
]

import os
inputs = []
dir = os.path.dirname(__file__)

with open(os.path.join(dir, 'input.txt'), 'r') as file:
    inputs = [line.strip() for line in file]

inputs = [input.split(' ') for input in inputs]
def isValid(strs, poss):
  local = []
  count = 0
  for str in strs:
    if str == '#':
      count += 1
    else:
      if count > 0:
        local.append(count)
      count = 0
  if count > 0:
    local.append(count)
  
  return local == poss

def dfs(strs, poss, total, index):
  if total == 0 and isValid(strs, poss):
    return 1
  if total < 0:
    return 0

  res = 0
  for i in range(index, len(strs)):
    if strs[i] == '?':
      strs[i] = '#'
      res = res + dfs(strs, poss, total - 1, i)
      strs[i] = '?'
  return res


res = 0
for i, input in enumerate(inputs):
  print(f"Processing {i}/{len(inputs)}")
  strs, poss = list(input[0]), list(map(lambda x: int(x), input[1].split(',')))
  total = 0
  for pos in poss:
    total += int(pos)
  for str in strs:
    if str == '#':
      total -= 1

  res += dfs(strs, poss, total, 0)
print(res)
