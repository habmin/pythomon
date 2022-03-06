import curses
import random
import time
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
    grid_height = 10
    grid_width = 10
    encounter_rate = 10
    grid = grid_maker(grid_height, grid_width, encounter_rate)

    # Loop until player is defeated or wins
    # while not player.defeated:
    #     # print grid
    player_x = 0
    player_y = 0
    
    while not player.defeated:
        stdscr.clear()

        if grid[player_y][player_x].terrain == "encounter":
            encounter(stdscr, height, width, player, Pythomon(pythodeck[random.randint(4, 23)]))
            # encounter(stdscr, height, width, player, Pythomon(pythodeck[24]))
            grid[player_y][player_x].terrain = "grass"
            stdscr.clear()
        
        elif grid[player_y][player_x].terrain == "store":
            stdscr.clear()

        elif grid[player_y][player_x].terrain == "trainer":
            stdscr.clear()

        print_grid(stdscr, height, width, grid)

        keypress = stdscr.getch()
        if keypress == curses.KEY_LEFT and not player_x == 0:
            grid[player_y][player_x].player_occupied = False
            player_x -= 1
            grid[player_y][player_x].player_occupied = True
        elif keypress == curses.KEY_RIGHT and not player_x == grid_width - 1:
            grid[player_y][player_x].player_occupied = False
            player_x += 1
            grid[player_y][player_x].player_occupied = True
        elif keypress == curses.KEY_UP and not player_y == 0:
            grid[player_y][player_x].player_occupied = False
            player_y -= 1
            grid[player_y][player_x].player_occupied = True
        elif keypress == curses.KEY_DOWN and not player_y == grid_height - 1:
            grid[player_y][player_x].player_occupied = False
            player_y += 1
            grid[player_y][player_x].player_occupied = True    
        
        stdscr.refresh()
    
    # Done with game, reset curs_set and end
    curses.curs_set(1)
    curses.endwin()
    exit(0)

if __name__ == "__main__":
    curses.wrapper(main)
                                                        