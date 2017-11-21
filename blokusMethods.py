import random

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
            
    def __str__(self):
        return '{} {} {}'.format(self.name, self.squares, self.dim)
    
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
        
class Board(object):
            
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
    
    def humanPlay(self, click):
        '''for use with tkinter gui. For human player's moves.
        Will take left click in gui and add a '2' to the board's grid at the coordinates that were clicked
        since tkinter grid goes from 1 to 20 instead of 0 to 19, subtract coords by 1
        '''
        coordinates = [int(click[0])-1, int(click[1])-1]
        print(coordinates)
        self.grid[coordinates[0]][coordinates[1]] = 2
        
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
        
    
    def playPiece(self, corner, blokusPiece = BlokusPiece.pieceList(), pieceCounter = 0, cornerCounter = 0):
        '''this module puts together one move to play on the Board. Combines other modules
        
        blokusPiece is taken from the BlokusPiece.piecelist. It includes three items per piece. 
        The third item is the instance data.
        
        pieceCounter variable will be used at the bottom for recursive calls to get new blokusPieces
        
        cornerCounter variable will be used at the bottom for recursive calls to get new corners to play off of
        '''
        #make sure there are other pieces left to play. If no pieces are left, it's game over
        try:
            if len(blokusPiece) < 1:
                return None
        except TypeError:
            #print(blokusPiece)
            return None

              
        #align the blokus piece to fit into the grid dim.
        #note that the third item in the list for blokusPiece is the instance data, 
            #which is why there is a [2] index
        try:
            placements = Board.pieceAlign(blokusPiece[pieceCounter][2], corner[cornerCounter], 2)
            #print('line 197', placements)
            #print('placements are:', placements)
        #if the corner produces an out of range index, look for a new corner
        except TypeError:
            #print(corner, 'corner is')
            #print('blokus piece', blokusPiece)
            #print('piece counter', pieceCounter)
            pass
        
        #check if the piece fits the grid 
        try:
            
            if Board.pieceFit(self, placements):
            
                #print('piece fits!')
                #fit piece onto 20x20 grid
                #mount piece onto grid
                for i in range(len(placements[0])):
                    self.grid[placements[0][i][0]][placements[0][i][1]] = 1
            
                #remove blokus piece
                BlokusPiece.removeReg(blokusPiece[pieceCounter][2])
                
                return placements
        
            #if the piece doesn't fit, try rotating the piece to see if it works. Rotate three times.
            else:
                #print('piece aint fittin. Rotatin it')
                #print(self.grid)
                for edgeCount in range(2,blokusPiece[pieceCounter][3]+1):
                    
                    #on the second run through all the rotations, going to mirror the piece to get more fit options for asymmetrical pieces
                    for m in range(0,2):
                        
                        if m%2 == 1:
                            blokusPiece[pieceCounter][2].mirror()
                        
                        for i in range(0,4):
                                                           
                            placements = Board.pieceAlign(blokusPiece[pieceCounter][2].rotate(), corner[cornerCounter], edgeCount)
                            #print('line 236', placements)
                            #in the event that the placement works, then mount the piece on the board and remove the piece from the list
                            if Board.pieceFit(self, placements):
                                #print('rotated piece fits!')
                                #fit piece onto 20x20 grid
                                #mount piece onto grid
                                for j in range(len(placements[0])):
                                    self.grid[placements[0][j][0]][placements[0][j][1]] = 1
                            
                                #remove blokus piece
                                BlokusPiece.removeReg(blokusPiece[pieceCounter][2])
                                
                                return placements
        except UnboundLocalError:
            #print(corner, blokusPiece, pieceCounter, cornerCounter, 'unboundlocalerror!')
            return None
                      
        #in the event that the piece doesn't fit after being rotated, get a new piece to try to fit in corner
        #While not an iron clad rule, it's often best practice to play the largest pieces when you can.
        #as a result, if the next piece is going to move down in size, it would preferable to look for a new corner
        #additionally, in starting a new corner, revert back to the top of the blokus piecelist
        try:
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
        
        #in the event of an index error, the computer should look for a new corner to play
        except IndexError:
            #print('line 274 index error') 
            pass
        return None
    
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
                        playedSpots.append([(i+j)/2, i, j])
                        
            #print('playedSpots', playedSpots)
            
            
            #for each played spot, produce as many corner locations that are not adjacent to any existing pieces
            cornerSpots = []
            direction = ['NE', 'SE', 'NW', 'SW']
            for i in range(len(playedSpots)):
                for d in direction:
                    if Board.cornerCheck(self, playedSpots[i], d):
                        
                        if Board.adjacentCheck(self, playedSpots[i], d):
                            if d == 'NE':
                                cornerSpots.append([(playedSpots[i][1]-1) + (playedSpots[i][2]+1)/2, playedSpots[i][1]-1, playedSpots[i][2]+1])
                            elif d == 'SE':
                                cornerSpots.append([(playedSpots[i][1]+1) + (playedSpots[i][2]+1)/2, playedSpots[i][1]+1, playedSpots[i][2]+1])
                            elif d == 'NW':
                                cornerSpots.append([(playedSpots[i][1]-1) + (playedSpots[i][2]-1)/2, playedSpots[i][1]-1, playedSpots[i][2]-1])
                            else:
                                cornerSpots.append([(playedSpots[i][1]+1) + (playedSpots[i][2]-1)/2, playedSpots[i][1]+1, playedSpots[i][2]-1])
            
            #remove cornerSpots that are not in range
            removeList = []
            for item in cornerSpots:
                if item[1] < 0:
                    removeList.append(item)
                    continue
                if item[2] < 0:
                    removeList.append(item)
                    continue
                if item[2] > 19:
                    removeList.append(item)
                    continue
                if item[2] > 19:
                    removeList.append(item)
                                   
            cornerSpots[:] = [x for x in cornerSpots if x not in removeList]
            
            #to make the computer's a little more unpredictable, we will add an rng number to the average row/column total before sorting
            random.seed()
            
            randList = []
            for i in range(len(cornerSpots)):
                #for the randomization, using a normal dist with mu of 10 and sigma 1.5. This will allow for some variation but not a whole lot.
                randList.append(random.normalvariate(10, 2))
            
            for i in range(len(cornerSpots)):
                cornerSpots[i][0] = cornerSpots[i][0]+randList[i]
            
                     
            cornerSpots.sort(reverse = True)
            #print('cornerSpots', cornerSpots)              
            corners = []
            for i in range(len(cornerSpots)):
                corners.append(cornerSpots[i][1:])                    
            
            #print(corners)
            #return the list of corner spots arranged in order of distance from starting position
            return corners
    
    def cornerCheck(self, playedSpot, direction):
        '''check that the corner to be played is available for play'''
        
        if direction == 'SE':
            try:
                
                if self.grid[playedSpot[1]+1][playedSpot[2]+1] == 0:
                    return True
            except IndexError:
                return False
        elif direction == 'NE':
            try:
                
                if self.grid[playedSpot[1]-1][playedSpot[2]+1] == 0:
                    return True
            except IndexError:
                return False
        if direction == 'SW':
            try:
                
                if self.grid[playedSpot[1]+1][playedSpot[2]-1] == 0:
                    return True
            except IndexError:
                return False
        if direction == 'NW':
            try:
                
                if self.grid[playedSpot[1]-1][playedSpot[2]-1] == 0:
                    return True
            except IndexError:
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
        if playedSpot[1] not in indexOOB:
            indexError.append(False)
        else:
            indexError.append(True)
        
        if playedSpot[2] not in indexOOB:
            indexError.append(False)
        else:
            indexError.append(True)
            
        #this is the adjacent check for the grid spots with no index errors arising from the adjacent check
        if indexError == [False, False]:
            
            if direction == 'SE':
                #corner furthest from starting point (southeast on grid view)
                if self.grid[playedSpot[1]+2][playedSpot[2]+1] != 1:
                    if self.grid[playedSpot[1]+1][playedSpot[2]+2] != 1:
                        if self.grid[playedSpot[1]][playedSpot[2]+1] != 1:
                            if self.grid[playedSpot[1]+1][playedSpot[2]] != 1:
                                return True
                                        
            elif direction == 'NE':                            
            #corner northeast on grid view
                if self.grid[playedSpot[1]-2][playedSpot[2]+1] != 1:
                    if self.grid[playedSpot[1]-1][playedSpot[2]+2] != 1:
                        if self.grid[playedSpot[1]][playedSpot[2]+1] != 1:
                            if self.grid[playedSpot[1]-1][playedSpot[2]] != 1:
                                return True
            
            elif direction == 'NW':
                if self.grid[playedSpot[1]-2][playedSpot[2]-1] != 1:
                    if self.grid[playedSpot[1]-1][playedSpot[2]] != 1:
                        if self.grid[playedSpot[1]][playedSpot[2]-1] != 1:
                            if self.grid[playedSpot[1]-1][playedSpot[2]-2] != 1:
                                return True
            
            elif direction == 'SW':
                if self.grid[playedSpot[1]+2][playedSpot[2]-1] != 1:
                    if self.grid[playedSpot[1]+1][playedSpot[2]] != 1:
                        if self.grid[playedSpot[1]][playedSpot[2]-1] != 1:
                            if self.grid[playedSpot[1]+1][playedSpot[2]-2] != 1:
                                return True
        ####
        ####
        #### now for the corners with potential index errors for rows only
        elif indexError == [True, False]:
            if playedSpot[1] == 0:
                if direction == 'SE':
                    #corner furthest from starting point (southeast on grid view)
                    if self.grid[playedSpot[1]+2][playedSpot[2]+1] != 1:
                        if self.grid[playedSpot[1]+1][playedSpot[2]+2] != 1:
                            if self.grid[playedSpot[1]][playedSpot[2]+1] != 1:
                                if self.grid[playedSpot[1]+1][playedSpot[2]] != 1:
                                    return True
                                        
                elif direction == 'NE':                            
                #corner northeast on grid view
                    return False
                
                elif direction == 'NW':
                    return False
                
                elif direction == 'SW':
                    if self.grid[playedSpot[1]+2][playedSpot[2]-1] != 1:
                        if self.grid[playedSpot[1]+1][playedSpot[2]] != 1:
                            if self.grid[playedSpot[1]][playedSpot[2]-1] != 1:
                                if self.grid[playedSpot[1]+1][playedSpot[2]-2] != 1:
                                    return True
            elif playedSpot[1] == 1:
                if direction == 'SE':
                    #corner furthest from starting point (southeast on grid view)
                    if self.grid[playedSpot[1]+2][playedSpot[2]+1] != 1:
                        if self.grid[playedSpot[1]+1][playedSpot[2]+2] != 1:
                            if self.grid[playedSpot[1]][playedSpot[2]+1] != 1:
                                if self.grid[playedSpot[1]+1][playedSpot[2]] != 1:
                                    return True
                                        
                elif direction == 'NE':                            
                #corner northeast on grid view
                    if self.grid[playedSpot[1]-1][playedSpot[2]+2] != 1:
                        if self.grid[playedSpot[1]][playedSpot[2]+1] != 1:
                            if self.grid[playedSpot[1]-1][playedSpot[2]] != 1:
                                return True
                
                elif direction == 'NW':
                    if self.grid[playedSpot[1]-1][playedSpot[2]] != 1:
                        if self.grid[playedSpot[1]][playedSpot[2]-1] != 1:
                            if self.grid[playedSpot[1]-1][playedSpot[2]-2] != 1:
                                return True
                
                elif direction == 'SW':
                    if self.grid[playedSpot[1]+2][playedSpot[2]-1] != 1:
                        if self.grid[playedSpot[1]+1][playedSpot[2]] != 1:
                            if self.grid[playedSpot[1]][playedSpot[2]-1] != 1:
                                if self.grid[playedSpot[1]+1][playedSpot[2]-2] != 1:
                                    return True
        
            elif playedSpot[1] == 18:
        
                if direction == 'SE':
                    #corner furthest from starting point (southeast on grid view)
                    
                    if self.grid[playedSpot[1]+1][playedSpot[2]+2] != 1:
                        if self.grid[playedSpot[1]][playedSpot[2]+1] != 1:
                            if self.grid[playedSpot[1]+1][playedSpot[2]] != 1:
                                return True
                                            
                elif direction == 'NE':                            
                #corner northeast on grid view
                    if self.grid[playedSpot[1]-2][playedSpot[2]+1] != 1:
                        if self.grid[playedSpot[1]-1][playedSpot[2]+2] != 1:
                            if self.grid[playedSpot[1]][playedSpot[2]+1] != 1:
                                if self.grid[playedSpot[1]-1][playedSpot[2]] != 1:
                                    return True
                
                elif direction == 'NW':
                    if self.grid[playedSpot[1]-2][playedSpot[2]-1] != 1:
                        if self.grid[playedSpot[1]-1][playedSpot[2]] != 1:
                            if self.grid[playedSpot[1]][playedSpot[2]-1] != 1:
                                if self.grid[playedSpot[1]-1][playedSpot[2]-2] != 1:
                                    return True
                
                elif direction == 'SW':
                    
                    if self.grid[playedSpot[1]+1][playedSpot[2]] != 1:
                        if self.grid[playedSpot[1]][playedSpot[2]-1] != 1:
                            if self.grid[playedSpot[1]+1][playedSpot[2]-2] != 1:
                                return True
            else:
                if direction == 'SE':
                    #corner furthest from starting point (southeast on grid view)
                    
                    return False
                                            
                elif direction == 'NE':                            
                #corner northeast on grid view
                    if self.grid[playedSpot[1]-2][playedSpot[2]+1] != 1:
                        if self.grid[playedSpot[1]-1][playedSpot[2]+2] != 1:
                            if self.grid[playedSpot[1]][playedSpot[2]+1] != 1:
                                if self.grid[playedSpot[1]-1][playedSpot[2]] != 1:
                                    return True
                
                elif direction == 'NW':
                    if self.grid[playedSpot[1]-2][playedSpot[2]-1] != 1:
                        if self.grid[playedSpot[1]-1][playedSpot[2]] != 1:
                            if self.grid[playedSpot[1]][playedSpot[2]-1] != 1:
                                if self.grid[playedSpot[1]-1][playedSpot[2]-2] != 1:
                                    return True
                
                elif direction == 'SW':
                    
                    return False
        ####
        ####
        #### now for the corners with potential index errors for columns only
        elif indexError == [False, True]:
            if playedSpot[2] == 0:
                if direction == 'SE':
                    #corner furthest from starting point (southeast on grid view)
                    if self.grid[playedSpot[1]+2][playedSpot[2]+1] != 1:
                        if self.grid[playedSpot[1]+1][playedSpot[2]+2] != 1:
                            if self.grid[playedSpot[1]][playedSpot[2]+1] != 1:
                                if self.grid[playedSpot[1]+1][playedSpot[2]] != 1:
                                    return True
                                        
                elif direction == 'NE':                            
                #corner northeast on grid view
                    if self.grid[playedSpot[1]-2][playedSpot[2]+1] != 1:
                        if self.grid[playedSpot[1]-1][playedSpot[2]+2] != 1:
                            if self.grid[playedSpot[1]][playedSpot[2]+1] != 1:
                                if self.grid[playedSpot[1]-1][playedSpot[2]] != 1:
                                    return True
                
                elif direction == 'NW':
                    return False
                
                elif direction == 'SW':
                    return False
                
            elif playedSpot[2] == 1:
                if direction == 'SE':
                    #corner furthest from starting point (southeast on grid view)
                    if self.grid[playedSpot[1]+2][playedSpot[2]+1] != 1:
                        if self.grid[playedSpot[1]+1][playedSpot[2]+2] != 1:
                            if self.grid[playedSpot[1]][playedSpot[2]+1] != 1:
                                if self.grid[playedSpot[1]+1][playedSpot[2]] != 1:
                                    return True
                                        
                elif direction == 'NE':                            
                #corner northeast on grid view
                    if self.grid[playedSpot[1]-2][playedSpot[2]+1] != 1:
                        if self.grid[playedSpot[1]-1][playedSpot[2]+2] != 1:
                            if self.grid[playedSpot[1]][playedSpot[2]+1] != 1:
                                if self.grid[playedSpot[1]-1][playedSpot[2]] != 1:
                                    return True
                
                elif direction == 'NW':
                    if self.grid[playedSpot[1]-2][playedSpot[2]-1] != 1:
                        if self.grid[playedSpot[1]-1][playedSpot[2]] != 1:
                            if self.grid[playedSpot[1]][playedSpot[2]-1] != 1:
                                return True
                
                elif direction == 'SW':
                    if self.grid[playedSpot[1]+2][playedSpot[2]-1] != 1:
                        if self.grid[playedSpot[1]+1][playedSpot[2]] != 1:
                            if self.grid[playedSpot[1]][playedSpot[2]-1] != 1:
                                    return True
        
            elif playedSpot[2] == 18:
        
                if direction == 'SE':
                    #corner furthest from starting point (southeast on grid view)
                    if self.grid[playedSpot[1]+2][playedSpot[2]+1] != 1:
                        if self.grid[playedSpot[1]][playedSpot[2]+1] != 1:
                            if self.grid[playedSpot[1]+1][playedSpot[2]] != 1:
                                return True
                                                                
                elif direction == 'NE':                            
                #corner northeast on grid view
                    if self.grid[playedSpot[1]-2][playedSpot[2]+1] != 1:
                        if self.grid[playedSpot[1]][playedSpot[2]+1] != 1:
                            if self.grid[playedSpot[1]-1][playedSpot[2]] != 1:
                                return True
                
                elif direction == 'NW':
                    if self.grid[playedSpot[1]-2][playedSpot[2]-1] != 1:
                        if self.grid[playedSpot[1]-1][playedSpot[2]] != 1:
                            if self.grid[playedSpot[1]][playedSpot[2]-1] != 1:
                                if self.grid[playedSpot[1]-1][playedSpot[2]-2] != 1:
                                    return True
                
                elif direction == 'SW':
                    
                    if self.grid[playedSpot[1]+2][playedSpot[2]-1] != 1:
                        if self.grid[playedSpot[1]+1][playedSpot[2]] != 1:
                            if self.grid[playedSpot[1]][playedSpot[2]-1] != 1:
                                if self.grid[playedSpot[1]+1][playedSpot[2]-2] != 1:
                                    return True                                
            else:
                if direction == 'SE':
                    #corner furthest from starting point (southeast on grid view)
                    
                    return False
                                            
                elif direction == 'NE':                            
                    return False
                
                elif direction == 'NW':
                    if self.grid[playedSpot[1]-2][playedSpot[2]-1] != 1:
                        if self.grid[playedSpot[1]-1][playedSpot[2]] != 1:
                            if self.grid[playedSpot[1]][playedSpot[2]-1] != 1:
                                if self.grid[playedSpot[1]-1][playedSpot[2]-2] != 1:
                                    return True
                
                elif direction == 'SW':
                    
                    if self.grid[playedSpot[1]+2][playedSpot[2]-1] != 1:
                        if self.grid[playedSpot[1]+1][playedSpot[2]] != 1:
                            if self.grid[playedSpot[1]][playedSpot[2]-1] != 1:
                                if self.grid[playedSpot[1]+1][playedSpot[2]-2] != 1:
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
                    if self.grid[playedSpot[1]+2][playedSpot[2]+1] != 1:
                        if self.grid[playedSpot[1]+1][playedSpot[2]+2] != 1:
                            if self.grid[playedSpot[1]][playedSpot[2]+1] != 1:
                                if self.grid[playedSpot[1]+1][playedSpot[2]] != 1:
                                    return True                                           
                elif direction == 'NE':                            
                    return False
                
                elif direction == 'NW':
                    return False
                
                elif direction == 'SW':
                    if self.grid[playedSpot[1]+2][playedSpot[2]-1] != 1:
                        if self.grid[playedSpot[1]+1][playedSpot[2]] != 1:
                            if self.grid[playedSpot[1]][playedSpot[2]-1] != 1:
                                return True
                
            elif playedSpot[1:] == [0, 18]:
                if direction == 'SE':
                    #corner furthest from starting point (southeast on grid view)
                    if self.grid[playedSpot[1]+2][playedSpot[2]+1] != 1:
                        if self.grid[playedSpot[1]][playedSpot[2]+1] != 1:
                                if self.grid[playedSpot[1]+1][playedSpot[2]] != 1:
                                    return True                                           
                elif direction == 'NE':                            
                    return False
                
                elif direction == 'NW':
                    return False
                
                elif direction == 'SW':
                    if self.grid[playedSpot[1]+2][playedSpot[2]-1] != 1:
                        if self.grid[playedSpot[1]+1][playedSpot[2]] != 1:
                            if self.grid[playedSpot[1]][playedSpot[2]-1] != 1:
                                if self.grid[playedSpot[1]+1][playedSpot[2]-2] != 1:
                                    return True
               
            elif playedSpot[1:] == [0,19]:
                return False
            
            elif playedSpot[1:] == [1,0]:
                if direction == 'SE':
                   if self.grid[playedSpot[1]+2][playedSpot[2]+1] != 1:
                        if self.grid[playedSpot[1]+1][playedSpot[2]+2] != 1:
                            if self.grid[playedSpot[1]][playedSpot[2]+1] != 1:
                                if self.grid[playedSpot[1]+1][playedSpot[2]] != 1:
                                    return True                                       
                elif direction == 'NE':                            
                    return False
                
                elif direction == 'NW':
                    return False
                
                elif direction == 'SW':
                   return False
                                
            elif playedSpot[1:] == [1,1]:
                if direction == 'SE':
                   if self.grid[playedSpot[1]+2][playedSpot[2]+1] != 1:
                        if self.grid[playedSpot[1]+1][playedSpot[2]+2] != 1:
                            if self.grid[playedSpot[1]][playedSpot[2]+1] != 1:
                                if self.grid[playedSpot[1]+1][playedSpot[2]] != 1:
                                    return True                                       
                elif direction == 'NE':                            
                    if self.grid[playedSpot[1]][playedSpot[2]+1] != 1:
                            if self.grid[playedSpot[1]-1][playedSpot[2]] != 1:
                                return True
                
                elif direction == 'NW':
                    return False
                
                elif direction == 'SW':
                   if self.grid[playedSpot[1]+2][playedSpot[2]-1] != 1:
                        if self.grid[playedSpot[1]+1][playedSpot[2]] != 1:
                            if self.grid[playedSpot[1]][playedSpot[2]-1] != 1:
                                return True
               
            elif playedSpot[1:] == [1,18]:
                if direction == 'SE':
                   if self.grid[playedSpot[1]+2][playedSpot[2]+1] != 1:
                        if self.grid[playedSpot[1]][playedSpot[2]+1] != 1:
                                if self.grid[playedSpot[1]+1][playedSpot[2]] != 1:
                                    return True                                       
                elif direction == 'NE':                            
                    return False
                
                elif direction == 'NW':
                    if self.grid[playedSpot[1]-1][playedSpot[2]] != 1:
                        if self.grid[playedSpot[1]][playedSpot[2]-1] != 1:
                            if self.grid[playedSpot[1]-1][playedSpot[2]-2] != 1:
                                return True
                
                elif direction == 'SW':
                   if self.grid[playedSpot[1]+2][playedSpot[2]-1] != 1:
                        if self.grid[playedSpot[1]+1][playedSpot[2]] != 1:
                            if self.grid[playedSpot[1]][playedSpot[2]-1] != 1:
                                if self.grid[playedSpot[1]+1][playedSpot[2]-2] != 1:
                                    return True
                                
            elif playedSpot[1:] == [1,19]:
                if direction == 'SE':
                   return False
                                       
                elif direction == 'NE':                            
                    return False
                
                elif direction == 'NW':
                    if self.grid[playedSpot[1]-1][playedSpot[2]] != 1:
                        if self.grid[playedSpot[1]][playedSpot[2]-1] != 1:
                            if self.grid[playedSpot[1]-1][playedSpot[2]-2] != 1:
                                return True
                
                elif direction == 'SW':
                   if self.grid[playedSpot[1]+2][playedSpot[2]-1] != 1:
                        if self.grid[playedSpot[1]+1][playedSpot[2]] != 1:
                            if self.grid[playedSpot[1]][playedSpot[2]-1] != 1:
                                if self.grid[playedSpot[1]+1][playedSpot[2]-2] != 1:
                                    return True
                                
            elif playedSpot[1:] == [18, 0]:
                if direction == 'SE':
                    #corner furthest from starting point (southeast on grid view)
                    
                    if self.grid[playedSpot[1]+1][playedSpot[2]+2] != 1:
                        if self.grid[playedSpot[1]][playedSpot[2]+1] != 1:
                            if self.grid[playedSpot[1]+1][playedSpot[2]] != 1:
                                return True
                                            
                elif direction == 'NE':                            
                #corner northeast on grid view
                    if self.grid[playedSpot[1]-2][playedSpot[2]+1] != 1:
                        if self.grid[playedSpot[1]-1][playedSpot[2]+2] != 1:
                            if self.grid[playedSpot[1]][playedSpot[2]+1] != 1:
                                if self.grid[playedSpot[1]-1][playedSpot[2]] != 1:
                                    return True
                
                elif direction == 'NW':
                    return False
                
                elif direction == 'SW':
                    
                    return False
                            
            elif playedSpot[1:] == [18, 1]:
                if direction == 'SE':
                    #corner furthest from starting point (southeast on grid view)
                    
                    if self.grid[playedSpot[1]+1][playedSpot[2]+2] != 1:
                        if self.grid[playedSpot[1]][playedSpot[2]+1] != 1:
                            if self.grid[playedSpot[1]+1][playedSpot[2]] != 1:
                                return True
                                            
                elif direction == 'NE':                            
                #corner northeast on grid view
                    if self.grid[playedSpot[1]-2][playedSpot[2]+1] != 1:
                        if self.grid[playedSpot[1]-1][playedSpot[2]+2] != 1:
                            if self.grid[playedSpot[1]][playedSpot[2]+1] != 1:
                                if self.grid[playedSpot[1]-1][playedSpot[2]] != 1:
                                    return True
                
                elif direction == 'NW':
                    if self.grid[playedSpot[1]-2][playedSpot[2]-1] != 1:
                        if self.grid[playedSpot[1]-1][playedSpot[2]] != 1:
                            if self.grid[playedSpot[1]][playedSpot[2]-1] != 1:
                                return True
                
                elif direction == 'SW':
                    
                    if self.grid[playedSpot[1]+1][playedSpot[2]] != 1:
                        if self.grid[playedSpot[1]][playedSpot[2]-1] != 1:
                            return True
                            
            elif playedSpot[1:] == [18, 18]:
                if direction == 'SE':
                    #corner furthest from starting point (southeast on grid view)
                    
                    if self.grid[playedSpot[1]][playedSpot[2]+1] != 1:
                            if self.grid[playedSpot[1]+1][playedSpot[2]] != 1:
                                return True
                                            
                elif direction == 'NE':                            
                #corner northeast on grid view
                    if self.grid[playedSpot[1]-2][playedSpot[2]+1] != 1:
                        if self.grid[playedSpot[1]][playedSpot[2]+1] != 1:
                                if self.grid[playedSpot[1]-1][playedSpot[2]] != 1:
                                    return True
                
                elif direction == 'NW':
                    if self.grid[playedSpot[1]-2][playedSpot[2]-1] != 1:
                        if self.grid[playedSpot[1]-1][playedSpot[2]] != 1:
                            if self.grid[playedSpot[1]][playedSpot[2]-1] != 1:
                                if self.grid[playedSpot[1]-1][playedSpot[2]-2] != 1:
                                    return True
                
                elif direction == 'SW':
                    
                    if self.grid[playedSpot[1]+1][playedSpot[2]] != 1:
                        if self.grid[playedSpot[1]][playedSpot[2]-1] != 1:
                            if self.grid[playedSpot[1]+1][playedSpot[2]-2] != 1:
                                return True
                            
            elif playedSpot[1:] == [18, 19]:
                if direction == 'SE':
                    #corner furthest from starting point (southeast on grid view)
                    
                    return False
                                            
                elif direction == 'NE':                            
                    return False
                
                elif direction == 'NW':
                    if self.grid[playedSpot[1]-2][playedSpot[2]-1] != 1:
                        if self.grid[playedSpot[1]-1][playedSpot[2]] != 1:
                            if self.grid[playedSpot[1]][playedSpot[2]-1] != 1:
                                if self.grid[playedSpot[1]-1][playedSpot[2]-2] != 1:
                                    return True
                
                elif direction == 'SW':
                    
                    if self.grid[playedSpot[1]+1][playedSpot[2]] != 1:
                        if self.grid[playedSpot[1]][playedSpot[2]-1] != 1:
                            if self.grid[playedSpot[1]+1][playedSpot[2]-2] != 1:
                                return True
                            
            elif playedSpot[1:] == [19, 0]:
                return False
                
            elif playedSpot[1:] == [19, 1]:
                if direction == 'SE':
                    #corner furthest from starting point (southeast on grid view)
                    
                    return False
                                            
                elif direction == 'NE':                            
                #corner northeast on grid view
                    if self.grid[playedSpot[1]-2][playedSpot[2]+1] != 1:
                        if self.grid[playedSpot[1]-1][playedSpot[2]+2] != 1:
                            if self.grid[playedSpot[1]][playedSpot[2]+1] != 1:
                                if self.grid[playedSpot[1]-1][playedSpot[2]] != 1:
                                    return True
                
                elif direction == 'NW':
                    if self.grid[playedSpot[1]-2][playedSpot[2]-1] != 1:
                        if self.grid[playedSpot[1]-1][playedSpot[2]] != 1:
                            if self.grid[playedSpot[1]][playedSpot[2]-1] != 1:
                                return True
                
                elif direction == 'SW':
                    
                    return False
                
            elif playedSpot[1:] == [19, 18]:
                if direction == 'SE':
                    #corner furthest from starting point (southeast on grid view)
                    
                    return False
                                            
                elif direction == 'NE':                            
                #corner northeast on grid view
                    if self.grid[playedSpot[1]-2][playedSpot[2]+1] != 1:
                        if self.grid[playedSpot[1]][playedSpot[2]+1] != 1:
                                if self.grid[playedSpot[1]-1][playedSpot[2]] != 1:
                                    return True
                
                elif direction == 'NW':
                    if self.grid[playedSpot[1]-2][playedSpot[2]-1] != 1:
                        if self.grid[playedSpot[1]-1][playedSpot[2]] != 1:
                            if self.grid[playedSpot[1]][playedSpot[2]-1] != 1:
                                if self.grid[playedSpot[1]-1][playedSpot[2]-2] != 1:
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
    
        return [pieceLocations, self.name]
    
    def pieceFit(self, placements):
        '''check if the piece will fit into the grid
            check there's no index range issues 
            check that the board has opening in those places where the piece will land
            and finally, check to make sure that there are no pieces adjacently placed'''
        
        squares = len(placements[0])
        
        #first part - check that there's no index range errors
        
        for i in range(squares):
            for j in range(2):
                try:
                    if placements[0][i][j] < 0 or placements[0][i][j] > 19:
                        return False
                except IndexError:
                    print(placements, 'line 949 index error')
                    return None
                
        #second part - check that the board's grid has opening in those spaces
        grid = Board.getGrid(self)
        
        for i in range(squares):
            if grid[placements[0][i][0]][placements[0][i][1]] != 0:
                return False
        
        #third part - check to make sure that the new pieces will not be adjacent to any existing computer pieces
        for i in range(squares):
                
                #for squares along walls/corners, index range will arise.
                #the following addresses the index issues and checks for adjacent placements
                
            if placements[0][i][0] != 0 and placements[0][i][1] != 0 and placements[0][i][0] != 19 and placements[0][i][1] != 19:
                                      
                if self.grid[placements[0][i][0]+1][placements[0][i][1]] == 1:
                    return False
                if self.grid[placements[0][i][0]][placements[0][i][1]+1] == 1:
                    return False
                if self.grid[placements[0][i][0]][placements[0][i][1]-1] == 1:
                    return False
                if self.grid[placements[0][i][0]-1][placements[0][i][1]] == 1:
                    return False
            
            elif placements[0][i][0] == 0 and placements[0][i][1] == 19:
                if self.grid[placements[0][i][0]+1][placements[0][i][1]] == 1:
                    return False
                if self.grid[placements[0][i][0]][placements[0][i][1]-1] == 1:
                    return False
            
            elif placements[0][i][0] == 19 and placements[0][i][1] == 0:
                if self.grid[placements[0][i][0]][placements[0][i][1]+1] == 1:
                    return False
                if self.grid[placements[0][i][0]][placements[0][i][1]-1] == 1:
                    return False
            
            elif placements[0][i][0] == 0:
                if self.grid[placements[0][i][0]+1][placements[0][i][1]] == 1:
                    return False
                if self.grid[placements[0][i][0]][placements[0][i][1]+1] == 1:
                    return False
                if self.grid[placements[0][i][0]][placements[0][i][1]-1] == 1:
                    return False
            
            elif placements[0][i][1] == 0:
                if self.grid[placements[0][i][0]+1][placements[0][i][1]] == 1:
                    return False
                if self.grid[placements[0][i][0]][placements[0][i][1]+1] == 1:
                    return False
                if self.grid[placements[0][i][0]-1][placements[0][i][1]] == 1:
                    return False                
            
            elif placements[0][i][0] == 19 and placements[0][i][1] == 19:
                if self.grid[placements[0][i][0]-1][placements[0][i][1]] == 1:
                    return False
                if self.grid[placements[0][i][0]][placements[0][i][1]-1] == 1:
                    return False
            
            elif placements[0][i][0] == 19:
                if self.grid[placements[0][i][0]-1][placements[0][i][1]] == 1:
                    return False
                if self.grid[placements[0][i][0]][placements[0][i][1]+1] == 1:
                    return False
                if self.grid[placements[0][i][0]][placements[0][i][1]-1] == 1:
                    return False
                
            elif placements[0][i][1] == 19:
                if self.grid[placements[0][i][0]-1][placements[0][i][1]] == 1:
                    return False
                if self.grid[placements[0][i][0]+1][placements[0][i][1]] == 1:
                    return False
                if self.grid[placements[0][i][0]][placements[0][i][1]-1] == 1:
                    return False
            
        return True
    

#==============================================================================
# gameBo = Board()
# 
# gameBo.playPiece(gameBo.cornerChoice(), BlokusPiece.pieceList())
#==============================================================================

#BlokusPiece.pieceList()

