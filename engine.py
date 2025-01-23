"""
Stores all info and determines valid moves.
"""


#board as a class for organization sakes
class Board:
    """    #collects value of n
    while True:
        try:
            #global n
            #n = int(input("Enter N val: "))

            n = main.n
            #if (n > 8) or (n < 4):
            #raise ValueError("Please enter val between 4 and 8")
            break
        except ValueError:
            print("Enter valid input")"""

    def __init__(self, nVal):
        global n
        n = nVal

        #creates board list
        global board
        global qLocation
        board = []
        qLocation = {}
        for rows in range(n):
            board.append([])
            for columns in range(n):
                board[rows].append("  ")

        #prints final board
        self.PrintBoard()
        #self.Move()

    def PrintBoard(self):
        for i in range(n):
            print(board[i])
        print()
        return board

    #move cursor across board and allow player to decide where to place
    #if statements not only collect the players request, but also ensure the index does not move out of bounds
    def Move(self):
        cursor = {"row" : 0, "column" : 0} #cursor holds the current cursor location as user moves through the board
        while True: #movement loop
            #makes sure the current space is empty before placing cursor
            if board[cursor["row"]] [cursor["column"]] == '  ':
                board[cursor["row"]] [cursor["column"]] = '*♛*'
            else:
                board[cursor["row"]] [cursor["column"]] += "!"
            self.PrintBoard()


            if (board[cursor["row"]] [cursor["column"]] == '*♛*') and ([[cursor["row"]], [cursor["column"]]] not in qLocation.values()):
                board[cursor["row"]] [cursor["column"]] = "  "
            else:
                board[cursor["row"]] [cursor["column"]] = board[cursor["row"]] [cursor["column"]][:-1]


            arrow = str(input("WASD then ENTER to move the cursor, ENTER to place a queen")).lower() #stores movement request
            if (arrow == "w") and (cursor["row"] > 0):
                cursor["row"] -= 1
            elif (arrow == "a") and (cursor["column"] > 0):
                cursor["column"] -= 1
            elif (arrow == "s") and (cursor["row"] < n-1):
                    cursor["row"] += 1
            elif (arrow == "d") and (cursor["column"] < n-1):
                    cursor["column"] += 1
            elif arrow == "":
                if (board[cursor["row"]][cursor["column"]] == "  ") and self.ValidateMove([cursor["row"],cursor["column"]]):
                    board[cursor["row"]][cursor["column"]] = f'Q{len(qLocation) + 1}'
                else:
                    print('Invalid Move!')
                    continue
                qLocation[f'Q{len(qLocation) + 1}'] = [cursor["row"],cursor["column"]]
                break
            else:
                print("Enter W, A, S, or D to move, and ENTER to confirm")
        return self.PrintBoard()

    def ValidateMove(self, potentialQueen):
        #checks validation for every queen by checking that there are no shared columns or rows
        if len(qLocation) > 0:
            for queen in qLocation:
                #checks columns and rows
                if (potentialQueen[0] == qLocation[queen][0]) or (potentialQueen[1] == qLocation[queen][1]):
                    print(f'You are trying to place a queen in the same row or column as {queen}!')
                    return False
                #checks diagonals
                elif (abs(potentialQueen[0] - qLocation[queen][0])) == (abs(potentialQueen[1] - qLocation[queen][1])):
                    print(f'You are trying to place a queen diagonal from {queen}!')
                    return False
                else:
                    continue
            return True
        else:
            return True

    def getBoard(self):
        return board


if __name__ == '__main__':
    #create board object
    b = Board(int(input("Enter n val: ")))

    #this should keep track of the overall amount of queens being placed
    #and prevent anymore from being added after the amount reaches n
    roundIndex = 1
    while roundIndex < n:
        Board.Move(b)
        roundIndex+= 1