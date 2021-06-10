from graphics import *

global board
board = [[0 for i in range(9)] for j in range(9)]

global values
values = [0]*81

global value
value = [0]*81


def printBoard():
    print("+==========================+")
    for i in range(len(board)):
        print("| ", end="")
        for j in range (len(board[i])):
            if(j % 3 == 0 and j != 0):
                print(" | ", end="")
            if board[i][j] == 0:
                print("  ", end="")
            else:
                print(board[i][j], end=" ")
        print(" | ")
        if((i+1) % 3 == 0 and i != 0):
            print("+==========================+")

def drawBoardSolution():
    win = GraphWin("Sudoku", 470, 470)

    line = Rectangle(Point(5, 470), Point(0,0))
    line2 = Rectangle(Point(0, 0), Point(470, 5))
    line3 = Rectangle(Point(470, 0), Point(465, 470))
    line4 = Rectangle(Point(0, 470), Point(470, 465))
    line5 = Rectangle(Point(155, 0), Point(160, 470))
    line6 = Rectangle(Point(310, 470), Point(315, 0))
    line7 = Rectangle(Point(0, 155), Point(470, 160))
    line8 = Rectangle(Point(470, 310), Point(0, 315))

    line.setFill("black")
    line2.setFill("black")
    line3.setFill("black")
    line4.setFill("black")
    line5.setFill("black")
    line6.setFill("black")
    line7.setFill("black")
    line8.setFill("black")

    line4.draw(win)
    line3.draw(win)
    line2.draw(win)
    line.draw(win)
    line5.draw(win)
    line6.draw(win)
    line7.draw(win)
    line8.draw(win)

    smallLine1 = Line(Point(55, 0), Point(55, 470))
    smallLine2 = Line(Point(105, 0), Point(105, 470))
    smallLine3 = Line(Point(210, 0), Point(210, 470))
    smallLine4 = Line(Point(260, 0), Point(260, 470))
    smallLine5 = Line(Point(365, 0), Point(365, 470))
    smallLine6 = Line(Point(415, 0), Point(415, 470))

    smallLine7 = Line(Point(0, 55), Point(470, 55))
    smallLine8 = Line(Point(0, 105), Point(470, 105))
    smallLine9 = Line(Point(0, 210), Point(470, 210))
    smallLine10 = Line(Point(0, 260), Point(470, 260))
    smallLine11 = Line(Point(0, 365), Point(470, 365))
    smallLine12 = Line(Point(0, 415), Point(470, 415))

    smallLine1.draw(win)
    smallLine2.draw(win)
    smallLine3.draw(win)
    smallLine4.draw(win)
    smallLine5.draw(win)
    smallLine6.draw(win)
    smallLine7.draw(win)
    smallLine8.draw(win)
    smallLine9.draw(win)
    smallLine10.draw(win)
    smallLine11.draw(win)
    smallLine12.draw(win)

    x = 27
    y = 30

    input_box1 = Text(Point(x,y), str(value[0]))
    x += 50
    input_box2 = Text(Point(x,y), str(value[1]))
    x += 50
    input_box3 = Text(Point(x,y), str(value[2]))
    x += 55
    input_box4 = Text(Point(x,y), str(value[3]))
    x += 50
    input_box5 = Text(Point(x,y), str(value[4]))
    x += 50
    input_box6 = Text(Point(x,y), str(value[5]))
    x += 55
    input_box7 = Text(Point(x,y), str(value[6]))
    x += 50
    input_box8 = Text(Point(x,y), str(value[7]))
    x += 50
    input_box9 = Text(Point(x,y), str(value[8]))

    x = 27
    y += 50
    input_box11 = Text(Point(x,y), str(value[9]))
    x += 50
    input_box12 = Text(Point(x,y), str(value[10]))
    x += 50
    input_box13 = Text(Point(x,y), str(value[11]))
    x += 55
    input_box14 = Text(Point(x,y), str(value[12]))
    x += 50
    input_box15 = Text(Point(x,y), str(value[13]))
    x += 50
    input_box16 = Text(Point(x,y), str(value[14]))
    x += 55
    input_box17 = Text(Point(x,y), str(value[15]))
    x += 50
    input_box18 = Text(Point(x,y), str(value[16]))
    x += 50
    input_box19 = Text(Point(x,y), str(value[17]))

    x = 27
    y += 50
    input_box21 = Text(Point(x,y), str(value[18]))
    x += 50
    input_box22 = Text(Point(x,y), str(value[19]))
    x += 50
    input_box23 = Text(Point(x,y), str(value[20]))
    x += 55
    input_box24 = Text(Point(x,y), str(value[21]))
    x += 50
    input_box25 = Text(Point(x,y), str(value[22]))
    x += 50
    input_box26 = Text(Point(x,y), str(value[23]))
    x += 55
    input_box27 = Text(Point(x,y), str(value[24]))
    x += 50
    input_box28 = Text(Point(x,y), str(value[25]))
    x += 50
    input_box29 = Text(Point(x,y), str(value[26]))

    x = 27
    y += 55
    input_box31 = Text(Point(x,y), str(value[27]))
    x += 50
    input_box32 = Text(Point(x,y), str(value[28]))
    x += 50
    input_box33 = Text(Point(x,y), str(value[29]))
    x += 55
    input_box34 = Text(Point(x,y), str(value[30]))
    x += 50
    input_box35 = Text(Point(x,y), str(value[31]))
    x += 50
    input_box36 = Text(Point(x,y), str(value[32]))
    x += 55
    input_box37 = Text(Point(x,y), str(value[33]))
    x += 50
    input_box38 = Text(Point(x,y), str(value[34]))
    x += 50
    input_box39 = Text(Point(x,y), str(value[35]))

    x = 27
    y += 50
    input_box41 = Text(Point(x,y), str(value[36]))
    x += 50
    input_box42 = Text(Point(x,y), str(value[37]))
    x += 50
    input_box43 = Text(Point(x,y), str(value[38]))
    x += 55
    input_box44 = Text(Point(x,y), str(value[39]))
    x += 50
    input_box45 = Text(Point(x,y), str(value[40]))
    x += 50
    input_box46 = Text(Point(x,y), str(value[41]))
    x += 55
    input_box47 = Text(Point(x,y), str(value[42]))
    x += 50
    input_box48 = Text(Point(x,y), str(value[43]))
    x += 50
    input_box49 = Text(Point(x,y), str(value[44]))

    x = 27
    y += 50
    input_box51 = Text(Point(x,y), str(value[45]))
    x += 50
    input_box52 = Text(Point(x,y), str(value[46]))
    x += 50
    input_box53 = Text(Point(x,y), str(value[47]))
    x += 55
    input_box54 = Text(Point(x,y), str(value[48]))
    x += 50
    input_box55 = Text(Point(x,y), str(value[49]))
    x += 50
    input_box56 = Text(Point(x,y), str(value[50]))
    x += 55
    input_box57 = Text(Point(x,y), str(value[51]))
    x += 50
    input_box58 = Text(Point(x,y), str(value[52]))
    x += 50
    input_box59 = Text(Point(x,y), str(value[53]))

    x = 27
    y += 55
    input_box61 = Text(Point(x,y), str(value[54]))
    x += 50
    input_box62 = Text(Point(x,y), str(value[55]))
    x += 50
    input_box63 = Text(Point(x,y), str(value[56]))
    x += 55
    input_box64 = Text(Point(x,y), str(value[57]))
    x += 50
    input_box65 = Text(Point(x,y), str(value[58]))
    x += 50
    input_box66 = Text(Point(x,y), str(value[59]))
    x += 55
    input_box67 = Text(Point(x,y), str(value[60]))
    x += 50
    input_box68 = Text(Point(x,y), str(value[61]))
    x += 50
    input_box69 = Text(Point(x,y), str(value[62]))

    x = 27
    y += 50
    input_box71 = Text(Point(x,y), str(value[63]))
    x += 50
    input_box72 = Text(Point(x,y), str(value[64]))
    x += 50
    input_box73 = Text(Point(x,y), str(value[65]))
    x += 55
    input_box74 = Text(Point(x,y), str(value[66]))
    x += 50
    input_box75 = Text(Point(x,y), str(value[67]))
    x += 50
    input_box76 = Text(Point(x,y), str(value[68]))
    x += 55
    input_box77 = Text(Point(x,y), str(value[69]))
    x += 50
    input_box78 = Text(Point(x,y), str(value[70]))
    x += 50
    input_box79 = Text(Point(x,y), str(value[71]))

    x = 27
    y += 50
    input_box81 = Text(Point(x,y), str(value[72]))
    x += 50
    input_box82 = Text(Point(x,y), str(value[73]))
    x += 50
    input_box83 = Text(Point(x,y), str(value[74]))
    x += 55
    input_box84 = Text(Point(x,y), str(value[75]))
    x += 50
    input_box85 = Text(Point(x,y), str(value[76]))
    x += 50
    input_box86 = Text(Point(x,y), str(value[77]))
    x += 55
    input_box87 = Text(Point(x,y), str(value[78]))
    x += 50
    input_box88 = Text(Point(x,y), str(value[79]))
    x += 50
    input_box89 = Text(Point(x,y), str(value[80]))


    input_box1.draw(win)
    input_box2.draw(win)
    input_box3.draw(win)
    input_box4.draw(win)
    input_box5.draw(win)
    input_box6.draw(win)
    input_box7.draw(win)
    input_box8.draw(win)
    input_box9.draw(win)
    input_box11.draw(win)
    input_box12.draw(win)
    input_box13.draw(win)
    input_box14.draw(win)
    input_box15.draw(win)
    input_box16.draw(win)
    input_box17.draw(win)
    input_box18.draw(win)
    input_box19.draw(win)
    input_box21.draw(win)
    input_box22.draw(win)
    input_box23.draw(win)
    input_box24.draw(win)
    input_box25.draw(win)
    input_box26.draw(win)
    input_box27.draw(win)
    input_box28.draw(win)
    input_box29.draw(win)
    input_box31.draw(win)
    input_box32.draw(win)
    input_box33.draw(win)
    input_box34.draw(win)
    input_box35.draw(win)
    input_box36.draw(win)
    input_box37.draw(win)
    input_box38.draw(win)
    input_box39.draw(win)
    input_box41.draw(win)
    input_box42.draw(win)
    input_box43.draw(win)
    input_box44.draw(win)
    input_box45.draw(win)
    input_box46.draw(win)
    input_box47.draw(win)
    input_box48.draw(win)
    input_box49.draw(win)
    input_box51.draw(win)
    input_box52.draw(win)
    input_box53.draw(win)
    input_box54.draw(win)
    input_box55.draw(win)
    input_box56.draw(win)
    input_box57.draw(win)
    input_box58.draw(win)
    input_box59.draw(win)
    input_box61.draw(win)
    input_box62.draw(win)
    input_box63.draw(win)
    input_box64.draw(win)
    input_box65.draw(win)
    input_box66.draw(win)
    input_box67.draw(win)
    input_box68.draw(win)
    input_box69.draw(win)
    input_box71.draw(win)
    input_box72.draw(win)
    input_box73.draw(win)
    input_box74.draw(win)
    input_box75.draw(win)
    input_box76.draw(win)
    input_box77.draw(win)
    input_box78.draw(win)
    input_box79.draw(win)
    input_box81.draw(win)
    input_box82.draw(win)
    input_box83.draw(win)
    input_box84.draw(win)
    input_box85.draw(win)
    input_box86.draw(win)
    input_box87.draw(win)
    input_box88.draw(win)
    input_box89.draw(win)

    win.getMouse() # Pause to view result
    win.close()    # Close window when done


