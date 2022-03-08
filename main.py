from sys import platform
import random
from classes import *

def grid_maker(height, width, encounter_rate, store_row, store_col, player_x, player_y):
    # Create height by width grid and fill with Squares/Terrain
    grid = [[Square("grass") for i in range(width)] for j in range(height)]

    # Player always starts in upper left
    grid[player_y][player_x].player_occupied = True

    # Trainer is always in bottom right
    grid[height - 1][width - 1].terrain = "trainer"

    # Place Store
    grid[store_row][store_col].terrain = "store"

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

    while True:
        # Start Splash Screen
        start_screen(stdscr, height, width)

        # Create Player
        player = create_player(stdscr, height, width)
        # Create grid
        grid_height = 15
        grid_width = 15
        encounter_rate = 20
        
        # create store
        store = Store()
        while len(player.trophies) < 4:
            # Player's coordinates
            player_x = 0
            player_y = 0
            # Randomly place one store
            store_row = random.randint(0, grid_height - 1)
            store_col = random.randint(0, grid_width - 1)
            # Make sure location is not the starting player position or Trainer position
            while (store_row == player_y and store_col == player_x) or (store_row == grid_height - 1 and store_col == grid_width - 1):
                store_row = random.randint(0, grid_height - 1)
                store_col = random.randint(0, grid_width - 1)
            
            grid = grid_maker(grid_height, grid_width, encounter_rate, store_row, store_col, player_x, player_y)
            while not player.defeated:
                stdscr.clear()

                if grid[player_y][player_x].terrain == "encounter":
                    encounter(stdscr, height, width, player, Pythomon(pythodeck[random.randint(4, 23)]), "Wild")
                    grid = grid_maker(grid_height, grid_width, encounter_rate, store_row, store_col, player_x, player_y)
                    stdscr.clear()
                
                elif grid[player_y][player_x].terrain == "store":
                    print_store(stdscr, height, width, player, store)
                    stdscr.clear()

                elif grid[player_y][player_x].terrain == "trainer":
                    if trainer_battle(stdscr, height, width, player):
                        break
                    stdscr.clear()

                print_grid(stdscr, height, width, grid, player)

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
                elif keypress == ord('q'):
                    quit_prompt(stdscr)

                stdscr.refresh()
        print_victory(stdscr, height, width, player)
    # Done with game, reset curs_set and end
    curses.curs_set(1)
    curses.endwin()
    exit(0)

if __name__ == "__main__":
    try:
        import curses
        from screens import *
    except ModuleNotFoundError:
        if platform == "win32":
            print("Module 'windows-curses' was not found, and is required to run pythomon. Use 'pip install windows-curses' to install module.")
            exit(1)
        else:
            print("Module 'curses' was not found, and is required to run pythomon")
            exit(1)
    curses.wrapper(main)
                                                        