inventory = [] #inventário do usuário
gameLoop = True #variável que controla o loop do jogo

while gameLoop:
  print("You are in a dark room. Moonlight shines through the window. \nThere is GOLD in a corner, along with a SHOVEL and a ROPE. \nThere is a DOOR to the EAST.")
  print("Command?")

  times = 0
  command = 0
  while command != "open door":
    command = input().lower()
    if command == "pick up shovel":
      inventory.append("Shovel")
      print("Taken")
    elif command == "pick up gold":
      inventory.append("Gold")
      print("Taken.")
    elif command == "pick up rope":
      inventory.append("Rope")
      print("Taken")
    elif command == "open door" or command == "open the door":
      break
    else:
      print("Pick up your stuff.")

  print("You open the door.\nDirection?")
  direction = input().lower()
  print("Reap your reward. \nPALE LUNA SMILES AT YOU.")

  #LOOP NA FLORESTA
  while times <= 3:
    direction = input("You are in a forest. There are paths to the WEST, NORTH and EAST. \nCommand?").lower()
    times+=1

  #FINAL
  print("PALE LUNA SMILES WIDE. \nThere are no paths.")
  print("PALE LUNA SMILES WIDE. \nThe ground is soft.")
  print("PALE LUNA SMILES WIDE. \nHere.")
  command = input("Command?").lower()

  #FINALIZAÇÃO: CAVAR, JOGAR O OURO E TAPAR O BURACO:
  while command != "dig" and command != "dig a hole" and command != "dig hole":
    print("You can't do that. Dig a hole first.")
    command = input("Command?").lower()
  
  print("You dig a hole.")
  command = input("Command?").lower()
  while command != "drop gold" and command != "drop the gold":
    print("Bury your treasure.")
    command = input("Command?")

  print("You drop the gold in the hole")
  command = input("Command?")
  while command != "tap hole" and command != "fill hole" and command != "fill the hole" and command != "tap the hole":
    print("Hide your treasure.")
    command = input("Command?")

  while times <= 10:
    print("Congratulations")
    print(f"{'-' * 4} 40.24248 {'-' * 4} \n{'-' * 4} -121.4434 {'-' * 4}")
    times += 1

  gameLoop = False