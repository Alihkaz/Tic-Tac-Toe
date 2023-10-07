from replit import clear

from checking import Checking
from positions import Positions
from graphics import Substitute

positions=Positions()
checking=Checking()
substitute=Substitute()




def check_input(user_input,user_answer,check):

   if (user_input>9) or (user_input<=0):              
      user_input=(int(input("Invalid position , position must be between 1 and 9 ! Enter new Position \n")))
      check_input(user_input,user_answer,check)
  
   elif (user_input in user_answer) or (user_input in check):              
      user_input=(int(input("Position Taken , Enter Another position!")))
      check_input(user_input,user_answer,check)
      
   elif (user_input not in user_answer) or (user_input not in check) :
      user_answer.append(user_input)
      return True

   
         
  


def game_start():
  
    Game_is_on=True
    user1_answer=[]
    user2_answer=[]

         
    while Game_is_on is True :


   
        user1_input=(int(input("Player1 Enter a position:\n ")))
        check_input(user1_input,user1_answer,user2_answer)
        substitute.substitute_By_X(user1_input,status=1)
         
        
      
        if len(user1_answer)>=3 :
          
              pos=positions.result()          
              x=checking.check_answer1(user1_answer,pos)
          
              if x==0:
              
                print("Congratulations player 1 , you won the game!")
                substitute.substitute_By_X(user1_input,status='end')
                Game_is_on=False
                
                restart_answer=input("Do You Want To Restart The Game ? Y or N:\n ").upper()
                if restart_answer=='Y':
                  substitute.substitute_By_X(user1_input,status='end')
                  clear()
                  game_start()

                else:
                  substitute.substitute_By_X(user1_input,status='end')
                  quit()
                  clear()
                 
    
              if  len(user1_answer)==5 and x!=0:
                print("Draw!")
                restart_answer=input("Do You Want To Restart The Game ? Y or N:\n ").upper()
                if restart_answer=='Y':
                  substitute.substitute_By_X(user1_input,status='end')
                  game_start()

                else:
                  substitute.substitute_By_X(user1_input,status='end')
                  quit()
                  clear()
                 
                  
                
                
    
      
        user2_input=(int(input("Player2 Enter a position:\n ")))
        check_input(user2_input,user2_answer,user1_answer)
        substitute.substitute_By_O(user2_input,status=1)
      
        if len(user2_answer)>=3 and len(user2_answer)<=5 :
          
              pos=positions.result()
               
              x=checking.check_answer2(user2_answer,pos)
                           
              if x==0:
              
                print("Congratulations player 2 , you won the game!")
                Game_is_on=False
                
                restart_answer=input("Do You Want To Restart The Game ? Y or N:\n ").upper()
                if restart_answer=='Y':
                  
                  clear()
                  game_start()
                  substitute.substitute_By_O(user2_input,status='end')
                  

                else:
                  
                  quit()
                  clear()
                  substitute.substitute_By_O(user1_input,status='end')
                 

    
          
    
  
game_start()  