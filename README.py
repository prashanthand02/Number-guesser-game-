# Number-guesser-game-
import random
print("Welcome there")
top_range = input("Enter the range u want to play in: ")
print("You get 5 attempts")
if top_range.lstrip("-").isnumeric():
  top_range = int(top_range)
  if top_range <= 0:
    print("Range should be higher than zero")
  else:
    x = top_range
else:
  print("Enter a number")
