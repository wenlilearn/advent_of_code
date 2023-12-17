# inputs = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"
# inputs = inputs.split(',')
import os
inputs = []
dir = os.path.dirname(__file__)

with open(os.path.join(dir, 'input.txt'), 'r') as file:
    inputs = [line.strip() for line in file]
inputs = inputs[0].split(',')
print(inputs)
def hash(input):
  total = 0
  for c in input:
    total += ord(c)
    total *= 17
    total %= 256
  return total

total = 0
for input in inputs:
  total += hash(input)
print(total)