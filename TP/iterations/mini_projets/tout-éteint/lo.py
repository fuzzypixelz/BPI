"""
Implémenter une interface en mode texte pour le jeu lights out.
"""
# see https://en.wikipedia.org/wiki/Block_Elements
FULL_BLOCK = '\u2588'
EMPTY_BLOCK = ' '
CELL_WIDTH = 5
CELL_HEIGHT = 3 
WIDTH = 5
HEIGHT = 5
LETTERS = [chr(i) for i in range(65, 91)]
# see https://tldp.org/HOWTO/Bash-Prompt-HOWTO/x361.html
# 7 is a special number here, it counts for the space taken by the horizontal borders and the prompt.
ANSI_ESC = f'\033[{HEIGHT*CELL_HEIGHT+7}A'

def get_board_line(line_config, label):
    thin_line = ''
    for column in range(WIDTH):
        block = FULL_BLOCK if line_config[column] else EMPTY_BLOCK
        thin_line += block*CELL_WIDTH
    thin_line = f'|{thin_line}|'
    line = ''
    for i in range(CELL_HEIGHT):
        ident = label if i == CELL_HEIGHT//2 else ' '
        line += ident + ' ' + thin_line + '\n'
    return line

def get_board_upper_labels():
    horizontal_labels = '\n   '
    for i in range(WIDTH):
        horizontal_labels += ' '*(CELL_WIDTH//2) + str(i) + ' '*(CELL_WIDTH//2)
    return horizontal_labels + '\n'

def get_board_horizontal_border():
    return '  +' + '-'*CELL_WIDTH*WIDTH + '+' + '\n'

def get_board(board_config):
    """
    lines contient des listes qui donnent les indice des cases allumées
    """
    board = get_board_upper_labels() + get_board_horizontal_border() 
    for line_config, letter in zip(board_config, LETTERS):
        board += get_board_line(line_config, letter)
    board += get_board_horizontal_border() 
    return board

def update_board_config(board_config, lit_cell):
    """
    Lights up lit_cell, and changes the board config accordingly.
    """
    cell_line = lit_cell[0]
    cell_column = lit_cell[1]
    for i, j in zip(
            [cell_line, cell_line, cell_line, cell_line+1, cell_line-1],
            [cell_column, cell_column+1, cell_column-1, cell_column, cell_column]
        ):
        if i >= WIDTH or j >= HEIGHT or i < 0 or j < 0: continue
        board_config[i][j] = not board_config[i][j] 

def game_over(board_config):
    for i in range(WIDTH):
        for j in range(HEIGHT):
            if board_config[i][j]: return False
    return True

def prompt_move():
    move = input('You next move: ')
    return ord(move[0])-ord('A'), int(move[1])

def import_level(level):
    board_config = []
    path = f'niveau{level}'
    with open(path, 'r') as f:
        for line in f:
            line_config = []
            for c in line:
                if c == '.': 
                    line_config.append(True)
                else:
                    line_config.append(False)
            board_config.append(line_config)
    return board_config

def clear():
    print(ANSI_ESC)
