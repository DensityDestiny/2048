import random
import os


def i_choose_you():
  # Just printing the Board
  for i, b in enumerate(grid):
      print(b, end="      ")
      if (i + 1) % 4 == 0:
        print()
        print()
        print()
        print()


def prepare_for_trouble():
  # Ask for input and flip board accordingly. If invalid try again
  global grid
  inv = True
  while inv:
    list = []
    r = False
    t = False
    x = False
    i_choose_you()
    dir = input("What direction do you want?\n")
    os.system("clear")
    if dir == "d":
      grid.reverse()
      r = True
    if dir == "l":
      for i in range(4):
        list.append(grid[0 + i])
        list.append(grid[4 + i])
        list.append(grid[8 + i])
        list.append(grid[12 + i])
      grid = list.copy()
      t = True
    if dir == "r":
      for i in range(4):
        list.append(grid[3 - i])
        list.append(grid[7 - i])
        list.append(grid[11 - i])
        list.append(grid[15 - i])
      grid = list.copy()
      x = True
    for i, b in enumerate(grid):
      if dir == "u" or dir == "d" or dir == "l" or dir == "r":
        if isinstance(b, int):
          if i > 3:
            place = i
            for z in range(3):
              stop = False 
              if grid[place - 4] == grid[place] or grid[place - 4] == "-":
                if grid[place - 4] == grid[place]:
                  grid[place] *= 2
                  stop = True
                grid[place - 4] = grid[place]
                grid[place] = "-"
                place -= 4
                inv = False
              if stop:
                break
    if t:
      list = []
      for i in range(4):
        list.append(grid[0 + i])
        list.append(grid[4 + i])
        list.append(grid[8 + i])
        list.append(grid[12 + i])
      grid = list.copy()
    if x:
      list = []
      for i in range(4):
        list.append(grid[12 + i])
        list.append(grid[8 + i])
        list.append(grid[4 + i])
        list.append(grid[0 + i])
      grid = list.copy()
    if r:
      grid.reverse()


def and_make_it_double():
  # Finding Random position to place a 2 and sometimes a 4
  empty_space = []
  random_num = random.randint(1, 6)
  for i in range(len(grid)):
    if grid[i] == "-":
      empty_space.append(i)
  if len(empty_space) == 0:
    return False
  if random_num == 1:
    grid[empty_space[random.randint(0, len(empty_space) - 1)]] = 4
  else:
    grid[empty_space[random.randint(0, len(empty_space) - 1)]] = 2
  return True
# to protect the world from devastation
# to unite all peoples within our nation
# jessie
# james
# team rocket blasts off at the spped of light!!
# prepare to fight..???
# meowth thats right
  

round = 0
print("Score: N/A\n\n")
while True:
  grid = ["-", "-", "-", "-",
        "-", "-", "-", "-",
        "-", "-", "-", "-",
        "-", "-", "-", "-",]
  run = and_make_it_double()
  mind = []
  round += 1
  while run:
    prepare_for_trouble()
    run = and_make_it_double()
    score = 0
    for i in grid:
      if isinstance(i, int):
        score += i
    print(f"Score: {score}\n\n")
    for i in grid:
      if i == 2048:
        i_choose_you()
        print("EZ")
        gotta_catch_them_all = input("Keep going?... ").lower()
        if gotta_catch_them_all == "n" or gotta_catch_them_all == "no":
          run = False
  
  
  print(f"Final Score: {score}\n\n")
