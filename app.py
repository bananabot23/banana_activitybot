print("Title of program: Activity bot")
print()
while True:
  description = input("What do you like to do?")

  list_of_words = description.split()

  feelings_list = []
  activity_list = []
  counter = 0
  
  for each_word in list_of_words:
    
    if each_word == "outside":
      feelings_list.append("outside")
      activity_list.append("go out for a walk?")
      counter += 1
    if each_word == "sleep":
      feelings_list.append("sleep")
      activity_list.append("have a nap")
      counter += 1
    if each_word == "game":
      feelings_list.append("game")
      activity_list.append("have fun and don't forget to take a break in between")
      counter += 1

  if counter == 0:
    
      output = "Sorry I don't really understand. Please use different words?"

  elif counter == 1:
    
      output = "It seems that you are feeling quite " + feelings_list[0] + ". However, do remember that "+  activity_list[0] + "! Hope you will enjoy yourself :)"  

  else:

    feelings = ""    
    for i in range(len( activity_list)-1):
      feelings += activity_list[i] + ", "
    feelings += "and " +  activity_list[-1]
    
    encouragement = ""    
    for j in range(len( activity_list)-1):
      encouragement += activity_list[i] + ", "
    encouragement += "and " + activity_list[-1]

    output = "It seems that you are feeling quite " + feelings + ". hope you try and "+ activity + "! Hope you will enjoy yourself :)"

  print()
  print(output)
  print()
