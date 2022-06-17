chess_field = input("Please enter the name of your chess field: ")
chess_field1 = chess_field[0]
chess_field2 = int(chess_field[1])
if chess_field1 == "a":
    chess_field1 = 1
elif chess_field1 == "b":
    chess_field1 = 2
elif chess_field1 == "c":
    chess_field1 = 3
elif chess_field1 == "d":
    chess_field1 = 4
elif chess_field1 == "e":
    chess_field1 = 5
elif chess_field1 == "f":
    chess_field1 = 6
elif chess_field1 == "g":
    chess_field1 = 7
elif chess_field1 == "h":
    chess_field1 = 8
chess_field = chess_field1 + chess_field2
if chess_field % 2 == 0:
  print ("Your chess field is black")
elif chess_field % 2 == 1:
  print ("Your chess field is white")
else:
  print ("There is no such chess field")
