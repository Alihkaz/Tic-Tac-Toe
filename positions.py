
import numpy as np

class Positions():

    def __init__(self):
        
        self.wining_positions=[]
        self.Tic_Board= np.array([[ 1, 2, 3],
                                  [ 4, 5, 6 ],
                                  [ 7, 8, 9]])
      

    #########################################################################
    #extracting the winning structures from the array ! 
    def printDiagonalStructure(self,mat, n):
     
        principal = []
        secondary = []
        global wining_positions
        for i in range(0, n):
            principal.append(mat[i][i])
            secondary.append(mat[i][n - i - 1])
        self.wining_positions.append((principal,secondary))
             
    
    
    ##########################################################################
    
    def printColumnStructure(self,mat,n) :
    
         global wining_positions
         for j in range(0, n):
            x=(mat[:,j])
            self.wining_positions.append(x.tolist())
            
              
    
    ################################################################################
    
    
    def printRowStructure(self,arr,n) :
    
      global wining_positions
      for  i in range(0, n):
        self.wining_positions.append(arr[i].tolist())
     
        
    
    #################################################################################
    
    
    def result(self):
      
        self.printDiagonalStructure(self.Tic_Board, 3)
        self.printRowStructure(self.Tic_Board,3)
        self.printColumnStructure(self.Tic_Board,3)
      
        x=self.wining_positions[0]

      
        for diagonals in x:
          self.wining_positions.append(diagonals)
        self.wining_positions.remove(([1, 5, 9], [3, 5, 7]))
        return self.wining_positions
    
    

