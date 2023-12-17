import os

inputs = []
dir = os.path.dirname(__file__)

with open(os.path.join(dir, 'input.txt'), 'r') as file:
    inputs = [line.strip() for line in file]

inputs = [list(input) for input in inputs]
orig_inputs = ''.join(map(lambda x: ''.join(x), inputs))
# print(orig_inputs)
m, n = len(inputs), len(inputs[0])
visited = {}

for k in range(1, 124):
  for _ in range(4):
    for i in range(n):
      for j in range(m):
          if inputs[j][i] == 'O':
            inputs[j][i] = '.'
            x = j
            while x >= 0 and inputs[x][i] == '.':
              x -= 1
            inputs[x + 1][i] = 'O'
    inputs = list(map(list, zip(*inputs)))
    inputs = [row[::-1] for row in inputs]

i, j = 0, 0
for k in range(1, 20):
  for _ in range(4):
    for i in range(n):
      for j in range(m):
          if inputs[j][i] == 'O':
            inputs[j][i] = '.'
            x = j
            while x >= 0 and inputs[x][i] == '.':
              x -= 1
            inputs[x + 1][i] = 'O'
    inputs = list(map(list, zip(*inputs)))
    inputs = [row[::-1] for row in inputs]

# for k in range(1, 999999):
#   for _ in range(4):
#     for i in range(n):
#       for j in range(m):
#           if inputs[j][i] == 'O':
#             inputs[j][i] = '.'
#             x = j
#             while x >= 0 and inputs[x][i] == '.':
#               x -= 1
#             inputs[x + 1][i] = 'O'
#     inputs = list(map(list, zip(*inputs)))
#     inputs = [row[::-1] for row in inputs]
#   print(f"current iteration: {k}")
#   cur = ''.join(map(lambda x: ''.join(x), inputs))
#   # print('\n'.join(list(map(lambda x: ''.join(x), inputs))))
#   if cur not in visited:
#     visited[cur] = 0
#   visited[cur] += 1
#   if visited[cur] == 3:
#     break
# print(visited.values())
# ones = 0
# twos = 0
# for key in visited:
#   if visited[key] == 1:
#     ones += 1
#   if visited[key] == 2 or visited[key] == 3:
#     twos += 1
# print(ones, twos)

# def find_dup(visited):
#   for i in range(1, len(visited)):
#     for j in range(i + 1, len(visited)):
#       if visited[j] == visited[i]:
#         return i + 1, j + 1
#   return -1, -1

# i, j = 0, 0
# found = False
# i, j = find_dup(visited)
# print(i, j)
total_rows = len(inputs)
totals = [0] * total_rows

for i, input in enumerate(inputs):
  totals[i] = input.count('O')
# print(totals)
  
res = 0
totals.reverse()
for i, total in enumerate(totals):
  res += total * (i + 1)
print(res)

# 105008 Correct Answer