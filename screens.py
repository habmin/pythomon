import curses
import time
import random
from classes import *
from prompts import *
from assets import title
from assets import gameover
from assets import traits
from assets import pythodeck

def start_screen(stdscr, h, w):
    subtitle = "Pythomon! - A Python Battle Game!"
    directions = "Use arrow keys to select"

    # Menu selection variables
    menu = ["New Game", "Quit"]
    selection = 0
    keypress = 0

    while True:
        stdscr.clear()

        # Title Banner
        for i, line in enumerate(title):
            stdscr.attron(curses.color_pair(2))
            stdscr.addstr((h // 2) - (10 - i), ((w // 2) - (len(line) // 2)), line)
            stdscr.attroff(curses.color_pair(2))
        stdscr.addstr((h // 2) - 6, ((w // 2) - (len(subtitle) // 2)), subtitle)
        stdscr.addstr((h // 2) + 3, ((w // 2) - (len(directions) // 2)), directions)
        
        # Menu Selection
        print_menu_center(stdscr, (h // 2), w, menu, selection)

        # Keyboard listeners
        keypress = stdscr.getch()
        if keypress == curses.KEY_UP and selection > 0:
            selection -= 1
        elif keypress == curses.KEY_DOWN and selection < (len(menu) - 1):
            selection += 1
        elif (keypress == curses.KEY_ENTER or keypress in [10, 13]) and menu[selection] == "New Game":
            break
        elif (keypress == curses.KEY_ENTER or keypress in [10, 13]) and menu[selection] == "Quit":
            curses.curs_set(1)
            curses.endwin()
            exit(0)
        
        stdscr.refresh()

    return

def create_player(stdscr, h, w):
    title = "Create your trainer"
    player_name_buffer = ""
    player_gender_buffer = ""
    player_trait_buffer = ""

    # Menu selection variables
    menu = ["Trainer's Name", "Trainer's Gender", "Nature", "Starter", "Finish"]
    selection = 0
    trait_selection = 0
    starter_selection = 0
    keypress = 0
    while True:
        curses.curs_set(1)
        stdscr.clear()

        # Title Banner
        stdscr.addstr(1, ((w // 2) - (len(title) // 2)), title)
        
        # Menu Selection
        for i, option in enumerate(menu):
            if i == selection:
                stdscr.attron(curses.color_pair(1))
                stdscr.addstr(5 + i, ((w // 2) - 30), option)
                stdscr.attroff(curses.color_pair(1))
            else:
                stdscr.addstr(5 + i, ((w // 2) - 30), option)
        
        # Player input display
        stdscr.addstr(5, ((w // 2) - 12), player_name_buffer)
        stdscr.addstr(6, ((w // 2) - 12), player_gender_buffer)
        stdscr.addstr(7, ((w // 2) - 12), traits[trait_selection])
        stdscr.addstr(8, ((w // 2) - 12), pythodeck[starter_selection]["name"])
        stdscr.addstr(10, ((w // 2) - 12), "HP: {}".format(str(pythodeck[starter_selection]["hp"])))
        stdscr.addstr(11, ((w // 2) - 12), "Base Attack: {}".format(str(pythodeck[starter_selection]["base_atk"])))
        stdscr.addstr(12, ((w // 2) - 12), "Gender: {}".format(str(pythodeck[starter_selection]["gender"])))
        for i, line in enumerate(pythodeck[starter_selection]["art"]):
            stdscr.addstr(i + 13, ((w // 2) - 12), line)
        
        # Cursor selection location
        if menu[selection] == "Trainer's Name":
            stdscr.move(5, ((w // 2) - 12 + len(player_name_buffer)))
        elif menu[selection] == "Trainer's Gender":
            stdscr.move(6, ((w // 2) - 12 + len(player_gender_buffer)))
        elif menu[selection] == "Nature":
            curses.curs_set(0)
            stdscr.addstr(7, (w // 2) - 14, "<")
            stdscr.addstr(7, (w // 2) - 11 + len(traits[trait_selection]), ">")
        elif menu[selection] == "Starter":
            curses.curs_set(0)
            stdscr.addstr(8, (w // 2) - 14, "<")
            stdscr.addstr(8, (w // 2) - 11 + len(pythodeck[starter_selection]["name"]), ">")
        else:
            curses.curs_set(0)

        # Keyboard listeners
        keypress = stdscr.getch()
        if keypress == curses.KEY_UP and selection > 0:
            selection -= 1
        elif keypress == curses.KEY_DOWN and selection < (len(menu) - 1):
            selection += 1
        elif (keypress == curses.KEY_ENTER or keypress in [10, 13]) and menu[selection] == "Finish":
            return Player(Pythomon(pythodeck[starter_selection]),player_name_buffer, player_gender_buffer, player_trait_buffer)

        # Input handlers
        elif menu[selection] == "Trainer's Name":
            if keypress >= 32 and keypress <= 126 and len(player_name_buffer) <= 15:
                player_name_buffer += chr(keypress)
            elif keypress in [8, 127] and len(player_name_buffer) != 0:
                player_name_buffer = player_name_buffer[:-1]
        elif menu[selection] == "Trainer's Gender":
            if keypress >= 32 and keypress <= 126 and len(player_gender_buffer) <= 15:
                player_gender_buffer += chr(keypress)
            elif keypress in [8, 127] and len(player_gender_buffer) != 0:
                player_gender_buffer = player_gender_buffer[:-1]
        elif menu[selection] == "Nature":
            if keypress == curses.KEY_LEFT:
                trait_selection = (trait_selection - 1) % len(traits)
            elif keypress == curses.KEY_RIGHT:
                trait_selection = (trait_selection + 1) % len(traits)
        elif menu[selection] == "Starter":
            if keypress == curses.KEY_LEFT:
                starter_selection = (starter_selection - 1) % 4
            elif keypress == curses.KEY_RIGHT:
                starter_selection = (starter_selection + 1) % 4
        stdscr.refresh()

def print_grid(stdscr, h, w, grid, player):
    # Create top line of grid box
    line = "═" * (3 * len(grid[0]))
    stdscr.addstr(0, 1, f"╔{line}╗")

    # Print grid, with each cell being a grass or special event location (store, encounter, trainer)
    for i, row in enumerate(grid):
        # Box padding
        stdscr.addstr(1 + i, 1, "║")
        for j, cell in enumerate(row):
            # Cycle through different 'grass' padding characters
            fill = "▒"
            if i % 2 == 0:
                fill = "░"    
            if cell.player_occupied:
                stdscr.addstr(1 + i, 2 + (3 * j), f"{fill}Y{fill}")
            elif cell.terrain == "trainer":
                stdscr.addstr(1 + i, 2 + (3 * j), f"{fill}T{fill}")
            elif cell.terrain == "encounter":
                stdscr.addstr(1 + i, 2 + (3 * j), f"{fill}E{fill}")
            elif cell.terrain == "store":
                stdscr.addstr(1 + i, 2 + (3 * j), f"{fill}${fill}")
            # Choose grass type based on 'fill' type
            else:
                if fill == "▒":
                    stdscr.addstr(1 + i, 2 + (3 * j), f"{fill}░{fill}")
                else:
                    stdscr.addstr(1 + i, 2 + (3 * j), f"{fill}▒{fill}")
        stdscr.addstr(1 + i, 2 + (3 * (j + 1)), "║")
    # Create bottom line of grid box
    stdscr.addstr(len(grid) + 1, 1, f"╚{line}╝")

    # Print info and instructions
    stdscr.addstr(4, (3 * len(grid[0])) + 7, f"{player.name}")
    stdscr.addstr(5, (3 * len(grid[0])) + 7, f"Money: ${player.money}")
    stdscr.addstr(6, (3 * len(grid[0])) + 7, f"Pythomon: {len(list(filter(lambda pythomon: pythomon.hp > 0, player.pythomon)))}/{len(player.pythomon)}")
    stdscr.addstr(7, (3 * len(grid[0])) + 7, "Use arrow keys to move")
    stdscr.addstr(8, (3 * len(grid[0])) + 7, "$ = Store, T = Trainer Battle")
    stdscr.addstr(9, (3 * len(grid[0])) + 7, "Press 'q' anytime to exit game")

def gameover(stdscr, h, w):
    thanks = "Thanks for playing!"
    stdscr.clear()
    for i, line in enumerate(gameover):
        stdscr.attron(curses.color_pair(2))
        stdscr.addstr((h // 2) - (10 - i), ((w // 2) - (len(line) // 2)), line)
        stdscr.attroff(curses.color_pair(2))
    stdscr.addstr((h // 2) + 2, ((w // 2) - (len(thanks) // 2)), thanks)
    stdscr.refresh()
    time.sleep(5)

def encounter(stdscr, h, w, player, pythomon_target):
    init_menu = ["Fight", "Item", "Run"]
    engaged_menu = ["Attack", "Item", "Switch", "Run"]
    moves_selection = 0
    init_selection = 0
    item_selection = 0
    mode = "Start"
    keypress = 0
    pythodeck_selection = 0
    pytho_start_range = 0
    pytho_end_range = pytho_start_range + min(len(player.pythomon), 4)
    pytho_max_range = len(player.pythomon)
    item_start_range = 0
    item_end_range = item_start_range + min(len(player.bag), 4)
    item_max_range = len(player.bag)
    # 1 starts with players turn
    turn = 1
    deployed = False
    while pythomon_target.hp > 0:
        stdscr.clear()

        # print encountered pythomon until dead
        print_pythomon(stdscr, 3, 50, pythomon_target, False, False)
        
        # Print player's pythomon once selected/deployed
        if deployed:
            print_pythomon(stdscr, 3, 5, player.pythomon[pythodeck_selection + pytho_start_range], True, False)

        # Players turn
        if turn % 2 == 1:
            # Initial start of encounter mode
            
            # Engaged mode (selected a pythomon)
            if mode == "Start":
                # Print initial menu
                print_menu_1(stdscr, 19, 5, init_menu, init_selection)
                
                keypress = stdscr.getch()
                if keypress == curses.KEY_UP and init_selection > 0:
                    init_selection -= 1
                elif keypress == curses.KEY_DOWN and init_selection < (len(init_menu) - 1):
                    init_selection += 1
                elif (keypress == curses.KEY_ENTER or keypress in [10, 13]) and init_menu[init_selection] == "Fight":
                    mode = "Select Pythomon"
                elif (keypress == curses.KEY_ENTER or keypress in [10, 13]) and init_menu[init_selection] == "Item":
                    mode = "Start-Item"
                elif (keypress == curses.KEY_ENTER or keypress in [10, 13]) and init_menu[init_selection] == "Run":
                    break

            elif mode == "Select Pythomon":
                # Print initial menu
                print_menu_1(stdscr, 19, 5, init_menu, init_selection)

                # select from player's pythomon roster
                print_menu_select_pythomon(stdscr, 19, 20, player.pythomon[pytho_start_range:min(pytho_end_range, pytho_max_range)], pythodeck_selection)

                keypress = stdscr.getch()    
            
                if keypress == curses.KEY_UP and pythodeck_selection > pytho_start_range:
                    pythodeck_selection -= 1
                elif keypress == curses.KEY_UP and pythodeck_selection == pytho_start_range and pythodeck_selection > 0:
                    pytho_start_range -= 1
                    pytho_end_range -= 1
                elif keypress == curses.KEY_DOWN and pythodeck_selection < (len(player.pythomon[pytho_start_range:min(pytho_end_range, pytho_max_range)]) - 1):
                    pythodeck_selection += 1
                elif keypress == curses.KEY_DOWN and pythodeck_selection == (len(player.pythomon[pytho_start_range:min(pytho_end_range, pytho_max_range)]) - 1) and pytho_end_range != len(player.pythomon):
                    pytho_start_range += 1
                    pytho_end_range += 1
                elif keypress == curses.KEY_BACKSPACE or keypress == 8:
                    mode = "Start"
                elif (keypress == curses.KEY_ENTER or keypress in [10, 13]) and player.pythomon[pythodeck_selection + pytho_start_range].status == "alive":
                    deployed = True
                    mode = "Engaged"
                
            elif mode == "Start-Item":
                # Print initial menu
                print_menu_1(stdscr, 19, 5, init_menu, init_selection)

                stdscr.addstr(19, 15, ">")
                if len(player.bag) == 0:
                    stdscr.attron(curses.color_pair(1))
                    stdscr.addstr(19, 20, "No Items")
                    stdscr.attroff(curses.color_pair(1))
                else:
                    print_menu_1(stdscr, 19, 20, player.bag[item_start_range:min(item_end_range, item_max_range)], item_selection)
    
                keypress = stdscr.getch()    
            
                if keypress == curses.KEY_UP and item_selection > item_start_range:
                    item_selection -= 1
                elif keypress == curses.KEY_UP and item_selection == item_start_range and item_selection > 0:
                    item_start_range -= 1
                    item_end_range -= 1
                elif keypress == curses.KEY_DOWN and item_selection < (len(player.bag[item_start_range:min(item_end_range, item_max_range)]) - 1):
                    item_selection += 1
                elif keypress == curses.KEY_DOWN and item_selection == (len(player.bag[item_start_range:min(item_end_range, item_max_range)]) - 1) and item_end_range != len(player.bag):
                    item_start_range += 1
                    item_end_range += 1
                elif keypress == curses.KEY_BACKSPACE or keypress == 8:
                    mode = "Start"
                elif (keypress == curses.KEY_ENTER or keypress in [10, 13]):
                    if player.bag[item_selection + item_start_range] == "Capture Ball":
                        capture_prompts(stdscr, 17, w, player, None, item_selection + item_start_range, pythomon_target, "Wild", False)
                    else:
                        mode = "Start-Heal"
            
            elif mode == "Start-Heal":
                health_selection = 0
                if player.bag[item_selection + item_start_range] == "Revive":
                    damaged_pythomon = list(filter(lambda pythomon: pythomon.status == "dead", player.pythomon))
                else:
                    damaged_pythomon = list(filter(lambda pythomon: pythomon.hp < pythomon.max_hp and pythomon.status == "alive", player.pythomon))
                damaged_start_range = 0
                damaged_end_range = damaged_start_range + min(len(damaged_pythomon), 4)
                damaged_max_range = len(damaged_pythomon)
                
                # print initial menu
                print_menu_1(stdscr, 19, 5, init_menu, init_selection)
                # print start-item menu
                stdscr.addstr(19, 15, ">")
                print_menu_1(stdscr, 19, 20, player.bag[item_start_range:min(item_end_range, item_max_range)], item_selection)
                # print heal menu
                stdscr.addstr(19, 37, ">")
                print_heal_menu(stdscr, 19, 42, damaged_pythomon[damaged_start_range:min(damaged_end_range, damaged_max_range)], health_selection, damaged_start_range, damaged_end_range, damaged_max_range, player.bag[item_selection + item_start_range])
                
                keypress = stdscr.getch()  
                
                if keypress == curses.KEY_UP and health_selection > damaged_start_range:
                    health_selection -= 1
                elif keypress == curses.KEY_UP and health_selection == damaged_start_range and health_selection > 0:
                    damaged_start_range -= 1
                    damaged_end_range -= 1
                elif keypress == curses.KEY_DOWN and health_selection < (len(damaged_pythomon[damaged_start_range:min(damaged_end_range, damaged_max_range)]) - 1):
                    health_selection += 1
                elif keypress == curses.KEY_DOWN and health_selection == (len(damaged_pythomon[damaged_start_range:min(damaged_end_range, damaged_max_range)]) - 1) and damaged_end_range != len(damaged_pythomon):
                    damaged_start_range += 1
                    damaged_end_range += 1
                elif keypress == curses.KEY_BACKSPACE or keypress == 8:
                    mode = "Start-Item"
                elif (keypress == curses.KEY_ENTER or keypress in [10, 13]) and len(damaged_pythomon) > 0:
                    if player.bag[item_selection + item_start_range] == "Revive":
                        damaged_pythomon[health_selection + damaged_start_range].revive()
                    elif player.bag[item_selection + item_start_range] == "Health Spray":
                        damaged_pythomon[health_selection + damaged_start_range].heal(20)
                    else:
                        damaged_pythomon[health_selection + damaged_start_range].heal(50)
                    player.bag.pop(item_selection + item_start_range)
                    item_start_range = 0
                    item_end_range = item_start_range + min(len(player.bag), 4)
                    item_max_range = len(player.bag)
                    mode = "Start-Item"
            
            elif mode == "Engaged":                
                # Print menu option for engaged mode
                print_menu_1(stdscr, 19, 5, engaged_menu, init_selection)

                keypress = stdscr.getch()
                if keypress == curses.KEY_UP and init_selection > 0:
                    init_selection -= 1
                elif keypress == curses.KEY_DOWN and init_selection < (len(engaged_menu) - 1):
                    init_selection += 1
                elif (keypress == curses.KEY_ENTER or keypress in [10, 13]) and engaged_menu[init_selection] == "Attack":
                    mode = "Attack"
                elif (keypress == curses.KEY_ENTER or keypress in [10, 13]) and engaged_menu[init_selection] == "Item":
                    pass
                elif (keypress == curses.KEY_ENTER or keypress in [10, 13]) and engaged_menu[init_selection] == "Switch":
                    pass
                elif (keypress == curses.KEY_ENTER or keypress in [10, 13]) and engaged_menu[init_selection] == "Run":
                    break
                
            elif mode == "Attack":
                # Print menu option for engaged mode
                print_menu_1(stdscr, 19, 5, engaged_menu, init_selection)
                stdscr.addstr(19, 15, ">")
                for i, option in enumerate(player.pythomon[pythodeck_selection + pytho_start_range].moves):
                    blank_space = ' ' * (16 - len(option["name"]))
                    if i == moves_selection:
                        stdscr.attron(curses.color_pair(1))
                        stdscr.addstr((19) + i, 20, "{}{}POW:{}".format(option["name"], blank_space, option["power"]))
                        stdscr.attroff(curses.color_pair(1))
                    else:
                        stdscr.addstr((19) + i, 20, "{}{}POW:{}".format(option["name"], blank_space, option["power"]))

                keypress = stdscr.getch()

                if keypress == curses.KEY_UP and moves_selection > 0:
                    moves_selection -= 1
                elif keypress == curses.KEY_DOWN and moves_selection < (len(player.pythomon[pythodeck_selection + pytho_start_range].moves) - 1):
                    moves_selection += 1
                elif keypress == curses.KEY_BACKSPACE or keypress == 8:
                    mode = "Engaged"
                elif (keypress == curses.KEY_ENTER or keypress in [10, 13]):
                    # Commence attack! Returns true if target is defeated
                    if attack_prompts(stdscr, 17, w, f"{player.name}'s", player.pythomon[pythodeck_selection + pytho_start_range], moves_selection, pythomon_target, True):
                        win_prompts(stdscr, 17, w, player, player.pythomon[pythodeck_selection + pytho_start_range], pythomon_target, "Wild")
                        # exit encounter
                        break
                    else:
                        turn += 1
                        mode = "CPU"


        # computer's turn
        else:
            if attack_prompts(stdscr, 17, w, "Wild", pythomon_target, random.randint(0, len(pythomon_target.moves) - 1), player.pythomon[pythodeck_selection + pytho_start_range], False):
                if defeated_prompts(stdscr, 17, w, player, player.pythomon[pythodeck_selection + pytho_start_range], pythomon_target, "Wild"):
                    gameover(stdscr, h, w)
                    return True
                else:
                    deployed = False
                    mode = "Start"
            else:
                mode = "Engaged"
            turn += 1

        stdscr.refresh()
    
    # player was not defeated by encounter
    return False
