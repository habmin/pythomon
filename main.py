import curses

def start_screen(stdscr, h, w):
    title = ["  _ \ \ \   / __ __|  |   |   _ \    \  |   _ \    \  |  |",
             " |   | \   /     |    |   |  |   |  |\/ |  |   |    \ |  |",
             " ___/     |      |    ___ |  |   |  |   |  |   |  |\  | _|",
             "_|       _|     _|   _|  _| \___/  _|  _| \___/  _| \_| _)"]
    subtitle = "Pythomon! - A Python Battle Game!"
    directions = "Press 'Enter' to begin, or 'q' to exit."

    keypress = 0
    while (keypress != curses.KEY_ENTER or keypress != 10):
        stdscr.clear()
        if keypress == ord('q'):
            exit(0)
        elif keypress == curses.KEY_ENTER or keypress in [10, 13]:
            break
        for i, line in enumerate(title):
            stdscr.attron(curses.color_pair(2))
            stdscr.addstr((h // 2) - (10 - i), ((w // 2) - (len(line) // 2)), line)
            stdscr.attroff(curses.color_pair(2))
        stdscr.addstr((h // 2) - 6, ((w // 2) - (len(subtitle) // 2)), subtitle)
        stdscr.addstr((h // 2) + 3, ((w // 2) - (len(directions) // 2)), directions, curses.A_REVERSE)
        stdscr.refresh()
        keypress = stdscr.getch()
    return


def menu_display(stdscr, menu, selected, h, w):
    stdscr.clear()
    for i, option in enumerate(menu):
        if i == selected:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr((h // 2) + i, ((w // 2) - (len(option) // 2)), option)
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr((h // 2) + i, ((w // 2) - (len(option) // 2)), option)
    stdscr.refresh()
    return

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

    # Menu Selection Screen
    selection = 0
    menu = ["Option 1", "Option 2", "Option 3", "Quit"]
    keypress = 0
    menu_display(stdscr, menu, selection, height, width)
    while True:
        keypress = stdscr.getch()
        if keypress == curses.KEY_UP and selection > 0:
            selection -= 1
        elif keypress == curses.KEY_DOWN and selection < (len(menu) - 1):
            selection += 1
        elif (keypress == curses.KEY_ENTER or keypress in [10, 13]) and menu[selection] == "Quit":
            break
        menu_display(stdscr, menu, selection, height, width)
        stdscr.refresh()

    # Done with program, reset curs_set and end
    curses.curs_set(1)
    curses.endwin()
    exit(0)

if __name__ == "__main__":
    curses.wrapper(main)
                                                            