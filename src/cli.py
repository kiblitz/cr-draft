
import draft
import os

def run():
  picks = [[],[]]
  pairs = draft.pairs()

  for player in range(1, 3):
    os.system("clear")
    pre = "[Player %d]: " % player
    input(pre + "(Enter when ready) ")

    pair = 0
    while pair < 4:
      pick = input(pre + "%s (1), %s (2) " % 
        (draft.get_name(pairs[player - 1][pair][0]), 
         draft.get_name(pairs[player - 1][pair][1])))

      if pick in ("1", "2"):
        npick = int(pick)
        picks[player - 1].append(pairs[player - 1][pair][npick - 1]) 
        picks[2 - player].append(pairs[player - 1][pair][2 - npick]) 
        pair += 1
  
  for player in range(1, 3):
    os.system("clear")
    pre = "[Player %d]: " % player
    input(pre + "(Enter to show) ")
    
    input(list(map(draft.get_name, picks[player - 1]))) 
  
  os.system("clear")

run()
