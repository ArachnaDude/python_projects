# importing random range from Python's random module
from random import randrange


# define board as a 3 element list, each element is another 3 element list.
board = [
  [[1],[2],[3]],
  [[4],["X"],[6]],
  [[7],[8],[9]]
  ]




def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    for field in board:
      print(field)

def make_list_of_free_fields(board): # FUNCTION COMPLETE (pending)
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
  free_fields = []
  for i in range(3):
    for j in range(3):
      if type(board[i][j][0]) == int:
        free_fields.append((i,j))
  return(free_fields)

def draw_move(board):
  # The function draws the computer's move and updates the board.

  free_fields = make_list_of_free_fields(board)
  # checks if is new game - (1,1) is field 5
  # if available, computer always selects this space
  # then calls enter_move 
  if (1, 1) in free_fields:
    board[free_fields[4][0]][free_fields[4][1]][0] = "X"
    display_board(board)
    # INCLUDE enter_move here
  else:
    # selects random element from list of free spaces
    # assigns X to it, and redraws board.
    # calls enter_move
    random_field = free_fields[randrange(len(free_fields))]
    board[random_field[0][random_field[1]]][0] = "X"
    display_board(board)
    #INCLUDE enter_move here


def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.

    free_fields = make_list_of_free_fields(board)

    numbers_to_spaces = {
    1: (0,0),
    2: (0,1),
    3: (0,2),
    4: (1,0),
    5: (1,1),
    6: (1,2),
    7: (2,0),
    8: (2,1),
    9: (2,2)
    }


    try:
      value = int(input("Enter your move: "))
      if value > 0 and value < 10:
        # print(value, "is a valid number")
        user_number = numbers_to_spaces[value]
        if user_number in free_fields:
          # print( value, "is an empty space")
          board[user_number[0]][user_number[1]][0] = "O"
          display_board(board)
          draw_move(board)
        else:
          print("Space already occupied")
          enter_move(board)
      else: 
        print("Please enter a valid number")
        enter_move(board)
    except ValueError:
      print("Please enter a valid number")
      enter_move(board)
    except:
      print("I don't know what went wrong")
      enter_move(board)



# def victory_for(board, sign):
#     # The function analyzes the board's status in order to check if 
#     # the player using 'O's or 'X's has won the game


draw_move(board)