# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 15:55:55 2017

@author: LukeK
"""

import random
import operator

PIECES = [
    ('I1', 2,[2,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]),
    ('I2', 2,[2,1,0,0,0], [0,0,0,0,0], [0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]),
    ('F5', 5,[0,2,3,0,0], [4,1,0,0,0], [0,5,0,0,0],[0,0,0,0,0],[0,0,0,0,0]),
    ('I3', 2,[2,1,1,0,0], [0,0,0,0,0], [0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]),
    ('I4', 2,[2,1,1,1,0], [0,0,0,0,0], [0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]),
    ('I5', 2,[2,1,1,1,1], [0,0,0,0,0], [0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]),
    ('L4', 4,[4,1,2,0,0], [3,0,0,0,0], [0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]),
    ('L5', 4,[2,1,3,0,0], [1,0,0,0,0], [4,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]),
    ('O4', 2,[2,1,0,0,0], [1,1,0,0,0], [0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]),
    ('P5', 4,[4,1,1,2,0], [3,0,0,0,0], [0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]),
    ('Q5', 5,[2,4,0,0,0], [5,1,0,0,0], [3,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]),
    ('S5', 5,[2,1,3,0,0], [0,0,4,5,0], [0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]),
    ('T4', 4,[2,1,3,0,0], [0,4,0,0,0], [0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]),
    ('T5', 4,[2,1,3,0,0], [0,1,0,0,0], [0,4,0,0,0],[0,0,0,0,0],[0,0,0,0,0]),
    ('U5', 5,[2,1,3,0,0], [4,0,5,0,0], [0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]),
    ('V3', 3,[2,3,0,0,0], [1,0,0,0,0], [0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]),
    ('W5', 5,[0,2,3,0,0], [4,5,0,0,0], [1,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]),
    ('X5', 2,[0,2,0,0,0], [1,1,1,0,0], [0,1,0,0,0],[0,0,0,0,0],[0,0,0,0,0]),
    ('Y5', 4,[2,1,1,3,0], [0,4,0,0,0], [0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]),
    ('Z4', 4,[0,2,1,0,0], [4,3,0,0,0], [0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]),
    ('Z5', 5,[2,3,0,0,0], [0,1,0,0,0], [0,4,5,0,0],[0,0,0,0,0],[0,0,0,0,0]),
] 


class BlokusPiece(object):
    
    pieces = 0
    
    _registry = []
    
     
    def __init__(self, name, squares, dim, edges):
        
            self.name = name
                
            self.squares = int(squares)
                    
            self.dim = dim
            
            self.edges = edges
            
            BlokusPiece.pieces += 1
            
            self._registry.append(self)
           
    
    def getDim(self):
        return self.dim
    
    def getSquares(self):
        return self.squares
    
    def getName(self):
        return self.name
    
    def getEdges(self):
        return self.edges
    
    def rotate(self):
        '''rotate the blokus piece 90 degrees clockwise'''
        size = 5
                
        for layer in range(0,2):
            first = layer
            last = size - first - 1
                  
            # Move within a single layer (i.e. element loop).
            for element in range(first, last):
    
                offset = element - first
    
                top = self.dim[first][element]
                right_side = self.dim[element][last]
                bottom = self.dim[last][last-offset]
                left_side = self.dim[last-offset][first]
    
                self.dim[first][element] = left_side
                self.dim[element][last] = top
                self.dim[last][last-offset] = right_side
                self.dim[last-offset][first] = bottom
            
        return self
    
    def mirror(self):
        '''produces mirror dimensions of a blokus piece'''
        first = self.dim[0]
        second = self.dim[1]
        third = self.dim[2]
        fourth = self.dim[3]
        fifth = self.dim[4]
        
        mirror = (fifth, fourth, third, second, first)
        
        self.dim = mirror
                                
        return self
    
    def pieceList():
        '''
        randomly arrange the registry for choosing pieces. 
        will be used in the Board.playPiece method        
        '''
        pieceList = []
        #code to get a list of the piece name and squares via _registry
        for i in BlokusPiece._registry:
            pieceList.append([i.getSquares(), i.getName(), i, i.getEdges()])
                
        #randomly arrange all squares
        from random import shuffle
        shuffle(pieceList)

        #code to sort by squares in descending order
        pieceList.sort(reverse = True, key=lambda x: x[0])
        
        return pieceList
    
    def removeReg(instance):
        '''remove a blokus piece from the registry'''
        for i in BlokusPiece._registry:
            if instance == i:
                BlokusPiece._registry.remove(i)
                break
        return None
    
objs = [BlokusPiece(name = PIECES[i][0], squares = PIECES[i][0][1], dim = PIECES[i][2:], edges = PIECES[i][1]) for i in range(len(PIECES))]
        
class Board(BlokusPiece):
            
    #create new 20x20 grid of zeroes
    grid = []
    
    for i in range(20):
        grid.append([0])
        for j in range(19):
            grid[i].append(0)
    
    def __init__(self):
        self.grid = Board.grid
            
    def getGrid(self):
        return self.grid
    
    def getRegistry(self):
        return self._registry
    
    def humanPlayer1(self, click):
        '''for use with tkinter gui. For human player's moves.
        Will take left click in gui and add a '2' to the board's grid at the coordinates that were clicked
        since tkinter grid goes from 1 to 20 instead of 0 to 19, subtract coords by 1
        '''
        coordinates = [int(click[0])-1, int(click[1])-1]
        print(coordinates)
        self.grid[coordinates[0]][coordinates[1]] = 2
        
    def humanPlayer2(self, click):
        '''for use with tkinter gui. For human player's moves.
        Will take left click in gui and add a '2' to the board's grid at the coordinates that were clicked
        since tkinter grid goes from 1 to 20 instead of 0 to 19, subtract coords by 1
        '''
        coordinates = [int(click[0])-1, int(click[1])-1]
        print(coordinates)
        self.grid[coordinates[0]][coordinates[1]] = 3
        
    def humanPlayer3(self, click):
        '''for use with tkinter gui. For human player's moves.
        Will take left click in gui and add a '2' to the board's grid at the coordinates that were clicked
        since tkinter grid goes from 1 to 20 instead of 0 to 19, subtract coords by 1
        '''
        coordinates = [int(click[0])-1, int(click[1])-1]
        print(coordinates)
        self.grid[coordinates[0]][coordinates[1]] = 4
        
    def compPlay(self, click):
        '''for use with tkinter gui. For computer player's moves.
        Will take right click in gui and add a '1' to the board's grid at the coordinates that were clicked
        since tkinter grid goes from 1 to 20 instead of 0 to 19, subtract coords by 1
        '''
        coordinates = [int(click[0])-1, int(click[1])-1]
        print(coordinates)
        self.grid[coordinates[0]][coordinates[1]] = 1
    
    def clearPlay(self, click):
        '''To alleviate mistakes, clearPlay will allow a refresh of a square
        since tkinter grid goes from 1 to 20 instead of 0 to 19, subtract coords by 1
        '''
        coordinates = [int(click[0])-1, int(click[1])-1]
        print(coordinates)
        self.grid[coordinates[0]][coordinates[1]] = 0
        
    def pieceList(self):
        '''
        randomly arrange the registry for choosing pieces. 
        will be used in the Board.playPiece method        
        '''
        pieceList = []
        #code to get a list of the piece name and squares via _registry
        for i in self._registry:
            pieceList.append([i.getSquares(), i.getName(), i, i.getEdges()])
                
        #randomly arrange all squares
        from random import shuffle
        shuffle(pieceList)

        #code to sort by squares in descending order
        pieceList.sort(reverse = True, key=lambda x: x[0])
        
        return pieceList
    
    def playPiece(self, corner, blokusPiece, pieceCounter = 0, cornerCounter = 0):
        '''this module puts together one move to play on the Board. Combines other modules
        
        blokusPiece is taken from the BlokusPiece.piecelist. It includes three items per piece. 
        The third item is the instance data.
        
        pieceCounter variable will be used at the bottom for recursive calls to get new blokusPieces
        
        cornerCounter variable will be used at the bottom for recursive calls to get new corners to play off of
        '''
        
        placements = Board.pieceAlign(blokusPiece[pieceCounter][2], corner[cornerCounter], 2)
        
        if Board.pieceFit(self, placements):
            
                #print('piece fits!')
                #fit piece onto 20x20 grid
                #mount piece onto grid
                for i in range(len(placements)):
                    self.grid[placements[i][0]][placements[i][1]] = 1
            
                #remove blokus piece
                #Board.removeReg(blokusPiece[pieceCounter][2])
                
                return placements, blokusPiece[pieceCounter][2]
        
        #if the piece doesn't fit, try rotating the piece to see if it works. Rotate three times.
        else:
            
            for edgeCount in range(2,blokusPiece[pieceCounter][3]+1):
                
                #on the second run through all the rotations, going to mirror the piece to get more fit options for asymmetrical pieces
                for m in range(0,2):
                    
                    if m%2 == 1:
                        blokusPiece[pieceCounter][2].mirror()
                    
                    for i in range(0,4):
                                                       
                        placements = Board.pieceAlign(blokusPiece[pieceCounter][2].rotate(), corner[cornerCounter], edgeCount)
                        
                        if Board.pieceFit(self, placements):
                            
                            #fit piece onto 20x20 grid
                            #mount piece onto grid
                            for j in range(len(placements)):
                                self.grid[placements[j][0]][placements[j][1]] = 1
                        
                            #remove blokus piece
                            #Board.removeReg(blokusPiece[pieceCounter][2])
                            
                            return placements, blokusPiece[pieceCounter][2]
       
                      
        #in the event that the piece doesn't fit after being rotated, get a new piece to try to fit in corner
        #While not an iron clad rule, it's often best practice to play the largest pieces when you can.
        #as a result, if the next piece is going to move down in size, it would preferable to look for a new corner
        #additionally, in starting a new corner, revert back to the top of the blokus piecelist
        
        #print('pieceCounter', pieceCounter, blokusPiece[pieceCounter][1])
        if blokusPiece[pieceCounter+1][0] < blokusPiece[pieceCounter][0]:
        
            #if corners are still available, continue to try and place biggest pieces in board
            if len(corner) > cornerCounter+1:
                return Board.playPiece(self, corner = corner, blokusPiece = blokusPiece, pieceCounter = 0, cornerCounter = cornerCounter+1)
            #if the corners run dry, go back to the first corner and start trying to play smaller pieces
            else:
                #to remove an infinite loop, blokusPiece will be reduced to only the smaller sized squares. Otherwise, the recursion call on line 243 will revert back to the biggest squares and work through the same process
                
                blokusPiece = blokusPiece[pieceCounter+1:]
                #print('blokusPiece line 269', blokusPiece)
                return Board.playPiece(self, corner = corner, blokusPiece = blokusPiece, pieceCounter = 0, cornerCounter = 0)
                            
        else:
            return Board.playPiece(self, corner = corner, blokusPiece = blokusPiece, pieceCounter = pieceCounter+1, cornerCounter = cornerCounter)
            
        return None
    
    def playPieceMiddle(self, corner, blokusPiece, movesList, backupMovesList, cornerCounter = 0):
        '''Plays a five square piece on the board. Iterates one corner at a time.
        A threshold is set for what move is playable. If a move is playable, the cpu will play it. 
        If no moves reach the threshold for an acceptable move, the cpu will play the best move based on how the moves are sorted.
        '''
        blokusFives = blokusPiece[:-9]
        print('top of function. {}'.format(cornerCounter))
        #print('movesList {}, backupMovesList {}'.format(movesList, backupMovesList))
         
        for item in blokusFives: 
            
            #store the blokus piece currently worked on so it can be removed when chosen
            blokusItem = item
            
            for edgeCount in range(2,item[3]+1):
                        
                    #on the second run through all the rotations, going to mirror the piece to get more fit options for asymmetrical pieces
                    for m in range(0,2):
                        
                        if m%2 == 1:
                            item[2].mirror()
                            
                        for i in range(0,4):
                            
                            item[2].rotate()
                            
                            placements = Board.pieceAlign(item[2], corner[cornerCounter], edgeCount)
                            
                            if Board.pieceFit(self, placements):
                                
                                hug1, hug2 = Board.hugging(self, placements, Board.playableCorners(self, placements))
                                
                                if hug1[0] == True:
                                    try:
                                        if hug2[0][0] > 0:
                                            #print('hug1:', hug1)
                                            #print('hug2:', hug2)
                                            playableCorners = len(hug2)
                                            #print('length of hug2, and hug2 and placements{}{}{}'.format(len(hug2), hug2, placements))
                                            
                                            huggedCorners = 0
                                            doubleHugs = 0
                                            huggedSpace = 0
                                            
                                            for j in hug2:
                                                if j[0] == 2:
                                                    #only count a hug if free space is greater than 10
                                                    if j[1] > 10:
                                                        huggedCorners += 1
                                                        doubleHugs += 1
                                                        if j[1] > huggedSpace:
                                                            huggedSpace = j[1]
                                                elif j[0] == 1:
                                                    #only count a hug if free space is greater than 10
                                                    if j[1] > 10:
                                                        huggedCorners += 1
                                                        if j[1] > huggedSpace:
                                                            huggedSpace = j[1]
                                            
                                            movesList.append((placements, doubleHugs, huggedCorners, playableCorners, huggedSpace, blokusItem[2]))
                                        #as a backup, store non-hugging moves as a backup
                                        else:
                                            squaresTouch = hug1[1]
                                            playableCorners = len(hug2)
                                            playSpace = 0
                                            for k in hug2[1:]:
                                                playSpace += k[1]
                                            backupMovesList.append([placements, playableCorners, playSpace, squaresTouch, blokusItem[2]])
                                        
                                    except TypeError:
                                        if hug2[0] > 0:
                                    
                                            playableCorners = 1
                                            
                                            huggedCorners = 0
                                            doubleHugs = 0
                                            huggedSpace = 0
                                            
                                            for l in hug2[1:]:
                                                if l[0] == 2:
                                                    #only count a hug if free space is greater than 10
                                                    if l[1] > 10:
                                                        huggedCorners += 1
                                                        doubleHugs += 1
                                                        if l[1] > huggedSpace:
                                                            huggedSpace = l[1]
                                                elif l[0] == 1:
                                                    #only count a hug if free space is greater than 10
                                                    if l[1] > 10:
                                                        huggedCorners += 1
                                                        if l[1] > huggedSpace:
                                                            huggedSpace = l[1]
                                            
                                            movesList.append([placements, doubleHugs, huggedCorners, playableCorners, huggedSpace, blokusItem[2]])
                                        else:
                                            squaresTouch = hug1[1]
                                            playableCorners = 1
                                            playSpace = 0
                                            for m in hug2[1:]:
                                                playSpace += m[1]
                                            backupMovesList.append([placements, playableCorners, playSpace, squaresTouch, blokusItem[2]])
                                        
                                                
                                    
        #once the iteration is done, sort the movesList.
        #movesList will prioritize 1) moves with a multi-hug(meaning they hug two squares at once),  
        # 2) moves that have multiple hugged corners, 3) moves with most Free Space, 
        # 4) moves with most playable corners
        #print(movesList)
        #print(backupMovesList)
        if len(movesList) > 0:
            
            
            
            movesList = sorted(movesList, reverse = True, key = lambda x: (x[1], x[2], x[3], x[4]))
            print('hugged moves, {}'.format(cornerCounter))
            #print(movesList)
            
            if cornerCounter < 3:
                                
                #if the move has a double hug or multiple hugged corners, go ahead and play it. Otherwise, move on to the next corner and look for a better placement
                if movesList[0][1] > 0 or movesList[0][2] > 1:
                    
                
                    #place on board
                    for placement in movesList[0][0]:
                        self.grid[placement[0]][placement[1]] = 1
                             
                    return movesList[0][0], movesList[0][5]    
            
                elif len(corner) > cornerCounter+1:
                    
                    
                    print('but no good hugged moves, {}'.format(cornerCounter))
                    return Board.playPieceMiddle(self, corner = corner, blokusPiece = blokusPiece, movesList = movesList, backupMovesList = backupMovesList, cornerCounter = cornerCounter + 1)
                #in the event that there are no more corners to test, return the best move based on the scoring method
                else:
                    #place on board
                    print('place on board, no more corners')
                    for placement in movesList[0][0]:
                        self.grid[placement[0]][placement[1]] = 1
                             
                    return movesList[0][0], movesList[0][5]
            
            else:
                #if the move has a double hug or multiple hugged corners, go ahead and play it. Otherwise, move on to the next corner and look for a better placement
                if movesList[0][2] > 0:
                    
                
                    #place on board
                    for placement in movesList[0][0]:
                        self.grid[placement[0]][placement[1]] = 1
                             
                    return movesList[0][0], movesList[0][5]    
            
                elif len(corner) > cornerCounter+1:
                    
                    
                    print('but no good hugged moves, {}'.format(cornerCounter))
                    return Board.playPieceMiddle(self, corner = corner, blokusPiece = blokusPiece, movesList = movesList, backupMovesList = backupMovesList, cornerCounter = cornerCounter + 1)
                #in the event that there are no more corners to test, return the best move based on the scoring method
                else:
                    #place on board
                    for placement in movesList[0][0]:
                        self.grid[placement[0]][placement[1]] = 1
                             
                    return movesList[0][0], movesList[0][5]
            
        else:
            backupMovesList = sorted(backupMovesList, reverse = True, key = lambda x: (x[1],x[2], x[3]))
            
            print('no hugged moves, {}'.format(cornerCounter))
            
            if len(corner) > cornerCounter+1:
                
                return Board.playPieceMiddle(self, corner = corner, blokusPiece = blokusPiece, movesList = movesList, backupMovesList = backupMovesList, cornerCounter = cornerCounter + 1)
            
            else:
                #place on board
                print('place on board, no more corners')
                for placement in backupMovesList[0][0]:
                    self.grid[placement[0]][placement[1]] = 1
                         
                return backupMovesList[0][0], backupMovesList[0][4]     
                                
        return None, None
    
    def playPieceEnd(self, corner, blokusPiece, movesList, backupMovesList, badMovesList, cornerCounter = 0):
        '''Operates similarly to playPieceMiddle, with a couple of tweaks. 
        It finds moves for all of the remaining pieces and it has different thresholds for what move is playable.
        movesList stores moves that fit onto the board, have playable corners and also have hugged corners
        backupMovesList stores moves that fit onto the board, have playable corners, but no hugged corners
        badMovesList stores moves that fit onto the board but have no playable corners. They are dead end moves saved for the end of the game.
        '''
                
        print('top of function. {}'.format(cornerCounter))
        #print('movesList {}, backupMovesList {}'.format(movesList, backupMovesList))
         
        for item in blokusPiece: 
            
            #store the blokus piece currently worked on so it can be removed when chosen
            blokusItem = item
            
            for edgeCount in range(2,item[3]+1):
                        
                    #on the second run through all the rotations, going to mirror the piece to get more fit options for asymmetrical pieces
                    for m in range(0,2):
                        
                        if m%2 == 1:
                            item[2].mirror()
                            
                        for i in range(0,4):
                            
                            item[2].rotate()
                            
                            placements = Board.pieceAlign(item[2], corner[cornerCounter], edgeCount)
                            
                            if Board.pieceFit(self, placements):
                                
                                hug1, hug2 = Board.hugging(self, placements, Board.playableCorners(self, placements))
                                
                                if hug1[0] == True:
                                    try:
                                        if hug2[0][0] > 0:
                                            #print('hug1:', hug1)
                                            #print('hug2:', hug2)
                                            playableCorners = len(hug2)
                                            #print('length of hug2, and hug2 and placements{}{}{}'.format(len(hug2), hug2, placements))
                                            
                                            huggedCorners = 0
                                            doubleHugs = 0
                                            huggedSpace = 0
                                            
                                            for j in hug2:
                                                if j[0] == 2:
                                                    #only count a hug if free space is greater than 10
                                                    if j[1] > 10:
                                                        huggedCorners += 1
                                                        doubleHugs += 1
                                                        if j[1] > huggedSpace:
                                                            huggedSpace = j[1]
                                                elif j[0] == 1:
                                                    #only count a hug if free space is greater than 10
                                                    if j[1] > 10:
                                                        huggedCorners += 1
                                                        if j[1] > huggedSpace:
                                                            huggedSpace = j[1]
                                            
                                            movesList.append((placements, len(placements), doubleHugs, huggedCorners, playableCorners, huggedSpace, blokusItem[2]))
                                        #as a backup, store non-hugging moves as a backup
                                        else:
                                            squaresTouch = hug1[1]
                                            playableCorners = len(hug2)
                                            playSpace = 0
                                            for k in hug2:
                                                playSpace += k[1]
                                            backupMovesList.append([placements, len(placements), playableCorners, playSpace, squaresTouch, blokusItem[2]])
                                        
                                    except TypeError:
                                        if hug2[0] > 0:
                                    
                                            playableCorners = 1
                                            
                                            huggedCorners = 0
                                            doubleHugs = 0
                                            huggedSpace = 0
                                            
                                            for l in hug2[1:]:
                                                if l[0] == 2:
                                                    #only count a hug if free space is greater than 10
                                                    if l[1] > 10:
                                                        huggedCorners += 1
                                                        doubleHugs += 1
                                                        if l[1] > huggedSpace:
                                                            huggedSpace = l[1]
                                                elif l[0] == 1:
                                                    #only count a hug if free space is greater than 10
                                                    if l[1] > 10:
                                                        huggedCorners += 1
                                                        if l[1] > huggedSpace:
                                                            huggedSpace = l[1]
                                            
                                            movesList.append([placements, len(placements), doubleHugs, huggedCorners, playableCorners, huggedSpace, blokusItem[2]])
                                        else:
                                            squaresTouch = hug1[1]
                                            playableCorners = 1
                                            playSpace = 0
                                            for m in hug2:
                                                playSpace += m[1]
                                            backupMovesList.append([placements, len(placements), playableCorners, playSpace, squaresTouch, blokusItem[2]])
                                else:
                                    badMovesList.append([placements, blokusItem[2], len(placements)])
        
        #print('movesList', movesList)
        #print('backupMovesList', backupMovesList)
                                            
        if len(movesList) > 0:
            
            if cornerCounter < 6:
                
                movesList = sorted(movesList, reverse = True, key = lambda x: (x[1], x[2], x[3], x[4], x[5]))
                print('hugged moves, {}'.format(cornerCounter))
                #print('movesList,', movesList[0:4])
                #print(movesList)
                                
                #if the move is a 5 piece, go ahead and play it. 
                if movesList[0][1] == 5:
                                    
                    #place on board
                    for placement in movesList[0][0]:
                        self.grid[placement[0]][placement[1]] = 1
                             
                    return movesList[0][0], movesList[0][6]    
                
                #if the move is a four piece, look for at least two playable corners and a hugged corner
                elif movesList[0][1] == 4 and movesList[0][3] > 0 and movesList[0][4] > 1:
                    
                    
                    #place on board
                    for placement in movesList[0][0]:
                        self.grid[placement[0]][placement[1]] = 1
                             
                    return movesList[0][0], movesList[0][6]
                
                elif len(corner) > cornerCounter+1:
                    
                    
                    print('but no good hugged moves, {}'.format(cornerCounter))
                    return Board.playPieceEnd(self, corner = corner, blokusPiece = blokusPiece, movesList = movesList, backupMovesList = backupMovesList, badMovesList = badMovesList, cornerCounter = cornerCounter + 1)
                #in the event that there are no more corners to test, return the best move based on the scoring method
                else:
                    #place on board
                    print('place on board, no more corners')
                    for placement in movesList[0][0]:
                        self.grid[placement[0]][placement[1]] = 1
                             
                    return movesList[0][0], movesList[0][6]
            
            else:
                #print('movesList,', movesList[0:4])
                #if the move is a 5 piece, go ahead and play it. 
                if movesList[0][1] == 5:
                                    
                    #place on board
                    for placement in movesList[0][0]:
                        self.grid[placement[0]][placement[1]] = 1
                             
                    return movesList[0][0], movesList[0][6]    
                
                #if the move is a four piece, look for at least one playable corner and play it
                elif movesList[0][1] == 4 and movesList[0][4] > 0:
                                       
                    #place on board
                    for placement in movesList[0][0]:
                        self.grid[placement[0]][placement[1]] = 1
                             
                    return movesList[0][0], movesList[0][6]
                
                #if it's a 3 piece but has two playable corners, play it.
                elif movesList[0][1] == 3 and movesList[0][4] > 2:
                    #place on board
                    for placement in movesList[0][0]:
                        self.grid[placement[0]][placement[1]] = 1
                             
                    return movesList[0][0], movesList[0][6]
                
                #if it's a 1 or 2 piece but has at least 6 play space, play it.
                elif movesList[0][1] in [1,2] and movesList[0][5] >= 6:
                    #place on board
                    for placement in movesList[0][0]:
                        self.grid[placement[0]][placement[1]] = 1
                             
                    return movesList[0][0], movesList[0][6]       
            
                elif len(corner) > cornerCounter+1:
                    
                    
                    print('but no good hugged moves, {}'.format(cornerCounter))
                    return Board.playPieceEnd(self, corner = corner, blokusPiece = blokusPiece, movesList = movesList, backupMovesList = backupMovesList, badMovesList = badMovesList, cornerCounter = cornerCounter + 1)
                #in the event that there are no more corners to test, return the best move based on the scoring method
                else:
                    #place on board
                    for placement in movesList[0][0]:
                        self.grid[placement[0]][placement[1]] = 1
                             
                    return movesList[0][0], movesList[0][6]
            
        elif len(backupMovesList) > 1:
            backupMovesList = sorted(backupMovesList, reverse = True, key = lambda x: (x[1],x[2], x[3], x[4]))
            
            print('no hugged moves, {}'.format(cornerCounter))
            #print(backupMovesList[0:3])
            
            #play five piece if it's playable                      
            if backupMovesList[0][1] == 5:
                #place on board
                for placement in backupMovesList[0][0]:
                    self.grid[placement[0]][placement[1]] = 1
                         
                return backupMovesList[0][0], backupMovesList[0][5]
            
            elif len(corner) > cornerCounter + 1:
                
                return Board.playPieceEnd(self, corner = corner, blokusPiece = blokusPiece, movesList = movesList, backupMovesList = backupMovesList, badMovesList = badMovesList, cornerCounter = cornerCounter + 1)
                             
            else:
                
                #place best move on board
                for placement in backupMovesList[0][0]:
                    self.grid[placement[0]][placement[1]] = 1
                         
                return backupMovesList[0][0], backupMovesList[0][5]
            
        #if there were no moves w/ playable corners (only badMovesList has options),
        #go on to next corner unless there are no more corners. In that case, play a move        
        else:
            print('only bad moves', cornerCounter)
            if len(corner) > cornerCounter + 1:
            
                return Board.playPieceEnd(self, corner = corner, blokusPiece = blokusPiece, movesList = movesList, backupMovesList = backupMovesList, badMovesList = badMovesList, cornerCounter = cornerCounter + 1)
                          
            else:
                if len(badMovesList) > 1:
                    
                    badMovesList = sorted(badMovesList, reverse = True, key = lambda x: (x[2]))
                
                    #place first move on board. The moves are sorted by piece size.
                    for placement in badMovesList[0][0]:
                        self.grid[placement[0]][placement[1]] = 1
                             
                    return badMovesList[0][0], badMovesList[0][1]
                
                elif len(badMovesList) == 1:
                    #place only move on board
                    for placement in badMovesList[0]:
                        self.grid[placement[0]][placement[1]] = 1
                             
                    return badMovesList[0], badMovesList[1]
                
                                  
        return None, None
    
    def playPieceConsolidated(self):
        '''combines playPiece, playPieceMiddle and playPieceEnd to form Anna Gen 2 play.
        playPiece is used in the first 4 turns, playPieceMiddle is used for turns 5-9,
        and playPieceEnd is used for the remainder of the game.
        
        '''
        
        turn = 22 - len(Board._registry)
        print('turn:', turn)
        #print(Board.pieceList(self))
        if turn < 5:
            compMove, piecePlayed = Board.playPiece(self, corner = Board.cornerChoice(self), blokusPiece = Board.pieceList(self))
            if compMove == None:
                return 'Game Over'
            else:
                print(piecePlayed.getName())
                Board.removeReg(piecePlayed)
                return compMove
        elif turn < 10:
            compMove, piecePlayed = Board.playPieceMiddle(self, corner = Board.cornerChoiceRandom(self), blokusPiece = Board.pieceList(self), movesList = [], backupMovesList = [])
            if compMove == None:
                return 'Game Over'
            else:
                print(piecePlayed.getName())
                Board.removeReg(piecePlayed)
                return compMove
        else:
            compMove, piecePlayed = Board.playPieceEnd(self, corner = Board.cornerChoiceRandom(self), blokusPiece = Board.pieceList(self), movesList = [], backupMovesList = [], badMovesList = [])
            if compMove == None:
                return 'Game Over'
            else:
                print(piecePlayed)
                Board.removeReg(piecePlayed)
                return compMove   
               
        return 'Test function'
    
    def playableCorners(self, placements):
        '''playableCorners Method will return the playable corners for a potential move
        it will also return the coordinates of the played move that produce the playable corner, and the direction of the corner'''
        #break placements down so it only includes the coordinates, not the name of the piece
        
        cornerSpots = []
        direction = ['NE', 'SE', 'NW', 'SW']
        
        for i in range(len(placements)):
                for d in direction:
                    if Board.cornerCheck(self, placements[i], d, placements):
                        
                        if Board.adjacentCheckPlayable(self, placements[i], d, placements):
                            if d == 'NE':
                                cornerSpots.append([placements[i][0]-1, placements[i][1]+1, d])
                            elif d == 'SE':
                                cornerSpots.append([placements[i][0]+1, placements[i][1]+1, d])
                            elif d == 'NW':
                                cornerSpots.append([placements[i][0]-1, placements[i][1]-1, d])
                            else:
                                cornerSpots.append([placements[i][0]+1, placements[i][1]-1, d])
        
        #remove duplicate playable corners
        foundCorners = []
        finalPlayableCorners = []
        for spot in cornerSpots:
            if [spot[0],spot[1]] not in foundCorners:
                foundCorners.append([spot[0],spot[1]])
                finalPlayableCorners.append(spot)
            
        return finalPlayableCorners 
    
    
    def hugging(self, placements, playableCorners):
        '''hugging refers to a type piece placement where the played piece is adjacent to the opponent 
        and the corner that opens up from the played piece is also adjacent to the opponent.
        Takes in a potential played piece on the board that fits on the board
        Hugging method will return true/false on whether or not it is hugging
        Hugging method will return how much space is available for next move
        Hugging method will return how many corners are hugging.
        Hugging method will return how many squares hug an opponent
        '''
        hugging = []
        #if playable corners is empty, return False
        if len(playableCorners) == 0:
            hugging.append(False)
            
        else:
            hugging.append(True)
            
        #identify how many squares of the potential placement will be touching an opponent
        #use squaresTouch method to get # of squares touching opponents. 
        squaresTouchCount = Board.squaresTouch(self, placements)
        
        #add squaresTouchCount to the hugging data and then return if there's no playable corner
        hugging.append(squaresTouchCount)
        
        if hugging[0] == False:
            return hugging, None
        
        #for each playable corner, identify if it is hugging. count the hugs and store the hugged corners
        
        hugCorners = []
        
        for corner in playableCorners:
            #subsetting based on potential corner. Hence twos and threes in brackets 
            #looking for whether or not there are one or two hugs for each playable corner. 
            
            if corner[2] == 'NE':
                
                if self.grid[corner[0]][corner[1]-1] != 0 and self.grid[corner[0]][corner[1]] == self.grid[corner[0]][corner[1]-1]:
                    
                    freeSpace = Board.playSpace(self, [corner[0], corner[1]],{})
                    
                    hugCorners.append([2, len(freeSpace), corner[0], corner[1]])
                    
                elif self.grid[corner[0]][corner[1]-1] != 0 or self.grid[corner[0]][corner[1]] != 0:
                    freeSpace = Board.playSpace(self, [corner[0], corner[1]],{})
                    hugCorners.append([1, len(freeSpace), corner[0], corner[1]])
                    
                else:
                    freeSpace = Board.playSpace(self, [corner[0], corner[1]],{})
                    hugCorners.append([0, len(freeSpace), corner[0], corner[1]])
            
            elif corner[2] == 'NW':
                
                if self.grid[corner[0]][corner[1]+1] != 0 and self.grid[corner[0]][corner[1]] == self.grid[corner[0]][corner[1]+1]:
                    freeSpace = Board.playSpace(self, [corner[0], corner[1]],{})
                    hugCorners.append([2, len(freeSpace), corner[0], corner[1]])
                    
                elif self.grid[corner[0]][corner[1]+1] != 0 or self.grid[corner[0]][corner[1]] != 0:
                    freeSpace = Board.playSpace(self, [corner[0], corner[1]],{})
                    hugCorners.append([1, len(freeSpace), corner[0], corner[1]])
                
                else:
                    freeSpace = Board.playSpace(self, [corner[0], corner[1]],{})
                    hugCorners.append([0, len(freeSpace), corner[0], corner[1]])
            
            elif corner[2] == 'SW':
                
                if self.grid[corner[0]][corner[1]+1] != 0 and self.grid[corner[0]][corner[1]] == self.grid[corner[0]][corner[1]+1]:
                    freeSpace = Board.playSpace(self, [corner[0], corner[1]],{})
                    hugCorners.append([2, len(freeSpace), corner[0], corner[1]])
                    
                elif self.grid[corner[0]][corner[1]+1] != 0 or self.grid[corner[0]][corner[1]] != 0:
                    freeSpace = Board.playSpace(self, [corner[0], corner[1]],{})
                    hugCorners.append([1, len(freeSpace), corner[0], corner[1]])
                    
                else:
                    freeSpace = Board.playSpace(self, [corner[0], corner[1]],{})
                    hugCorners.append([0, len(freeSpace), corner[0], corner[1]])
                    
            else:
                #'SE'
                if self.grid[corner[0]][corner[1]-1] != 0 and self.grid[corner[0]][corner[1]] == self.grid[corner[0]][corner[1]-1]:
                    freeSpace = Board.playSpace(self, [corner[0], corner[1]],{})
                    hugCorners.append([2, len(freeSpace), corner[0], corner[1]])
                    
                elif self.grid[corner[0]][corner[1]-1] != 0 or self.grid[corner[0]][corner[1]] != 0:
                    freeSpace = Board.playSpace(self, [corner[0], corner[1]],{})
                    hugCorners.append([1, len(freeSpace), corner[0], corner[1]])
                else:
                    freeSpace = Board.playSpace(self, [corner[0], corner[1]],{})
                    hugCorners.append([0, len(freeSpace), corner[0], corner[1]])
        
        #sort the corners based on hugs, then play space
        
        hugCorners.sort(reverse = True, key = operator.itemgetter(0,1))
        
        return hugging, hugCorners
        
        
        
    def playSpace(self, playableCorner, playSpaceDict = {}):
        '''method takes in playbleCorners and is utilized within the hugging method. Specifically takes in [playableCorners[2], playableCorners[3]] and {} for playSpaceDict
        Purpose is to gauge how much space is available for play from a potential corner
        method will look for the total amount of open, playable space from a playable corner
        does not consider space that is not in the direct open space that could be accessed. For a future generation
        '''
        #print(1, playableCorner, playSpaceDict.keys())
        if len(playSpaceDict) == 0:
            playSpaceDict[(playableCorner[0], playableCorner[1])] = 1
        #for each playableSpace, starting w/ playableCorner, scan if there's playable space in each adjacent direction
        
        directions = ['N', 'S', 'E', 'W']
        
        #loop through each direction, check if the adjacent space is open, and it has no adjacent square played by Anna
        for d in directions:
            if Board.spaceCheck(self, playableCorner, d):
                    
                if d == 'N':
                    
                    if (playableCorner[0]-1, playableCorner[1]) not in playSpaceDict.keys():
                        
                        
                        playSpaceDict[(playableCorner[0]-1, playableCorner[1])] = 1
                        
                        #print(2, playSpaceDict.keys())
                        
                        #recursive call
                        recurSpaces = Board.playSpace(self, [playableCorner[0]-1, playableCorner[1]], playSpaceDict)
                    
                        for item in recurSpaces:
                            if item not in playSpaceDict:
                                playSpaceDict[item] = 1
                
                elif d == 'S':
                    
                    if (playableCorner[0]+1, playableCorner[1]) not in playSpaceDict.keys():
                        
                        playSpaceDict[(playableCorner[0]+1, playableCorner[1])] = 1
                        
                        #print(3, playSpaceDict.keys())
                        
                        #recursive call
                        recurSpaces = Board.playSpace(self, [playableCorner[0]+1, playableCorner[1]], playSpaceDict)
                    
                        for item in recurSpaces:
                            if item not in playSpaceDict:
                                playSpaceDict[item] = 1
                
                
                elif d=='W':
                    
                    if (playableCorner[0], playableCorner[1]-1) not in playSpaceDict.keys():
                        
                        playSpaceDict[(playableCorner[0], playableCorner[1]-1)] = 1
                        
                        #print(4, playSpaceDict.keys())
                        #recursive call
                        recurSpaces = Board.playSpace(self, [playableCorner[0], playableCorner[1]-1], playSpaceDict)
                    
                        for item in recurSpaces:
                            if item not in playSpaceDict:
                                playSpaceDict[item] = 1
                
                elif d == 'E':
                    
                    if (playableCorner[0], playableCorner[1]+1) not in playSpaceDict.keys():
                        
                        playSpaceDict[(playableCorner[0], playableCorner[1]+1)] = 1
                        
                        #print(5, playSpaceDict.keys())
                        #recursive call
                        recurSpaces = Board.playSpace(self, [playableCorner[0], playableCorner[1]+1], playSpaceDict)
                    
                        for item in recurSpaces:
                            if item not in playSpaceDict:
                                playSpaceDict[item] = 1
                    
        #print(6, playableCorner, playSpaceDict.keys())
        return playSpaceDict
    
    def squaresTouch(self, placements):
        '''used in the hugging method to determine how many squares of the potential played piece would touch an opponent's square.
        each square could touch an opponent as many as three times.
        for placements input, make sure to enter placements into function call
        '''
        direction = ['E', 'W', 'N', 'S']
        squaresTouch = 0
        opponent = [2,3,4]
        
        for coord in placements:
            
            for d in direction:
                
                if d == 'E':
                    try:
                
                        if self.grid[coord[0]][coord[1]+1] in opponent:
                            squaresTouch += 1
                            
                    except IndexError:
                        pass
                elif d == 'W':
                    try:
                
                        if self.grid[coord[0]][coord[1]-1] in opponent:
                            squaresTouch += 1
                            
                    except IndexError:
                        pass
                elif d == 'N':
                    try:
                
                        if self.grid[coord[0]-1][coord[1]] in opponent:
                            squaresTouch += 1
                            
                    except IndexError:
                        pass
                else:
                    try:
                
                        if self.grid[coord[0]+1][coord[1]] in opponent:
                            squaresTouch += 1
                            
                    except IndexError:
                        pass
                    
        return squaresTouch
      
    
    def cornerChoice(self):
        '''
        Chooses the corner where the computer will play.
        First play is at the corner of the board. Any following play 
        requires piece to be placed diagonal to an existing played spot
        
        rank is an input to choose the rank of the largest average row and column total
        e.g. choosing rank 1 will pick the corner furthest from the starting point
        each successive rank value corresponds to the order of the row and corner averages
        '''
        if self.grid[0][0] == 0:
            return [[0,0]]
        else:
        #only deal with pieces played by computer for now. 
        #ignore pieces played by opponents
        
            #find points that contain a 1 and then sort them by largest average value
            #for starters, return the corner furthest from initial play spot
            playedSpots = []
            for i in range(20):
                for j in range(20):
                    if self.grid[i][j] == 1:
                        playedSpots.append([i, j, (i+j)/2])
                        
            #print('playedSpots', playedSpots)
            
            
            #for each played spot, produce as many corner locations that are not adjacent to any existing pieces
            cornerSpots = []
            direction = ['NE', 'SE', 'NW', 'SW']
            for i in range(len(playedSpots)):
                for d in direction:
                    if Board.cornerCheck(self, playedSpots[i], d, placements = []):
                        
                        if Board.adjacentCheck(self, playedSpots[i], d):
                            if d == 'NE':
                                cornerSpots.append([playedSpots[i][0]-1, playedSpots[i][1]+1, ((playedSpots[i][0]-1) + (playedSpots[i][1]+1))/2])
                            elif d == 'SE':
                                cornerSpots.append([playedSpots[i][0]+1, playedSpots[i][1]+1, ((playedSpots[i][0]+1) + (playedSpots[i][1]+1))/2])
                            elif d == 'NW':
                                cornerSpots.append([playedSpots[i][0]-1, playedSpots[i][1]-1, ((playedSpots[i][0]-1) + (playedSpots[i][1]-1))/2])
                            else:
                                cornerSpots.append([playedSpots[i][0]+1, playedSpots[i][1]-1, ((playedSpots[i][0]+1) + (playedSpots[i][1]-1))/2])
            
            #remove cornerSpots that are not in range
            removeList = []
            for item in cornerSpots:
                if item[0] < 0:
                    removeList.append(item)
                    continue
                if item[1] < 0:
                    removeList.append(item)
                    continue
                if item[0] > 19:
                    removeList.append(item)
                    continue
                if item[1] > 19:
                    removeList.append(item)
                                   
            cornerSpots[:] = [x for x in cornerSpots if x not in removeList]
            
            
                     
            cornerSpots.sort(reverse = True, key = lambda x:(x[2]))
            #print('cornerSpots', cornerSpots)              
            corners = []
            for i in range(len(cornerSpots)):
                corners.append(cornerSpots[i][0:2])                    
            
            #print(corners)
            #return the list of corner spots arranged in order of distance from starting position
            return corners
        
    def cornerChoiceRandom(self):
        '''
        Chooses the corner where the computer will play. 
        Whereas cornerChoice() picks the corner furthest from opening placement,
        cornerChoiceRandom() adds a bit of randomness to the order of the corners
        so that the cornerChoice is less predictable
        '''
        if self.grid[0][0] == 0:
            return [[0,0]]
        else:
        #only deal with pieces played by computer for now. 
        #ignore pieces played by opponents
        
            #find points that contain a 1 and then sort them by largest average value
            #for starters, return the corner furthest from initial play spot
            playedSpots = []
            for i in range(20):
                for j in range(20):
                    if self.grid[i][j] == 1:
                        playedSpots.append([i, j, (i+j)/2])
                        
            #print('playedSpots', playedSpots)
            
            
            #for each played spot, produce as many corner locations that are not adjacent to any existing pieces
            cornerSpots = []
            direction = ['NE', 'SE', 'NW', 'SW']
            for i in range(len(playedSpots)):
                for d in direction:
                    if Board.cornerCheck(self, playedSpots[i], d, placements = []):
                        
                        if Board.adjacentCheck(self, playedSpots[i], d):
                            if d == 'NE':
                                cornerSpots.append([playedSpots[i][0]-1, playedSpots[i][1]+1, ((playedSpots[i][0]-1) + (playedSpots[i][1]+1))/2])
                            elif d == 'SE':
                                cornerSpots.append([playedSpots[i][0]+1, playedSpots[i][1]+1, ((playedSpots[i][0]+1) + (playedSpots[i][1]+1))/2])
                            elif d == 'NW':
                                cornerSpots.append([playedSpots[i][0]-1, playedSpots[i][1]-1, ((playedSpots[i][0]-1) + (playedSpots[i][1]-1))/2])
                            else:
                                cornerSpots.append([playedSpots[i][0]+1, playedSpots[i][1]-1, ((playedSpots[i][0]+1) + (playedSpots[i][1]-1))/2])
            
            #remove cornerSpots that are not in range
            removeList = []
            for item in cornerSpots:
                if item[0] < 0:
                    removeList.append(item)
                    continue
                if item[1] < 0:
                    removeList.append(item)
                    continue
                if item[0] > 19:
                    removeList.append(item)
                    continue
                if item[1] > 19:
                    removeList.append(item)
                                   
            cornerSpots[:] = [x for x in cornerSpots if x not in removeList]
            
            #to make the computer's a little more unpredictable, we will add an rng number to the average row/column total before sorting
            random.seed()
            
            randList = []
            for i in range(len(cornerSpots)):
                #for the randomization, using a normal dist with mu of 10 and sigma 3. This will allow for some variation but not a whole lot.
                randList.append(random.normalvariate(10, 3))
            
            for i in range(len(cornerSpots)):
                cornerSpots[i][2] = cornerSpots[i][2]+randList[i]
                     
            cornerSpots.sort(reverse = True, key = lambda x:(x[2]))
            #print('cornerSpots', cornerSpots)              
            corners = []
            for i in range(len(cornerSpots)):
                corners.append(cornerSpots[i][0:2])                    
            
            #print(corners)
            #return the list of corner spots arranged in order of distance from starting position
            return corners
    
    
    
    def cornerCheck(self, playedSpot, direction, placements):
        '''check that the corner to be played is available for play'''
        
        if direction == 'SE':
            try:
                
                if self.grid[playedSpot[0]+1][playedSpot[1]+1] == 0:
                    if [playedSpot[0]+1, playedSpot[1]+1] not in placements:
                        return True
            except IndexError:
                return False
        elif direction == 'NE':
            try:
                
                if self.grid[playedSpot[0]-1][playedSpot[1]+1] == 0:
                    if [playedSpot[0]-1, playedSpot[1]+1] not in placements:
                        return True
            except IndexError:
                return False
        if direction == 'SW':
            try:
                
                if self.grid[playedSpot[0]+1][playedSpot[1]-1] == 0:
                    if [playedSpot[0]+1, playedSpot[1]-1] not in placements:
                        return True
            except IndexError:
                return False
        if direction == 'NW':
            try:
                
                if self.grid[playedSpot[0]-1][playedSpot[1]-1] == 0:
                    if [playedSpot[0]-1, playedSpot[1]-1] not in placements:
                        return True
            except IndexError:
                return False
        
        return False
                    
    def spaceCheck(self, playableCorner, direction):
        '''Space Check is used in the playSpace method to check if a given square is playable
        Takes in playable corner specified from playSpace method function call
        It checks if the square is empty and Anna has not already played adjacent to it'''
        #before checking adjacency, identify potential indexerrors since the grid is only 20x20
        indexOOB = [0, 1, 18, 19]
        
        indexError = []
        if playableCorner[0] not in indexOOB:
            indexError.append(False)
        else:
            indexError.append(True)
        
        if playableCorner[1] not in indexOOB:
            indexError.append(False)
        else:
            indexError.append(True)
            
        #this is the adjacent check for the grid spots with no index errors arising from the adjacent check
        if indexError == [False, False]:
            
            if direction == 'N' and self.grid[playableCorner[0]-1][playableCorner[1]] == 0:
                
                if self.grid[playableCorner[0]-2][playableCorner[1]] != 1:
                    if self.grid[playableCorner[0]-1][playableCorner[1]+1] != 1:
                        if self.grid[playableCorner[0]-1][playableCorner[1]-1] != 1:
                            return True
                                        
            elif direction == 'S' and self.grid[playableCorner[0]+1][playableCorner[1]] == 0:
                
                if self.grid[playableCorner[0]+2][playableCorner[1]] != 1:
                    if self.grid[playableCorner[0]+1][playableCorner[1]+1] != 1:
                        if self.grid[playableCorner[0]+1][playableCorner[1]-1] != 1:
                            return True
            
            elif direction == 'W' and self.grid[playableCorner[0]][playableCorner[1]-1] == 0:
                
                if self.grid[playableCorner[0]-1][playableCorner[1]-1] != 1:
                    if self.grid[playableCorner[0]+1][playableCorner[1]-1] != 1:
                        if self.grid[playableCorner[0]][playableCorner[1]-2] != 1:
                            return True
            
            elif direction == 'E' and self.grid[playableCorner[0]][playableCorner[1]+1] == 0:
                
                if self.grid[playableCorner[0]-1][playableCorner[1]+1] != 1:
                    if self.grid[playableCorner[0]+1][playableCorner[1]+1] != 1:
                        if self.grid[playableCorner[0]][playableCorner[1]+2] != 1:
                            return True
            
            
        ####
        ####
        #### now for the corners with potential index errors for rows only
        elif indexError == [True, False]:
            if playableCorner[0] == 0:
                if direction == 'S' and self.grid[playableCorner[0]+1][playableCorner[1]] == 0:
                
                    if self.grid[playableCorner[0]+2][playableCorner[1]] != 1:
                        if self.grid[playableCorner[0]+1][playableCorner[1]+1] != 1:
                            if self.grid[playableCorner[0]+1][playableCorner[1]-1] != 1:
                                return True
                                        
                elif direction == 'E' and self.grid[playableCorner[0]][playableCorner[1]+1] == 0:
                
                    if self.grid[playableCorner[0]+1][playableCorner[1]+1] != 1:
                        if self.grid[playableCorner[0]][playableCorner[1]+2] != 1:
                            return True
                
                elif direction == 'W' and self.grid[playableCorner[0]][playableCorner[1]-1] == 0:
                
                    if self.grid[playableCorner[0]+1][playableCorner[1]-1] != 1:
                        if self.grid[playableCorner[0]][playableCorner[1]-2] != 1:
                            return True
                
                
            elif playableCorner[0] == 1:
                if direction == 'N' and self.grid[playableCorner[0]-1][playableCorner[1]] == 0:
                
                    if self.grid[playableCorner[0]-1][playableCorner[1]+1] != 1:
                        if self.grid[playableCorner[0]-1][playableCorner[1]-1] != 1:
                            return True
                                        
                elif direction == 'S' and self.grid[playableCorner[0]+1][playableCorner[1]] == 0:
                    
                    if self.grid[playableCorner[0]+2][playableCorner[1]] != 1:
                        if self.grid[playableCorner[0]+1][playableCorner[1]+1] != 1:
                            if self.grid[playableCorner[0]+1][playableCorner[1]-1] != 1:
                                return True
                
                elif direction == 'W' and self.grid[playableCorner[0]][playableCorner[1]-1] == 0:
                    
                    if self.grid[playableCorner[0]-1][playableCorner[1]-1] != 1:
                        if self.grid[playableCorner[0]+1][playableCorner[1]-1] != 1:
                            if self.grid[playableCorner[0]][playableCorner[1]-2] != 1:
                                return True
                
                elif direction == 'E' and self.grid[playableCorner[0]][playableCorner[1]+1] == 0:
                    
                    if self.grid[playableCorner[0]-1][playableCorner[1]+1] != 1:
                        if self.grid[playableCorner[0]+1][playableCorner[1]+1] != 1:
                            if self.grid[playableCorner[0]][playableCorner[1]+2] != 1:
                                return True
    
            elif playableCorner[0] == 18:
                if direction == 'N' and self.grid[playableCorner[0]-1][playableCorner[1]] == 0:
                
                    if self.grid[playableCorner[0]-2][playableCorner[1]] != 1:
                        if self.grid[playableCorner[0]-1][playableCorner[1]+1] != 1:
                            if self.grid[playableCorner[0]-1][playableCorner[1]-1] != 1:
                                return True
                                        
                elif direction == 'S' and self.grid[playableCorner[0]+1][playableCorner[1]] == 0:
                    
                    if self.grid[playableCorner[0]+1][playableCorner[1]+1] != 1:
                        if self.grid[playableCorner[0]+1][playableCorner[1]-1] != 1:
                            return True
                
                elif direction == 'W' and self.grid[playableCorner[0]][playableCorner[1]-1] == 0:
                    
                    if self.grid[playableCorner[0]-1][playableCorner[1]-1] != 1:
                        if self.grid[playableCorner[0]+1][playableCorner[1]-1] != 1:
                            if self.grid[playableCorner[0]][playableCorner[1]-2] != 1:
                                return True
                
                elif direction == 'E' and self.grid[playableCorner[0]][playableCorner[1]+1] == 0:
                    
                    if self.grid[playableCorner[0]-1][playableCorner[1]+1] != 1:
                        if self.grid[playableCorner[0]+1][playableCorner[1]+1] != 1:
                            if self.grid[playableCorner[0]][playableCorner[1]+2] != 1:
                                return True
        
                
            else:
                if direction == 'N' and self.grid[playableCorner[0]-1][playableCorner[1]] == 0:
                
                    if self.grid[playableCorner[0]-2][playableCorner[1]] != 1:
                        if self.grid[playableCorner[0]-1][playableCorner[1]+1] != 1:
                            if self.grid[playableCorner[0]-1][playableCorner[1]-1] != 1:
                                return True
                                          
                elif direction == 'W' and self.grid[playableCorner[0]][playableCorner[1]-1] == 0:
                    
                    if self.grid[playableCorner[0]-1][playableCorner[1]-1] != 1:
                        if self.grid[playableCorner[0]][playableCorner[1]-2] != 1:
                            return True
                
                elif direction == 'E' and self.grid[playableCorner[0]][playableCorner[1]+1] == 0:
                    
                    if self.grid[playableCorner[0]-1][playableCorner[1]+1] != 1:
                        if self.grid[playableCorner[0]][playableCorner[1]+2] != 1:
                            return True
                
        ####
        ####
        #### now for the corners with potential index errors for columns only
        elif indexError == [False, True]:
            if playableCorner[1] == 0:
                if direction == 'N' and self.grid[playableCorner[0]-1][playableCorner[1]] == 0:
                
                    if self.grid[playableCorner[0]-2][playableCorner[1]] != 1:
                        if self.grid[playableCorner[0]-1][playableCorner[1]+1] != 1:
                            return True
                                            
                elif direction == 'S' and self.grid[playableCorner[0]+1][playableCorner[1]] == 0:
                    
                    if self.grid[playableCorner[0]+2][playableCorner[1]] != 1:
                        if self.grid[playableCorner[0]+1][playableCorner[1]+1] != 1:
                            return True
                
                                
                elif direction == 'E' and self.grid[playableCorner[0]][playableCorner[1]+1] == 0:
                    
                    if self.grid[playableCorner[0]-1][playableCorner[1]+1] != 1:
                        if self.grid[playableCorner[0]+1][playableCorner[1]+1] != 1:
                            if self.grid[playableCorner[0]][playableCorner[1]+2] != 1:
                                return True
                
            elif playableCorner[1] == 1:
                if direction == 'N' and self.grid[playableCorner[0]-1][playableCorner[1]] == 0:
                
                    if self.grid[playableCorner[0]-2][playableCorner[1]] != 1:
                        if self.grid[playableCorner[0]-1][playableCorner[1]+1] != 1:
                            if self.grid[playableCorner[0]-1][playableCorner[1]-1] != 1:
                                return True
                                            
                elif direction == 'S' and self.grid[playableCorner[0]+1][playableCorner[1]] == 0:
                    
                    if self.grid[playableCorner[0]+2][playableCorner[1]] != 1:
                        if self.grid[playableCorner[0]+1][playableCorner[1]+1] != 1:
                            if self.grid[playableCorner[0]+1][playableCorner[1]-1] != 1:
                                return True
                
                elif direction == 'W' and self.grid[playableCorner[0]][playableCorner[1]-1] == 0:
                    
                    if self.grid[playableCorner[0]-1][playableCorner[1]-1] != 1:
                        if self.grid[playableCorner[0]+1][playableCorner[1]-1] != 1:
                            return True
                
                elif direction == 'E' and self.grid[playableCorner[0]][playableCorner[1]+1] == 0:
                    
                    if self.grid[playableCorner[0]-1][playableCorner[1]+1] != 1:
                        if self.grid[playableCorner[0]+1][playableCorner[1]+1] != 1:
                            if self.grid[playableCorner[0]][playableCorner[1]+2] != 1:
                                return True
        
            elif playableCorner[1] == 18:
                if direction == 'N' and self.grid[playableCorner[0]-1][playableCorner[1]] == 0:
                
                    if self.grid[playableCorner[0]-2][playableCorner[1]] != 1:
                        if self.grid[playableCorner[0]-1][playableCorner[1]+1] != 1:
                            if self.grid[playableCorner[0]-1][playableCorner[1]-1] != 1:
                                return True
                                            
                elif direction == 'S' and self.grid[playableCorner[0]+1][playableCorner[1]] == 0:
                    
                    if self.grid[playableCorner[0]+2][playableCorner[1]] != 1:
                        if self.grid[playableCorner[0]+1][playableCorner[1]+1] != 1:
                            if self.grid[playableCorner[0]+1][playableCorner[1]-1] != 1:
                                return True
                
                elif direction == 'W' and self.grid[playableCorner[0]][playableCorner[1]-1] == 0:
                    
                    if self.grid[playableCorner[0]-1][playableCorner[1]-1] != 1:
                        if self.grid[playableCorner[0]+1][playableCorner[1]-1] != 1:
                            if self.grid[playableCorner[0]][playableCorner[1]-2] != 1:
                                return True
                
                elif direction == 'E' and self.grid[playableCorner[0]][playableCorner[1]+1] == 0:
                    
                    if self.grid[playableCorner[0]-1][playableCorner[1]+1] != 1:
                        if self.grid[playableCorner[0]+1][playableCorner[1]+1] != 1:
                            return True
                                            
            else:
                if direction == 'N' and self.grid[playableCorner[0]-1][playableCorner[1]] == 0:
                
                    if self.grid[playableCorner[0]-2][playableCorner[1]] != 1:
                        if self.grid[playableCorner[0]-1][playableCorner[1]-1] != 1:
                            return True
                                            
                elif direction == 'S' and self.grid[playableCorner[0]+1][playableCorner[1]] == 0:
                    
                    if self.grid[playableCorner[0]+2][playableCorner[1]] != 1:
                        if self.grid[playableCorner[0]+1][playableCorner[1]-1] != 1:
                            return True
                
                elif direction == 'W' and self.grid[playableCorner[0]][playableCorner[1]-1] == 0:
                    
                    if self.grid[playableCorner[0]-1][playableCorner[1]-1] != 1:
                        if self.grid[playableCorner[0]+1][playableCorner[1]-1] != 1:
                            if self.grid[playableCorner[0]][playableCorner[1]-2] != 1:
                                return True
                                
                
        ####
        ####
        #### now for the corners with potential index errors for columns and rows
        elif indexError == [False, False]:
            if playableCorner[1:] == [0,0]:
                return False
            
                
            elif playableCorner[1:] == [0, 18]:
                                                           
                if direction == 'S' and self.grid[playableCorner[0]+1][playableCorner[1]] == 0:
                    
                    if self.grid[playableCorner[0]+2][playableCorner[1]] != 1:
                        if self.grid[playableCorner[0]+1][playableCorner[1]+1] != 1:
                            if self.grid[playableCorner[0]+1][playableCorner[1]-1] != 1:
                                return True
                
                elif direction == 'W' and self.grid[playableCorner[0]][playableCorner[1]-1] == 0:
                    
                    if self.grid[playableCorner[0]+1][playableCorner[1]-1] != 1:
                        if self.grid[playableCorner[0]][playableCorner[1]-2] != 1:
                            return True
              
                 
            elif playableCorner[1:] == [1,18]:
                if direction == 'N' and self.grid[playableCorner[0]-1][playableCorner[1]] == 0:
                
                    if self.grid[playableCorner[0]-1][playableCorner[1]+1] != 1:
                        if self.grid[playableCorner[0]-1][playableCorner[1]-1] != 1:
                            return True
                                            
                elif direction == 'S' and self.grid[playableCorner[0]+1][playableCorner[1]] == 0:
                    
                    if self.grid[playableCorner[0]+2][playableCorner[1]] != 1:
                        if self.grid[playableCorner[0]+1][playableCorner[1]+1] != 1:
                            if self.grid[playableCorner[0]+1][playableCorner[1]-1] != 1:
                                return True
                
                elif direction == 'W' and self.grid[playableCorner[0]][playableCorner[1]-1] == 0:
                    
                    if self.grid[playableCorner[0]-1][playableCorner[1]-1] != 1:
                        if self.grid[playableCorner[0]+1][playableCorner[1]-1] != 1:
                            if self.grid[playableCorner[0]][playableCorner[1]-2] != 1:
                                return True
                
                elif direction == 'E' and self.grid[playableCorner[0]][playableCorner[1]+1] == 0:
                    
                    if self.grid[playableCorner[0]-1][playableCorner[1]+1] != 1:
                        if self.grid[playableCorner[0]+1][playableCorner[1]+1] != 1:
                            return True
                
            elif playableCorner[1:] == [1,19]:
                
                                            
                if direction == 'S' and self.grid[playableCorner[0]+1][playableCorner[1]] == 0:
                    
                    if self.grid[playableCorner[0]+2][playableCorner[1]] != 1:
                        if self.grid[playableCorner[0]+1][playableCorner[1]-1] != 1:
                            return True
                
                elif direction == 'W' and self.grid[playableCorner[0]][playableCorner[1]-1] == 0:
                    
                    if self.grid[playableCorner[0]-1][playableCorner[1]-1] != 1:
                        if self.grid[playableCorner[0]+1][playableCorner[1]-1] != 1:
                            if self.grid[playableCorner[0]][playableCorner[1]-2] != 1:
                                return True
                               
                                
            elif playableCorner[1:] == [18, 0]:
                if direction == 'N' and self.grid[playableCorner[0]-1][playableCorner[1]] == 0:
                
                    if self.grid[playableCorner[0]-2][playableCorner[1]] != 1:
                        if self.grid[playableCorner[0]-1][playableCorner[1]-1] != 1:
                            return True
                                            
                elif direction == 'S' and self.grid[playableCorner[0]+1][playableCorner[1]] == 0:
                    
                    if self.grid[playableCorner[0]+1][playableCorner[1]+1] != 1:
                        if self.grid[playableCorner[0]+1][playableCorner[1]-1] != 1:
                            return True
                                                
                elif direction == 'E' and self.grid[playableCorner[0]][playableCorner[1]+1] == 0:
                    
                    if self.grid[playableCorner[0]-1][playableCorner[1]+1] != 1:
                        if self.grid[playableCorner[0]+1][playableCorner[1]+1] != 1:
                            if self.grid[playableCorner[0]][playableCorner[1]+2] != 1:
                                return True
                            
            elif playableCorner[1:] == [18, 1]:
                if direction == 'N' and self.grid[playableCorner[0]-1][playableCorner[1]] == 0:
                
                    if self.grid[playableCorner[0]-2][playableCorner[1]] != 1:
                        if self.grid[playableCorner[0]-1][playableCorner[1]+1] != 1:
                            if self.grid[playableCorner[0]-1][playableCorner[1]-1] != 1:
                                return True
                                            
                elif direction == 'S' and self.grid[playableCorner[0]+1][playableCorner[1]] == 0:
                    
                    if self.grid[playableCorner[0]+1][playableCorner[1]+1] != 1:
                        if self.grid[playableCorner[0]+1][playableCorner[1]-1] != 1:
                            return True
                
                elif direction == 'W' and self.grid[playableCorner[0]][playableCorner[1]-1] == 0:
                    
                    if self.grid[playableCorner[0]-1][playableCorner[1]-1] != 1:
                        if self.grid[playableCorner[0]+1][playableCorner[1]-1] != 1:
                            return True
                
                elif direction == 'E' and self.grid[playableCorner[0]][playableCorner[1]+1] == 0:
                    
                    if self.grid[playableCorner[0]-1][playableCorner[1]+1] != 1:
                        if self.grid[playableCorner[0]+1][playableCorner[1]+1] != 1:
                            if self.grid[playableCorner[0]][playableCorner[1]+2] != 1:
                                return True
                
            elif playableCorner[1:] == [18, 18]:
                if direction == 'N' and self.grid[playableCorner[0]-1][playableCorner[1]] == 0:
                
                    if self.grid[playableCorner[0]-2][playableCorner[1]] != 1:
                        if self.grid[playableCorner[0]-1][playableCorner[1]+1] != 1:
                            if self.grid[playableCorner[0]-1][playableCorner[1]-1] != 1:
                                return True
                                            
                elif direction == 'S' and self.grid[playableCorner[0]+1][playableCorner[1]] == 0:
                    
                    if self.grid[playableCorner[0]+1][playableCorner[1]+1] != 1:
                        if self.grid[playableCorner[0]+1][playableCorner[1]-1] != 1:
                            return True
                
                elif direction == 'W' and self.grid[playableCorner[0]][playableCorner[1]-1] == 0:
                    
                    if self.grid[playableCorner[0]-1][playableCorner[1]-1] != 1:
                        if self.grid[playableCorner[0]+1][playableCorner[1]-1] != 1:
                            if self.grid[playableCorner[0]][playableCorner[1]-2] != 1:
                                return True
                
                elif direction == 'E' and self.grid[playableCorner[0]][playableCorner[1]+1] == 0:
                    
                    if self.grid[playableCorner[0]-1][playableCorner[1]+1] != 1:
                        if self.grid[playableCorner[0]+1][playableCorner[1]+1] != 1:
                            return True
                            
            elif playableCorner[1:] == [18, 19]:
                if direction == 'N' and self.grid[playableCorner[0]-1][playableCorner[1]] == 0:
                
                    if self.grid[playableCorner[0]-2][playableCorner[1]] != 1:
                        if self.grid[playableCorner[0]-1][playableCorner[1]-1] != 1:
                            return True
                            
                elif direction == 'W' and self.grid[playableCorner[0]][playableCorner[1]-1] == 0:
                    
                    if self.grid[playableCorner[0]-1][playableCorner[1]-1] != 1:
                        if self.grid[playableCorner[0]+1][playableCorner[1]-1] != 1:
                            if self.grid[playableCorner[0]][playableCorner[1]-2] != 1:
                                return True
                
            elif playableCorner[1:] == [19, 1]:
                if direction == 'N' and self.grid[playableCorner[0]-1][playableCorner[1]] == 0:
                
                    if self.grid[playableCorner[0]-2][playableCorner[1]] != 1:
                        if self.grid[playableCorner[0]-1][playableCorner[1]+1] != 1:
                            if self.grid[playableCorner[0]-1][playableCorner[1]-1] != 1:
                                return True
                           
                
                elif direction == 'E' and self.grid[playableCorner[0]][playableCorner[1]+1] == 0:
                    
                    if self.grid[playableCorner[0]-1][playableCorner[1]+1] != 1:
                        if self.grid[playableCorner[0]][playableCorner[1]+2] != 1:
                            return True
                
            elif playableCorner[1:] == [19, 18]:
                if direction == 'N' and self.grid[playableCorner[0]-1][playableCorner[1]] == 0:
                
                    if self.grid[playableCorner[0]-2][playableCorner[1]] != 1:
                        if self.grid[playableCorner[0]-1][playableCorner[1]+1] != 1:
                            if self.grid[playableCorner[0]-1][playableCorner[1]-1] != 1:
                                return True
                             
                elif direction == 'W' and self.grid[playableCorner[0]][playableCorner[1]-1] == 0:
                    
                    if self.grid[playableCorner[0]-1][playableCorner[1]-1] != 1:
                        if self.grid[playableCorner[0]][playableCorner[1]-2] != 1:
                            return True
                
            
            elif playableCorner[1:] == [19,19]:
                return False
            elif playableCorner[1:] == [0,1]:
                return False
            elif playableCorner[1:] == [0,19]:
                return False
            elif playableCorner[1:] == [1,0]:
                return False
            elif playableCorner[1:] == [1,1]:
                return False
            elif playableCorner[1:] == [19, 0]:
                return False
                
        
        return False
    
    def adjacentCheck(self, playedSpot, direction):
        '''adjacentCheck method will be used within the cornerChoice method 
        to identify if all adjacent locations to the proposed cornerSpot have not been used by computer
        playedSpot will be a list of three items, item 2 will be row # and item 3 will be column #
        direction indicates which corner from the playedSpot will be evaluated. Options are northeast, southeast, northwest and southwest'''
        
        #before checking adjacency, identify potential indexerrors since the grid is only 20x20
        indexOOB = [0,1,18,19]
        
        indexError = []
        if playedSpot[0] not in indexOOB:
            indexError.append(False)
        else:
            indexError.append(True)
        
        if playedSpot[1] not in indexOOB:
            indexError.append(False)
        else:
            indexError.append(True)
            
        #this is the adjacent check for the grid spots with no index errors arising from the adjacent check
        if indexError == [False, False]:
            
            if direction == 'SE':
                #corner furthest from starting point (southeast on grid view)
                if self.grid[playedSpot[0]+2][playedSpot[1]+1] != 1:
                    if self.grid[playedSpot[0]+1][playedSpot[1]+2] != 1:
                        if self.grid[playedSpot[0]][playedSpot[1]+1] != 1:
                            if self.grid[playedSpot[0]+1][playedSpot[1]] != 1:
                                return True
                                        
            elif direction == 'NE':                            
            #corner northeast on grid view
                if self.grid[playedSpot[0]-2][playedSpot[1]+1] != 1:
                    if self.grid[playedSpot[0]-1][playedSpot[1]+2] != 1:
                        if self.grid[playedSpot[0]][playedSpot[1]+1] != 1:
                            if self.grid[playedSpot[0]-1][playedSpot[1]] != 1:
                                return True
            
            elif direction == 'NW':
                if self.grid[playedSpot[0]-2][playedSpot[1]-1] != 1:
                    if self.grid[playedSpot[0]-1][playedSpot[1]] != 1:
                        if self.grid[playedSpot[0]][playedSpot[1]-1] != 1:
                            if self.grid[playedSpot[0]-1][playedSpot[1]-2] != 1:
                                return True
            
            elif direction == 'SW':
                if self.grid[playedSpot[0]+2][playedSpot[1]-1] != 1:
                    if self.grid[playedSpot[0]+1][playedSpot[1]] != 1:
                        if self.grid[playedSpot[0]][playedSpot[1]-1] != 1:
                            if self.grid[playedSpot[0]+1][playedSpot[1]-2] != 1:
                                return True
        ####
        ####
        #### now for the corners with potential index errors for rows only
        elif indexError == [True, False]:
            if playedSpot[0] == 0:
                if direction == 'SE':
                    #corner furthest from starting point (southeast on grid view)
                    if self.grid[playedSpot[0]+2][playedSpot[1]+1] != 1:
                        if self.grid[playedSpot[0]+1][playedSpot[1]+2] != 1:
                            if self.grid[playedSpot[0]][playedSpot[1]+1] != 1:
                                if self.grid[playedSpot[0]+1][playedSpot[1]] != 1:
                                    return True
                                        
                elif direction == 'NE':                            
                #corner northeast on grid view
                    return False
                
                elif direction == 'NW':
                    return False
                
                elif direction == 'SW':
                    if self.grid[playedSpot[0]+2][playedSpot[1]-1] != 1:
                        if self.grid[playedSpot[0]+1][playedSpot[1]] != 1:
                            if self.grid[playedSpot[0]][playedSpot[1]-1] != 1:
                                if self.grid[playedSpot[0]+1][playedSpot[1]-2] != 1:
                                    return True
            elif playedSpot[0] == 1:
                if direction == 'SE':
                    #corner furthest from starting point (southeast on grid view)
                    if self.grid[playedSpot[0]+2][playedSpot[1]+1] != 1:
                        if self.grid[playedSpot[0]+1][playedSpot[1]+2] != 1:
                            if self.grid[playedSpot[0]][playedSpot[1]+1] != 1:
                                if self.grid[playedSpot[0]+1][playedSpot[1]] != 1:
                                    return True
                                        
                elif direction == 'NE':                            
                #corner northeast on grid view
                    if self.grid[playedSpot[0]-1][playedSpot[1]+2] != 1:
                        if self.grid[playedSpot[0]][playedSpot[1]+1] != 1:
                            if self.grid[playedSpot[0]-1][playedSpot[1]] != 1:
                                return True
                
                elif direction == 'NW':
                    if self.grid[playedSpot[0]-1][playedSpot[1]] != 1:
                        if self.grid[playedSpot[0]][playedSpot[1]-1] != 1:
                            if self.grid[playedSpot[0]-1][playedSpot[1]-2] != 1:
                                return True
                
                elif direction == 'SW':
                    if self.grid[playedSpot[0]+2][playedSpot[1]-1] != 1:
                        if self.grid[playedSpot[0]+1][playedSpot[1]] != 1:
                            if self.grid[playedSpot[0]][playedSpot[1]-1] != 1:
                                if self.grid[playedSpot[0]+1][playedSpot[1]-2] != 1:
                                    return True
        
            elif playedSpot[0] == 18:
        
                if direction == 'SE':
                    #corner furthest from starting point (southeast on grid view)
                    
                    if self.grid[playedSpot[0]+1][playedSpot[1]+2] != 1:
                        if self.grid[playedSpot[0]][playedSpot[1]+1] != 1:
                            if self.grid[playedSpot[0]+1][playedSpot[1]] != 1:
                                return True
                                            
                elif direction == 'NE':                            
                #corner northeast on grid view
                    if self.grid[playedSpot[0]-2][playedSpot[1]+1] != 1:
                        if self.grid[playedSpot[0]-1][playedSpot[1]+2] != 1:
                            if self.grid[playedSpot[0]][playedSpot[1]+1] != 1:
                                if self.grid[playedSpot[0]-1][playedSpot[1]] != 1:
                                    return True
                
                elif direction == 'NW':
                    if self.grid[playedSpot[0]-2][playedSpot[1]-1] != 1:
                        if self.grid[playedSpot[0]-1][playedSpot[1]] != 1:
                            if self.grid[playedSpot[0]][playedSpot[1]-1] != 1:
                                if self.grid[playedSpot[0]-1][playedSpot[1]-2] != 1:
                                    return True
                
                elif direction == 'SW':
                    
                    if self.grid[playedSpot[0]+1][playedSpot[1]] != 1:
                        if self.grid[playedSpot[0]][playedSpot[1]-1] != 1:
                            if self.grid[playedSpot[0]+1][playedSpot[1]-2] != 1:
                                return True
            else:
                if direction == 'SE':
                    #corner furthest from starting point (southeast on grid view)
                    
                    return False
                                            
                elif direction == 'NE':                            
                #corner northeast on grid view
                    if self.grid[playedSpot[0]-2][playedSpot[1]+1] != 1:
                        if self.grid[playedSpot[0]-1][playedSpot[1]+2] != 1:
                            if self.grid[playedSpot[0]][playedSpot[1]+1] != 1:
                                if self.grid[playedSpot[0]-1][playedSpot[1]] != 1:
                                    return True
                
                elif direction == 'NW':
                    if self.grid[playedSpot[0]-2][playedSpot[1]-1] != 1:
                        if self.grid[playedSpot[0]-1][playedSpot[1]] != 1:
                            if self.grid[playedSpot[0]][playedSpot[1]-1] != 1:
                                if self.grid[playedSpot[0]-1][playedSpot[1]-2] != 1:
                                    return True
                
                elif direction == 'SW':
                    
                    return False
        ####
        ####
        #### now for the corners with potential index errors for columns only
        elif indexError == [False, True]:
            if playedSpot[1] == 0:
                if direction == 'SE':
                    #corner furthest from starting point (southeast on grid view)
                    if self.grid[playedSpot[0]+2][playedSpot[1]+1] != 1:
                        if self.grid[playedSpot[0]+1][playedSpot[1]+2] != 1:
                            if self.grid[playedSpot[0]][playedSpot[1]+1] != 1:
                                if self.grid[playedSpot[0]+1][playedSpot[1]] != 1:
                                    return True
                                        
                elif direction == 'NE':                            
                #corner northeast on grid view
                    if self.grid[playedSpot[0]-2][playedSpot[1]+1] != 1:
                        if self.grid[playedSpot[0]-1][playedSpot[1]+2] != 1:
                            if self.grid[playedSpot[0]][playedSpot[1]+1] != 1:
                                if self.grid[playedSpot[0]-1][playedSpot[1]] != 1:
                                    return True
                
                elif direction == 'NW':
                    return False
                
                elif direction == 'SW':
                    return False
                
            elif playedSpot[1] == 1:
                if direction == 'SE':
                    #corner furthest from starting point (southeast on grid view)
                    if self.grid[playedSpot[0]+2][playedSpot[1]+1] != 1:
                        if self.grid[playedSpot[0]+1][playedSpot[1]+2] != 1:
                            if self.grid[playedSpot[0]][playedSpot[1]+1] != 1:
                                if self.grid[playedSpot[0]+1][playedSpot[1]] != 1:
                                    return True
                                        
                elif direction == 'NE':                            
                #corner northeast on grid view
                    if self.grid[playedSpot[0]-2][playedSpot[1]+1] != 1:
                        if self.grid[playedSpot[0]-1][playedSpot[1]+2] != 1:
                            if self.grid[playedSpot[0]][playedSpot[1]+1] != 1:
                                if self.grid[playedSpot[0]-1][playedSpot[1]] != 1:
                                    return True
                
                elif direction == 'NW':
                    if self.grid[playedSpot[0]-2][playedSpot[1]-1] != 1:
                        if self.grid[playedSpot[0]-1][playedSpot[1]] != 1:
                            if self.grid[playedSpot[0]][playedSpot[1]-1] != 1:
                                return True
                
                elif direction == 'SW':
                    if self.grid[playedSpot[0]+2][playedSpot[1]-1] != 1:
                        if self.grid[playedSpot[0]+1][playedSpot[1]] != 1:
                            if self.grid[playedSpot[0]][playedSpot[1]-1] != 1:
                                    return True
        
            elif playedSpot[1] == 18:
        
                if direction == 'SE':
                    #corner furthest from starting point (southeast on grid view)
                    if self.grid[playedSpot[0]+2][playedSpot[1]+1] != 1:
                        if self.grid[playedSpot[0]][playedSpot[1]+1] != 1:
                            if self.grid[playedSpot[0]+1][playedSpot[1]] != 1:
                                return True
                                                                
                elif direction == 'NE':                            
                #corner northeast on grid view
                    if self.grid[playedSpot[0]-2][playedSpot[1]+1] != 1:
                        if self.grid[playedSpot[0]][playedSpot[1]+1] != 1:
                            if self.grid[playedSpot[0]-1][playedSpot[1]] != 1:
                                return True
                
                elif direction == 'NW':
                    if self.grid[playedSpot[0]-2][playedSpot[1]-1] != 1:
                        if self.grid[playedSpot[0]-1][playedSpot[1]] != 1:
                            if self.grid[playedSpot[0]][playedSpot[1]-1] != 1:
                                if self.grid[playedSpot[0]-1][playedSpot[1]-2] != 1:
                                    return True
                
                elif direction == 'SW':
                    
                    if self.grid[playedSpot[0]+2][playedSpot[1]-1] != 1:
                        if self.grid[playedSpot[0]+1][playedSpot[1]] != 1:
                            if self.grid[playedSpot[0]][playedSpot[1]-1] != 1:
                                if self.grid[playedSpot[0]+1][playedSpot[1]-2] != 1:
                                    return True                                
            else:
                if direction == 'SE':
                    #corner furthest from starting point (southeast on grid view)
                    
                    return False
                                            
                elif direction == 'NE':                            
                    return False
                
                elif direction == 'NW':
                    if self.grid[playedSpot[0]-2][playedSpot[1]-1] != 1:
                        if self.grid[playedSpot[0]-1][playedSpot[1]] != 1:
                            if self.grid[playedSpot[0]][playedSpot[1]-1] != 1:
                                if self.grid[playedSpot[0]-1][playedSpot[1]-2] != 1:
                                    return True
                
                elif direction == 'SW':
                    
                    if self.grid[playedSpot[0]+2][playedSpot[1]-1] != 1:
                        if self.grid[playedSpot[0]+1][playedSpot[1]] != 1:
                            if self.grid[playedSpot[0]][playedSpot[1]-1] != 1:
                                if self.grid[playedSpot[0]+1][playedSpot[1]-2] != 1:
                                    return True
        ####
        ####
        #### now for the corners with potential index errors for columns and rows
        elif indexError == [False, False]:
            if playedSpot[1:] == [0,0]:
                return False
            elif playedSpot[1:] == [19,19]:
                return False
            elif playedSpot[1:] == [0,1]:
                if direction == 'SE':
                    #corner furthest from starting point (southeast on grid view)
                    if self.grid[playedSpot[0]+2][playedSpot[1]+1] != 1:
                        if self.grid[playedSpot[0]+1][playedSpot[1]+2] != 1:
                            if self.grid[playedSpot[0]][playedSpot[1]+1] != 1:
                                if self.grid[playedSpot[0]+1][playedSpot[1]] != 1:
                                    return True                                           
                elif direction == 'NE':                            
                    return False
                
                elif direction == 'NW':
                    return False
                
                elif direction == 'SW':
                    if self.grid[playedSpot[0]+2][playedSpot[1]-1] != 1:
                        if self.grid[playedSpot[0]+1][playedSpot[1]] != 1:
                            if self.grid[playedSpot[0]][playedSpot[1]-1] != 1:
                                return True
                
            elif playedSpot[1:] == [0, 18]:
                if direction == 'SE':
                    #corner furthest from starting point (southeast on grid view)
                    if self.grid[playedSpot[0]+2][playedSpot[1]+1] != 1:
                        if self.grid[playedSpot[0]][playedSpot[1]+1] != 1:
                                if self.grid[playedSpot[0]+1][playedSpot[1]] != 1:
                                    return True                                           
                elif direction == 'NE':                            
                    return False
                
                elif direction == 'NW':
                    return False
                
                elif direction == 'SW':
                    if self.grid[playedSpot[0]+2][playedSpot[1]-1] != 1:
                        if self.grid[playedSpot[0]+1][playedSpot[1]] != 1:
                            if self.grid[playedSpot[0]][playedSpot[1]-1] != 1:
                                if self.grid[playedSpot[0]+1][playedSpot[1]-2] != 1:
                                    return True
               
            elif playedSpot[1:] == [0,19]:
                return False
            
            elif playedSpot[1:] == [1,0]:
                if direction == 'SE':
                   if self.grid[playedSpot[0]+2][playedSpot[1]+1] != 1:
                        if self.grid[playedSpot[0]+1][playedSpot[1]+2] != 1:
                            if self.grid[playedSpot[0]][playedSpot[1]+1] != 1:
                                if self.grid[playedSpot[0]+1][playedSpot[1]] != 1:
                                    return True                                       
                elif direction == 'NE':                            
                    return False
                
                elif direction == 'NW':
                    return False
                
                elif direction == 'SW':
                   return False
                                
            elif playedSpot[1:] == [1,1]:
                if direction == 'SE':
                   if self.grid[playedSpot[0]+2][playedSpot[1]+1] != 1:
                        if self.grid[playedSpot[0]+1][playedSpot[1]+2] != 1:
                            if self.grid[playedSpot[0]][playedSpot[1]+1] != 1:
                                if self.grid[playedSpot[0]+1][playedSpot[1]] != 1:
                                    return True                                       
                elif direction == 'NE':                            
                    if self.grid[playedSpot[0]][playedSpot[1]+1] != 1:
                            if self.grid[playedSpot[0]-1][playedSpot[1]] != 1:
                                return True
                
                elif direction == 'NW':
                    return False
                
                elif direction == 'SW':
                   if self.grid[playedSpot[0]+2][playedSpot[1]-1] != 1:
                        if self.grid[playedSpot[0]+1][playedSpot[1]] != 1:
                            if self.grid[playedSpot[0]][playedSpot[1]-1] != 1:
                                return True
               
            elif playedSpot[1:] == [1,18]:
                if direction == 'SE':
                   if self.grid[playedSpot[0]+2][playedSpot[1]+1] != 1:
                        if self.grid[playedSpot[0]][playedSpot[1]+1] != 1:
                                if self.grid[playedSpot[0]+1][playedSpot[1]] != 1:
                                    return True                                       
                elif direction == 'NE':                            
                    return False
                
                elif direction == 'NW':
                    if self.grid[playedSpot[0]-1][playedSpot[1]] != 1:
                        if self.grid[playedSpot[0]][playedSpot[1]-1] != 1:
                            if self.grid[playedSpot[0]-1][playedSpot[1]-2] != 1:
                                return True
                
                elif direction == 'SW':
                   if self.grid[playedSpot[0]+2][playedSpot[1]-1] != 1:
                        if self.grid[playedSpot[0]+1][playedSpot[1]] != 1:
                            if self.grid[playedSpot[0]][playedSpot[1]-1] != 1:
                                if self.grid[playedSpot[0]+1][playedSpot[1]-2] != 1:
                                    return True
                                
            elif playedSpot[1:] == [1,19]:
                if direction == 'SE':
                   return False
                                       
                elif direction == 'NE':                            
                    return False
                
                elif direction == 'NW':
                    if self.grid[playedSpot[0]-1][playedSpot[1]] != 1:
                        if self.grid[playedSpot[0]][playedSpot[1]-1] != 1:
                            if self.grid[playedSpot[0]-1][playedSpot[1]-2] != 1:
                                return True
                
                elif direction == 'SW':
                   if self.grid[playedSpot[0]+2][playedSpot[1]-1] != 1:
                        if self.grid[playedSpot[0]+1][playedSpot[1]] != 1:
                            if self.grid[playedSpot[0]][playedSpot[1]-1] != 1:
                                if self.grid[playedSpot[0]+1][playedSpot[1]-2] != 1:
                                    return True
                                
            elif playedSpot[1:] == [18, 0]:
                if direction == 'SE':
                    #corner furthest from starting point (southeast on grid view)
                    
                    if self.grid[playedSpot[0]+1][playedSpot[1]+2] != 1:
                        if self.grid[playedSpot[0]][playedSpot[1]+1] != 1:
                            if self.grid[playedSpot[0]+1][playedSpot[1]] != 1:
                                return True
                                            
                elif direction == 'NE':                            
                #corner northeast on grid view
                    if self.grid[playedSpot[0]-2][playedSpot[1]+1] != 1:
                        if self.grid[playedSpot[0]-1][playedSpot[1]+2] != 1:
                            if self.grid[playedSpot[0]][playedSpot[1]+1] != 1:
                                if self.grid[playedSpot[0]-1][playedSpot[1]] != 1:
                                    return True
                
                elif direction == 'NW':
                    return False
                
                elif direction == 'SW':
                    
                    return False
                            
            elif playedSpot[1:] == [18, 1]:
                if direction == 'SE':
                    #corner furthest from starting point (southeast on grid view)
                    
                    if self.grid[playedSpot[0]+1][playedSpot[1]+2] != 1:
                        if self.grid[playedSpot[0]][playedSpot[1]+1] != 1:
                            if self.grid[playedSpot[0]+1][playedSpot[1]] != 1:
                                return True
                                            
                elif direction == 'NE':                            
                #corner northeast on grid view
                    if self.grid[playedSpot[0]-2][playedSpot[1]+1] != 1:
                        if self.grid[playedSpot[0]-1][playedSpot[1]+2] != 1:
                            if self.grid[playedSpot[0]][playedSpot[1]+1] != 1:
                                if self.grid[playedSpot[0]-1][playedSpot[1]] != 1:
                                    return True
                
                elif direction == 'NW':
                    if self.grid[playedSpot[0]-2][playedSpot[1]-1] != 1:
                        if self.grid[playedSpot[0]-1][playedSpot[1]] != 1:
                            if self.grid[playedSpot[0]][playedSpot[1]-1] != 1:
                                return True
                
                elif direction == 'SW':
                    
                    if self.grid[playedSpot[0]+1][playedSpot[1]] != 1:
                        if self.grid[playedSpot[0]][playedSpot[1]-1] != 1:
                            return True
                            
            elif playedSpot[1:] == [18, 18]:
                if direction == 'SE':
                    #corner furthest from starting point (southeast on grid view)
                    
                    if self.grid[playedSpot[0]][playedSpot[1]+1] != 1:
                            if self.grid[playedSpot[0]+1][playedSpot[1]] != 1:
                                return True
                                            
                elif direction == 'NE':                            
                #corner northeast on grid view
                    if self.grid[playedSpot[0]-2][playedSpot[1]+1] != 1:
                        if self.grid[playedSpot[0]][playedSpot[1]+1] != 1:
                                if self.grid[playedSpot[0]-1][playedSpot[1]] != 1:
                                    return True
                
                elif direction == 'NW':
                    if self.grid[playedSpot[0]-2][playedSpot[1]-1] != 1:
                        if self.grid[playedSpot[0]-1][playedSpot[1]] != 1:
                            if self.grid[playedSpot[0]][playedSpot[1]-1] != 1:
                                if self.grid[playedSpot[0]-1][playedSpot[1]-2] != 1:
                                    return True
                
                elif direction == 'SW':
                    
                    if self.grid[playedSpot[0]+1][playedSpot[1]] != 1:
                        if self.grid[playedSpot[0]][playedSpot[1]-1] != 1:
                            if self.grid[playedSpot[0]+1][playedSpot[1]-2] != 1:
                                return True
                            
            elif playedSpot[1:] == [18, 19]:
                if direction == 'SE':
                    #corner furthest from starting point (southeast on grid view)
                    
                    return False
                                            
                elif direction == 'NE':                            
                    return False
                
                elif direction == 'NW':
                    if self.grid[playedSpot[0]-2][playedSpot[1]-1] != 1:
                        if self.grid[playedSpot[0]-1][playedSpot[1]] != 1:
                            if self.grid[playedSpot[0]][playedSpot[1]-1] != 1:
                                if self.grid[playedSpot[0]-1][playedSpot[1]-2] != 1:
                                    return True
                
                elif direction == 'SW':
                    
                    if self.grid[playedSpot[0]+1][playedSpot[1]] != 1:
                        if self.grid[playedSpot[0]][playedSpot[1]-1] != 1:
                            if self.grid[playedSpot[0]+1][playedSpot[1]-2] != 1:
                                return True
                            
            elif playedSpot[1:] == [19, 0]:
                return False
                
            elif playedSpot[1:] == [19, 1]:
                if direction == 'SE':
                    #corner furthest from starting point (southeast on grid view)
                    
                    return False
                                            
                elif direction == 'NE':                            
                #corner northeast on grid view
                    if self.grid[playedSpot[0]-2][playedSpot[1]+1] != 1:
                        if self.grid[playedSpot[0]-1][playedSpot[1]+2] != 1:
                            if self.grid[playedSpot[0]][playedSpot[1]+1] != 1:
                                if self.grid[playedSpot[0]-1][playedSpot[1]] != 1:
                                    return True
                
                elif direction == 'NW':
                    if self.grid[playedSpot[0]-2][playedSpot[1]-1] != 1:
                        if self.grid[playedSpot[0]-1][playedSpot[1]] != 1:
                            if self.grid[playedSpot[0]][playedSpot[1]-1] != 1:
                                return True
                
                elif direction == 'SW':
                    
                    return False
                
            elif playedSpot[1:] == [19, 18]:
                if direction == 'SE':
                    #corner furthest from starting point (southeast on grid view)
                    
                    return False
                                            
                elif direction == 'NE':                            
                #corner northeast on grid view
                    if self.grid[playedSpot[0]-2][playedSpot[1]+1] != 1:
                        if self.grid[playedSpot[0]][playedSpot[1]+1] != 1:
                                if self.grid[playedSpot[0]-1][playedSpot[1]] != 1:
                                    return True
                
                elif direction == 'NW':
                    if self.grid[playedSpot[0]-2][playedSpot[1]-1] != 1:
                        if self.grid[playedSpot[0]-1][playedSpot[1]] != 1:
                            if self.grid[playedSpot[0]][playedSpot[1]-1] != 1:
                                if self.grid[playedSpot[0]-1][playedSpot[1]-2] != 1:
                                    return True
                
                elif direction == 'SW':
                    
                    return False
        
        return False
    
    def adjacentCheckPlayable(self, playedSpot, direction, placements):
        '''adjacentCheck method will be used within the cornerChoice method 
        to identify if all adjacent locations to the proposed cornerSpot have not been used by computer
        playedSpot will be a list of three items, item 2 will be row # and item 3 will be column #
        direction indicates which corner from the playedSpot will be evaluated. Options are northeast, southeast, northwest and southwest'''
        
        #before checking adjacency, identify potential indexerrors since the grid is only 20x20
        indexOOB = [0,1,18,19]
        
        indexError = []
        if playedSpot[0] not in indexOOB:
            indexError.append(False)
        else:
            indexError.append(True)
        
        if playedSpot[1] not in indexOOB:
            indexError.append(False)
        else:
            indexError.append(True)
            
        #this is the adjacent check for the grid spots with no index errors arising from the adjacent check
        if indexError == [False, False]:
            
            if direction == 'SE':
                #corner furthest from starting point (southeast on grid view)
                if self.grid[playedSpot[0]+2][playedSpot[1]+1] != 1 and [playedSpot[0]+2, playedSpot[1]+1] not in placements:
                    if self.grid[playedSpot[0]+1][playedSpot[1]+2] != 1 and [playedSpot[0]+1, playedSpot[1]+2] not in placements:
                        if self.grid[playedSpot[0]][playedSpot[1]+1] != 1 and [playedSpot[0], playedSpot[1]+1] not in placements:
                            if self.grid[playedSpot[0]+1][playedSpot[1]] != 1 and [playedSpot[0]+1, playedSpot[1]] not in placements:
                                return True
                                        
            elif direction == 'NE':                            
            #corner northeast on grid view
                if self.grid[playedSpot[0]-2][playedSpot[1]+1] != 1 and [playedSpot[0]-2, playedSpot[1]+1] not in placements:
                    if self.grid[playedSpot[0]-1][playedSpot[1]+2] != 1 and [playedSpot[0]-1, playedSpot[1]+2] not in placements:
                        if self.grid[playedSpot[0]][playedSpot[1]+1] != 1 and [playedSpot[0], playedSpot[1]+1] not in placements:
                            if self.grid[playedSpot[0]-1][playedSpot[1]] != 1 and [playedSpot[0]-1, playedSpot[1]] not in placements:
                                return True
            
            elif direction == 'NW':
                if self.grid[playedSpot[0]-2][playedSpot[1]-1] != 1 and [playedSpot[0]-2, playedSpot[1]-1] not in placements:
                    if self.grid[playedSpot[0]-1][playedSpot[1]] != 1 and [playedSpot[0]-1, playedSpot[1]] not in placements:
                        if self.grid[playedSpot[0]][playedSpot[1]-1] != 1 and [playedSpot[0], playedSpot[1]-1] not in placements:
                            if self.grid[playedSpot[0]-1][playedSpot[1]-2] != 1 and [playedSpot[0]-1, playedSpot[1]-2] not in placements:
                                return True
            
            elif direction == 'SW':
                if self.grid[playedSpot[0]+2][playedSpot[1]-1] != 1 and [playedSpot[0]+2, playedSpot[1]-1] not in placements:
                    if self.grid[playedSpot[0]+1][playedSpot[1]] != 1 and [playedSpot[0]+1, playedSpot[1]] not in placements:
                        if self.grid[playedSpot[0]][playedSpot[1]-1] != 1 and [playedSpot[0], playedSpot[1]-1] not in placements:
                            if self.grid[playedSpot[0]+1][playedSpot[1]-2] != 1 and [playedSpot[0]+1, playedSpot[1]-2] not in placements:
                                return True
        ####
        ####
        #### now for the corners with potential index errors for rows only
        elif indexError == [True, False]:
            if playedSpot[0] == 0:
                if direction == 'SE':
                    #corner furthest from starting point (southeast on grid view)
                    if self.grid[playedSpot[0]+2][playedSpot[1]+1] != 1 and [playedSpot[0]+2, playedSpot[1]+1] not in placements:
                        if self.grid[playedSpot[0]+1][playedSpot[1]+2] != 1 and [playedSpot[0]+1, playedSpot[1]+2] not in placements:
                            if self.grid[playedSpot[0]][playedSpot[1]+1] != 1 and [playedSpot[0], playedSpot[1]+1] not in placements:
                                if self.grid[playedSpot[0]+1][playedSpot[1]] != 1 and [playedSpot[0]+1, playedSpot[1]] not in placements:
                                    return True
                                        
                elif direction == 'NE':                            
                #corner northeast on grid view
                    return False
                
                elif direction == 'NW':
                    return False
                
                elif direction == 'SW':
                    if self.grid[playedSpot[0]+2][playedSpot[1]-1] != 1 and [playedSpot[0]+2, playedSpot[1]-1] not in placements:
                        if self.grid[playedSpot[0]+1][playedSpot[1]] != 1 and [playedSpot[0]+1, playedSpot[1]] not in placements:
                            if self.grid[playedSpot[0]][playedSpot[1]-1] != 1 and [playedSpot[0], playedSpot[1]-1] not in placements:
                                if self.grid[playedSpot[0]+1][playedSpot[1]-2] != 1 and [playedSpot[0]+1, playedSpot[1]-2] not in placements:
                                    return True
            elif playedSpot[0] == 1:
                if direction == 'SE':
                    #corner furthest from starting point (southeast on grid view)
                    if self.grid[playedSpot[0]+2][playedSpot[1]+1] != 1 and [playedSpot[0]+2, playedSpot[1]+1] not in placements:
                        if self.grid[playedSpot[0]+1][playedSpot[1]+2] != 1 and [playedSpot[0]+1, playedSpot[1]+2] not in placements:
                            if self.grid[playedSpot[0]][playedSpot[1]+1] != 1 and [playedSpot[0], playedSpot[1]+1] not in placements:
                                if self.grid[playedSpot[0]+1][playedSpot[1]] != 1 and [playedSpot[0]+1, playedSpot[1]] not in placements:
                                    return True
                                        
                elif direction == 'NE':                            
                #corner northeast on grid view
                    if self.grid[playedSpot[0]-1][playedSpot[1]+2] != 1 and [playedSpot[0]-1, playedSpot[1]+2] not in placements:
                        if self.grid[playedSpot[0]][playedSpot[1]+1] != 1 and [playedSpot[0], playedSpot[1]+1] not in placements:
                            if self.grid[playedSpot[0]-1][playedSpot[1]] != 1 and [playedSpot[0]-1, playedSpot[1]] not in placements:
                                return True
                
                elif direction == 'NW':
                    if self.grid[playedSpot[0]-1][playedSpot[1]] != 1 and [playedSpot[0]-1, playedSpot[1]] not in placements:
                        if self.grid[playedSpot[0]][playedSpot[1]-1] != 1 and [playedSpot[0], playedSpot[1]-1] not in placements:
                            if self.grid[playedSpot[0]-1][playedSpot[1]-2] != 1 and [playedSpot[0]-1, playedSpot[1]-2] not in placements:
                                return True
                
                elif direction == 'SW':
                    if self.grid[playedSpot[0]+2][playedSpot[1]-1] != 1 and [playedSpot[0]+2, playedSpot[1]-1] not in placements:
                        if self.grid[playedSpot[0]+1][playedSpot[1]] != 1 and [playedSpot[0]+1, playedSpot[1]] not in placements:
                            if self.grid[playedSpot[0]][playedSpot[1]-1] != 1 and [playedSpot[0], playedSpot[1]-1] not in placements:
                                if self.grid[playedSpot[0]+1][playedSpot[1]-2] != 1 and [playedSpot[0]+1, playedSpot[1]-2] not in placements:
                                    return True
        
            elif playedSpot[0] == 18:
        
                if direction == 'SE':
                    #corner furthest from starting point (southeast on grid view)
                    
                    if self.grid[playedSpot[0]+1][playedSpot[1]+2] != 1 and [playedSpot[0]+1, playedSpot[1]+2] not in placements:
                        if self.grid[playedSpot[0]][playedSpot[1]+1] != 1 and [playedSpot[0], playedSpot[1]+1] not in placements:
                            if self.grid[playedSpot[0]+1][playedSpot[1]] != 1 and [playedSpot[0]+1, playedSpot[1]] not in placements:
                                return True
                                            
                elif direction == 'NE':                            
                #corner northeast on grid view
                    if self.grid[playedSpot[0]-2][playedSpot[1]+1] != 1 and [playedSpot[0]-2, playedSpot[1]+1] not in placements:
                        if self.grid[playedSpot[0]-1][playedSpot[1]+2] != 1 and [playedSpot[0]-1, playedSpot[1]+2] not in placements:
                            if self.grid[playedSpot[0]][playedSpot[1]+1] != 1 and [playedSpot[0], playedSpot[1]+1] not in placements:
                                if self.grid[playedSpot[0]-1][playedSpot[1]] != 1 and [playedSpot[0]-1, playedSpot[1]] not in placements:
                                    return True
                
                elif direction == 'NW':
                    if self.grid[playedSpot[0]-2][playedSpot[1]-1] != 1 and [playedSpot[0]-2, playedSpot[1]-1] not in placements:
                        if self.grid[playedSpot[0]-1][playedSpot[1]] != 1 and [playedSpot[0]-1, playedSpot[1]] not in placements:
                            if self.grid[playedSpot[0]][playedSpot[1]-1] != 1 and [playedSpot[0], playedSpot[1]-1] not in placements:
                                if self.grid[playedSpot[0]-1][playedSpot[1]-2] != 1 and [playedSpot[0]-1, playedSpot[1]-2] not in placements:
                                    return True
                
                elif direction == 'SW':
                    
                    if self.grid[playedSpot[0]+1][playedSpot[1]] != 1 and [playedSpot[0]+1, playedSpot[1]] not in placements:
                        if self.grid[playedSpot[0]][playedSpot[1]-1] != 1 and [playedSpot[0], playedSpot[1]-1] not in placements:
                            if self.grid[playedSpot[0]+1][playedSpot[1]-2] != 1 and [playedSpot[0]+1, playedSpot[1]-2] not in placements:
                                return True
            else:
                if direction == 'SE':
                    #corner furthest from starting point (southeast on grid view)
                    
                    return False
                                            
                elif direction == 'NE':                            
                #corner northeast on grid view
                    if self.grid[playedSpot[0]-2][playedSpot[1]+1] != 1 and [playedSpot[0]-2, playedSpot[1]+1] not in placements:
                        if self.grid[playedSpot[0]-1][playedSpot[1]+2] != 1 and [playedSpot[0]-1, playedSpot[1]+2] not in placements:
                            if self.grid[playedSpot[0]][playedSpot[1]+1] != 1 and [playedSpot[0], playedSpot[1]+1] not in placements:
                                if self.grid[playedSpot[0]-1][playedSpot[1]] != 1 and [playedSpot[0]-1, playedSpot[1]] not in placements:
                                    return True
                
                elif direction == 'NW':
                    if self.grid[playedSpot[0]-2][playedSpot[1]-1] != 1 and [playedSpot[0]-2, playedSpot[1]-1] not in placements:
                        if self.grid[playedSpot[0]-1][playedSpot[1]] != 1 and [playedSpot[0]-1, playedSpot[1]] not in placements:
                            if self.grid[playedSpot[0]][playedSpot[1]-1] != 1 and [playedSpot[0], playedSpot[1]-1] not in placements:
                                if self.grid[playedSpot[0]-1][playedSpot[1]-2] != 1 and [playedSpot[0]-1, playedSpot[1]-2] not in placements:
                                    return True
                
                elif direction == 'SW':
                    
                    return False
        ####
        ####
        #### now for the corners with potential index errors for columns only
        elif indexError == [False, True]:
            if playedSpot[1] == 0:
                if direction == 'SE':
                    #corner furthest from starting point (southeast on grid view)
                    if self.grid[playedSpot[0]+2][playedSpot[1]+1] != 1 and [playedSpot[0]+2, playedSpot[1]+1] not in placements:
                        if self.grid[playedSpot[0]+1][playedSpot[1]+2] != 1 and [playedSpot[0]+1, playedSpot[1]+2] not in placements:
                            if self.grid[playedSpot[0]][playedSpot[1]+1] != 1 and [playedSpot[0], playedSpot[1]+1] not in placements:
                                if self.grid[playedSpot[0]+1][playedSpot[1]] != 1 and [playedSpot[0]+1, playedSpot[1]] not in placements:
                                    return True
                                        
                elif direction == 'NE':                            
                #corner northeast on grid view
                    if self.grid[playedSpot[0]-2][playedSpot[1]+1] != 1 and [playedSpot[0]-2, playedSpot[1]+1] not in placements:
                        if self.grid[playedSpot[0]-1][playedSpot[1]+2] != 1 and [playedSpot[0]-1, playedSpot[1]+2] not in placements:
                            if self.grid[playedSpot[0]][playedSpot[1]+1] != 1 and [playedSpot[0], playedSpot[1]+1] not in placements:
                                if self.grid[playedSpot[0]-1][playedSpot[1]] != 1 and [playedSpot[0]-1, playedSpot[1]] not in placements:
                                    return True
                
                elif direction == 'NW':
                    return False
                
                elif direction == 'SW':
                    return False
                
            elif playedSpot[1] == 1:
                if direction == 'SE':
                    #corner furthest from starting point (southeast on grid view)
                    if self.grid[playedSpot[0]+2][playedSpot[1]+1] != 1 and [playedSpot[0]+2, playedSpot[1]+1] not in placements:
                        if self.grid[playedSpot[0]+1][playedSpot[1]+2] != 1 and [playedSpot[0]+1, playedSpot[1]+2] not in placements:
                            if self.grid[playedSpot[0]][playedSpot[1]+1] != 1 and [playedSpot[0], playedSpot[1]+1] not in placements:
                                if self.grid[playedSpot[0]+1][playedSpot[1]] != 1 and [playedSpot[0]+1, playedSpot[1]] not in placements:
                                    return True
                                        
                elif direction == 'NE':                            
                #corner northeast on grid view
                    if self.grid[playedSpot[0]-2][playedSpot[1]+1] != 1 and [playedSpot[0]-2, playedSpot[1]+1] not in placements:
                        if self.grid[playedSpot[0]-1][playedSpot[1]+2] != 1 and [playedSpot[0]-1, playedSpot[1]+2] not in placements:
                            if self.grid[playedSpot[0]][playedSpot[1]+1] != 1 and [playedSpot[0], playedSpot[1]+1] not in placements:
                                if self.grid[playedSpot[0]-1][playedSpot[1]] != 1 and [playedSpot[0]-1, playedSpot[1]] not in placements:
                                    return True
                
                elif direction == 'NW':
                    if self.grid[playedSpot[0]-2][playedSpot[1]-1] != 1 and [playedSpot[0]-2, playedSpot[1]-1] not in placements:
                        if self.grid[playedSpot[0]-1][playedSpot[1]] != 1 and [playedSpot[0]-1, playedSpot[1]] not in placements:
                            if self.grid[playedSpot[0]][playedSpot[1]-1] != 1 and [playedSpot[0], playedSpot[1]-1] not in placements:
                                return True
                
                elif direction == 'SW':
                    if self.grid[playedSpot[0]+2][playedSpot[1]-1] != 1 and [playedSpot[0]+2, playedSpot[1]-1] not in placements:
                        if self.grid[playedSpot[0]+1][playedSpot[1]] != 1 and [playedSpot[0]+1, playedSpot[1]] not in placements:
                            if self.grid[playedSpot[0]][playedSpot[1]-1] != 1 and [playedSpot[0], playedSpot[1]-1] not in placements:
                                    return True
        
            elif playedSpot[1] == 18:
        
                if direction == 'SE':
                    #corner furthest from starting point (southeast on grid view)
                    if self.grid[playedSpot[0]+2][playedSpot[1]+1] != 1 and [playedSpot[0]+2, playedSpot[1]+1] not in placements:
                        if self.grid[playedSpot[0]][playedSpot[1]+1] != 1 and [playedSpot[0], playedSpot[1]+1] not in placements:
                            if self.grid[playedSpot[0]+1][playedSpot[1]] != 1 and [playedSpot[0]+1, playedSpot[1]] not in placements:
                                return True
                                                                
                elif direction == 'NE':                            
                #corner northeast on grid view
                    if self.grid[playedSpot[0]-2][playedSpot[1]+1] != 1 and [playedSpot[0]-2, playedSpot[1]+1] not in placements:
                        if self.grid[playedSpot[0]][playedSpot[1]+1] != 1 and [playedSpot[0], playedSpot[1]+1] not in placements:
                            if self.grid[playedSpot[0]-1][playedSpot[1]] != 1 and [playedSpot[0]-1, playedSpot[1]] not in placements:
                                return True
                
                elif direction == 'NW':
                    if self.grid[playedSpot[0]-2][playedSpot[1]-1] != 1 and [playedSpot[0]-2, playedSpot[1]-1] not in placements:
                        if self.grid[playedSpot[0]-1][playedSpot[1]] != 1 and [playedSpot[0]-1, playedSpot[1]] not in placements:
                            if self.grid[playedSpot[0]][playedSpot[1]-1] != 1 and [playedSpot[0], playedSpot[1]-1] not in placements:
                                if self.grid[playedSpot[0]-1][playedSpot[1]-2] != 1 and [playedSpot[0]-1, playedSpot[1]-2] not in placements:
                                    return True
                
                elif direction == 'SW':
                    
                    if self.grid[playedSpot[0]+2][playedSpot[1]-1] != 1 and [playedSpot[0]+2, playedSpot[1]-1] not in placements:
                        if self.grid[playedSpot[0]+1][playedSpot[1]] != 1 and [playedSpot[0]+1, playedSpot[1]] not in placements:
                            if self.grid[playedSpot[0]][playedSpot[1]-1] != 1 and [playedSpot[0], playedSpot[1]-1] not in placements:
                                if self.grid[playedSpot[0]+1][playedSpot[1]-2] != 1 and [playedSpot[0]+1, playedSpot[1]-2] not in placements:
                                    return True                                
            else:
                if direction == 'SE':
                    #corner furthest from starting point (southeast on grid view)
                    
                    return False
                                            
                elif direction == 'NE':                            
                    return False
                
                elif direction == 'NW':
                    if self.grid[playedSpot[0]-2][playedSpot[1]-1] != 1 and [playedSpot[0]-2, playedSpot[1]-1] not in placements:
                        if self.grid[playedSpot[0]-1][playedSpot[1]] != 1 and [playedSpot[0]-1, playedSpot[1]] not in placements:
                            if self.grid[playedSpot[0]][playedSpot[1]-1] != 1 and [playedSpot[0], playedSpot[1]-1] not in placements:
                                if self.grid[playedSpot[0]-1][playedSpot[1]-2] != 1 and [playedSpot[0]-1, playedSpot[1]-2] not in placements:
                                    return True
                
                elif direction == 'SW':
                    
                    if self.grid[playedSpot[0]+2][playedSpot[1]-1] != 1 and [playedSpot[0]+2, playedSpot[1]-1] not in placements:
                        if self.grid[playedSpot[0]+1][playedSpot[1]] != 1 and [playedSpot[0]+1, playedSpot[1]] not in placements:
                            if self.grid[playedSpot[0]][playedSpot[1]-1] != 1 and [playedSpot[0], playedSpot[1]-1] not in placements:
                                if self.grid[playedSpot[0]+1][playedSpot[1]-2] != 1 and [playedSpot[0]+1, playedSpot[1]-2] not in placements:
                                    return True
        ####
        ####
        #### now for the corners with potential index errors for columns and rows
        elif indexError == [False, False]:
            if playedSpot[1:] == [0,0]:
                return False
            elif playedSpot[1:] == [19,19]:
                return False
            elif playedSpot[1:] == [0,1]:
                if direction == 'SE':
                    #corner furthest from starting point (southeast on grid view)
                    if self.grid[playedSpot[0]+2][playedSpot[1]+1] != 1 and [playedSpot[0]+2, playedSpot[1]+1] not in placements:
                        if self.grid[playedSpot[0]+1][playedSpot[1]+2] != 1 and [playedSpot[0]+1, playedSpot[1]+2] not in placements:
                            if self.grid[playedSpot[0]][playedSpot[1]+1] != 1 and [playedSpot[0], playedSpot[1]+1] not in placements:
                                if self.grid[playedSpot[0]+1][playedSpot[1]] != 1 and [playedSpot[0]+1, playedSpot[1]] not in placements:
                                    return True                                           
                elif direction == 'NE':                            
                    return False
                
                elif direction == 'NW':
                    return False
                
                elif direction == 'SW':
                    if self.grid[playedSpot[0]+2][playedSpot[1]-1] != 1 and [playedSpot[0]+2, playedSpot[1]-1] not in placements:
                        if self.grid[playedSpot[0]+1][playedSpot[1]] != 1 and [playedSpot[0]+1, playedSpot[1]] not in placements:
                            if self.grid[playedSpot[0]][playedSpot[1]-1] != 1 and [playedSpot[0], playedSpot[1]-1] not in placements:
                                return True
                
            elif playedSpot[1:] == [0, 18]:
                if direction == 'SE':
                    #corner furthest from starting point (southeast on grid view)
                    if self.grid[playedSpot[0]+2][playedSpot[1]+1] != 1 and [playedSpot[0]+2, playedSpot[1]+1] not in placements:
                        if self.grid[playedSpot[0]][playedSpot[1]+1] != 1 and [playedSpot[0], playedSpot[1]+1] not in placements:
                                if self.grid[playedSpot[0]+1][playedSpot[1]] != 1 and [playedSpot[0]+1, playedSpot[1]] not in placements:
                                    return True                                           
                elif direction == 'NE':                            
                    return False
                
                elif direction == 'NW':
                    return False
                
                elif direction == 'SW':
                    if self.grid[playedSpot[0]+2][playedSpot[1]-1] != 1 and [playedSpot[0]+2, playedSpot[1]-1] not in placements:
                        if self.grid[playedSpot[0]+1][playedSpot[1]] != 1 and [playedSpot[0]+1, playedSpot[1]] not in placements:
                            if self.grid[playedSpot[0]][playedSpot[1]-1] != 1 and [playedSpot[0], playedSpot[1]-1] not in placements:
                                if self.grid[playedSpot[0]+1][playedSpot[1]-2] != 1 and [playedSpot[0]+1, playedSpot[1]-2] not in placements:
                                    return True
               
            elif playedSpot[1:] == [0,19]:
                return False
            
            elif playedSpot[1:] == [1,0]:
                if direction == 'SE':
                   if self.grid[playedSpot[0]+2][playedSpot[1]+1] != 1 and [playedSpot[0]+2, playedSpot[1]+1] not in placements:
                        if self.grid[playedSpot[0]+1][playedSpot[1]+2] != 1 and [playedSpot[0]+1, playedSpot[1]+2] not in placements:
                            if self.grid[playedSpot[0]][playedSpot[1]+1] != 1 and [playedSpot[0], playedSpot[1]+1] not in placements:
                                if self.grid[playedSpot[0]+1][playedSpot[1]] != 1 and [playedSpot[0]+1, playedSpot[1]] not in placements:
                                    return True                                       
                elif direction == 'NE':                            
                    return False
                
                elif direction == 'NW':
                    return False
                
                elif direction == 'SW':
                   return False
                                
            elif playedSpot[1:] == [1,1]:
                if direction == 'SE':
                   if self.grid[playedSpot[0]+2][playedSpot[1]+1] != 1 and [playedSpot[0]+2, playedSpot[1]+1] not in placements:
                        if self.grid[playedSpot[0]+1][playedSpot[1]+2] != 1 and [playedSpot[0]+1, playedSpot[1]+2] not in placements:
                            if self.grid[playedSpot[0]][playedSpot[1]+1] != 1 and [playedSpot[0], playedSpot[1]+1] not in placements:
                                if self.grid[playedSpot[0]+1][playedSpot[1]] != 1 and [playedSpot[0]+1, playedSpot[1]] not in placements:
                                    return True                                       
                elif direction == 'NE':                            
                    if self.grid[playedSpot[0]][playedSpot[1]+1] != 1 and [playedSpot[0], playedSpot[1]+1] not in placements:
                            if self.grid[playedSpot[0]-1][playedSpot[1]] != 1 and [playedSpot[0]-1, playedSpot[1]] not in placements:
                                return True
                
                elif direction == 'NW':
                    return False
                
                elif direction == 'SW':
                   if self.grid[playedSpot[0]+2][playedSpot[1]-1] != 1 and [playedSpot[0]+2, playedSpot[1]-1] not in placements:
                        if self.grid[playedSpot[0]+1][playedSpot[1]] != 1 and [playedSpot[0]+1, playedSpot[1]] not in placements:
                            if self.grid[playedSpot[0]][playedSpot[1]-1] != 1 and [playedSpot[0], playedSpot[1]-1] not in placements:
                                return True
               
            elif playedSpot[1:] == [1,18]:
                if direction == 'SE':
                   if self.grid[playedSpot[0]+2][playedSpot[1]+1] != 1 and [playedSpot[0]+2, playedSpot[1]+1] not in placements:
                        if self.grid[playedSpot[0]][playedSpot[1]+1] != 1 and [playedSpot[0], playedSpot[1]+1] not in placements:
                                if self.grid[playedSpot[0]+1][playedSpot[1]] != 1 and [playedSpot[0]+1, playedSpot[1]] not in placements:
                                    return True                                       
                elif direction == 'NE':                            
                    return False
                
                elif direction == 'NW':
                    if self.grid[playedSpot[0]-1][playedSpot[1]] != 1 and [playedSpot[0]-1, playedSpot[1]] not in placements:
                        if self.grid[playedSpot[0]][playedSpot[1]-1] != 1 and [playedSpot[0], playedSpot[1]-1] not in placements:
                            if self.grid[playedSpot[0]-1][playedSpot[1]-2] != 1 and [playedSpot[0]-1, playedSpot[1]-2] not in placements:
                                return True
                
                elif direction == 'SW':
                   if self.grid[playedSpot[0]+2][playedSpot[1]-1] != 1 and [playedSpot[0]+2, playedSpot[1]-1] not in placements:
                        if self.grid[playedSpot[0]+1][playedSpot[1]] != 1 and [playedSpot[0]+1, playedSpot[1]] not in placements:
                            if self.grid[playedSpot[0]][playedSpot[1]-1] != 1 and [playedSpot[0], playedSpot[1]-1] not in placements:
                                if self.grid[playedSpot[0]+1][playedSpot[1]-2] != 1 and [playedSpot[0]+1, playedSpot[1]-2] not in placements:
                                    return True
                                
            elif playedSpot[1:] == [1,19]:
                if direction == 'SE':
                   return False
                                       
                elif direction == 'NE':                            
                    return False
                
                elif direction == 'NW':
                    if self.grid[playedSpot[0]-1][playedSpot[1]] != 1 and [playedSpot[0]-1, playedSpot[1]] not in placements:
                        if self.grid[playedSpot[0]][playedSpot[1]-1] != 1 and [playedSpot[0], playedSpot[1]-1] not in placements:
                            if self.grid[playedSpot[0]-1][playedSpot[1]-2] != 1 and [playedSpot[0]-1, playedSpot[1]-2] not in placements:
                                return True
                
                elif direction == 'SW':
                   if self.grid[playedSpot[0]+2][playedSpot[1]-1] != 1 and [playedSpot[0]+2, playedSpot[1]-1] not in placements:
                        if self.grid[playedSpot[0]+1][playedSpot[1]] != 1 and [playedSpot[0]+1, playedSpot[1]] not in placements:
                            if self.grid[playedSpot[0]][playedSpot[1]-1] != 1 and [playedSpot[0], playedSpot[1]-1] not in placements:
                                if self.grid[playedSpot[0]+1][playedSpot[1]-2] != 1 and [playedSpot[0]+1, playedSpot[1]-2] not in placements:
                                    return True
                                
            elif playedSpot[1:] == [18, 0]:
                if direction == 'SE':
                    #corner furthest from starting point (southeast on grid view)
                    
                    if self.grid[playedSpot[0]+1][playedSpot[1]+2] != 1 and [playedSpot[0]+1, playedSpot[1]+2] not in placements:
                        if self.grid[playedSpot[0]][playedSpot[1]+1] != 1 and [playedSpot[0], playedSpot[1]+1] not in placements:
                            if self.grid[playedSpot[0]+1][playedSpot[1]] != 1 and [playedSpot[0]+1, playedSpot[1]] not in placements:
                                return True
                                            
                elif direction == 'NE':                            
                #corner northeast on grid view
                    if self.grid[playedSpot[0]-2][playedSpot[1]+1] != 1 and [playedSpot[0]-2, playedSpot[1]+1] not in placements:
                        if self.grid[playedSpot[0]-1][playedSpot[1]+2] != 1 and [playedSpot[0]-1, playedSpot[1]+2] not in placements:
                            if self.grid[playedSpot[0]][playedSpot[1]+1] != 1 and [playedSpot[0], playedSpot[1]+1] not in placements:
                                if self.grid[playedSpot[0]-1][playedSpot[1]] != 1 and [playedSpot[0]-1, playedSpot[1]] not in placements:
                                    return True
                
                elif direction == 'NW':
                    return False
                
                elif direction == 'SW':
                    
                    return False
                            
            elif playedSpot[1:] == [18, 1]:
                if direction == 'SE':
                    #corner furthest from starting point (southeast on grid view)
                    
                    if self.grid[playedSpot[0]+1][playedSpot[1]+2] != 1 and [playedSpot[0]+1, playedSpot[1]+2] not in placements:
                        if self.grid[playedSpot[0]][playedSpot[1]+1] != 1 and [playedSpot[0], playedSpot[1]+1] not in placements:
                            if self.grid[playedSpot[0]+1][playedSpot[1]] != 1 and [playedSpot[0]+1, playedSpot[1]] not in placements:
                                return True
                                            
                elif direction == 'NE':                            
                #corner northeast on grid view
                    if self.grid[playedSpot[0]-2][playedSpot[1]+1] != 1 and [playedSpot[0]-2, playedSpot[1]+1] not in placements:
                        if self.grid[playedSpot[0]-1][playedSpot[1]+2] != 1 and [playedSpot[0]-1, playedSpot[1]+2] not in placements:
                            if self.grid[playedSpot[0]][playedSpot[1]+1] != 1 and [playedSpot[0], playedSpot[1]+1] not in placements:
                                if self.grid[playedSpot[0]-1][playedSpot[1]] != 1 and [playedSpot[0]-1, playedSpot[1]] not in placements:
                                    return True
                
                elif direction == 'NW':
                    if self.grid[playedSpot[0]-2][playedSpot[1]-1] != 1 and [playedSpot[0]-2, playedSpot[1]-1] not in placements:
                        if self.grid[playedSpot[0]-1][playedSpot[1]] != 1 and [playedSpot[0]-1, playedSpot[1]] not in placements:
                            if self.grid[playedSpot[0]][playedSpot[1]-1] != 1 and [playedSpot[0], playedSpot[1]-1] not in placements:
                                return True
                
                elif direction == 'SW':
                    
                    if self.grid[playedSpot[0]+1][playedSpot[1]] != 1 and [playedSpot[0]+1, playedSpot[1]] not in placements:
                        if self.grid[playedSpot[0]][playedSpot[1]-1] != 1 and [playedSpot[0], playedSpot[1]-1] not in placements:
                            return True
                            
            elif playedSpot[1:] == [18, 18]:
                if direction == 'SE':
                    #corner furthest from starting point (southeast on grid view)
                    
                    if self.grid[playedSpot[0]][playedSpot[1]+1] != 1 and [playedSpot[0], playedSpot[1]+1] not in placements:
                            if self.grid[playedSpot[0]+1][playedSpot[1]] != 1 and [playedSpot[0]+1, playedSpot[1]] not in placements:
                                return True
                                            
                elif direction == 'NE':                            
                #corner northeast on grid view
                    if self.grid[playedSpot[0]-2][playedSpot[1]+1] != 1 and [playedSpot[0]-2, playedSpot[1]+1] not in placements:
                        if self.grid[playedSpot[0]][playedSpot[1]+1] != 1 and [playedSpot[0], playedSpot[1]+1] not in placements:
                                if self.grid[playedSpot[0]-1][playedSpot[1]] != 1 and [playedSpot[0]-1, playedSpot[1]] not in placements:
                                    return True
                
                elif direction == 'NW':
                    if self.grid[playedSpot[0]-2][playedSpot[1]-1] != 1 and [playedSpot[0]-2, playedSpot[1]-1] not in placements:
                        if self.grid[playedSpot[0]-1][playedSpot[1]] != 1 and [playedSpot[0]-1, playedSpot[1]] not in placements:
                            if self.grid[playedSpot[0]][playedSpot[1]-1] != 1 and [playedSpot[0], playedSpot[1]-1] not in placements:
                                if self.grid[playedSpot[0]-1][playedSpot[1]-2] != 1 and [playedSpot[0]-1, playedSpot[1]-2] not in placements:
                                    return True
                
                elif direction == 'SW':
                    
                    if self.grid[playedSpot[0]+1][playedSpot[1]] != 1 and [playedSpot[0]+1, playedSpot[1]] not in placements:
                        if self.grid[playedSpot[0]][playedSpot[1]-1] != 1 and [playedSpot[0], playedSpot[1]-1] not in placements:
                            if self.grid[playedSpot[0]+1][playedSpot[1]-2] != 1 and [playedSpot[0]+1, playedSpot[1]-2] not in placements:
                                return True
                            
            elif playedSpot[1:] == [18, 19]:
                if direction == 'SE':
                    #corner furthest from starting point (southeast on grid view)
                    
                    return False
                                            
                elif direction == 'NE':                            
                    return False
                
                elif direction == 'NW':
                    if self.grid[playedSpot[0]-2][playedSpot[1]-1] != 1 and [playedSpot[0]-2, playedSpot[1]-1] not in placements:
                        if self.grid[playedSpot[0]-1][playedSpot[1]] != 1 and [playedSpot[0]-1, playedSpot[1]] not in placements:
                            if self.grid[playedSpot[0]][playedSpot[1]-1] != 1 and [playedSpot[0], playedSpot[1]-1] not in placements:
                                if self.grid[playedSpot[0]-1][playedSpot[1]-2] != 1 and [playedSpot[0]-1, playedSpot[1]-2] not in placements:
                                    return True
                
                elif direction == 'SW':
                    
                    if self.grid[playedSpot[0]+1][playedSpot[1]] != 1 and [playedSpot[0]+1, playedSpot[1]] not in placements:
                        if self.grid[playedSpot[0]][playedSpot[1]-1] != 1 and [playedSpot[0], playedSpot[1]-1] not in placements:
                            if self.grid[playedSpot[0]+1][playedSpot[1]-2] != 1 and [playedSpot[0]+1, playedSpot[1]-2] not in placements:
                                return True
                            
            elif playedSpot[1:] == [19, 0]:
                return False
                
            elif playedSpot[1:] == [19, 1]:
                if direction == 'SE':
                    #corner furthest from starting point (southeast on grid view)
                    
                    return False
                                            
                elif direction == 'NE':                            
                #corner northeast on grid view
                    if self.grid[playedSpot[0]-2][playedSpot[1]+1] != 1 and [playedSpot[0]-2, playedSpot[1]+1] not in placements:
                        if self.grid[playedSpot[0]-1][playedSpot[1]+2] != 1 and [playedSpot[0]-1, playedSpot[1]+2] not in placements:
                            if self.grid[playedSpot[0]][playedSpot[1]+1] != 1 and [playedSpot[0], playedSpot[1]+1] not in placements:
                                if self.grid[playedSpot[0]-1][playedSpot[1]] != 1 and [playedSpot[0]-1, playedSpot[1]] not in placements:
                                    return True
                
                elif direction == 'NW':
                    if self.grid[playedSpot[0]-2][playedSpot[1]-1] != 1 and [playedSpot[0]-2, playedSpot[1]-1] not in placements:
                        if self.grid[playedSpot[0]-1][playedSpot[1]] != 1 and [playedSpot[0]-1, playedSpot[1]] not in placements:
                            if self.grid[playedSpot[0]][playedSpot[1]-1] != 1 and [playedSpot[0], playedSpot[1]-1] not in placements:
                                return True
                
                elif direction == 'SW':
                    
                    return False
                
            elif playedSpot[1:] == [19, 18]:
                if direction == 'SE':
                    #corner furthest from starting point (southeast on grid view)
                    
                    return False
                                            
                elif direction == 'NE':                            
                #corner northeast on grid view
                    if self.grid[playedSpot[0]-2][playedSpot[1]+1] != 1 and [playedSpot[0]-2, playedSpot[1]+1] not in placements:
                        if self.grid[playedSpot[0]][playedSpot[1]+1] != 1 and [playedSpot[0], playedSpot[1]+1] not in placements:
                                if self.grid[playedSpot[0]-1][playedSpot[1]] != 1 and [playedSpot[0]-1, playedSpot[1]] not in placements:
                                    return True
                
                elif direction == 'NW':
                    if self.grid[playedSpot[0]-2][playedSpot[1]-1] != 1 and [playedSpot[0]-2, playedSpot[1]-1] not in placements:
                        if self.grid[playedSpot[0]-1][playedSpot[1]] != 1 and [playedSpot[0]-1, playedSpot[1]] not in placements:
                            if self.grid[playedSpot[0]][playedSpot[1]-1] != 1 and [playedSpot[0], playedSpot[1]-1] not in placements:
                                if self.grid[playedSpot[0]-1][playedSpot[1]-2] != 1 and [playedSpot[0]-1, playedSpot[1]-2] not in placements:
                                    return True
                
                elif direction == 'SW':
                    
                    return False
        
        return False
    
    
    def pieceAlign(self, corner, edge):
        ''' detect the first 'one' in the blokus piece array by searching for the 2.
        align piece from starting spot onto grid based on corner.
        ignore index out of range issues for now'''
        
        squares = self.getSquares()
        piece = self.getDim()
        
        counter1 = 0
        counter2 = 0
        pieceSpot = []
        
        pieceCount = 0
        
        #find the fixed piece origin. This is marked as a 2 in the piece
        
        while 1 != pieceCount:
            #identify the indices of blokus piece
            if piece[counter1][counter2] == edge:
                pieceCount += 1
                pieceSpot.append([counter1,counter2])
                     
            #increment to move through 5x5 array
            counter2 += 1
            
            #when counter1 reaches five, reset counter1 to zero and increment counter2
            if counter2 == 5:
                counter2 = 0
                counter1 += 1
        
        counter1 = 0
        counter2 = 0
        
        #find the remaining pieces in the blokus piece
        while squares != pieceCount:
            #identify the indices of blokus piece
            if piece[counter1][counter2] != edge and piece[counter1][counter2] != 0:
                pieceCount += 1
                pieceSpot.append([counter1,counter2])
                     
            #increment to move through 5x5 array
            counter2 += 1
            
            #when counter1 reaches five, reset counter1 to zero and increment counter2
            if counter2 == 5:
                counter2 = 0
                counter1 += 1
                
              
        pieceLocations = pieceSpot
        
        #relate pieceSpots to one another
        
        rowSubtract = pieceLocations[0][0]
        colSubtract = pieceLocations[0][1]
        
        
        
        for i in range(squares):
            for j in range(2):
                if j % 2 == 0:
                    pieceLocations[i][j] -= rowSubtract
                if j % 2 == 1:
                    pieceLocations[i][j] -= colSubtract
        
        #working with the first identified piece as the corner piece,
        #add the corner dimensions to each pieceLocation
        
        for i in range(squares):
            for j in range(2):
                if j % 2 == 0:
                    pieceLocations[i][j] += corner[0]
                if j % 2 == 1:
                    pieceLocations[i][j] += corner[1]
        
        return pieceLocations
    
    def pieceFit(self, placements):
        '''check if the piece will fit into the grid
            check there's no index range issues 
            check that the board has opening in those places where the piece will land
            and finally, check to make sure that there are no pieces adjacently placed'''
        
        squares = len(placements)
        
        #first part - check that there's no index range errors
        
        for i in range(squares):
            for j in range(2):
                try:
                    if placements[i][j] < 0 or placements[i][j] > 19:
                        return False
                except IndexError:
                    
                    return None
                
        #second part - check that the board's grid has opening in those spaces
        grid = Board.getGrid(self)
        
        for i in range(squares):
            if grid[placements[i][0]][placements[i][1]] != 0:
                return False
        
        #third part - check to make sure that the new pieces will not be adjacent to any existing computer pieces
        for i in range(squares):
                
                #for squares along walls/corners, index range will arise.
                #the following addresses the index issues and checks for adjacent placements
                
            if placements[i][0] != 0 and placements[i][1] != 0 and placements[i][0] != 19 and placements[i][1] != 19:
                                      
                if self.grid[placements[i][0]+1][placements[i][1]] == 1:
                    return False
                if self.grid[placements[i][0]][placements[i][1]+1] == 1:
                    return False
                if self.grid[placements[i][0]][placements[i][1]-1] == 1:
                    return False
                if self.grid[placements[i][0]-1][placements[i][1]] == 1:
                    return False
            
            elif placements[i][0] == 0 and placements[i][1] == 19:
                if self.grid[placements[i][0]+1][placements[i][1]] == 1:
                    return False
                if self.grid[placements[i][0]][placements[i][1]-1] == 1:
                    return False
            
            elif placements[i][0] == 19 and placements[i][1] == 0:
                if self.grid[placements[i][0]][placements[i][1]+1] == 1:
                    return False
                if self.grid[placements[i][0]][placements[i][1]-1] == 1:
                    return False
            
            elif placements[i][0] == 0:
                if self.grid[placements[i][0]+1][placements[i][1]] == 1:
                    return False
                if self.grid[placements[i][0]][placements[i][1]+1] == 1:
                    return False
                if self.grid[placements[i][0]][placements[i][1]-1] == 1:
                    return False
            
            elif placements[i][1] == 0:
                if self.grid[placements[i][0]+1][placements[i][1]] == 1:
                    return False
                if self.grid[placements[i][0]][placements[i][1]+1] == 1:
                    return False
                if self.grid[placements[i][0]-1][placements[i][1]] == 1:
                    return False                
            
            elif placements[i][0] == 19 and placements[i][1] == 19:
                if self.grid[placements[i][0]-1][placements[i][1]] == 1:
                    return False
                if self.grid[placements[i][0]][placements[i][1]-1] == 1:
                    return False
            
            elif placements[i][0] == 19:
                if self.grid[placements[i][0]-1][placements[i][1]] == 1:
                    return False
                if self.grid[placements[i][0]][placements[i][1]+1] == 1:
                    return False
                if self.grid[placements[i][0]][placements[i][1]-1] == 1:
                    return False
                
            elif placements[i][1] == 19:
                if self.grid[placements[i][0]-1][placements[i][1]] == 1:
                    return False
                if self.grid[placements[i][0]+1][placements[i][1]] == 1:
                    return False
                if self.grid[placements[i][0]][placements[i][1]-1] == 1:
                    return False
            
        return True
    
practiceBoard = Board()

Board._registry

len(Board._registry)

#practiceBoard.playPiece(corner = practiceBoard.cornerChoice())

practiceBoard.getGrid()

len(practiceBoard._registry)

#practiceBoard.playPieceConsolidated()

#practiceBoard.pieceList()





