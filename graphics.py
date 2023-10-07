



class Substitute:

  def __init__(self):
        
      
        self.board = [  "|___|","|___|","|___|",
                        "|___|","|___|","|___|",
                        "|___|","|___|","|___|"]

        
    
        
       
                
       

    
             


  def substitute_By_X(self,user1_input,status):
    
    
      
    if status=="end":
       self.board = [  "|___|","|___|","|___|",
                        "|___|","|___|","|___|",
                        "|___|","|___|","|___|"]
    else:
      self.board.insert(user1_input-1,'|X|') 
  
      for n in range(0,9,3):
          print(self.board[n:n+3])
    
          
    
  def substitute_By_O(self,user2_input,status):
  
   
      
    if status=="end":
       self.board = [  "|___|","|___|","|___|",
                        "|___|","|___|","|___|",
                        "|___|","|___|","|___|"]
    else:
      
        self.board.insert(user2_input-1,'|O|')
        for n in range(0,9,3):
           print(self.board[n:n+3])
      
    

   
