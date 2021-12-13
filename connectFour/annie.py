import random

from .constants import RED, WHITE, COLS, ROWS

class Annie:


  # Functions for evaluating the board. These functions will be used by the minimax algorithm.
  # this function will get the score!
  
  
  # The idea here for evaluation was using "streaks" on the board, 
  # or how many pieces in a row the player currently has. 
  # Different streaks are weighted differently, with a four streak being weighed the highest and a two streak the lowest, 
  # with singular pieces not taken into consideration. The streaks in all directions 
  # (horizontal, vertical and diagonal) are added together, multiplied by their weight 
  # and summed with the other streaks to produce a score, with the red score being subtracted 
  # from the white score to produce the total score. 
  # A problem with the evaluation currently is that it cannot evaluate horizontally forwards, only backwards.
  # Functions for evaluating the board. These functions will be used by the minimax algorithm.

    # this function will get the score!
    #okay first time editing this LMAO took me a while to figure out i need to use spyder 
    #should check for streaks probably (three in a row more valuable than two)
    #also make indication if it's at the end the board then throw away option 
    #depth is already set so don't have to worry about it :/ 
    
 
  #REMEMBER TO USE ".COLOR" OR ELSE YOU WILL DIE IN A VERY BAD WAY   
  

#checks how many pieces in a row  
#might want to use moves available :/ 

