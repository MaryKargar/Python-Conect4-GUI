#tkinter für GUI
from tkinter import *
import time

class Connect4:

    def __init__(self):
        self.numberOfColumns = 7
        self.numberOfLines = 6
        self.board = [ [ '  ' for _ in range( self.numberOfColumns)] for _ in range(self.numberOfLines) ]

    def displayBoard(self):
        for i, line in enumerate(self.board):
            # Printing the line separators
            print("_" * self.numberOfColumns * 4)
            # Printing the line
            print(*line, sep=' |')
            # Printing numbers
        print('    '.join(str(x) for x in range(self.numberOfColumns)))

    def isAvailable(self, line, column):
        if line[column] == '  ':
            return True
        return False

    def player_choice(self):
        choice = int(input("Please select an empty space between 0 and 6 : "))
        while self.board[0][choice] != '  ':
            choice = int(input("This column is full. Please choose between 0 and 6 : "))
        return choice

    def player_input(self):
        player1 = input("Please pick a marker 'X' or 'O' ")
        while True:
            if player1.upper() == 'X':
                player2='O'
                print("You've choosen " + player1 + ". Player 2 will be " + player2)
                return player1.upper(),player2
            elif player1.upper() == 'O':
                player2='X'
                print("You've choosen " + player1 + ". Player 2 will be " + player2)
                return player1.upper(),player2
            else:
                player1 = input("Please pick a marker 'X' or 'O' ")

    def checkLines(self, marker, board=None):
        if board is None:
            board=self.board
        # Checkin lines
        for line in board:
            for i in range(0,len(line)):
                if i < len(line) - 3:
                    if line[i] == line[i+1] == line[i+2] == line[i+3] ==  marker:
                        return True

    def checkDiags(self, marker):
        diagBoard = []
        for i, line in enumerate(self.board):
            for idx, item in enumerate(line):
                # Find of there is some marker
                if item ==  marker:
                    diagBoard.append(int(str(i)+str(idx)))

        for item in diagBoard:
            if int(item) + 11 in diagBoard and int(item) + 22 in diagBoard and int(item) + 33 in diagBoard:
                return True

        for item in reversed(diagBoard):
            if int(item) - 9 in diagBoard and int(item) - 18 in diagBoard and int(item) - 27 in diagBoard:
                return True

    def generateReversedBoard(self):
        reversedBoard = []
        for line in self.board:
            for index, item in enumerate(line):
                try:
                    reversedBoard[index].append(item)
                except:
                    reversedBoard.append([])
                    reversedBoard[index].append(item)
        return reversedBoard

    def play(self, playercolumn, marker):
        for item in reversed(self.board):
            if self.isAvailable(item, playercolumn):
                item[playercolumn] = " " + marker
                return True
        return False




def enter():
    global col
    col=use.get()
    col=int(col)
    # print(col)
    global m
    m=opt.get()
    # print(m)
    row=0
    for item in reversed(c.board):
        if  c.isAvailable(item, col-1):
            item[col-1] = m
            break
        row+=1
    if m=='X':
                print(row,col)
                canvas.create_text((col)*50-25,300-(row+1)*50+25,fill="red",text='X',font=("Helvetica",16))
    else:
                canvas.create_text((col)*50-25,300-(row+1)*50+25,fill="black",text='O',font=("Helvetica",16))

    rB = c.generateReversedBoard()
    if c.checkLines(m) or c.checkLines(m, rB) or c.checkDiags(m):
                c.displayBoard()
                showwin() 

#Der Gewinner verwendet auch die gleichen Definitionen wie in der vorherigen connect 4-Datei, um Zeilen, Spalten und spiel regeln  zu überprüfen.

def showwin():  
    winner=Label(ws,text=f'Winner is {m}', width=500,  font=("Helvetica",16))
    winner.pack() 
    
    # Der Exit-Button wird verwendet, um das Spiel mit dem Befehl ws.destory() zu beenden.
def dest():
    ws.destroy()

def begin():
    global c
    c= Connect4()


ws = Tk()
ws.title('Game')
ws.geometry('1000x900')
ws.config(bg='#345')

#Mit Canvas gestalten wir einen 6*7 Tabellen
canvas = Canvas(
    ws,
    height=300,
    width=350,
    bg="#fff"
    )
canvas.pack()
i=0
while i<=6:
    canvas.create_line(0,i*50,350,i*50,fill='red')
    canvas.create_line(i*50,0,i*50,300,fill='red')
    i+=1

# Dazu gehören Buttons die Start- und End zum Auswählen von x, o und Enter
# Um das erste Spiel zu starten, müssen Sie die Start Button drücken
# In diesem Fall wird der start-Befehl im Startbutton ausgeführt, in dem zuvor das Gewinnt Spiel aufgerufen wurde.


# Um x, o auf der Seite zu platzieren, müssen wir die richtigen Koordinaten erhalten
# Dann gib es auf die Canvas

Options = ["Choose X or O", "X", "O"]
User = ['Col.', 1, 2, 3, 4, 5, 6, 7]

opt = StringVar(ws)
opt.set(Options[0])

use = StringVar(ws)
use.set(User[0])

w = OptionMenu(ws, opt, *Options[1:])
w.pack()

v = OptionMenu(ws, use, *User[1:])
v.pack()

# Die Enter-Button zeigt die Eingaben der beiden Optionbutton zur Auswahl von x, o und column im Canvas
button1= Button(ws, text="Enter", command=enter)
button1.pack()

button2 = Button(ws, text="Exit", command=dest)
button2.pack(side=RIGHT)

startbutton=Button(ws,text='Start',command=begin)
startbutton.pack(side=LEFT)


ws.mainloop()