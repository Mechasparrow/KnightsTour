'''
General Chess Functions
chess.py
Author: Michael Navazhylau
'''

# Generates a board with nothing on it
def gen_board(w, h):
  board = []
  for y in range(h):
    row = []
    for x in range(w):
      row.append(False)
    board.append(row)
  return board

# Generates the winning board state
def gen_win_board(w, h):
  board = []
  for y in range(h):
    row = []
    for x in range(w):
      row.append(True)
    board.append(row)
  return board 

# Creates a new copy of the board
def copy_board(board):
  return board[:]


# Renders out the chess board
def display_board(board, knight_position):
  board_width = len(board)
  board_height = len(board[0])

  board_tile = "|_"
  end_tile = "|_|"
  knight_tile = "|K"
  knight_tile_end = "|K|"
  taken_tile = "|T"
  taken_tile_end = "|T|"

  for y in range(board_height):
    
    board_row = ""
    for x in range(board_width):
      tile_taken = board[y][x]  
      knight_here = knight_position[0] == x and knight_position[1] == y

      if (x+1 != board_width):
        if (knight_here):
          board_row += knight_tile
        elif (tile_taken):
          board_row += taken_tile
        else:  
          board_row += board_tile
      else:
        if (knight_here):
          board_row += knight_tile_end
        elif (tile_taken):
          board_row += taken_tile_end
        else:
          board_row += end_tile 
      
    print(board_row)

# Mark a tile as visited
def take_tile(board, x, y):
  new_board = copy_board(board)
  new_board[y][x] = True
  return new_board

def untake_tile(board, x, y):
    new_board = copy_board(board)
    new_board[y][x] = True
    return new_board
