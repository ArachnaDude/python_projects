from random import randrange

class Game():
  def __init__(self) -> None:
    self.start_new_game()
    self.win_count = 0
    self.total_games_played = 0

  def start_new_game(self) -> None:
    """
    Resets the game board for a new game.
    """
    self.board = [
      [1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]
    ]

  def display_board(self) -> None:

    """
    When called, the function prints the 
    current board status to the console.
    """

    horizontal_border = "+-------" * 3 + "+"
    empty_row = "|       " * 3 + "|"
    
    print(horizontal_border)
    for row in self.board:
      print(empty_row)
      print("|   " + "   |   ".join(str(cell)for cell in row) + "   |")
      print(empty_row)
      print(horizontal_border)

  def make_list_of_free_fields(self) -> list[tuple[int, int]]:
    """
    The function returns a list of tuples of the free spaces left
    on the board. The tuples are in the format (row_number, column_number). 
    """
    free_fields = []

    for row_number in range(3):
      for column_number in range(3):
        if type(self.board[row_number][column_number]) == int:
          free_fields.append((row_number, column_number))
    return free_fields


  def draw_move(self) -> None:
    """
    The function selects the computer's move, and prints the 
    updated board to the console. If (1,1) is a free space, 
    the computer will always pick that space to start the game.
    """

    free_fields = self.make_list_of_free_fields()
    
    if (1,1) in free_fields:
      self.board[1][1] = "X"
      self.display_board()
    else:
      random_field = free_fields[randrange(len(free_fields))]
      self.board[random_field[0]][random_field[1]] = "X"
      self.display_board()

  
  def enter_move(self) -> None:
    """
    Asks the user for an integer corresponding to a square on
    the board. Re-promts if the input is out of range, not an int,
    or already taken, and redraws the updated board. 
    """

    free_fields = self.make_list_of_free_fields()

    numbers_to_spaces_dict = {1: (0,0), 2: (0,1), 3: (0,2), 4: (1,0), 5: (1, 1), 6: (1, 2), 7: (2,0), 8: (2,1), 9: (2, 2)}

    while True:

      try:
        player_selected_int = int(input("Select a square:\n"))

        if player_selected_int not in numbers_to_spaces_dict:
          continue
        
        player_coordinate = numbers_to_spaces_dict[player_selected_int]
        
        if player_coordinate in free_fields:
          self.board[player_coordinate[0]][player_coordinate[1]] = "O"
          self.display_board()
          break
        else:
          print("That space is already taken, try again.")
      
      except ValueError:
        print("Invalid selection, please select a square.")


  
  def check_victory(self, sign: str) -> str | None:
    """
    Analyses the board for an endgame condition. Returns winning sign,
    or None if there is no winner.
    """

    for row in self.board:
      if all(cell == sign for cell in row):
        return sign

    for column_number in range(3):
      if all(self.board[row][column_number] == sign for row in range(3)):
        return sign

    if all(self.board[i][i] == sign for i in range(3)) or \
      all(self.board[i][2 - i] == sign for i in range(3)):
      return sign

    return None

  def show_stats(self) -> None:
    """
    When called, function prints the played and win counts to the console.
    """
    print(f"Played: {self.total_games_played} games")
    print(f"Won {self.win_count} games")
      

  def play_game(self) -> None:
    """
    Starts and manages the logical flow of the game.

    The game starts with the computer picking a space, and continues
    until a victory or a draw is reached. The computer then asks if
    the player wants another game.
    """
    

    while True:
      self.start_new_game()
      print("Let's play a game of tic tac toe!\nComputer moves first")
      self.draw_move()
      
      while True:
        free_fields = self.make_list_of_free_fields()
        
        if len(free_fields) == 0:
          print("Draw")
          self.total_games_played += 1
          break

        self.enter_move()
        winner = self.check_victory("O")
        if winner:
          print(f"{winner} wins")
          self.total_games_played += 1
          self.win_count += 1
          break

        self.draw_move()
        winner = self.check_victory("X")
        if winner:
          self.total_games_played += 1
          print(f"{winner} wins")
          break
      
      print(f"Good game!\nWould you like to see your stats? y/n")
      stats_answer = str(input()).strip().lower()
      if stats_answer == "y":
        self.show_stats()
      print("Would you like to play again? y/n")
      replay_answer = str(input()).strip().lower()
      if replay_answer != "y":
        print("Thanks for playing")
        break

if __name__ == "__main__":
  tic_tac_toe = Game()
  tic_tac_toe.play_game()
