inputs = ["Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
"Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
"Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
"Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
"Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
"Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"]

import os

with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as file:
  inputs = [line.strip() for line in file]

res = 0
for input in inputs:
  nums = [i.strip() for i in input.split(':')]
  winning_nums, my_nums = nums[1].split(' | ')
  winning_nums, my_nums = winning_nums.replace("  ", " "), my_nums.replace("  ", " ")
  winning_nums, my_nums = winning_nums.strip(), my_nums.strip()
  winning_nums = set([int(x.strip()) for x in winning_nums.split(' ')])
  # print(my_nums)
  my_nums = [int(x.strip()) for x in my_nums.split(' ')]

  val = 0

  for num in my_nums:
    if num in winning_nums:
      if val == 0:
        val = 1
      else:
        val *= 2
  res += val
print(res)




