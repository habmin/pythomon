import curses
import time

from assets import trainer_art

# Helper/shorthand function that clears any player's input while sleep is active
def refresh_sleep(stdscr, sec):
    stdscr.refresh()
    time.sleep(sec)
    curses.flushinp()

# Helper/shorthand function when player wishes to quit
def quit_prompt(stdscr, h, w, g_h, g_w):
    stdscr.addstr((h // 2) - (g_h // 2), ((w // 2) - (g_w // 2)), "Are you sure you want to Quit? Press 'y' to confirm, otherwise press any other key to cancel")
    keypress = stdscr.getch()
    if keypress == ord('y'):
        curses.curs_set(1)
        curses.endwin()
        exit(0)

# A common print schematic for menu display and selections
# The list_up/list_down indicates are used for menus that have a dynamic menu size,
# and help indicate to the player there are more options than being shown in up
# or down directions.
# (pythodeck, item list)
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

# Specific menu format when displaying pythomon
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

# Prints menu using center paragraph formating
def print_menu_center(stdscr, h, w, menu, selection):
    for i, option in enumerate(menu):
        if i == selection:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(h + i, ((w // 2) - (len(option) // 2)), option)
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(h + i, ((w // 2) - (len(option) // 2)), option)

# Specific menu display/format when selection a healing item
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

# Prints pythomon art and info
def print_pythomon(stdscr, h, w, pythomon, player_ownership, dead):
    for i, line in enumerate(pythomon.art):
        # Prints blank spaces to convey pythomon has died
        if dead:
            stdscr.addstr(i + h, w, (' ' * len(line)))
        # Prints the art as formatted
        elif player_ownership:
            stdscr.addstr(i + h, w, line)
        # Mirrors the art to convey enemy pythomon (so they are facing each other)
        else:
            stdscr.addstr(i + h, w, line[::-1])
    stdscr.addstr(h + 9, w, pythomon.name)
    stdscr.addstr(h + 10, w, f"{pythomon.nature} {pythomon.gender}")
    stdscr.addstr(h + 11, w, f"HP: {pythomon.healthbar}")

def strike_animation(stdscr, h, w, pythomon, player_ownership):
    # Each frame is the width offset
    for i, offset in enumerate([0, 1, 2, 5, 2, 1, 0]):

        # Clear the space the pythomon animation will take place
        for j, line in enumerate(pythomon.art):
            if player_ownership:
                stdscr.addstr(j + h, w, (' ' * (len(line) + 5)))
            else:
                stdscr.addstr(j + h, w - 5, (' ' * (len(line) + 5)))

        # Print the pythomon, with each frame using the offset
        for k, line in enumerate(pythomon.art):
            if player_ownership:
                stdscr.addstr(k + h, w + offset, line)
            else:
                stdscr.addstr(k + h, w - offset, line[::-1])

        refresh_sleep(stdscr, 0.04)

def shake_pythomon(stdscr, h, w, pythomon, player_ownership):
    for i in range(15):
        for j, line in enumerate(pythomon.art):
            stdscr.addstr(j + h, w - 2, (' ' * (len(line) + 4)))
        for k, line in enumerate(pythomon.art):
            if i % 2 == 0:
                # Prints the art as formatted
                if player_ownership:
                    stdscr.addstr(k + h, w + 2, line)
                else:
                    stdscr.addstr(k + h, w + 2, line[::-1])
            else:
                if player_ownership:
                    stdscr.addstr(k + h, w -2, line)
                else:
                    stdscr.addstr(k + h, w -2, line[::-1])
        refresh_sleep(stdscr, 0.05)
    for i, line in enumerate(pythomon.art):
        stdscr.addstr(i + h, w - 2, (' ' * (len(line) + 4)))

# Attack prompt and sequence
def attack_prompts(stdscr, h, w, owner, attacker, move_idx, target, players_turn):
    # If the attacker defeats the targer, returns True
    did_defeat = attacker.attack(target, move_idx)
    stdscr.addstr(h, w, f"{' ' * 72}")
    stdscr.addstr(h, w, f"{owner} {attacker.name} uses {attacker.moves[move_idx].get('name')} against {target.name}!")
    refresh_sleep(stdscr, 1)
    if players_turn:
        strike_animation(stdscr, h - 13, w - 5 + 13, attacker, players_turn)
        shake_pythomon(stdscr, h - 13, w - 5 + 55, target, not players_turn)
        print_pythomon(stdscr, h - 13, w - 5 + 55, target, not players_turn, False)
    else:
        strike_animation(stdscr, h - 13, w - 5 + 55, attacker, players_turn)
        shake_pythomon(stdscr, h - 13, w - 5 + 13, target, not players_turn)
        print_pythomon(stdscr, h - 13, w - 5 + 13, target, not players_turn, False)
    stdscr.addstr(h, w, f"{' ' * 72}")
    stdscr.addstr(h, w, f"{target.name} took {attacker.base_atk + attacker.moves[move_idx].get('power')} damage!")
    refresh_sleep(stdscr, 2)
    return did_defeat

# Levels up if player wins a battle
def level_up_prompt(stdscr, h, w, player, players_pythomon, encounter):
    stdscr.addstr(h, w, f"{' ' * 72}")
    stdscr.addstr(h, w, f"{players_pythomon.name} gained {encounter.exp_prize} EXP!")
    refresh_sleep(stdscr, 2)
    if players_pythomon.level_up(encounter.exp_prize):
        stdscr.addstr(h, w, f"{' ' * 72}")
        stdscr.addstr(h, w, f"{players_pythomon.name} leveled up! Gained 3 MAX HP and ATK")
        refresh_sleep(stdscr, 2)
    
    # If player has more than one pythomon, will give half of the exp to the rest of the team
    if len(player.pythomon) > 1:
        stdscr.addstr(h, w, f"{' ' * 72}")
        stdscr.addstr(h, w, f"Your team gains {encounter.exp_prize // 2} EXP!")
        refresh_sleep(stdscr, 2)
    for pythomon in player.pythomon:
        # Skips the pythomon that won the battle
        if pythomon == players_pythomon:
            continue
        elif pythomon.level_up(encounter.exp_prize // 2):
            stdscr.addstr(h, w, f"{' ' * 72}")
            stdscr.addstr(h, w, f"{pythomon.name} leveled up! Gained 3 MAX HP and ATK")
            refresh_sleep(stdscr, 2)

# Win prompt sequence, used when the player wins a battle
def win_prompts(stdscr, h, w, player, players_pythomon, encounter, encounter_owner):
    print_pythomon(stdscr, h - 13, w - 5 + 55, encounter, False, True)
    stdscr.addstr(h, w, f"{' ' * 72}")
    stdscr.addstr(h, w, f"{player.name} defeated {encounter_owner} {encounter.name}!")
    refresh_sleep(stdscr, 2)
    stdscr.addstr(h, w, f"{' ' * 72}")
    stdscr.addstr(h, w, f"You gained ${encounter.money_prize}!")
    player.money += encounter.money_prize
    refresh_sleep(stdscr, 2)
    level_up_prompt(stdscr, h, w, player, players_pythomon, encounter)

# Capture pythomon sequence and prompt
def capture_prompts(stdscr, h, w, g_w, player, players_pythomon, item_idx, encounter, encounter_owner, engaged):
    # Checks to make sure player is engaged and is a wild pythomon (can't take a trainers pythomon!)
    if not engaged:
        stdscr.addstr(h, w, f"{' ' * 72}")
        stdscr.addstr(h, w, "Must engaged in battle first!")
        refresh_sleep(stdscr, 2)
    elif encounter_owner != "Wild":
        stdscr.addstr(h, w, f"{' ' * 72}")
        stdscr.addstr(h, w, "Can only use on Wild Pythomon!")
        refresh_sleep(stdscr, 2)
    else:
        player.bag.pop(item_idx)
        stdscr.addstr(h, w, f"{' ' * 72}")
        stdscr.addstr(h, w, f"Attempted to capture Wild {encounter.name}!")
        refresh_sleep(stdscr, 2)
        if encounter.hp <= encounter.max_hp * 0.4:
            # success
            print_pythomon(stdscr, h - 13, w - 5 + 55, encounter, False, True)
            player.pythomon.append(encounter)
            stdscr.addstr(h, w, f"{' ' * 72}")
            stdscr.addstr(h, w, f"You caught {encounter.name}!")
            refresh_sleep(stdscr, 2)
            stdscr.addstr(h, w, f"{' ' * 72}")
            stdscr.addstr(h, w, f"You gained ${encounter.money_prize}!")
            player.money += encounter.money_prize
            refresh_sleep(stdscr, 2)
            level_up_prompt(stdscr, h, w, player, players_pythomon, encounter)
            return True
        else:
            stdscr.addstr(h, w, f"{' ' * 72}")
            stdscr.addstr(h, w, f"{encounter.name} managed to escape!")
            refresh_sleep(stdscr, 2)
    return False

# Defeat sequence and prompt
def defeated_prompts(stdscr, h, w, player, defeated_pythomon, encounter, encounter_owner):
    print_pythomon(stdscr, h - 13, w - 5 + 13, defeated_pythomon, True, True)
    stdscr.addstr(h, w, f"{' ' * 72}")
    stdscr.addstr(h, w, f"{encounter_owner} {encounter.name} defeated your {defeated_pythomon.name}!")
    refresh_sleep(stdscr, 2)
    # If player's team is wiped out, the player is completed defeated
    if player.check_defeated():
        stdscr.addstr(h, w, f"{' ' * 72}")
        stdscr.addstr(h, w, f"Your entire team is wiped out!")
        refresh_sleep(stdscr, 3)
        return True
    return False

# Simple function to print the trainer art from assests
def print_trainer(stdscr, h, w):
    for i, line in enumerate(trainer_art):
        stdscr.addstr(h + i, (w // 2) - (len(line)// 2), line)

# Prints a double line box around the terminal's dimensions
def print_box(stdscr, h, w, g_h, g_w):
    line = "═" * (g_w - 2)
    stdscr.addstr((h // 2) - (g_h // 2), (w // 2) - (g_w // 2), f"╔{line}╗")
    for i in range(g_h - 2):
        stdscr.addstr((h // 2) - (g_h // 2) + i + 1, (w // 2) - (g_w // 2), "║")
        stdscr.addstr((h // 2) - (g_h // 2) + i + 1, (w // 2) + ((g_w // 2) - 1), "║")
    stdscr.addstr((h // 2) + (g_h // 2) - 1, (w // 2) - (g_w // 2), f"╚{line}╝")