def drawBoard():
    win = GraphWin("Sudoku", 470, 470)
    #line2 = Rectanlge(Point(), Point())

    line = Rectangle(Point(5, 470), Point(0,0))
    line2 = Rectangle(Point(0, 0), Point(470, 5))
    line3 = Rectangle(Point(470, 0), Point(465, 470))
    line4 = Rectangle(Point(0, 470), Point(470, 465))
    line5 = Rectangle(Point(155, 0), Point(160, 470))
    line6 = Rectangle(Point(310, 470), Point(315, 0))
    line7 = Rectangle(Point(0, 155), Point(470, 160))
    line8 = Rectangle(Point(470, 310), Point(0, 315))

    line.setFill("black")
    line2.setFill("black")
    line3.setFill("black")
    line4.setFill("black")
    line5.setFill("black")
    line6.setFill("black")
    line7.setFill("black")
    line8.setFill("black")

    line4.draw(win)
    line3.draw(win)
    line2.draw(win)
    line.draw(win)
    line5.draw(win)
    line6.draw(win)
    line7.draw(win)
    line8.draw(win)

    smallLine1 = Line(Point(55, 0), Point(55, 470))
    smallLine2 = Line(Point(105, 0), Point(105, 470))
    smallLine3 = Line(Point(210, 0), Point(210, 470))
    smallLine4 = Line(Point(260, 0), Point(260, 470))
    smallLine5 = Line(Point(365, 0), Point(365, 470))
    smallLine6 = Line(Point(415, 0), Point(415, 470))

    smallLine7 = Line(Point(0, 55), Point(470, 55))
    smallLine8 = Line(Point(0, 105), Point(470, 105))
    smallLine9 = Line(Point(0, 210), Point(470, 210))
    smallLine10 = Line(Point(0, 260), Point(470, 260))
    smallLine11 = Line(Point(0, 365), Point(470, 365))
    smallLine12 = Line(Point(0, 415), Point(470, 415))

    smallLine1.draw(win)
    smallLine2.draw(win)
    smallLine3.draw(win)
    smallLine4.draw(win)
    smallLine5.draw(win)
    smallLine6.draw(win)
    smallLine7.draw(win)
    smallLine8.draw(win)
    smallLine9.draw(win)
    smallLine10.draw(win)
    smallLine11.draw(win)
    smallLine12.draw(win)

    x = 27
    y = 30

    input_box1 = Entry(Point(x,y), 3)
    x += 50
    input_box2 = Entry(Point(x,y), 3)
    x += 50
    input_box3 = Entry(Point(x,y), 3)
    x += 55
    input_box4 = Entry(Point(x,y), 3)
    x += 50
    input_box5 = Entry(Point(x,y), 3)
    x += 50
    input_box6 = Entry(Point(x,y), 3)
    x += 55
    input_box7 = Entry(Point(x,y), 3)
    x += 50
    input_box8 = Entry(Point(x,y), 3)
    x += 50
    input_box9 = Entry(Point(x,y), 3)


    x = 27
    y += 50
    input_box11 = Entry(Point(x,y), 3)
    x += 50
    input_box12 = Entry(Point(x,y), 3)
    x += 50
    input_box13 = Entry(Point(x,y), 3)
    x += 55
    input_box14 = Entry(Point(x,y), 3)
    x += 50
    input_box15 = Entry(Point(x,y), 3)
    x += 50
    input_box16 = Entry(Point(x,y), 3)
    x += 55
    input_box17 = Entry(Point(x,y), 3)
    x += 50
    input_box18 = Entry(Point(x,y), 3)
    x += 50
    input_box19 = Entry(Point(x,y), 3)

    x = 27
    y += 50
    input_box21 = Entry(Point(x,y), 3)
    x += 50
    input_box22 = Entry(Point(x,y), 3)
    x += 50
    input_box23 = Entry(Point(x,y), 3)
    x += 55
    input_box24 = Entry(Point(x,y), 3)
    x += 50
    input_box25 = Entry(Point(x,y), 3)
    x += 50
    input_box26 = Entry(Point(x,y), 3)
    x += 55
    input_box27 = Entry(Point(x,y), 3)
    x += 50
    input_box28 = Entry(Point(x,y), 3)
    x += 50
    input_box29 = Entry(Point(x,y), 3)

    x = 27
    y += 55
    input_box31 = Entry(Point(x,y), 3)
    x += 50
    input_box32 = Entry(Point(x,y), 3)
    x += 50
    input_box33 = Entry(Point(x,y), 3)
    x += 55
    input_box34 = Entry(Point(x,y), 3)
    x += 50
    input_box35 = Entry(Point(x,y), 3)
    x += 50
    input_box36 = Entry(Point(x,y), 3)
    x += 55
    input_box37 = Entry(Point(x,y), 3)
    x += 50
    input_box38 = Entry(Point(x,y), 3)
    x += 50
    input_box39 = Entry(Point(x,y), 3)

    x = 27
    y += 50
    input_box41 = Entry(Point(x,y), 3)
    x += 50
    input_box42 = Entry(Point(x,y), 3)
    x += 50
    input_box43 = Entry(Point(x,y), 3)
    x += 55
    input_box44 = Entry(Point(x,y), 3)
    x += 50
    input_box45 = Entry(Point(x,y), 3)
    x += 50
    input_box46 = Entry(Point(x,y), 3)
    x += 55
    input_box47 = Entry(Point(x,y), 3)
    x += 50
    input_box48 = Entry(Point(x,y), 3)
    x += 50
    input_box49 = Entry(Point(x,y), 3)

    x = 27
    y += 50
    input_box51 = Entry(Point(x,y), 3)
    x += 50
    input_box52 = Entry(Point(x,y), 3)
    x += 50
    input_box53 = Entry(Point(x,y), 3)
    x += 55
    input_box54 = Entry(Point(x,y), 3)
    x += 50
    input_box55 = Entry(Point(x,y), 3)
    x += 50
    input_box56 = Entry(Point(x,y), 3)
    x += 55
    input_box57 = Entry(Point(x,y), 3)
    x += 50
    input_box58 = Entry(Point(x,y), 3)
    x += 50
    input_box59 = Entry(Point(x,y), 3)

    x = 27
    y += 55
    input_box61 = Entry(Point(x,y), 3)
    x += 50
    input_box62 = Entry(Point(x,y), 3)
    x += 50
    input_box63 = Entry(Point(x,y), 3)
    x += 55
    input_box64 = Entry(Point(x,y), 3)
    x += 50
    input_box65 = Entry(Point(x,y), 3)
    x += 50
    input_box66 = Entry(Point(x,y), 3)
    x += 55
    input_box67 = Entry(Point(x,y), 3)
    x += 50
    input_box68 = Entry(Point(x,y), 3)
    x += 50
    input_box69 = Entry(Point(x,y), 3)

    x = 27
    y += 50
    input_box71 = Entry(Point(x,y), 3)
    x += 50
    input_box72 = Entry(Point(x,y), 3)
    x += 50
    input_box73 = Entry(Point(x,y), 3)
    x += 55
    input_box74 = Entry(Point(x,y), 3)
    x += 50
    input_box75 = Entry(Point(x,y), 3)
    x += 50
    input_box76 = Entry(Point(x,y), 3)
    x += 55
    input_box77 = Entry(Point(x,y), 3)
    x += 50
    input_box78 = Entry(Point(x,y), 3)
    x += 50
    input_box79 = Entry(Point(x,y), 3)

    x = 27
    y += 50
    input_box81 = Entry(Point(x,y), 3)
    x += 50
    input_box82 = Entry(Point(x,y), 3)
    x += 50
    input_box83 = Entry(Point(x,y), 3)
    x += 55
    input_box84 = Entry(Point(x,y), 3)
    x += 50
    input_box85 = Entry(Point(x,y), 3)
    x += 50
    input_box86 = Entry(Point(x,y), 3)
    x += 55
    input_box87 = Entry(Point(x,y), 3)
    x += 50
    input_box88 = Entry(Point(x,y), 3)
    x += 50
    input_box89 = Entry(Point(x,y), 3)

    input_box1.setFill("white")
    input_box2.setFill("white")
    input_box3.setFill("white")
    input_box4.setFill("white")
    input_box5.setFill("white")
    input_box6.setFill("white")
    input_box7.setFill("white")
    input_box8.setFill("white")
    input_box9.setFill("white")
    input_box11.setFill("white")
    input_box12.setFill("white")
    input_box13.setFill("white")
    input_box14.setFill("white")
    input_box15.setFill("white")
    input_box16.setFill("white")
    input_box17.setFill("white")
    input_box18.setFill("white")
    input_box19.setFill("white")
    input_box21.setFill("white")
    input_box22.setFill("white")
    input_box23.setFill("white")
    input_box24.setFill("white")
    input_box25.setFill("white")
    input_box26.setFill("white")
    input_box27.setFill("white")
    input_box28.setFill("white")
    input_box29.setFill("white")
    input_box31.setFill("white")
    input_box32.setFill("white")
    input_box33.setFill("white")
    input_box34.setFill("white")
    input_box35.setFill("white")
    input_box36.setFill("white")
    input_box37.setFill("white")
    input_box38.setFill("white")
    input_box39.setFill("white")
    input_box41.setFill("white")
    input_box42.setFill("white")
    input_box43.setFill("white")
    input_box44.setFill("white")
    input_box45.setFill("white")
    input_box46.setFill("white")
    input_box47.setFill("white")
    input_box48.setFill("white")
    input_box49.setFill("white")
    input_box51.setFill("white")
    input_box52.setFill("white")
    input_box53.setFill("white")
    input_box54.setFill("white")
    input_box55.setFill("white")
    input_box56.setFill("white")
    input_box57.setFill("white")
    input_box58.setFill("white")
    input_box59.setFill("white")
    input_box61.setFill("white")
    input_box62.setFill("white")
    input_box63.setFill("white")
    input_box64.setFill("white")
    input_box65.setFill("white")
    input_box66.setFill("white")
    input_box67.setFill("white")
    input_box68.setFill("white")
    input_box69.setFill("white")
    input_box71.setFill("white")
    input_box72.setFill("white")
    input_box73.setFill("white")
    input_box74.setFill("white")
    input_box75.setFill("white")
    input_box76.setFill("white")
    input_box77.setFill("white")
    input_box78.setFill("white")
    input_box79.setFill("white")
    input_box81.setFill("white")
    input_box82.setFill("white")
    input_box83.setFill("white")
    input_box84.setFill("white")
    input_box85.setFill("white")
    input_box86.setFill("white")
    input_box87.setFill("white")
    input_box88.setFill("white")
    input_box89.setFill("white")

    input_box1.draw(win)
    input_box2.draw(win)
    input_box3.draw(win)
    input_box4.draw(win)
    input_box5.draw(win)
    input_box6.draw(win)
    input_box7.draw(win)
    input_box8.draw(win)
    input_box9.draw(win)
    input_box11.draw(win)
    input_box12.draw(win)
    input_box13.draw(win)
    input_box14.draw(win)
    input_box15.draw(win)
    input_box16.draw(win)
    input_box17.draw(win)
    input_box18.draw(win)
    input_box19.draw(win)
    input_box21.draw(win)
    input_box22.draw(win)
    input_box23.draw(win)
    input_box24.draw(win)
    input_box25.draw(win)
    input_box26.draw(win)
    input_box27.draw(win)
    input_box28.draw(win)
    input_box29.draw(win)
    input_box31.draw(win)
    input_box32.draw(win)
    input_box33.draw(win)
    input_box34.draw(win)
    input_box35.draw(win)
    input_box36.draw(win)
    input_box37.draw(win)
    input_box38.draw(win)
    input_box39.draw(win)
    input_box41.draw(win)
    input_box42.draw(win)
    input_box43.draw(win)
    input_box44.draw(win)
    input_box45.draw(win)
    input_box46.draw(win)
    input_box47.draw(win)
    input_box48.draw(win)
    input_box49.draw(win)
    input_box51.draw(win)
    input_box52.draw(win)
    input_box53.draw(win)
    input_box54.draw(win)
    input_box55.draw(win)
    input_box56.draw(win)
    input_box57.draw(win)
    input_box58.draw(win)
    input_box59.draw(win)
    input_box61.draw(win)
    input_box62.draw(win)
    input_box63.draw(win)
    input_box64.draw(win)
    input_box65.draw(win)
    input_box66.draw(win)
    input_box67.draw(win)
    input_box68.draw(win)
    input_box69.draw(win)
    input_box71.draw(win)
    input_box72.draw(win)
    input_box73.draw(win)
    input_box74.draw(win)
    input_box75.draw(win)
    input_box76.draw(win)
    input_box77.draw(win)
    input_box78.draw(win)
    input_box79.draw(win)
    input_box81.draw(win)
    input_box82.draw(win)
    input_box83.draw(win)
    input_box84.draw(win)
    input_box85.draw(win)
    input_box86.draw(win)
    input_box87.draw(win)
    input_box88.draw(win)
    input_box89.draw(win)

    win.getMouse() # Pause to view result


    values[0] = input_box1.getText()
    values[1] = input_box2.getText()
    values[2] = input_box3.getText()
    values[3] = input_box4.getText()
    values[4] = input_box5.getText()
    values[5] = input_box6.getText()
    values[6] = input_box7.getText()
    values[7] = input_box8.getText()
    values[8] = input_box9.getText()

    values[9] = input_box11.getText()
    values[10] = input_box12.getText()
    values[11] = input_box13.getText()
    values[12] = input_box14.getText()
    values[13] = input_box15.getText()
    values[14] = input_box16.getText()
    values[15] = input_box17.getText()
    values[16] = input_box18.getText()
    values[17] = input_box19.getText()

    values[18] = input_box21.getText()
    values[19] = input_box22.getText()
    values[20] = input_box23.getText()
    values[21] = input_box24.getText()
    values[22] = input_box25.getText()
    values[23] = input_box26.getText()
    values[24] = input_box27.getText()
    values[25] = input_box28.getText()
    values[26] = input_box29.getText()

    values[27] = input_box31.getText()
    values[28] = input_box32.getText()
    values[29] = input_box33.getText()
    values[30] = input_box34.getText()
    values[31] = input_box35.getText()
    values[32] = input_box36.getText()
    values[33] = input_box37.getText()
    values[34] = input_box38.getText()
    values[35] = input_box39.getText()

    values[36] = input_box41.getText()
    values[37] = input_box42.getText()
    values[38] = input_box43.getText()
    values[39] = input_box44.getText()
    values[40] = input_box45.getText()
    values[41] = input_box46.getText()
    values[42] = input_box47.getText()
    values[43] = input_box48.getText()
    values[44] = input_box49.getText()

    values[45] = input_box51.getText()
    values[46] = input_box52.getText()
    values[47] = input_box53.getText()
    values[48] = input_box54.getText()
    values[49] = input_box55.getText()
    values[50] = input_box56.getText()
    values[51] = input_box57.getText()
    values[52] = input_box58.getText()
    values[53] = input_box59.getText()

    values[54] = input_box61.getText()
    values[55] = input_box62.getText()
    values[56] = input_box63.getText()
    values[57] = input_box64.getText()
    values[58] = input_box65.getText()
    values[59] = input_box66.getText()
    values[60] = input_box67.getText()
    values[61] = input_box68.getText()
    values[62] = input_box69.getText()

    values[63] = input_box71.getText()
    values[64] = input_box72.getText()
    values[65] = input_box73.getText()
    values[66] = input_box74.getText()
    values[67] = input_box75.getText()
    values[68] = input_box76.getText()
    values[69] = input_box77.getText()
    values[70] = input_box78.getText()
    values[71] = input_box79.getText()

    values[72] = input_box81.getText()
    values[73] = input_box82.getText()
    values[74] = input_box83.getText()
    values[75] = input_box84.getText()
    values[76] = input_box85.getText()
    values[77] = input_box86.getText()
    values[78] = input_box87.getText()
    values[79] = input_box88.getText()
    values[80] = input_box89.getText()

    win.getMouse() # Pause to view result
    win.close()    # Close window when done

