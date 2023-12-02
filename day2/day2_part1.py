inputs = [
  "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
  "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
  "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
  "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
  "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"
]

# import requests
# response = requests.get("https://adventofcode.com/2023/day/2/input")
# print(response.text)

res = 0
for input in inputs:
  id = input.split(':')[0].split(' ')[1]
  id = int(id)

  input = input.split(':')[1].strip()
  input_doable = True
  for round in input.split(';'):
    amt_words = [amt_word.strip() for amt_word in round.split(', ')]

    red = 12
    green = 13
    blue = 14

    round_doable = True
    for amt_word in amt_words:
      amt_word = amt_word.split(' ')
      amount, color = int(amt_word[0]), amt_word[1]

      if color == 'red':
        red -= amount
        if red < 0:
          print("red overload!")
          round_doable = False
          break
      elif color == 'green':
        green -= amount
        if green < 0:
          print("green overload!")
          round_doable = False
          break
      elif color == 'blue':
        blue -= amount
        if blue < 0:
          print("blue overload!")
          round_doable = False
          break
    input_doable = input_doable and round_doable
    if not input_doable:
      break

  if input_doable:
    print(f"Game {id} is doable")
    res += id

print(res)

