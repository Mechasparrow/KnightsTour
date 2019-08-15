from chess import *
from move_io import *

# Generates a list of potential knight moves
def potential_knight_moves(board, knight_position):
  moves = []
  board_width = len(board)
  board_height = len(board[0])


  start_x = knight_position[0]
  start_y = knight_position[1]

  offset_x = [-2, -1, 1, 2]
  offset_y = [-2, -1, 1, 2]

  potential_move = (start_x + 2, start_y - 1)

  for x in offset_x:
    for y in offset_y:
      if not (abs(x) == abs(y)):
        potential_move = (start_x + x, start_y + y)
        
        if (potential_move[0]+1 > board_width or potential_move[1]+1 > board_height or potential_move[0] < 0 or potential_move[1] < 0):
          continue

        moves.append(potential_move)
  
  return moves


def Wolf_Value(board, x,y):
  potential_moves = potential_knight_moves(board, (x,y))
  h = len(potential_moves) - 1
  return h

# conduct the OPEN knights tour
chess_board = gen_board(5,5)
knight_position = (4, 4)

moves_list = []
moves_list.append(knight_position)

for i in range(25): 
  print("Iter " + str(i+1))

  if (i != 0):
    potential_move = knight_position
    potential_moves = potential_knight_moves(chess_board,knight_position)
    

    move_i = 0
    max_h = 8
    for i in range(len(potential_moves)):
      move = potential_moves[i]
      h = Wolf_Value(chess_board, move[0], move[1])
      tile = chess_board[move[1]][move[0]]
      #print ("W: " + str(h))
      if (h < max_h and tile == False):
        max_h = h
        move_i = i

    move = potential_moves[move_i]
    tile = chess_board[move[1]][move[0]]
    if (tile == False):
      potential_move = move

    chess_board = take_tile(chess_board, knight_position[0], knight_position[1])
    old_knight_pos = knight_position
    knight_position = potential_move
    
    if (knight_position == old_knight_pos):
      break
    else:
      moves_list.append(knight_position)

  display_board(chess_board, knight_position)
  print()

# Mark the last place knight is at as taken
chess_board = take_tile(chess_board, knight_position[0], knight_position[1])

win_board = gen_win_board(5,5)

if (win_board == chess_board):
    print ("Win state reached")
    print ("writing to system ....")
    save_tour("successful_tours/tour1.csv", moves_list)