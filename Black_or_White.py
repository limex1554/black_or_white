letters = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8}
numbers = (1, 2, 3, 4, 5, 6, 7, 8)

while True:
    while True:
        chessfield = input("Please enter the name of your chess field (e.g., 'a1'): ")
        if chessfield:
            break
        print("Input cannot be empty. Please try again.")

    chessfield = chessfield.lower()

    try:
        if chessfield[0] in letters and int(chessfield[1]) in numbers:
            chessfield0 = letters.get(chessfield[0])
            chessfield2 = chessfield0 + int(chessfield[1])

            if chessfield2 % 2 == 0:
                print("Your chess field is black.")
            else:
                print("Your chess field is white.")
        else:
            print("There is no such chess field.")
    except (IndexError, ValueError):
        print("Invalid input. Please enter a valid chess field (e.g., 'a1').")

    # Ask if the user wants to play again
    play_again = input("Do you want to play again? (yes or no): ").strip().lower()
    if play_again != "yes":
        print("Thank you for playing!")
        break
