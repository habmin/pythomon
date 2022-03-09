import curses
import random

from prompts import *

def battle(stdscr, h, w, g_h, g_w, player, pythomon_target, target_owner, init_menu, engaged_menu):
    # Menu selectors and range handlers for different menus
    
    # For attack moves selection/menu
    moves_selection = 0

    # For initial/engaged menu selection/menu
    init_selection = 0

    # For selecting and switching out pythomon selection/menu
    pythodeck_selection = 0
    pytho_start_range = 0
    pytho_end_range = pytho_start_range + min(len(player.pythomon), 4)
    pytho_max_range = len(player.pythomon)
    # Stores the index for current selected pythomon
    pytho_select_index = 0

    # For item selection/menu
    item_selection = 0
    item_start_range = 0
    item_end_range = item_start_range + min(len(player.bag), 4)
    item_max_range = len(player.bag)

    # For deciding which pythomon to heal selection/menu
    health_selection = 0
    damaged_start_range = 0

    # A key aspect in order for battle() to work, it's important to print and switch
    # to the relavent keyboard listeners in order to work the menu selection correctly.
    # This is done by switching to certain modes throughout the function's cycle.
    # Begin with 'Start' mode
    mode = "Start"
    # keypress handler
    keypress = 0
    # 1 starts with players turn, every odd turn is the players
    turn = 1
    # Used to show deployed pythomon or not
    deployed = False

    # Loops until target pythomon is defeated
    while pythomon_target.hp > 0:

        stdscr.clear()

        print_box(stdscr, h, w, g_h, g_w)

        g_h_offset = (h // 2) - (g_h // 2)

        # print encountered pythomon until dead
        print_pythomon(stdscr, g_h_offset + 2, ((w // 2) + (g_w // 2)) - 37, pythomon_target, False, False)
        
        # Print player's pythomon once selected/deployed
        if deployed:
            print_pythomon(stdscr, g_h_offset + 2, ((w // 2) - (g_w // 2)) + 13, player.pythomon[pytho_select_index], True, False)

        # Players turn
        if turn % 2 == 1:
            # Initial start of encounter mode
            if mode == "Start":
                # Print initial menu
                print_menu_1(stdscr, g_h_offset + 17, ((w // 2) - (g_w // 2)) + 5, init_menu, init_selection)
                
                keypress = stdscr.getch()
                if keypress == ord('q'):
                    quit_prompt(stdscr, h, w, g_h, g_w)

                elif keypress == curses.KEY_UP and init_selection > 0:
                    init_selection -= 1
                elif keypress == curses.KEY_DOWN and init_selection < (len(init_menu) - 1):
                    init_selection += 1
                elif (keypress == curses.KEY_ENTER or keypress in [10, 13]) and init_menu[init_selection] == "Fight":
                    mode = "Select Pythomon"
                elif (keypress == curses.KEY_ENTER or keypress in [10, 13]) and init_menu[init_selection] == "Item":
                    mode = "Start-Item"
                elif (keypress == curses.KEY_ENTER or keypress in [10, 13]) and init_menu[init_selection] == "Run":
                    break
            
            # Selection or switching out pokemon
            elif mode == "Select Pythomon" or mode == "Switch":
                # Print initial menu selection if selecting pythomon
                if mode == "Select Pythomon":
                    print_menu_1(stdscr, g_h_offset + 17, ((w // 2) - (g_w // 2)) + 5, init_menu, init_selection)
                # Print engaged menu if switching out pythomon
                else:
                    print_menu_1(stdscr, g_h_offset + 17, ((w // 2) - (g_w // 2)) + 5, engaged_menu, init_selection)
                
                # Print pythomon selection menu
                # Trims to at most 4 selection options based on the start and end ranges
                # The last two arguements will print scroll indicators if there's more options for
                # the player to choose from their total pythodeck
                print_menu_select_pythomon(stdscr, g_h_offset + 17, ((w // 2) - (g_w // 2)) + 20, player.pythomon[pytho_start_range:min(pytho_end_range, pytho_max_range)], pythodeck_selection, pytho_end_range < pytho_max_range, pytho_start_range > 0)

                # Keyboard listerners/handlers
                keypress = stdscr.getch()
                if keypress == ord('q'):
                    quit_prompt(stdscr, h, w, g_h, g_w)   

                elif keypress == curses.KEY_UP and pythodeck_selection > 0:
                    pythodeck_selection -= 1
                # Decrease the menu range (scroll up)
                elif keypress == curses.KEY_UP and pytho_start_range > 0 and pythodeck_selection == 0:
                    pytho_start_range -= 1
                    pytho_end_range -= 1
                elif keypress == curses.KEY_DOWN and pythodeck_selection < (len(player.pythomon[pytho_start_range:min(pytho_end_range, pytho_max_range)]) - 1):
                    pythodeck_selection += 1
                # Increase the menu range (scroll down)
                elif keypress == curses.KEY_DOWN and pythodeck_selection == (len(player.pythomon[pytho_start_range:min(pytho_end_range, pytho_max_range)]) - 1) and pytho_end_range != len(player.pythomon):
                    pytho_start_range += 1
                    pytho_end_range += 1
                elif keypress == curses.KEY_BACKSPACE or keypress == 8:
                    if mode == "Select Pythomon":
                        mode = "Start"
                    else:
                        mode = "Engaged"
                elif (keypress == curses.KEY_ENTER or keypress in [10, 13]) and player.pythomon[pythodeck_selection + pytho_start_range].status == "alive":
                    pytho_select_index = pythodeck_selection + pytho_start_range
                    pythodeck_selection = 0
                    pytho_start_range = 0
                    pytho_end_range = pytho_start_range + min(len(player.pythomon), 4)
                    pytho_max_range = len(player.pythomon)
                    deployed = True
                    mode = "Engaged"

            # Item selection menu
            elif mode == "Start-Item" or mode == "Engaged-Item":
                if mode == "Start-Item":
                    print_menu_1(stdscr, g_h_offset + 17, ((w // 2) - (g_w // 2)) + 5, init_menu, init_selection)
                else:
                    print_menu_1(stdscr, g_h_offset + 17, ((w // 2) - (g_w // 2)) + 5, engaged_menu, init_selection)

                stdscr.addstr(g_h_offset + 17, ((w // 2) - (g_w // 2)) + 15, ">")
                # Indicate if player has no items
                if len(player.bag) == 0:
                    stdscr.attron(curses.color_pair(1))
                    stdscr.addstr( g_h_offset + 17, ((w // 2) - (g_w // 2)) + 20, "No Items")
                    stdscr.attroff(curses.color_pair(1))
                # otherwise, Print item selection menu
                # Trims to at most 4 selection options based on the start and end ranges
                # The last two arguements will print scroll indicators if there's more options for
                # the player to choose from their total bag
                else:
                    print_menu_1(stdscr, g_h_offset + 17, ((w // 2) - (g_w // 2)) + 20, player.bag[item_start_range:min(item_end_range, item_max_range)], item_selection, item_start_range > 0, item_end_range < item_max_range)
    
                keypress = stdscr.getch()
                if keypress == ord('q'):
                    quit_prompt(stdscr, h, w, g_h, g_w)     
            
                elif keypress == curses.KEY_UP and item_selection > 0:
                    item_selection -= 1
                elif keypress == curses.KEY_UP and item_start_range > 0 and item_selection == 0:
                    item_start_range -= 1
                    item_end_range -= 1
                elif keypress == curses.KEY_DOWN and item_selection < (len(player.bag[item_start_range:min(item_end_range, item_max_range)]) - 1):
                    item_selection += 1
                elif keypress == curses.KEY_DOWN and item_selection == (len(player.bag[item_start_range:min(item_end_range, item_max_range)]) - 1) and item_end_range != len(player.bag):
                    item_start_range += 1
                    item_end_range += 1
                elif keypress == curses.KEY_BACKSPACE or keypress == 8:
                    if mode == "Start-Item":
                        mode = "Start"
                    else:
                        mode = "Engaged"
                elif (keypress == curses.KEY_ENTER or keypress in [10, 13]) and len(player.bag) != 0:
                    if player.bag[item_selection + item_start_range] == "Capture Ball":
                        if mode == "Start-Item":
                            capture_prompts(stdscr, g_h_offset + 15, ((w // 2) - (g_w // 2)) + 5, g_w, player, None, item_selection + item_start_range, pythomon_target, target_owner, False)
                        else:
                            if capture_prompts(stdscr, g_h_offset + 15, ((w // 2) - (g_w // 2)) + 5, g_w, player, player.pythomon[pytho_select_index], item_selection + item_start_range, pythomon_target, target_owner, True):
                                break
                    else:
                        if mode == "Start-Item":
                            mode = "Start-Heal"
                        else: 
                            mode = "Engaged-Heal"
            
            # Heal menu mode
            elif mode == "Start-Heal" or mode == "Engaged-Heal":
                # Create list/menu based if player is trying to revive dead pythomon or heal hurt pythomon
                if player.bag[item_selection + item_start_range] == "Revive":
                    damaged_pythomon = list(filter(lambda pythomon: pythomon.status == "dead", player.pythomon))
                else:
                    damaged_pythomon = list(filter(lambda pythomon: pythomon.hp < pythomon.max_hp and pythomon.status == "alive", player.pythomon))
                
                # These range handlers are initialized here to ensure dynamic sizing of the menu
                # As the menu length changes mid battle and item useage
                damaged_end_range = damaged_start_range + min(len(damaged_pythomon), 4)
                damaged_max_range = len(damaged_pythomon)         
                
                
                if mode == "Start-Heal":
                    print_menu_1(stdscr, g_h_offset + 17, ((w // 2) - (g_w // 2)) + 5, init_menu, init_selection)
                else:
                    print_menu_1(stdscr, g_h_offset + 17, ((w // 2) - (g_w // 2)) + 5, engaged_menu, init_selection)

                # print item menu
                stdscr.addstr(g_h_offset + 17, ((w // 2) - (g_w // 2)) + 15, ">")
                print_menu_1(stdscr, g_h_offset + 17, ((w // 2) - (g_w // 2)) + 20, player.bag[item_start_range:min(item_end_range, item_max_range)], item_selection, item_start_range > 0, item_end_range < item_max_range)
                
                # print heal menu
                print_heal_menu(stdscr, g_h_offset + 17, ((w // 2) - (g_w // 2)) + 41, damaged_pythomon[damaged_start_range:min(damaged_end_range, damaged_max_range)], health_selection, damaged_start_range, damaged_end_range, damaged_max_range, player.bag[item_selection + item_start_range])
                
                keypress = stdscr.getch()
                if keypress == ord('q'):
                    quit_prompt(stdscr, h, w, g_h, g_w)     
            
                elif keypress == curses.KEY_UP and health_selection > 0:
                    health_selection -= 1
                elif keypress == curses.KEY_UP and damaged_start_range > 0 and health_selection == 0:
                    damaged_start_range -= 1
                    damaged_end_range -= 1
                elif keypress == curses.KEY_DOWN and health_selection < (len(damaged_pythomon[damaged_start_range:min(damaged_end_range, damaged_max_range)]) - 1):
                    health_selection += 1
                elif keypress == curses.KEY_DOWN and health_selection == (len(damaged_pythomon[damaged_start_range:min(damaged_end_range, damaged_max_range)]) - 1) and damaged_end_range != len(damaged_pythomon):
                    damaged_start_range += 1
                    damaged_end_range += 1
                elif keypress == curses.KEY_BACKSPACE or keypress == 8:
                    if mode == "Start-Heal":
                        mode = "Start-Item"
                    else:
                        mode = "Engaged-Item"
                elif (keypress == curses.KEY_ENTER or keypress in [10, 13]) and len(damaged_pythomon) > 0:
                    if player.bag[item_selection + item_start_range] == "Revive":
                        damaged_pythomon[health_selection + damaged_start_range].revive()
                    elif player.bag[item_selection + item_start_range] == "Health Spray":
                        damaged_pythomon[health_selection + damaged_start_range].heal(20)
                    else:
                        damaged_pythomon[health_selection + damaged_start_range].heal(50)
                    # reset selection/range handlers
                    health_selection = 0
                    damaged_start_range = 0
                    player.bag.pop(item_selection + item_start_range)
                    item_selection = 0
                    item_start_range = 0
                    item_end_range = item_start_range + min(len(player.bag), 4)
                    item_max_range = len(player.bag)
                    stdscr.addstr(14, 5, f"HP: {player.pythomon[pytho_select_index]}")
                    if mode == "Start-Heal":
                        mode = "Start-Item"
                    else:
                        print_pythomon(stdscr, 14, 5, player.pythomon[health_selection + damaged_start_range], True, False)
                        turn += 1
                        mode = "CPU"
            
            elif mode == "Engaged":                
                # Print menu option for engaged mode
                print_menu_1(stdscr, g_h_offset + 17, ((w // 2) - (g_w // 2)) + 5, engaged_menu, init_selection)

                keypress = stdscr.getch()
                if keypress == ord('q'):
                    quit_prompt(stdscr, h, w, g_h, g_w)     
            
                elif keypress == curses.KEY_UP and init_selection > 0:
                    init_selection -= 1
                elif keypress == curses.KEY_DOWN and init_selection < (len(engaged_menu) - 1):
                    init_selection += 1
                elif (keypress == curses.KEY_ENTER or keypress in [10, 13]) and engaged_menu[init_selection] == "Attack":
                    mode = "Attack"
                elif (keypress == curses.KEY_ENTER or keypress in [10, 13]) and engaged_menu[init_selection] == "Item":
                    mode = "Engaged-Item"
                elif (keypress == curses.KEY_ENTER or keypress in [10, 13]) and engaged_menu[init_selection] == "Switch":
                    mode = "Switch"
                elif (keypress == curses.KEY_ENTER or keypress in [10, 13]) and engaged_menu[init_selection] == "Run":
                    break
                
            elif mode == "Attack":
                # Print menu option for engaged mode
                print_menu_1(stdscr, g_h_offset + 17, ((w // 2) - (g_w // 2)) + 5, engaged_menu, init_selection)
                
                stdscr.addstr(g_h_offset + 17, ((w // 2) - (g_w // 2)) + 15, ">")
                for i, option in enumerate(player.pythomon[pytho_select_index].moves):
                    blank_space = ' ' * (16 - len(option["name"]))
                    if i == moves_selection:
                        stdscr.attron(curses.color_pair(1))
                        stdscr.addstr((g_h_offset + 17) + i, ((w // 2) - (g_w // 2)) + 20, "{}{}POW:{}".format(option["name"], blank_space, option["power"]))
                        stdscr.attroff(curses.color_pair(1))
                    else:
                        stdscr.addstr((g_h_offset + 17) + i, ((w // 2) - (g_w // 2)) + 20, "{}{}POW:{}".format(option["name"], blank_space, option["power"]))

                keypress = stdscr.getch()
                if keypress == ord('q'):
                    quit_prompt(stdscr, h, w, g_h, g_w)     
            
                elif keypress == curses.KEY_UP and moves_selection > 0:
                    moves_selection -= 1
                elif keypress == curses.KEY_DOWN and moves_selection < (len(player.pythomon[pytho_select_index].moves) - 1):
                    moves_selection += 1
                elif keypress == curses.KEY_BACKSPACE or keypress == 8:
                    mode = "Engaged"
                elif (keypress == curses.KEY_ENTER or keypress in [10, 13]):
                    # Commence attack! Returns true if target is defeated
                    if attack_prompts(stdscr, g_h_offset + 15, ((w // 2) - (g_w // 2)) + 5, f"{player.name}'s", player.pythomon[pytho_select_index], moves_selection, pythomon_target, True):
                        win_prompts(stdscr, g_h_offset + 15, ((w // 2) - (g_w // 2)) + 5, player, player.pythomon[pytho_select_index], pythomon_target, target_owner)
                        # exit encounter
                        break
                    else:
                        turn += 1
                        mode = "CPU"
            
        # computer's turn
        else:
            # If player's pythomon is killed, returns true
            if attack_prompts(stdscr, g_h_offset + 15, ((w // 2) - (g_w // 2)) + 5, target_owner, pythomon_target, random.randint(0, len(pythomon_target.moves) - 1), player.pythomon[pytho_select_index], False):
                # If player's entire team is dead, the player loses and returns True
                if defeated_prompts(stdscr, g_h_offset + 15, ((w // 2) - (g_w // 2)) + 5, player, player.pythomon[pytho_select_index], pythomon_target, target_owner):
                    return True
                # Otherwise, player can send out another pythomon
                else:
                    deployed = False
                    mode = "Start"
            # Player's pythomon survived
            else:
                mode = "Engaged"
            # Player's turn
            turn += 1

        stdscr.refresh()
    
    # player was not defeated by battle
    return False
