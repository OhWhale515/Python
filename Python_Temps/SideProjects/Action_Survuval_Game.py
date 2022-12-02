print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

direction = input('Which what do u wanna go bro?, Left or Right:\n')
l = ('Left' or 'left')
r = ('Right' or 'right')

if direction == r:
  print('Damn It!!!\nYou fell! Game Over!')
  
elif direction == l:
  print('That was a close 1 man, sheeesh!!')

  patience = input('Hey man its gonna be awhile before rescue arrives,\nI think we should wait.\nThe current is pretty strong down there...Wait or Swim:\n')
  w = ('Wait' or 'wait')
  s = ('Swim' or 'swim')

  if patience == s:
    print('Awwww daaaaamn!! The Trout! Game Over!\nYou fell down the waterfall.')

  elif patience == w:
    print('There goes help!')

    door = input('We need to find which door leads to the chopper! Red, Blue or Yellow?:\n')
    r = ('Red' or 'red')
    b = ('Blue' or 'blue')
    y = ('Yellow' or 'yellow')

    if door == r:
      print('Oh NO!!!, The Fire!! GAME OVER!\nYou were burned alive.')
  
    elif door == b:
      print('Ahhhhhhh What is that???!!! GAME OVER!\nYou were eatin by Monsters.')

    elif door == y: 
      print('Man, We made it.\nCall your family and let them know you will be home safe.\nCongrats You WIN!!!')

else:
  print('Game Over')
