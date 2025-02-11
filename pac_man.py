#Define if Pac-Man Eats a Ghost
def eat_ghost(power_pellet_active, touching_ghost):
    if power_pellet_active and touching_ghost:
        return True
    else:
        return False
print(eat_ghost(True,False))
#Define if Pac-Man Scores
def score(touching_power_pellet, touching_dot):
    if touching_power_pellet or touching_dot:
        return True
    else:
        return False
print(score(True,True))
#Define if Pac-Man Loses
def lose(power_pellet_active, touching_ghost):
    if not touching_ghost and power_pellet_active:
        return False
    elif power_pellet_active and touching_ghost:
        return False
    else:
        return True
print(lose(False, True))
#Define if Pac-Man Wins
def win(has_eaten_all_dots, power_pellet_active, touching_ghost):
    if not has_eaten_all_dots and touching_ghost or not power_pellet_active and touching_ghost:
        return False
    else:
        return True
print(win(True,True,True))