def initializeBoard():
    drawBoard()
    print("Initializing")
    counter = 0

    for y in range(9):
        for x in range(9):        
            if not values[counter]:
                board[y][x] = 0
            else:
                board[y][x] = int(values[counter])
            counter += 1
        

    #board[0][2] = 6
    #board[0][5] = 1
    #board[0][6] = 8
    #board[0][7] = 4
    #board[0][8] = 9
    #board[1][1] = 3
    #board[2][4] = 2
    #board[2][8] = 6
    #board[3][3] = 4
    #board[3][6] = 3
    #board[3][7] = 2
    #board[4][0] = 4
    #board[4][5] = 3
    #board[5][0] = 6
    #board[5][5] = 8
    #board[6][1] = 1
    #board[6][4] = 6
    #board[6][8] = 3
    #board[7][5] = 5
    #board[7][8] = 4
    #board[8][1] = 2
    #board[8][2] = 9
    #board[8][4] = 7
    #board[8][5] = 4
    #board[8][8] = 5


def possible(y, x, n):
    global board
    for i in range(0, 9):
        if board[y][i] == n :
            return False
    for i in range(0, 9):
        if board[i][x] == n :
            return False
    x0 = (x//3)*3
    y0 = (y//3)*3    
    for i in range(0, 3):
        for j in range(0, 3):
            if board[y0+i][x0+j] == n :
                return False
    return True

def solve():
    global board
    for y in range(9):
        for x in range(9):
            if board[y][x] == 0:
                for n in range(1,10):
                    if possible(y,x,n):
                        board[y][x] = n
                        solve()
                        board[y][x] = 0
                return
    counter = 0
    for y in range(9):
        for x in range(9):
            value[counter] = board[y][x]
            counter += 1
    drawBoardSolution()
    printBoard()
    exit()


def main():
    initializeBoard()
    print(values)
    printBoard()
    print("\n\n")
    solve()

main()





