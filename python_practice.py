old_string = None
while True:
  mean_words =["mean","unkind"]
  
  user_input = input("Type something: ")
  if user_input == old_string:
    break
  print(user_input)
  print(user_input.count('e'))
  print(''.join(reversed(user_input)))
  if user_input == "DOUBLE":
    print(user_input)
  print(user_input.replace('s','*'))
  print(user_input.upper())
  if len(user_input) > 50:
    print("TOO LONG")
  for word in mean_words:
    if user_input == word:
      print("Be Nice")
  old_string = user_input
