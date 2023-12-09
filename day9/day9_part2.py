

import os
inputs = []
dir = os.path.dirname(__file__)

with open(os.path.join(dir, 'input.txt'), 'r') as file:
    inputs = [line.strip() for line in file]
# inputs = [
#   "0 3 6 9 12 15",
#   "1 3 6 10 15 21",
#   "10 13 16 21 30 45"
# ]
inputs.reverse()

res = 0
for input in inputs:
  numbers = [int(i) for i in input.split(" ")]
  numbers.reverse()
  
  local_diffs = numbers
  input_diffs = [numbers]

  while True:
    tmp = []
    all_zeros = True
    for i in range(1, len(local_diffs)):
      tmp.append(local_diffs[i] - local_diffs[i - 1])
      if local_diffs[i] - local_diffs[i - 1] != 0: 
        all_zeros = False
    input_diffs.append(tmp[::])
    local_diffs = tmp
    if all_zeros:
      break
    
  input_diffs.reverse()
  print(input_diffs)
  # print(input_diffs)
  acc = 0
  local = 0
  for i in range(1, len(input_diffs)):
    acc = input_diffs[i][-1] + input_diffs[i - 1][-1]
    local = acc
    input_diffs[i].append(acc)
    # print(input_diffs)
  res += local
print(res)
