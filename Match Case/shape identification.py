# shape identification
sides = "Enter the no of sides of your shape"
match sides:
    case circle if sides == 0:
        print("It is a circle or oval")
    case line if sides == 1:
        print("It is a line")
    case no if sides == 2:
        print("It has no shape")
    case tri if sides == 3:
        print("It is a triangle")
    case rect if sides == 4:
        print("It is a rectangle or square")
    case pent if sides == 5:
        print("It is a Pentagon")
    case hex if sides == 6:
        print("It is a hexagon")
    case hepta if sides == 7:
        print("It is a heptagon")
    case octa if sides == 8:
        print("It is a Octagon")
    case nona if sides == 9:
        print("It is Nonagon")
    case deca if sides == 10:
        print("It is Decagon")
    case _:
        print("It is polygon")
 