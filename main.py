import curses
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
    menu = ["Player's Name", "Player's Gender", "Nature", "Starter", "Finish"]
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
        stdscr.addstr(5, ((w // 2) - 14), player_name_buffer)
        stdscr.addstr(6, ((w // 2) - 14), player_gender_buffer)
        stdscr.addstr(7, ((w // 2) - 12), traits[trait_selection])
        stdscr.addstr(8, ((w // 2) - 12), pythodeck[starter_selection]["name"])
        stdscr.addstr(10, ((w // 2) - 12), "HP: {}".format(str(pythodeck[starter_selection]["hp"])))
        stdscr.addstr(11, ((w // 2) - 12), "Base Attack: {}".format(str(pythodeck[starter_selection]["base_atk"])))
        stdscr.addstr(12, ((w // 2) - 12), "Gender: {}".format(str(pythodeck[starter_selection]["gender"])))
        
        # Cursor location
        if menu[selection] == "Player's Name":
            stdscr.move(5, ((w // 2) - 14 + len(player_name_buffer)))
        elif menu[selection] == "Player's Gender":
            stdscr.move(6, ((w // 2) - 14 + len(player_gender_buffer)))
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
            return Player(player_name_buffer, player_gender_buffer, player_trait_buffer)
        
        # Input handlers
        elif menu[selection] == "Player's Name":
            if keypress >= 32 and keypress <= 126 and len(player_name_buffer) <= 15:
                player_name_buffer += chr(keypress)
            elif keypress in [8, 127] and len(player_name_buffer) != 0:
                player_name_buffer = player_name_buffer[:-1]
        elif menu[selection] == "Player's Gender":
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

                                                            