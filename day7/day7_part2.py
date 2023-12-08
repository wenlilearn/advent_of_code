# inputs = ["32T3K 765", "T55J5 684", "KK677 28", "KTJJT 220", "QQQJA 483"]

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

custom_order = 'J23456789TQKA'
def determine_bucket(cards):
  best_bucket = 1
  for i in range(1, len(custom_order)):
    local = cards.replace('J', custom_order[i])
    counter = Counter()
    for card in local:
      counter[card] += 1 
    print(counter)
    best_bucket = max(best_bucket, get_best_bucket(sorted(counter.values())))
  return best_bucket
    
def get_best_bucket(local):
  if local == [1,1,1,1,1]:
    return 1
  elif local == [1,1,1,2]:
    return 2
  elif local == [1,2,2]:
    return 3
  elif local == [1,1,3]:
    return 4
  elif local == [2,3]:
    return 5
  elif local == [1,4]:
    return 6
  elif local == [5]:
    return 7

for input in inputs:
  cards, bid = input.split(" ")
  bid = int(bid)

  bucket_index = determine_bucket(cards)
  buckets[bucket_index].append((cards, bid))
  
def compare_key(item):
    cards, bid = item
    return [custom_order.index(c) for c in cards]

for key in buckets:
    buckets[key].sort(key=compare_key)

rank = 1
res = 0
for bucket in buckets:
  for card, bid in buckets[bucket]:
    res += bid * rank
    rank += 1
print(res)