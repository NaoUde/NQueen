"""
Handles inputs and displays graphics
"""
from operator import truediv

#Setup:  imports, create the start menu, open the screen, take in the n value input
import pygame
import engine

pygame.init()

class Setup():
    #game window
    #Capital snakecase for pygame system constants, should not need to be changed after this point
    def __init__(self, w, h):
        self.SCREEN_WIDTH = w
        self.SCREEN_HEIGHT = h
        self.SCREEN = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))

    pygame.display.set_caption("N-Queen")
    global palette

    #central game palette
    palette = {"tan" : (231,207,188), "white":(255, 244, 236),"black":(12, 22, 24),"green":(0, 70, 67),"pink":(201, 134, 134)}

    #text
    global TITLE_FONT
    global SUBTITLE_FONT
    global TITLE_TEXT
    global TEXT_FONT
    global QUEEN_FONT

    TITLE_FONT = pygame.font.SysFont("Times New Roman", 60)
    SUBTITLE_FONT = pygame.font.SysFont("Times New Roman", 35)
    TEXT_FONT = pygame.font.SysFont("Times New Roman", 25)

    string = "♛"
    QUEEN_FONT = pygame.font.Font("segoe-ui-symbol.ttf", 64)

    TITLE_TEXT = "The N-Queen Problem" #names window

    def drawText(self,text,font, color, y, x = None):
        x = self.SCREEN_WIDTH//2 if x is None else x
        rendered = font.render(text,True,color)
        renderedRect = rendered.get_rect(center = (x,y))
        pygame.draw.rect(self.SCREEN,palette["green"],renderedRect)
        self.SCREEN.blit(rendered,renderedRect)

    #should have been a class... smh...
    def drawButton(self,text,x,y, color = (231,207,188), w = 25, h = 25,font = TEXT_FONT, fontColor = palette["black"]):
        textFont = font.render(text, True,fontColor)
        pygame.draw.rect(self.SCREEN,color,[x,y,w,h])
        self.SCREEN.blit(textFont,(x,y))
        return (x,y)

    def startScreen(self):
        self.SCREEN.fill(palette["green"])
        #displ title & instructions
        self.drawText(TITLE_TEXT,TITLE_FONT,palette["tan"],50)
        self.drawText("♛", QUEEN_FONT, palette["white"],50,100)
        self.drawText("♛", QUEEN_FONT, palette["black"],50,self.SCREEN_WIDTH-100)
        self.drawText("Challenge:", SUBTITLE_FONT,palette["white"],120)
        self.drawText("Place N chess queens on an NxN chessboard", TEXT_FONT,palette["tan"],170)
        self.drawText("so that no two queens can harm one another.", TEXT_FONT,palette["tan"],200)
        self.drawText("Pick your N:", SUBTITLE_FONT, palette["tan"],260)

        #create the 5 N val buttons using my function (4-8),
        # their locations stored in a list for later referencing
        nButton = {}

        for i in range(4,9):
            nButton[i] = self.drawButton(f" {i}",85 + (50*i), 300)

        return nButton

    def infoScreen(self):
        print("info!")

        while True:
            mouse = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    return

            self.drawText("In the game of Chess...", SUBTITLE_FONT, palette["tan"],50)
            self.drawText("The queen is one of the most powerful pieces, capable of moving", TEXT_FONT, palette["tan"], 100,
                          100)
            self.drawText("forwards, backwards, left, and right completely without bound.", TEXT_FONT, palette["tan"], 120,
                          100)
            self.drawText("In chess, to lose the queen is to practically lose the game itself!", TEXT_FONT, palette["tan"], 140,
                          100)

            self.drawText("In this challenge,", SUBTITLE_FONT, palette["tan"], 200,
                          self.SCREEN_WIDTH - 300)
            self.drawText("You've been challenged to place N (being a number between 4 and 8, inclusive)", TEXT_FONT, palette["tan"], 220,
                          self.SCREEN_WIDTH - 300)
            self.drawText(" Queens onto an N by N chessboard.", TEXT_FONT, palette["tan"],240,
                          self.SCREEN_WIDTH - 300)

            #self.drawButton("BEGIN!",self.SCREEN_WIDTH//2-50,300)



    def gameBoard(self, n, board):
            self.SCREEN.fill(palette["green"])
            for c in range(n):
                for r in range(n):
                    self.drawButton("", (self.SCREEN_WIDTH - (625) - 100) + (c * (625//n)), (self.SCREEN_HEIGHT - 625 - 50) + (r * (625//n)),
                                    palette["black"] if (r+(c%2)) % 2 == 0 else palette["white"],(625//n),(625//n))
                    #self.displayBoard(board, r,c)

            self.drawText(TITLE_TEXT,TITLE_FONT,palette["tan"],50)
            self.drawText("♛", QUEEN_FONT, palette["white"],50,200)
            self.drawText("♛", QUEEN_FONT, palette["black"],50,self.SCREEN_WIDTH-200)
            self.drawText("♛", QUEEN_FONT, palette["tan"],200,150)

            self.drawButton(" Main Menu", 75, 600, palette["tan"], 130, 30)
            self.drawButton(" Start Over", 80, 550, palette["tan"], 120, 30)
            self.drawButton(" Solve it for me!", 55, 650, palette["tan"], 175, 30)
            return board

    def displayBoard(self, board):
        for c in range(n):
            for r in range(n):
                if "Q" in board[r][c]:
                    self.drawButton("♛", (self.SCREEN_WIDTH - (625) - 100) + (c * (625 // n)),
                                    (self.SCREEN_HEIGHT - 625 - 50) + (r * (625 // n)),
                                    palette["black"] if (r + (c % 2)) % 2 == 0 else palette["white"], (625 // n),
                                    (625 // n), font = QUEEN_FONT, fontColor= palette["black"] if (r + (c % 2)) % 2 == 1 else palette["white"])

                elif "♛" in board[r][c]:
                    self.drawButton("♛", (self.SCREEN_WIDTH - (625) - 100) + (cursor["column"] * (625 // n)),
                                    (self.SCREEN_HEIGHT - 625 - 50) + (cursor["row"] * (625 // n)), palette["pink"],
                                    (625 // n),
                                    (625 // n), font=QUEEN_FONT, fontColor=palette["white"])

                else:
                    self.drawButton("", (self.SCREEN_WIDTH - (625) - 100) + (c * (625 // n)),
                        (self.SCREEN_HEIGHT - 625 - 50) + (r * (625 // n)),
                        palette["black"] if (r + (c % 2)) % 2 == 0 else palette["white"], (625 // n),
                        (625 // n))

    def move(self, board, cursor, direction = ""):
        board[cursor["row"]][cursor["column"]] = "" if board[cursor["row"]][cursor["column"]] == "♛" else board[cursor["row"]][cursor["column"]]


        if direction == "L" and cursor["column"] > 0:
            cursor["column"] -= 1
        elif direction == "R" and cursor["column"] < n-1:
            cursor["column"] += 1
        elif direction == "U" and cursor["row"] > 0:
            cursor["row"] -= 1
        elif direction == "D" and cursor["row"] < n-1:
            cursor["row"] += 1
        self.drawButton("♛", (self.SCREEN_WIDTH - (625) - 100) + (cursor["column"] * (625 // n)),
                        (self.SCREEN_HEIGHT - 625 - 50) + (cursor["row"] * (625 // n)),palette["pink"],(625//n),
                        (625//n), font = QUEEN_FONT, fontColor = palette["black"])

        if cursor["count"] == n:
            board[cursor["row"]][cursor["column"]] = "♛"
        else:
            board[cursor["row"]][cursor["column"]] = "♛" if board[cursor["row"]][cursor["column"]] == "" else board[cursor["row"]][cursor["column"]]
        return cursor

    def validateMove(self, board, newQueen, queenList, count):
        if len(queenList) > 0:
            print(queenList)
            for queen in queenList:
                print(queen)
                pygame.draw.rect(self.SCREEN,palette["green"],[25,350,250,175]) #x,y,w,h
                #columns and rows
                if newQueen[0] == queenList[queen][0]:
                    self.drawText(f"X",TITLE_FONT,palette["pink"],440, 150)
                    self.drawText(f"Same row as ({tuple(queenList[queen])[1] + 1}, {tuple(queenList[queen])[0] + 1})",TEXT_FONT,palette["pink"],380, 150)
                    return False
                elif newQueen[1] == queenList[queen][1]:
                    self.drawText(f"X",TITLE_FONT,palette["pink"],440, 150)
                    self.drawText(f"Same column as ({tuple(queenList[queen])[1] + 1}, {tuple(queenList[queen])[0] + 1})",TEXT_FONT,palette["pink"],380, 150)
                    return False
                elif abs(newQueen[0] - queenList[queen][0]) == abs(newQueen[1] - queenList[queen][1]):
                    self.drawText(f"X",TITLE_FONT,palette["pink"],440, 150)
                    self.drawText(f"Diagonal from ({tuple(queenList[queen])[1] + 1}, {tuple(queenList[queen])[0] + 1})",TEXT_FONT,palette["pink"],380, 150)
                    return False
        self.drawText(f"Great Work!", SUBTITLE_FONT, palette["white"], 425, 150)
        return True

    def branch(self):
        pass

    #recursion!!  ah!
    def autoSolve(self, board, queenList):
        r = 0
        c = 0
        queenCount = n
        while queenCount > 0:
            if validateMove(board, [r,c], queenList, queenCount):
                board[r][c] = "Q"
                queenList[f"Q{n+1-queenCount}"] = [r,c]
                r += 1
                queenCount -= 1
            else:
                c += 1

    def validateMove2(self, board, newQueen):
        for row in range(n):
            # columns
            if board[row][newQueen[0]] != "":
                print(f"False, column.  queen: {row},{newQueen[0]}")
                return False
            else:
                print("cont")
        print("True")
        return True

    def solveUntil(self, board, cursor):
        if cursor[1] >= n:
            return True

        for i in range(n):
            if self.validateMove2(board, cursor):
                board[cursor[0]][cursor[1]] = f"Q"
                cursor[1] += 1
                if self.solveUntil(board, cursor):
                    return True

                board[cursor[0]][cursor[1]] = ""
            else:
                cursor[0] = i
        return False

    def solveUntilBackup(self, board, cursor):
        for r in range(n):
            for c in range(0,n,2):
                try:
                    board[r][c] = "Q"
                except:
                    board[r][c-n+1] = "Q"
        return board

play = False
quit = play

MenuSetup = Setup(800, 600)
# central program loop
nButton = MenuSetup.startScreen()
n = 0
print("new")

while not quit:
    mouse = pygame.mouse.get_pos()

    #iterates through every event pygame notices to close the game
    for event in pygame.event.get():
        #looks for the x button press
        if event.type == pygame.QUIT:
            quit = True

        #onclick, check if the click was over any of the buttons
        if event.type == pygame.MOUSEBUTTONDOWN:
            for button in nButton: #for each button location, check if the mouse clicked
                if (nButton[button][0] <= mouse[0] <= nButton[button][0] + 25) and (nButton[button][1] <= mouse[1] <= nButton[button][1] + 25):
                    n = button

                    for i in range(4,9):
                        MenuSetup.drawButton(f" {i}", 85 + (50 * i), 300)
                        MenuSetup.drawButton(f" {button}", 85 + (50*button), 300, palette["white"])

            if (n != 0) and (MenuSetup,MenuSetup.SCREEN_WIDTH//2 - 30 <= mouse[0] <= MenuSetup.SCREEN_WIDTH//2 + 30) and (500 <= mouse[1] <= 550):
                play = True

        if n != 0:
            MenuSetup.drawText(f'N = {n}',TITLE_FONT,palette["white"],MenuSetup.SCREEN_WIDTH//2,400)
            MenuSetup.drawButton(" START",MenuSetup.SCREEN_WIDTH//2 - 60,500,palette["tan"], 125, 50, font = SUBTITLE_FONT)

        #Update screen at the end of loop
        pygame.display.update()

    if play:
        GameSetup = Setup(1200,800)
        #GameSetup.infoScreen()

        #gameplay setup
        board = GameSetup.gameBoard(n, [["" for c in range(n)] for r in range(n)])
        board[0][0] = "♛"
        cursor = {"row": 0, "column": 0, "count": n}
        queen = cursor
        queenList = {}
        GameSetup.move(board,cursor)

    #gameplay loop
    while play:
        mouse = pygame.mouse.get_pos()

        #update the n value and queens left
        GameSetup.drawText(f"N = {n}",SUBTITLE_FONT,palette["tan"],250,150)
        GameSetup.drawText(f"Queens Left: {cursor["count"]}",SUBTITLE_FONT,palette["tan"],300,150)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and cursor["count"] > 0:
                # move the cursor using WASD or arrow keys, checks if a valid direction
                if event.key == pygame.K_LEFT or event.key == pygame.K_a: cursor = GameSetup.move(board, cursor, "L")
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d: cursor = GameSetup.move(board, cursor, "R")
                if event.key == pygame.K_DOWN or event.key == pygame.K_s: cursor = GameSetup.move(board, cursor, "D")
                if event.key == pygame.K_UP or event.key == pygame.K_w: cursor = GameSetup.move(board, cursor, "U")

                #enter button press should check for valid placement and append queen to queenlist if valid
                if event.key == pygame.K_RETURN:
                    print(queenList)
                    queen = [cursor["row"],cursor["column"]]
                    if GameSetup.validateMove(board, queen, queenList, cursor["count"]):
                        queenList[f"Q{cursor["count"]}"] = queen
                        board[cursor["row"]][cursor["column"]] = f"Q{n + 1 - cursor["count"]}"
                        cursor["count"] -= 1

            #if the user presses the quit button
            if event.type == pygame.MOUSEBUTTONDOWN:
                #Main menu button press
                if (75 <= mouse[0] <= 205) and (600 <= mouse[1] <= 630):
                    play = False
                    MenuSetup = Setup(800, 600)

                #Start Over button press
                if (80 <= mouse[0] <= 200) and (550 <= mouse[1] <= 580):
                    GameSetup = Setup(1200, 800)
                    board = GameSetup.gameBoard(n, [["" for c in range(n)] for r in range(n)])
                    board[0][0] = "♛"
                    cursor = {"row": 0, "column": 0, "count": n}
                    queen = cursor
                    queenList = {}
                    GameSetup.move(board, cursor)

                #Solve for Me button press
                if (55 <= mouse[0] <= 230) and (650 <= mouse[1] <= 680):
                    GameSetup = Setup(1200, 800)
                    board = GameSetup.gameBoard(n, [["" for c in range(n)] for r in range(n)])
                    board[0][0] = "♛"
                    cursor = {"row": 0, "column": 0, "count": n}
                    queen = cursor
                    queenList = {}
                    GameSetup.move(board, cursor)

                    GameSetup.solveUntilBackup(board, [0,0])

            # looks for the x button press
            if event.type == pygame.QUIT:
                play = False
                quit = True

        #update screen by redrawing board
        if play == False:
            if not quit:
                MenuSetup = Setup(800, 600)
                # central program loop
                nButton = MenuSetup.startScreen()
                n = 0
                break
        GameSetup.displayBoard(board)
        pygame.display.update()


pygame.quit()
