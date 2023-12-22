import os
inputs = []
dir = os.path.dirname(__file__)
with open(os.path.join(dir, 'input.txt'), 'r') as file:
    inputs = [line.strip() for line in file]

def print_inputs(inputs):
  for input in inputs:
    print(input)

tmp = [[], []]
idx = 0
for input in inputs:
  if input == '':
     idx = 1
     continue
  tmp[idx].append(input) 
workflows = tmp[0]
ratings = tmp[1]

# process workflows
workflow_dict = {}
for workflow in workflows:
  rule_start = workflow.index('{')
  rule_end = workflow.index('}')

  label = workflow[:rule_start]
  rules = workflow[rule_start+1:rule_end].split(',')
  workflow_dict[label] = rules

# process ratings
import json
for i in range(len(ratings)):
  ratings[i] = ratings[i].replace('=', ':')
  for c in ['x', 'm', 'a', 's']:
    ratings[i] = ratings[i].replace(c, f"\"{c}\"")
  ratings[i] = json.loads(ratings[i])

def get_total_rating(rating):
  return sum(rating.values())

# import pprint
# pprint.pprint(workflow_dict)
res = 0

for rating in ratings:
    # print(rating)
    nxt = 'in'
    while True:
      # print(nxt)
      if nxt == 'A':
        res += get_total_rating(rating)
        break
      elif nxt == 'R':
        break
      rules = workflow_dict[nxt]
      for rule in rules:
        splitted = rule.split(':')
        if len(splitted) == 1:
          nxt = splitted[0] 
        else:
          if eval(splitted[0], {}, rating):
            nxt = splitted[1]
            break
print(res)

