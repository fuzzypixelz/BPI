#!/usr/bin/env python

import sys
import lo
import os
from random import randint

def start_game(board_config):
    moves = 0
    while not lo.game_over(board_config):
        moves += 1
        print(lo.get_board(board_config))
        lit_cell = lo.prompt_move()
        lo.update_board_config(board_config, lit_cell)
        lo.clear()
    #This is ugly and repulsive! If you can fix it please tell me.
    os.system("clear")
    print(f"""\u001b[{randint(30, 37)}m
                     ________                                                 ._. 
                    /  _____/_____    _____   ____     _______  __ ___________| | 
                   /   \  ___\__  \  /     \_/ __ \   /  _ \  \/ // __ \_  __ \ | 
                   \    \_\  \/ __ \|  Y Y  \  ___/  (  <_> )   /\  ___/|  | \/\| 
                    \______  (____  /__|_|  /\___  >  \____/ \_/  \___  >__|   __ 
                           \/     \/      \/     \/                   \/       \/ 
                       _____.___.________   ____ ___   __      __.___ _______ ._.     
                       \__  |   |\_____  \ |    |   \ /  \    /  \   |\      \| |     
                        /   |   | /   |   \|    |   / \   \/\/   /   |/   |   \ |     
                        \____   |/    |    \    |  /   \        /|   /    |    \|     
                        / ______|\_______  /______/     \__/\  / |___\____|__  /_     
                        \/               \/                  \/              \/\/ """)
    print(f'\u001b[0mFinished in {moves} moves. Play again?')
def main():
    if len(sys.argv) != 2:
        print(f'Usage: {sys.argv[0]} level-number')
    else:
        board_config = lo.import_level(sys.argv[1])
        start_game(board_config)        

if __name__ == "__main__":
    main()
