times = [51,69,98,78]
dists = [377,1171,1224,1505]

times = [51699878]
dists = [377117112241505]

def count_wins(times, dists, i):
  time = times[i]
  dist = dists[i]
  wins = 0

  for hold in range(0, time + 1):
    if hold == 0:
      curDist = 0
    else:
      speed = hold
      curDist = speed * (time - hold)
    if curDist > dist:
      wins += 1 
  return wins

res = 1
for i in range(len(times)):
  wins = count_wins(times, dists, i)
  res *= wins
print(res)
