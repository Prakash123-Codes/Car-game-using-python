start = False
while True:
  com = input("enter the command: ").lower()
  if com == "start":
    if start:
      print("Car is already Started")
    else:
      print("Car is Started")
      start = True
  elif com == "stop":
    if not start:
      print("Car is already Stopped")
    else:
      print("Car is Stopped")
      start = False
  elif com =="help":
          print('''
          start - to start the car
          stop - to stop the car
          quit - to end the game''')
  elif com == 'quit':
          print("The game is ended")
          break
  else:
    print("Sorry, I don't understand that")
print("Thank you for playing")