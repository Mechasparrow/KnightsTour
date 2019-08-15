
# Saves the list of chess knight positions
def save_tour(filepath, moves):

    f = open(filepath, "w+", encoding = "utf-8")

    lines_of_moves = []
    for move in moves:
        lines_of_moves.append(str(move[0]) + "," + str(move[1]) + "\n")

    f.writelines(lines_of_moves)
    f.close()