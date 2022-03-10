from sys import platform
import random

from classes import *

def grid_maker(height, width, encounter_rate, item_rate, store_row, store_col, player_x, player_y):
    # Create height by width grid and fill with Squares/Terrain
    grid = [[Square("grass") for i in range(width)] for j in range(height)]

    # Places player based on player x/y coordinates
    grid[player_y][player_x].player_occupied = True

    # Trainer is always in bottom right
    grid[height - 1][width - 1].terrain = "trainer"

    # Place Store
    grid[store_row][store_col].terrain = "store"

    # Make encounter_rate enemy encouter locations
    for i in range(encounter_rate):
        random_row = random.randint(0, height - 1)
        random_col = random.randint(0, width - 1)
        # Ensures placement is on unused terrain and not where player is located
        while grid[random_row][random_col].terrain != "grass" or grid[random_row][random_col].player_occupied == True:
            random_row = random.randint(0, height - 1)
            random_col = random.randint(0, width - 1)
        grid[random_row][random_col].terrain = "encounter"

    # Make remainder item locations
    if item_rate:
        for i in range(item_rate):
            random_row = random.randint(0, height - 1)
            random_col = random.randint(0, width - 1)
            # Ensures placement is on unused terrain and not where player is located
            while grid[random_row][random_col].terrain != "grass" or grid[random_row][random_col].player_occupied == True:
                random_row = random.randint(0, height - 1)
                random_col = random.randint(0, width - 1)
            grid[random_row][random_col].terrain = "item"

    return grid

def game_start(stdscr):
    # --- curses initializers ---
    curses.curs_set(0)                  # turn off cursor
    height, width = stdscr.getmaxyx()   # get terminal window height and width
    game_height = 25
    game_width = 92
    
    # Check to see if terminal window is minimum resolution for game
    if height < 25 or width < 92:
        raise Exception(f"Your terminal window dimensions are {height} X {width}. Must be at least {game_height} X {game_width}.")
    

    # 1: Black Font, White Background
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    # 2: Yellow Font, Blue Background (for Start Screen)
    curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLUE)

    # create store
    store = Store()

    # Grid dimensions and rate
    grid_height = 15
    grid_width = 15
    encounter_rate = 22
    item_rate = 5

    # Main loop, always run until user quits via pressing 'q'
    # after starting game and creating a player
    while True:
        # Start Splash Screen
        start_screen(stdscr, height, width, game_height, game_width)

        # Create Player Screen
        player = create_player(stdscr, height, width, game_height, game_width)

        # Gameplay loop:
        # Breaks when player wins with having all four tropies
        # Or when their team is fully defeated in battle
        while len(player.trophies) < 4 and not player.defeated:
            # Player's coordinates
            player_x = 0
            player_y = 0

            # Randomly place one store; find coordinates
            store_row = random.randint(0, grid_height - 1)
            store_col = random.randint(0, grid_width - 1)
            # Make sure location is not the starting player position or Trainer position
            while (store_row == player_y and store_col == player_x) or (store_row == grid_height - 1 and store_col == grid_width - 1):
                store_row = random.randint(0, grid_height - 1)
                store_col = random.randint(0, grid_width - 1)
            
            # Create grid
            grid = grid_maker(grid_height, grid_width, encounter_rate, item_rate, store_row, store_col, player_x, player_y)
            
            # Grid-movement loop
            # Breaks when lost a battle and after battle with trianer
            while True:
                stdscr.clear()

                if grid[player_y][player_x].terrain == "encounter":
                    # Create pythomon, change level based on amount of trophies a player has
                    encounter_pythomon = Pythomon(pythodeck[random.randint(4, 23)])
                    encounter_pythomon.base_atk += ((len(player.trophies) - 1) * 6)
                    encounter_pythomon.max_hp += ((len(player.trophies) - 1) * 6)
                    encounter_pythomon.hp = encounter_pythomon.max_hp

                    # Returns true if player loses
                    if encounter(stdscr, height, width, game_height, game_width, player, encounter_pythomon, "Wild"):
                        break
                    # Respawns new encounter locations
                    grid = grid_maker(grid_height, grid_width, encounter_rate, item_rate, store_row, store_col, player_x, player_y)
                    stdscr.clear()
                
                elif grid[player_y][player_x].terrain == "store":
                    print_store(stdscr, height, width, game_height, game_width, player, store)
                    stdscr.clear()

                elif grid[player_y][player_x].terrain == "trainer":
                    trainer_battle(stdscr, height, width, game_height, game_width, player)
                    stdscr.clear()
                    break

                # Prints grid if player lands on grass or item
                print_box(stdscr, height, width, game_height, game_width)
                print_grid(stdscr, height, width, game_height, game_width, grid, player)

                if grid[player_y][player_x].terrain == "item":
                    item_rate -= 1
                    random_item(stdscr, height, width, game_height, game_width, player, store)
                    grid[player_y][player_x].terrain = "grass"
                    #print_box(stdscr, height, width, game_height, game_width)
                    print_grid(stdscr, height, width, game_height, game_width, grid, player)

                # Keyboard listeners and handlers
                keypress = stdscr.getch()

                # Moves left
                if keypress == curses.KEY_LEFT and not player_x == 0:
                    grid[player_y][player_x].player_occupied = False
                    player_x -= 1
                    grid[player_y][player_x].player_occupied = True
                # Moves Right
                elif keypress == curses.KEY_RIGHT and not player_x == grid_width - 1:
                    grid[player_y][player_x].player_occupied = False
                    player_x += 1
                    grid[player_y][player_x].player_occupied = True
                # Moves up
                elif keypress == curses.KEY_UP and not player_y == 0:
                    grid[player_y][player_x].player_occupied = False
                    player_y -= 1
                    grid[player_y][player_x].player_occupied = True
                # Moves down
                elif keypress == curses.KEY_DOWN and not player_y == grid_height - 1:
                    grid[player_y][player_x].player_occupied = False
                    player_y += 1
                    grid[player_y][player_x].player_occupied = True
                # Presses 'q' for quit
                elif keypress == ord('q'):
                    quit_prompt(stdscr, height, width, game_height, game_width)

                stdscr.refresh()
    
        if not player.defeated:
            print_victory(stdscr, height, width, game_height, game_width)
        else:
            gameover_screen(stdscr, height, width, game_height, game_width)
    # Done with game, reset curs_set and end
    curses.curs_set(1)
    curses.endwin()
    exit(0)

if __name__ == "__main__":
    # Check to make sure curses module is installed
    # For windows systems, module used is windows-curses
    # Not sure if mac/darwin system will be different, only tested it with linux/ubuntu
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
    
    # Run program after passed module check
    curses.wrapper(game_start)
                                                        