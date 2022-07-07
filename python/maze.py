print("you are at the starting position")
print("the available moves are left, right, up and down")
current = input("enter your move : ")
current = current.lower()
if current == "left": ## starting position
    print("You can't go left from starting, you are dead")
elif current == "right": ## position 1
    print("you are on the right track, move ahead")
    print("from here you can move up,down and right")
    current = input("enter your move : ")
    current = current.lower()
    if current=="up": ## position 2
        print("you got a right move but there is wall ahead, so start again")
    elif current=="right": ## position 4
        print("you are on the right track, go ahead")
        current = input("choose left or right : ")
        current = current.lower()
        if current == "up" or current=="left" or current == "right":
            print("no up or down or right moves are available from here, start again")
        elif current=="down": ## position 5
            print("you are on the right track, move ahead")
            current = input("enter your move : ")
            current = current.lower()
            if current=="left" or current=="up" or current=="down":
                print("no up, down or left moves available here, start again")
            elif current=="right": ## position 6
                print("hurray, you reached at the end 😊😊 !!!")
            else:
                print("invlaid input, start again")
        else:
            print("invalid input, start again")
    elif current=="down": ## position 3
        print("you are on the right track, move ahead")
        current = input("enter your move : ")
        current = current.lower()
        if current=="up" or current=="left" or current=="down":
            print("no left or up or down moves are availabe here, start again")
        elif current=="right": ##position 5
            print("you are on the right track, move ahead")
            current = input("enter your move : ")
            current = current.lower()
            if current=="left" or current=="up" or current=="down":
                print("no up, down or left moves available here, start again")
            elif current=="right": ## position 6
                print("hurray, you reached at the end 😊😊 !!!")
            else:
                print("invlaid input, start again")
        else:
            print("invalid move, start again")
    elif current=="left":
         print("no left moves are available from here, start again")
    else:
        print("invalid move, start again")
elif current=="up" or current=="down":   
    print("no up or down moves are available from here, start again")
else:
    print("invalid input")

