import curses
import random
# import time
from classes import *
from screens import *

def grid_maker(height, width, encounter_rate):
    # Create height by width grid and fill with Squares/Terrain
    grid = [[Square("grass") for i in range(height)] for j in range(width)]
    # Player always starts in upper left
    grid[0][0].player_occupied = True
    # Trainer is always in bottom right
    grid[height - 1][width - 1].terrain = "trainer"
    # Randomly place one store
    random_store_row = random.randint(0, height - 1)
    random_store_col = random.randint(0, width - 1)
    # Make sure location is not the starting player position or Trainer position
    while (random_store_row == 0 and random_store_col == 0) or (random_store_row == height - 1 and random_store_col == width - 1):
        random_store_row = random.randint(0, height - 1)
        random_store_col = random.randint(0, width - 1)
    grid[random_store_row][random_store_col].terrain = "store"
    # Make encounter_rate enemy encouter locations
    for i in range(encounter_rate):
        random_row = random.randint(0, height - 1)
        random_col = random.randint(0, width - 1)
        while grid[random_row][random_col].terrain != "grass" or grid[random_row][random_col].player_occupied == True:
            random_row = random.randint(0, height - 1)
            random_col = random.randint(0, width - 1)
        grid[random_row][random_col].terrain = "encounter"
    return grid

def main(stdscr):
    # --- curses initializers ---
    curses.curs_set(0)                  # turn off cursor
    height, width = stdscr.getmaxyx()   # get terminal window height and width

    # 1: Black Font, White Background
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    # 2: Yellow Font, Blue Background (for Start Screen)
    curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLUE)

    # Start Splash Screen
    start_screen(stdscr, height, width)

    # Create Player
    player = create_player(stdscr, height, width)

    # Create grid
    grid = grid_maker(5, 5, 3)

    # Done with program, reset curs_set and end
    curses.curs_set(1)
    curses.endwin()
    exit(0)

if __name__ == "__main__":
    curses.wrapper(main)









    # print("░░░░░▄▄▀▀▀▀▀▀▀▀▀▄▄░░░░░")
    # print("░░░░█░░░░░░░░░░░░░█░░░░")
    # print("░░░█░░░░░░░░░░▄▄▄░░█░░░")
    # print("░░░█░░▄▄▄░░▄░░███░░█░░░")
    # print("░░░▄█░▄░░░▀▀▀░░░▄░█▄░░░")
    # print("░░░█░░▀█▀█▀█▀█▀█▀░░█░░░")
    # print("░░░▄██▄▄▀▀▀▀▀▀▀▄▄██▄░░░")
    # print("░▄█░█▀▀█▀▀▀█▀▀▀█▀▀█░█▄░")

                                                        