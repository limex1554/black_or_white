litery = {"a":1, "b":2, "c":3, "d":4, "e":5, "f":6, "g":7, "h":8}
cyfry = (1, 2, 3, 4, 5, 6, 7, 8)

pole = input("Please enter the name of your chess field: ")

if pole[0] in litery and int(pole[1]) in cyfry:
    pole0 = litery.get(pole[0])
    pole2 = pole0 +int(pole[1])
    print("Such chess field exists")
    if pole2 % 2 == 0:
        print("Your chess field is black")
    elif pole2 % 2 == 1:
        print("Your chess field is white")
else:
    print("There is no such chess field")