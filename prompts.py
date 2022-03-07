import curses
import time

def quit_prompt(stdscr):
    stdscr.addstr(0, 0, "Are you sure you want to Quit? Press 'y' to confirm, otherwise press any other key to cancel")
    keypress = stdscr.getch()
    if keypress == ord('y'):
        curses.curs_set(1)
        curses.endwin()
        exit(0)

def print_menu_1(stdscr, h, w, menu, selection):
    for i, option in enumerate(menu):
        if i == selection:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(h + i, w, option)
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(h + i, w, option)

def print_pythomon(stdscr, h, w, pythomon, player_ownership, dead):
    for i, line in enumerate(pythomon.art):
        if dead:
            stdscr.addstr(i + h, w, (' ' * 20))
        elif player_ownership:
            stdscr.addstr(i + h, w, line)
        else:
            stdscr.addstr(i + h, w, line[::-1])
    stdscr.addstr(h + 9, w, pythomon.name)
    stdscr.addstr(h + 10, w, f"{pythomon.nature} {pythomon.gender}")
    stdscr.addstr(h + 11, w, f"HP: {pythomon.healthbar}")

def attack_prompts(stdscr, h, w, owner, attacker, move_idx, target, players_turn):
    did_defeat = attacker.attack(target, move_idx)
    stdscr.addstr(h, 5, f"{owner} {attacker.name} uses {attacker.moves[move_idx].get('name')} against {target.name}!")
    stdscr.refresh()
    time.sleep(2)
    if players_turn:
        print_pythomon(stdscr, 3, 50, target, not players_turn, False)
    else:
        print_pythomon(stdscr, 3, 5, target, not players_turn, False)
    stdscr.addstr(h, 0, f"{' ' * w}")
    stdscr.addstr(h, 5, f"{target.name} took {attacker.base_atk + attacker.moves[move_idx].get('power')} damage!")
    stdscr.refresh()
    time.sleep(2)
    return did_defeat

def win_prompts(stdscr, h, w, player, players_pythomon, encounter, encounter_owner):
    stdscr.addstr(h, 0, f"{' ' * w}")
    print_pythomon(stdscr, 3, 50, encounter, False, True)
    stdscr.addstr(h, 5, f"{player.name} defeated {encounter_owner} {encounter.name}!")
    stdscr.refresh()
    time.sleep(2)
    stdscr.addstr(h, 0, f"{' ' * w}")
    stdscr.addstr(h, 5, f"You gained ${encounter.money_prize}!")
    player.money += encounter.money_prize
    stdscr.refresh()
    time.sleep(2)
    stdscr.addstr(h, 0, f"{' ' * w}")
    stdscr.addstr(h, 5, f"{players_pythomon.name} gained {encounter.exp_prize} EXP!")
    stdscr.refresh()
    time.sleep(2)
    if players_pythomon.level_up(encounter.exp_prize):
        stdscr.addstr(h, 0, f"{' ' * w}")
        stdscr.addstr(h, 5, f"{players_pythomon.name} leveled up! Gained 3 MAX HP and ATK")
        stdscr.refresh()
        time.sleep(2)
    stdscr.addstr(h, 0, f"{' ' * w}")
    stdscr.addstr(h, 5, f"Your team gains {encounter.exp_prize // 2} EXP!")
    stdscr.refresh()
    time.sleep(2)
    for pythomon in player.pythomon:
        if pythomon == players_pythomon:
            pass
        elif pythomon.level_up(encounter.exp_prize // 2):
            stdscr.addstr(h, 0, f"{' ' * w}")
            stdscr.addstr(h, 5, f"{pythomon.name} leveled up! Gained 3 MAX HP and ATK")
            stdscr.refresh()
            time.sleep(2)

def defeated_prompts(stdscr, h, w, player, defeated_pythomon, encounter, encounter_owner):
    print_pythomon(stdscr, 3, 5, defeated_pythomon, True, True)
    stdscr.addstr(h, 0, f"{' ' * w}")
    stdscr.addstr(h, 5, f"{encounter_owner} {encounter.name} defeated your {defeated_pythomon.name}!")
    stdscr.refresh()
    time.sleep(2)
    if player.check_defeated():
        stdscr.addstr(h, 0, f"{' ' * w}")
        stdscr.addstr(h, 5, f"Your entire team is wiped out!")
        stdscr.refresh()
        time.sleep(3)
        return True
    return False
