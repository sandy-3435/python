import random
list=[0,1,2,3,4,5,6,7,8]
print("LET'S START TIC TAC TOE GAME...........!")

hand=int(input("PLEASE SELECT YOUR HAND 1.'X' OR 2.'O':"))
#hand of a player selection
hands=['x','o']

if hand==1:
        computer_hands=str(hands[hand-2])
        human_hand=str(hands[hand-1])

if hand==2:
        computer_hand=hands[hand-2]
        human_hand=hands[hand-1]
        #printing the board befoe strting the game
def pre(*arg):
    for i in arg:
        print(i)
row1=[0,1,2]
row2=[3,4,5]
row3=[6,7,8]
print("TAKE  A LOOK AT THE TIC TAC TOE BOARD")
pre(row1,row2,row3)

#vadlidating positions
def user_position():

        print("user turn........")
        pos = int(input('PLEASE SELECT POSITION:'))
        list.remove(pos)
        try:
            if pos >=0 and pos<=2:
                row1[pos] =  human_hand

                pre(row1, row2, row3)
            if pos>=3 and  pos<=5:
                row2[pos-3]= human_hand
                pre(row1,row2,row3)
            if pos>=6 and pos<=8:
                row3[pos-6]= human_hand
                pre(row1,row2,row3)
            if pos>=9:
                print("PLEASE ENTER THE VALID INPUT:")
        except IndexError as index:
            print(index)
#computer positions
def computer_position():
    print("COMPUTER turn.......")
    pos2=random.choice(list)
    try:
        if pos2 >= 0 and pos2 <= 2:
            row1[pos2] =computer_hands
            pre(row1, row2, row3)
        if pos2 >= 3 and pos2 <= 5:
            row2[pos2 - 3] =computer_hands
            pre(row1, row2, row3)
        if pos2 >= 6 and pos2 <= 8:
            row3[pos2 - 6] =computer_hands
            pre(row1, row2, row3)
        if pos2 >= 9:
            print("PLEASE ENTER THE VALID INPUT:")
    except IndexError as index:
        print(index)
#validating the result
def result(row1,row2,row3):

    if row1[0]==row1[1]==row1[2]== human_hand:
        print('YOU WON')
        return False
    if row2[0] == row2[1] == row3[2] ==  human_hand:
        print('YOU WON')
        return False
    if row3[0] == row3[1] == row3[2] ==  human_hand:
        print('YOU WON')
        return False
    if row1[0] == row2[0] == row3[0] ==  human_hand:
        print('YOU WON')
        return False
    if row1[1] == row2[1] == row3[1] ==  human_hand:
        print('YOU WON')
        return False
    if row1[2] == row2[2] == row3[2] ==  human_hand:
        print('YOU WON')
        return False
    if row1[0] == row2[1] == row3[2] ==  human_hand:
        print('YOU WON')
        return False
    if row1[2] == row2[1] == row3[0] ==  human_hand:
        print('YOU WON')
    #computer result
    if row1[0] == row1[1] == row1[2] == computer_hands:
            print('YOU LOST')
            return False
    if row2[0] == row2[1] == row3[2] == computer_hands:
            print('YOU LOST')
            return False
    if row3[0] == row3[1] == row3[2] == computer_hands:
            print('YOU LOST')
            return False
    if row1[0] == row2[0] == row3[0] == computer_hands:
            print('YOU LOST')
            return False
    if row1[1] == row2[1] == row3[1] == computer_hands:
            print('YOU LOST')
            return False
    if row1[2] == row2[2] == row3[2] ==computer_hands:
            print('YOU LOST')
            return False
    if row1[0] == row2[1] == row3[2] == computer_hands:
            print('YOU LOST')
            return False
    if row1[2] == row2[1] == row3[0] ==computer_hands:
            print('YOU LOST')
            return False


#actual program starts
while(True):

    user_position()
    computer_position()
    if result(row1,row2,row3)==False:
        break
    
