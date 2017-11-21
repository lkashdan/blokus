# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 07:52:03 2017

@author: LukeK
"""

#imports
import os
os.chdir('C:\\Users\\LukeK\\Documents\\Python Scripts\\Blokus')

import blokusMethods

gameBoard = blokusMethods.Board()



from tkinter import *
 

#-------------- SET UP THE WINDOW FRAME --------------------------------
class launchScreen(Frame):
    #set the initial size of the window please change width and height
    #it uses these values to determine the window size
    #if you are on a resolution that is not 1920x1080

    def __init__(self, master=None, width=0.5, height=0.4):
        Frame.__init__(self, master)
        #pack the frame to cover the whole window
        self.pack(side=TOP, fill=BOTH, expand=YES)
        
        # get screen width and height
        ws = self.master.winfo_screenwidth()
        hs = self.master.winfo_screenheight()

        w = ws*width
        h = ws*height
        # calculate position x, y
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        self.master.geometry('%dx%d+%d+%d' % (w, h, x, y))

        #Make the screen appear on top of everything.
        self.master.overrideredirect(True)
        self.lift()
#Once it has launched do everything in Main
if __name__ == '__main__':
    root = Tk()
    #set the title of the applicaton window
    root.title('Blokus')
    coordinate={}
    def changecolor(row, column, canvas):
        canvas.itemconfig(coordinate[(row, column)], fill='yellow')

#--------------------- GAME STARTED ----------------------------------------
    def gameStart():
        global coordinate
        print("Game Started")
        #get rid of the launch screen elemenets and show the game board
        LaunchScrn.pack_forget()

        #this is where the 20x20 grid is made
        #set up the view of the game board
        def board(view):
            coordinate={}
            w=view.winfo_width()
            h=view.winfo_height()
            gridWidth = w / 20
            gridHeight = h / 20
            rowNumber = 0
            for row in range(20):
                columnNumber = 0
                rowNumber = rowNumber + 1
                for col in range(20):
                        columnNumber = columnNumber + 1
                        rect = view.create_rectangle(col * gridWidth,
                         row * gridHeight,
                         (col+1) * gridWidth,
                         (row+1) * gridHeight,
                         fill = '#ccc')
                         #Sets row, column
                        view.itemconfig(rect, tags=(str(rowNumber), str(columnNumber)))
                        coordinate[(row,col)]=rect
            return coordinate

        #set up the canvas for the game board grid
        viewCanvas = Canvas(root, width=root.winfo_width(), height=root.winfo_height(),bg="#ddd")
        viewCanvas.pack(side=TOP, fill=BOTH,padx=1,pady=1)
        
        #build class of spaces which are available
            #then on each click, reduce spaces
        #build class of pieces that can be used by computer
            #allow for pieces to be used by computer in any direction
        #create player movement. Can't go adjacent to their own pieces (need to store their moves)
        
        #create button that can be used for computer to decide when to play
        
        #when you click on the gameboard this event fires
        def clickOnGameBoard(event):
            if viewCanvas.find_withtag(CURRENT):
                clickSpot = viewCanvas.gettags(CURRENT)
                #print(clickSpot)
                viewCanvas.itemconfig(CURRENT, fill="firebrick")
                viewCanvas.update_idletasks()
                gameBoard.humanPlay(clickSpot)
                                        
        #bind an event when you click on the game board
        viewCanvas.bind("<Button-1>", clickOnGameBoard)
        
        def rightClickOnGameBoard(event):
            if viewCanvas.find_withtag(CURRENT):
                clickSpot = viewCanvas.gettags(CURRENT)
                viewCanvas.itemconfig(CURRENT, fill="yellow")
                viewCanvas.update_idletasks()
                gameBoard.compPlay(clickSpot)
                                                
        #bind an event when you click on the game board to input computerPlay
        viewCanvas.bind("<Button-3>", rightClickOnGameBoard)
        
        def middleClickOnGameBoard(event):
            if viewCanvas.find_withtag(CURRENT):
                clickSpot = viewCanvas.gettags(CURRENT)
                viewCanvas.itemconfig(CURRENT, fill='#ccc')
                viewCanvas.update_idletasks()
                gameBoard.clearPlay(clickSpot)
                print(gameBoard.getGrid())
                
                                
        #bind an event when you click on the game board to input computerPlay
        viewCanvas.bind("<Button-2>", middleClickOnGameBoard)
        
        #when return button is hit, computer play will be made
        def computerPlay(event):
            placements = gameBoard.playPiece(corner = gameBoard.cornerChoice(), blokusPiece = blokusMethods.BlokusPiece.pieceList())
            print(placements)
            print(gameBoard.getGrid())
              
        
        #bind an event when you double click button
        viewCanvas.bind("<Double-Button-1>", computerPlay)
        
        #update the game board after it is done being drawn.
        root.update_idletasks()

        #show the gameboard in the Canvas
        coordinate=board(viewCanvas)
        #changecolor(1, 2, viewCanvas)

        #when you click the quit button it returns you to the launch screen
        def clickToQuit(event):
            viewCanvas.destroy()
            label.pack_forget()
            LaunchScrn.pack(side=TOP, fill=BOTH, expand=YES)

        #sets up the button for the quit
        #quitPath = "images/exit.gif"
        #quitImg = PhotoImage(file=quitPath)
        #label = Label(root, image=quitImg)
        #label.image = quitImg # you need to cache this image or it's garbage collected
        #binds clicking this label to the quit event
        #label.bind("<Button-1>",clickToQuit)
        #label.pack(side=LEFT)




#------------ GAME ENDED --------------------
    def gameEnd():
        #quits the game
        def quitGame():
            print("Game Ended")
            LaunchScrn.after(3000,root.destroy())
        quitGame()

#---------------------------- LAUNCH SCREEN --------------------------------------------
    LaunchScrn = launchScreen(root)
    LaunchScrn.config(bg="#eee")

    b=Button(LaunchScrn,text='start', command=gameStart)
    #photo2=PhotoImage(file="images/start.gif")
    #b.config(image=photo2, width="300", height="50")
    b.pack(side=RIGHT, fill=X, padx=10, pady=10)

    b=Button(LaunchScrn, text='end',command=gameEnd)
    #photo4=PhotoImage(file="images/quit.gif")
    #b.config(image=photo4, width="300", height="50")
    b.pack(side=RIGHT, fill=X, padx=10, pady=10)

    root.mainloop()
    
    gameStart()
    
    