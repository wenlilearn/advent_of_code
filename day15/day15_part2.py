# inputs = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"
# inputs = inputs.split(',')

import os
inputs = []
dir = os.path.dirname(__file__)
with open(os.path.join(dir, 'input.txt'), 'r') as file:
    inputs = [line.strip() for line in file]
inputs = inputs[0].split(',')

def hash(input):
  total = 0
  for c in input:
    total += ord(c)
    total *= 17
    total %= 256
  return total

boxes = [list() for i in range(256)]
total = 0
for input in inputs:
  i = 0
  for i, c in enumerate(input):
    if c == '=' or c == '-':
      break
  label = input[:i]
  op = input[i]
  length = input[i + 1:]
  label_hash = hash(label)
  # print(f"label: {label}, op: {op}, length: {length}, label_hash: {label_hash}")

  if op == '=':
    found = False
    for elem in boxes[label_hash]:
      if elem[0] == label:
        elem[1] = length
        found = True
        break
    if not found:
      boxes[label_hash].append([label, length])
  else:
    to_delete = -1
    for i in range(len(boxes[label_hash])):
      if boxes[label_hash][i][0] == label:
        to_delete = i
        break
    if to_delete!= -1:
      boxes[label_hash].pop(to_delete)
# print(boxes)  

for i in range(256):
  for j, elem in enumerate(boxes[i]):
    total += int(elem[1]) * (j + 1) * (i + 1)
  
print(total)