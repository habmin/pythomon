import curses

def main(stdscr):
    curses.curs_set(0)
    keypress = 0
    stdscr.clear()
    while (keypress != ord('q')):
        stdscr.clear()
        height, width = stdscr.getmaxyx()
        if keypress == 0:
            stdscr.addstr((height // 2), (width // 2), f"Press a key (q to quit)")
        else:
            stdscr.addstr((height // 2), (width // 2), f"{chr(keypress)}")
        stdscr.refresh()
        keypress = stdscr.getch()
    curses.endwin()

if __name__ == "__main__":
    curses.wrapper(main)
