inputs = ["32T3K 765", "T55J5 684", "KK677 28", "KTJJT 220", "QQQJA 483"]

import os
inputs = []
dir = os.path.dirname(__file__)

with open(os.path.join(dir, 'input.txt'), 'r') as file:
    inputs = [line.strip() for line in file]

from collections import Counter

buckets = {
  1: [],
  2: [],
  3: [],
  4: [],
  5: [],
  6: [],
  7: []
}
for input in inputs:
  cards, bid = input.split(" ")
  bid = int(bid)

  counter = Counter()
  for card in cards:
    counter[card] += 1 
  combos = sorted(counter.values())

  if combos == [1,1,1,1,1]:
    buckets[1].append([cards, bid]) 
  elif combos == [1,1,1,2]:
    buckets[2].append([cards, bid])
  elif combos == [1,2,2]:
    buckets[3].append([cards, bid])
  elif combos == [1,1,3]:
    buckets[4].append([cards, bid])
  elif combos == [2,3]:
    buckets[5].append([cards, bid])
  elif combos == [1,4]:
    buckets[6].append([cards, bid])
  elif combos == [5]:
    buckets[7].append([cards, bid])
  
def compare_key(item):
    cards, bid = item
    return [custom_order.index(c) for c in cards]

custom_order = '23456789TJQKA'

for key in buckets:
    buckets[key].sort(key=compare_key)

print(buckets)
print(buckets.values())
rank = 1
res = 0
for bucket in buckets:
  for card, bid in buckets[bucket]:
    res += bid * rank
    rank += 1
print(res)