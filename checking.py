


class Checking():

  # Get all combination of user input  of length 3
   def check_answer1(self,user_answer1,positions):

      import itertools

      combinations =list(itertools.permutations(user_answer1, 3))
      

      for answer in combinations:
        if (list(answer)) in positions:
          return 0


   def check_answer2(self,user_answer2,positions):

      import itertools
  
      combinations =list(itertools.permutations(user_answer2, 3))
      
      
      
      for answer in combinations:
        if (list(answer)) in positions:
          return 0
      

  