"""Functions for implementing the rules of the classic arcade game Pac-Man."""


def eat_ghost(power_pellet_active, touching_ghost):
    """Verify that Pac-Man can eat a ghost if he is empowered by a power pellet.

    Parameters:
        power_pellet_active (bool): Does the player have an active power pellet?
        touching_ghost (bool): Is the player touching a ghost?

    Returns:
        bool: Can a ghost be eaten?

    """
    can_a_ghost_be_eaten = False
    if power_pellet_active == touching_ghost == True:
        can_a_ghost_be_eaten= True
        return can_a_ghost_be_eaten
    return can_a_ghost_be_eaten

def score(touching_power_pellet, touching_dot):
    """Verify that Pac-Man has scored when a power pellet or dot has been eaten.

    Parameters:
        touching_power_pellet (bool): Is the player touching a power pellet?
        touching_dot (bool): Is the player touching a dot?

    Returns:
        bool: Has the player scored or not?

    """
    has_the_player_scored_or_not = False
    if touching_power_pellet is True or touching_dot is True:
        has_the_player_scored_or_not = True
        return has_the_player_scored_or_not
    return has_the_player_scored_or_not


def lose(power_pellet_active, touching_ghost):
    """Trigger the game loop to end (GAME OVER) when Pac-Man touches a ghost without his power pellet.

    Parameters:
        power_pellet_active (bool): Does the player have an active power pellet?
        touching_ghost (bool): Is the player touching a ghost?

    Returns:
        bool: Has the player lost the game?
    """
    has_the_player_lost_the_game = True
    if power_pellet_active == touching_ghost == True:
        has_the_player_lost_the_game = False
        return False
    if power_pellet_active is True and touching_ghost is False:
        return False
    return has_the_player_lost_the_game


def win(has_eaten_all_dots, power_pellet_active, touching_ghost):
    """Trigger the victory event when all dots have been eaten.

    Parameters:
        has_eaten_all_dots (bool): Has the player "eaten" all the dots?
        power_pellet_active (bool): Does the player have an active power pellet?
        touching_ghost (bool): Is the player touching a ghost?

    Returns:
        bool: Has the player won the game?
    """
    if has_eaten_all_dots is True and power_pellet_active is True and touching_ghost is True:
        return True
    if has_eaten_all_dots is True and power_pellet_active is True and touching_ghost is False:
        return True
    if has_eaten_all_dots is True and power_pellet_active is False and touching_ghost is False:
        return True
    if has_eaten_all_dots is True and power_pellet_active is False and touching_ghost is True:
        return False
    if has_eaten_all_dots is False and power_pellet_active is True and touching_ghost is True:
        return False
    return True
