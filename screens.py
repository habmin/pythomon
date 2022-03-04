import curses
from sys import stderr
import time
from classes import *
from assets import traits
from assets import pythodeck

def start_screen(stdscr, h, w):
    title = ["  _ \ \ \   / __ __|  |   |   _ \    \  |   _ \    \  |  |",
             " |   | \   /     |    |   |  |   |  |\/ |  |   |    \ |  |",
             " ___/     |      |    ___ |  |   |  |   |  |   |  |\  | _|",
             "_|       _|     _|   _|  _| \___/  _|  _| \___/  _| \_| _)"]
    subtitle = "Pythomon! - A Python Battle Game!"
    directions = "Use arrow keys to select"

    # Menu selection variables
    menu = ["Start a New Game", "Quit"]
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
        for i, option in enumerate(menu):
            if i == selection:
                stdscr.attron(curses.color_pair(1))
                stdscr.addstr((h // 2) + i, ((w // 2) - (len(option) // 2)), option)
                stdscr.attroff(curses.color_pair(1))
            else:
                stdscr.addstr((h // 2) + i, ((w // 2) - (len(option) // 2)), option)

        # Keyboard listeners
        keypress = stdscr.getch()
        if keypress == curses.KEY_UP and selection > 0:
            selection -= 1
        elif keypress == curses.KEY_DOWN and selection < (len(menu) - 1):
            selection += 1
        elif (keypress == curses.KEY_ENTER or keypress in [10, 13]) and menu[selection] == "Start a New Game":
            break
        elif (keypress == curses.KEY_ENTER or keypress in [10, 13]) and menu[selection] == "Quit":
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
        # Cursor location
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

def print_grid(stdscr, h, w, grid):
    line = "═" * (3 * len(grid[0]))
    stdscr.addstr(1, 1, f"╔{line}╗")
    for i, row in enumerate(grid):
        stdscr.addstr(2 + i, 1, "║")
        for j, cell in enumerate(row):
            fill = "▒"
            if i % 2 == 0:
                fill = "░"
            if cell.player_occupied:
                stdscr.addstr(2 + i, 2 + (3 * j), f"{fill}Y{fill}")
            elif cell.terrain == "trainer":
                stdscr.addstr(2 + i, 2 + (3 * j), f"{fill}T{fill}")
            elif cell.terrain == "encounter":
                stdscr.addstr(2 + i, 2 + (3 * j), f"{fill}E{fill}")
            elif cell.terrain == "store":
                stdscr.addstr(2 + i, 2 + (3 * j), f"{fill}${fill}")
            else:
                if fill == "▒":
                    stdscr.addstr(2 + i, 2 + (3 * j), f"{fill}░{fill}")
                else:
                    stdscr.addstr(2 + i, 2 + (3 * j), f"{fill}▒{fill}")
        stdscr.addstr(2 + i, 2 + (3 * (j + 1)), "║")
    stdscr.addstr(len(grid) + 2, 1, f"╚{line}╝")

def output_pythomon_art(stdscr, h, w, pythomon, player_ownership):
    for i, line in enumerate(pythomon.art):
        if player_ownership:
            stdscr.addstr(i + h, w, line)
        else:
            stdscr.addstr(i + h, w, line[::-1])
    stdscr.addstr(h + 9, w, pythomon.name)
    stdscr.addstr(h + 10, w, f"{pythomon.nature} {pythomon.gender}")
    stdscr.addstr(h + 11, w, f"HP: {pythomon.healthbar}")

def attack_prompts(stdscr, h, w, owner, attacker, move_idx, target):
    stdscr.addstr(17, 5, f"{owner} {attacker.name} uses {attacker.moves[move_idx].get('name')} against {target.name}!")
    stdscr.refresh()
    time.sleep(2)
    stdscr.addstr(17, 5, f"{' ' * w}")
    stdscr.addstr(17, 5, f"{target.name} took {attacker.base_atk + attacker.moves[move_idx].get('power')} damage!")
    stdscr.refresh()
    time.sleep(2)
    return attacker.attack(target, move_idx)

def encounter(stdscr, h, w, player, pythomon_target):
    # 1. print encounter
    init_menu = ["Fight", "Item", "Run"]
    engaged_menu = ["Attack", "Item", "Switch", "Run"]
    moves_selection = 0
    init_selection = 0
    mode = "Start"
    keypress = 0
    pythodeck_selection = 0
    start_range = 0
    end_range = start_range + 4
    max_range = len(player.pythomon)
    turn = 1
    deployed = False
    while pythomon_target.hp > 0:
        stdscr.clear()

        # Always print encountered pythomon
        output_pythomon_art(stdscr, 3, 50, pythomon_target, False)
        
        if deployed:
            # Print player's pythomon
            output_pythomon_art(stdscr, 3, 5, player.pythomon[pythodeck_selection + start_range], True)

        if turn % 2 == 1:
            # Engaged mode (selected a pythomon)
            if mode == "Engaged" or mode == "Attack":                
                # Print menu option for engaged mode
                for i, option in enumerate(engaged_menu):
                    if i == init_selection:
                        stdscr.attron(curses.color_pair(1))
                        stdscr.addstr((19) + i, 5, option)
                        stdscr.attroff(curses.color_pair(1))
                    else:
                        stdscr.addstr(19 + i, 5, option)
                
                if mode == "Engaged":
                    keypress = stdscr.getch()
                    if keypress == curses.KEY_UP and init_selection > 0:
                        init_selection -= 1
                    elif keypress == curses.KEY_DOWN and init_selection < (len(engaged_menu) - 1):
                        init_selection += 1
                    elif (keypress == curses.KEY_ENTER or keypress in [10, 13]) and engaged_menu[init_selection] == "Attack":
                        mode = "Attack"
                
                elif mode == "Attack":
                    stdscr.addstr(19, 15, ">")
                    for i, option in enumerate(player.pythomon[pythodeck_selection + start_range].moves):
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
                    elif keypress == curses.KEY_DOWN and moves_selection < (len(player.pythomon[pythodeck_selection + start_range].moves) - 1):
                        moves_selection += 1
                    elif keypress == curses.KEY_BACKSPACE or keypress == 8:
                        mode = "Engaged"
                    elif (keypress == curses.KEY_ENTER or keypress in [10, 13]):
                        # Commence attack! Returns true if target is defeated
                        if attack_prompts(stdscr, h, w, f"{player.name}'s", player.pythomon[pythodeck_selection + start_range], moves_selection, pythomon_target):
                            # means player defeated
                            player.money += pythomon_target.money_prize
                            if player.pythomon[pythodeck_selection + start_range].level_up(pythomon_target.exp_prize):
                                # means pythomon leveled up
                                pass
                            # should break out of loop i guess
                        mode = "Engaged"

            # Initial start of encounter mode
            if mode == "Start" or mode == "Select Pythomon":
                # Print initial menu
                for i, option in enumerate(init_menu):
                    if i == init_selection:
                        stdscr.attron(curses.color_pair(1))
                        stdscr.addstr((19) + i, 5, option)
                        stdscr.attroff(curses.color_pair(1))
                    else:
                        stdscr.addstr(19 + i, 5, option)
                
                if mode == "Start":
                    keypress = stdscr.getch()
                    if keypress == curses.KEY_UP and init_selection > 0:
                        init_selection -= 1
                    elif keypress == curses.KEY_DOWN and init_selection < (len(init_menu) - 1):
                        init_selection += 1
                    elif (keypress == curses.KEY_ENTER or keypress in [10, 13]) and init_menu[init_selection] == "Fight":
                        mode = "Select Pythomon"

                elif mode == "Select Pythomon":
                    # select from player's pythomon roster
                    stdscr.addstr(19, 15, ">")
                    for i, option in enumerate(player.pythomon[start_range:min(end_range, max_range)]):
                        blank_space = ' ' * (16 - len(option.name))
                        if i == pythodeck_selection:
                            stdscr.attron(curses.color_pair(1))
                            stdscr.addstr((19) + i, 20, f"{option.name}{blank_space}HP:{option.hp}/{option.max_hp}")
                            stdscr.attroff(curses.color_pair(1))
                        else:
                            stdscr.addstr((19) + i, 20, f"{option.name}{blank_space}HP:{option.hp}/{option.max_hp}")
                
                    keypress = stdscr.getch()    
                
                    if keypress == curses.KEY_UP and pythodeck_selection > start_range:
                        pythodeck_selection -= 1
                    elif keypress == curses.KEY_UP and pythodeck_selection == start_range and pythodeck_selection > 0:
                        start_range -= 1
                        end_range -= 1
                    elif keypress == curses.KEY_DOWN and pythodeck_selection < (len(player.pythomon[start_range:min(end_range, max_range)]) - 1):
                        pythodeck_selection += 1
                    elif keypress == curses.KEY_DOWN and pythodeck_selection == (len(player.pythomon[start_range:min(end_range, max_range)]) - 1) and end_range != len(player.pythomon):
                        start_range += 1
                        end_range += 1
                    elif keypress == curses.KEY_BACKSPACE or keypress == 8:
                        mode = "Start"
                    elif (keypress == curses.KEY_ENTER or keypress in [10, 13]):
                        deployed = True
                        mode = "Engaged"
        # computer's turn
        else:
            pass
        stdscr.refresh()
    # 2. menu
        # fight
            # choose pokemon
        # item
        # run
    # 3. battle
        # if win, capture
        # if lose, go to next pythomon or game over

    stdscr.refresh()
    time.sleep(5)
