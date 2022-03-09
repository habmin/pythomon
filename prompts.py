import curses
import time
from assets import trainer_art

def refresh_sleep(stdscr, sec):
    stdscr.refresh()
    time.sleep(sec)
    curses.flushinp()

def quit_prompt(stdscr):
    stdscr.addstr(0, 0, "Are you sure you want to Quit? Press 'y' to confirm, otherwise press any other key to cancel")
    keypress = stdscr.getch()
    if keypress == ord('y'):
        curses.curs_set(1)
        curses.endwin()
        exit(0)

def print_menu_1(stdscr, h, w, menu, selection, list_up_indicate = False, list_down_indicate = False):
    if list_up_indicate:
        stdscr.addstr(h, w - 2, "▲")
    for i, option in enumerate(menu):
        if i == selection:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(h + i, w, option)
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(h + i, w, option)
    if list_down_indicate:
        stdscr.addstr(h + 3, w - 2, "▼")

def print_menu_select_pythomon(stdscr, h, w, menu, selection, list_down_indicate, list_up_indicate):
    stdscr.addstr(h, w - 5, ">")
    if list_up_indicate:
        stdscr.addstr(h, w - 2, "▲")
    for i, option in enumerate(menu):
        blank_space = ' ' * (16 - len(option.name))
        if i == selection:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(h + i, w, f"{option.name}{blank_space}HP:{option.hp}/{option.max_hp}")
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(h + i, w, f"{option.name}{blank_space}HP:{option.hp}/{option.max_hp}")
    if list_down_indicate:
        stdscr.addstr(h + 3, w - 2, "▼")

def print_menu_center(stdscr, h, w, menu, selection):
    for i, option in enumerate(menu):
        if i == selection:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(h + i, ((w // 2) - (len(option) // 2)), option)
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(h + i, ((w // 2) - (len(option) // 2)), option)

def print_heal_menu(stdscr, h, w, h_menu, h_selection, h_start, h_end, h_max, item):
    if len(h_menu) == 0:
        stdscr.attron(curses.color_pair(1))
        if item == "Revive":
            stdscr.addstr(h, w, "All Pythomon are alive")
        else:
            stdscr.addstr(h, w, "All Pythomon are at MAX HP")
        stdscr.attroff(curses.color_pair(1))
    else:
        print_menu_select_pythomon(stdscr, h, w, h_menu, h_selection, h_end < h_max, h_start > 0)

def print_pythomon(stdscr, h, w, pythomon, player_ownership, dead):
    for i, line in enumerate(pythomon.art):
        if dead:
            stdscr.addstr(i + h, w, (' ' * len(line)))
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
    refresh_sleep(stdscr, 2)
    if players_turn:
        print_pythomon(stdscr, 3, 50, target, not players_turn, False)
    else:
        print_pythomon(stdscr, 3, 5, target, not players_turn, False)
    stdscr.addstr(h, 0, f"{' ' * w}")
    stdscr.addstr(h, 5, f"{target.name} took {attacker.base_atk + attacker.moves[move_idx].get('power')} damage!")
    refresh_sleep(stdscr, 2)
    return did_defeat

def level_up_prompt(stdscr, h, w, player, players_pythomon, encounter):
    stdscr.addstr(h, 0, f"{' ' * w}")
    stdscr.addstr(h, 5, f"{players_pythomon.name} gained {encounter.exp_prize} EXP!")
    refresh_sleep(stdscr, 2)
    if players_pythomon.level_up(encounter.exp_prize):
        stdscr.addstr(h, 0, f"{' ' * w}")
        stdscr.addstr(h, 5, f"{players_pythomon.name} leveled up! Gained 3 MAX HP and ATK")
        refresh_sleep(stdscr, 2)
    if len(player.pythomon) > 1:
        stdscr.addstr(h, 0, f"{' ' * w}")
        stdscr.addstr(h, 5, f"Your team gains {encounter.exp_prize // 2} EXP!")
        refresh_sleep(stdscr, 2)
    for pythomon in player.pythomon:
        if pythomon == players_pythomon:
            continue
        elif pythomon.level_up(encounter.exp_prize // 2):
            stdscr.addstr(h, 0, f"{' ' * w}")
            stdscr.addstr(h, 5, f"{pythomon.name} leveled up! Gained 3 MAX HP and ATK")
            refresh_sleep(stdscr, 2)

def win_prompts(stdscr, h, w, player, players_pythomon, encounter, encounter_owner):
    stdscr.addstr(h, 0, f"{' ' * w}")
    print_pythomon(stdscr, 3, 50, encounter, False, True)
    stdscr.addstr(h, 5, f"{player.name} defeated {encounter_owner} {encounter.name}!")
    refresh_sleep(stdscr, 2)
    stdscr.addstr(h, 0, f"{' ' * w}")
    stdscr.addstr(h, 5, f"You gained ${encounter.money_prize}!")
    player.money += encounter.money_prize
    refresh_sleep(stdscr, 2)
    level_up_prompt(stdscr, h, w, player, players_pythomon, encounter)

def capture_prompts(stdscr, h, w, player, players_pythomon, item_idx, encounter, encounter_owner, engaged):
    if not engaged:
        stdscr.addstr(h, 0, f"{' ' * w}")
        stdscr.addstr(h, 5, "Must engaged in battle first!")
        refresh_sleep(stdscr, 2)
    elif encounter_owner != "Wild":
        stdscr.addstr(h, 0, f"{' ' * w}")
        stdscr.addstr(h, 5, "Can only use on Wild Pythomon!")
        refresh_sleep(stdscr, 2)
    else:
        player.bag.pop(item_idx)
        stdscr.addstr(h, 0, f"{' ' * w}")
        stdscr.addstr(h, 5, f"Attempted to capture Wild {encounter.name}!")
        refresh_sleep(stdscr, 2)
        if encounter.hp <= encounter.max_hp * 0.4:
            # success
            print_pythomon(stdscr, 3, 50, encounter, False, True)
            player.pythomon.append(encounter)
            stdscr.addstr(h, 0, f"{' ' * w}")
            stdscr.addstr(h, 5, f"You caught {encounter.name}!")
            refresh_sleep(stdscr, 2)
            level_up_prompt(stdscr, h, w, player, players_pythomon, encounter)
            return True
        else:
            stdscr.addstr(h, 0, f"{' ' * w}")
            stdscr.addstr(h, 5, f"{encounter.name} managed to escape!")
            refresh_sleep(stdscr, 2)
    return False

def defeated_prompts(stdscr, h, w, player, defeated_pythomon, encounter, encounter_owner):
    print_pythomon(stdscr, 3, 5, defeated_pythomon, True, True)
    stdscr.addstr(h, 0, f"{' ' * w}")
    stdscr.addstr(h, 5, f"{encounter_owner} {encounter.name} defeated your {defeated_pythomon.name}!")
    refresh_sleep(stdscr, 2)
    if player.check_defeated():
        stdscr.addstr(h, 0, f"{' ' * w}")
        stdscr.addstr(h, 5, f"Your entire team is wiped out!")
        refresh_sleep(stdscr, 3)
        return True
    return False

def print_trainer(stdscr, h, w):
    for i, line in enumerate(trainer_art):
        stdscr.addstr(h + i, (w // 2) - (len(line)// 2), line)

def print_box(stdscr, h, w):
    line = "═" * (w - 2)
    stdscr.addstr(0, 0, f"╔{line}╗")
    for i in range(h - 3):
        stdscr.addstr(i + 1, 0, "║")
        stdscr.addstr(i + 1, w - 1, "║")
    stdscr.addstr(h - 2, 0, f"╚{line}╝")