#there is something seriously wrong with this thing 
#let's rewrite it because god knows what is wrong 
  def checkVertical(self, color, board):
      streak_columns = []
      
      for column in range (COLS):
          counter = 0 
          
          for row in reversed(range(ROWS)):
              if board.board[row][column]!=0 and board.board[row][column].color ==color:
                  #print("yayyy")
                  counter+=1
              elif board.board[row][column]!=0 and board.board[row][column].color!=color:
                  counter=0
              
                  
                  
                 #column is full, sets the count to 0 because nothing to be done 
          if board.get_first_empty_spot(column)==-1:
              counter=0
          
          streak_columns.append(counter)
          
          
             
            
      return streak_columns
             
  
  
     
  def checkHorizontal(self, color, board):
      #CAN'T DETECT IN REVERSE :////
      #idk works in reverse now but not normally so idk how to fix that tbh 
      #it's annoying for sure :///
      
      
     
      
      streak_rows = []
      '''counter = 0 
      #used to be self.board 
      for row in range (ROWS):
          #print (list(reversed(row)))
          
          #print(row)
          for cols in range(COLS):
              
              if(board.board[row][cols]!=0 and board.board[row][cols].color==color):
                  if 0 in board.board[row][0:cols]:
                      counter+=0
                  
                  
                  counter+=1
                  
              elif(board.board[row][cols]!=0 and board.board[row][cols].color!=color):
                  if 0 in board.board[row][0:cols]:
                      counter+=0
                  counter=0
          if 0 not in board.board[row]:
              counter=0
          streak_rows.append(counter)'''
          
                 
        #check reverse thing that i cooked up 
        #it works in reverse now but not in the normal way so :/
        #have to make a new list of all the rows that have 0 count in them 
        
          
      newer_counter = 0
         
      for new_counter in range(ROWS):
              #print("new stuff")
              #print(new_counter)
              
                  
              for i in reversed(range(COLS)):
                  #print("haha")
                  #print(self.board[new_counter][i])
                  if board.board[new_counter][i]!=0 and board.board[new_counter][i].color==color:
                      
                      #ddd
                     # print("well that's a bummer")
                      if 0 in board.board[new_counter][::-1]:
                          #ddd
                          #print("haha gottem")
                          newer_counter+=0
                      newer_counter+=1
                  elif(board.board[new_counter][i]!=0 and board.board[new_counter][i].color!=color):
                      #ddd
                      if 0 in board.board[new_counter][::-1]:
                          #dddd
                          newer_counter+=0
                      newer_counter=0
              #print(newer_counter)
              #if len(streak_rows)==ROWS and streak_rows[new_counter]!=newer_counter:
              #streak_rows[new_counter] = newer_counter
              streak_rows.append(newer_counter)
                  
              
          #streak_rows[new_counter] = newer_counter
          #print("below me is the new counter")
          #print(newer_counter)
          #streak_rows[new_counter]=9
          #streak_rows[new_counter-1]=newer_counter
                          
     
      
      return streak_rows
  #FOR ALL OF THESE, CHECK 3-7 
  #disclaimer: this is probably the worst code you'll ever see. but it exists
  #for a reason 
  
  def getDiagonals(self, board):
      streak_diagonal_up=[[] for _ in range(ROWS + COLS - 1)]
      
      for column in range(COLS):
          for row in range (ROWS):
              #print('eh')
              streak_diagonal_up[column+row].append(board.board[row][column])
      return streak_diagonal_up
  def checkDiagonalUp(self, color, board):
      #diagonal still goes through all rows and columns, just differently 
      #first value in array is the diagonal that starts from col six, etc. 
      
      
      #[[matrix[y-x][x] for x in range(N) if 0<=y-x<N] for y in range(2*N-1)]
      #previous code :/ 
      diagonals_that_matter = []
      
      for i in range(3, 9):
          counter=0
          #print(streak_diagonal_up[i])
          for j in range(len(self.getDiagonals(board)[i])):
              #this is to avoid confusion not that it's any better
              confusion = self.getDiagonals(board)[i]
              if(confusion[j]!=0 and confusion[j].color==color):
                  counter+=1
                  #print("wahoo")
              elif(confusion[j]!=0 and confusion[j].color!=color):
                 counter=0
          if 0 not in self.getDiagonals(board)[i]:
              counter=0
          diagonals_that_matter.append(counter)
             
              
              
              
      
              
      
     
      
            
         
        
        
      
     
      
      
      return diagonals_that_matter
      #return streak_diagonal_up
  def checkDiagonalDown(self, color, board):
      #this will need counter diagonals 
      #first value in array is the diagonal that starts from col one 
      #this one will iterate by addition
      diagonals_that_matter=[]
      streak_diagonal_down =[[] for _ in range(len(self.getDiagonals(board)))]
      for column in range(COLS):
          for row in range(ROWS):
             #print("eh")
              streak_diagonal_down[column-row-(-ROWS+1)].append(board.board[row][column])
      for i in range(3,9):
          counter=0
          
          for j in reversed(range(len(streak_diagonal_down[i]))):
              confusion = streak_diagonal_down[i]
              if(confusion[j]!=0 and confusion[j].color==color):
                  counter+=1
              elif(confusion[j]!=0 and confusion[j].color!=color):
                  counter=0
          if 0 not in streak_diagonal_down[i]:
              counter=0
          diagonals_that_matter.append(counter)
          
         
         
                  
      return diagonals_that_matter
            
          
     
      
      
 
  
  def checkStreak(self, num_of_streaks, array_of_streaks):
      counter=0
      for element in array_of_streaks:
          if(element==num_of_streaks):
              counter+=1
      
      return counter
  
          
      
  def evaluate(self, board):
      #print("hhhh")
     # print(self.checkStreak(1, self.checkHorizontal(RED)))
      
     
      #all evaluation functions work now (except for checkStreak)
      #do something with the empty spaces as well 
      
      #print("this is a test")
      #print(self.test())
      #print(self.checkHorizontal(RED))
      #print(self.checkDiagonalUp(RED))
      #print(self.checkVertical(RED))
      #print(self.checkDiagonalDown(RED))
      
      return self.total_score(WHITE, board)-self.total_score(RED, board)
      
  
    

  #def evaluate(self):
       
     
     
    #print(self.board[1][1])
      #will use the above functions to evaluate for which is the best move 
      #evaluate from current position and then 
      
    #return self.total_score(WHITE) - self.total_score(RED)

  def total_score(self, color, board):
      check_4_vertical = self.checkStreak(4, self.checkVertical(color, board))
      check_4_horizontal = self.checkStreak(4, self.checkHorizontal(color, board))
      check_4_diagonal_up = self.checkStreak(4, self.checkDiagonalUp(color, board))
      check_4_diagonal_down = self.checkStreak(4, self.checkDiagonalDown(color, board))
      
      
      
      check_3_vertical = self.checkStreak(3, self.checkVertical(color, board))
      check_3_horizontal = self.checkStreak(3, self.checkHorizontal(color, board))
      check_3_diagonal_up = self.checkStreak(3, self.checkDiagonalUp(color, board))
      check_3_diagonal_down = self.checkStreak(3, self.checkDiagonalDown(color, board))
      
      
      
      
      check_2_vertical = self.checkStreak(2, self.checkVertical(color, board))
      check_2_horizontal = self.checkStreak(2, self.checkHorizontal(color, board))
      check_2_diagonal_up = self.checkStreak(2, self.checkDiagonalUp(color, board))
      check_2_diagonal_down = self.checkStreak(2, self.checkDiagonalDown(color, board))
      
      
      
      
      
      
      return 99999999*(check_4_vertical+check_4_horizontal+check_4_diagonal_up+check_4_diagonal_down)+1000*(check_3_vertical+check_3_horizontal+check_3_diagonal_up+check_3_diagonal_down
                 )+100*(check_2_vertical+check_2_horizontal+check_2_diagonal_up+check_2_diagonal_down)
      return 10 
      
      
      
      
    #print(self.board[0][6].color)
    #get coordinates somehow 
    
      #have to change this 
    #if winner return 10, else 
    #here is where the total score thing is ://// 
     
    

  

  # def evaluate(self, board):
  #   return self.total_score(WHITE, board) - self.total_score(RED, board)

  # def total_score(self, color, board):
  #   return random.randint(1,10)

