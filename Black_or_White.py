letters = {"a":1, "b":2, "c":3, "d":4, "e":5, "f":6, "g":7, "h":8}
numbers = (1, 2, 3, 4, 5, 6, 7, 8)

while True:
    chessfield = input("Please enter the name of your chess field: ")
    if chessfield:
        break
    print("Input cannot be empty. Please try again.")

chessfield = chessfield.lower()

try:
    if chessfield[0] in letters and int(chessfield[1]) in numbers:
        chessfield0 = letters.get(chessfield[0])
        chessfield2 = chessfield0 +int(chessfield[1])
        print("Such chess field exists")
        if chessfield2 % 2 == 0:
            print("Your chess field is black")
        elif chessfield2 % 2 == 1:
            print("Your chess field is white")
    else:
        print("There is no such chess field")
except IndexError:
    print("Index out of range")
