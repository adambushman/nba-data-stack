from typing import List, Tuple
import random


def generate_team_order() -> dict:
    """
    Generates a random ordering of teams and pick values; basically simulating post-lottery order.

    Parameters:
    -----------
        None

    Returns:
    --------
        (dict): a dictionary where keys correspond to all teams and items represent their pick values from the original draft order
    """
    teams = [
        "ATL", "BOS", "BRK", "CHA", "CLE", "CHI", "DAL", "DEN",
        "DET", "GSW", "HOU", "IND", "LAC", "LAL", "MEM", "MIA",
        "MIL", "MIN", "NOP", "NYK", "OKC", "ORL", "PHI", "PHX",
        "POR", "SAC", "SAS", "UTA", "TOR", "WAS"
    ]

    random.shuffle(teams)
    return {team: i + 1 for i, team in enumerate(teams)}


def prep_teams_and_picks(draft_order: dict, participating_teams: List[str]) -> dict:
    """
    Captures the team and pick value from the original draft order and prepping it in tuple format

    Parameters:
    -----------
        draft_order (dict): the original order of the draft where keys are teams and items are pick values
        participating_teams (List[str]): a list of abbreviated names for teams of interest

    Returns:
    --------
        (dict): a dictionary where keys correspond to participating teams and items represent their pick values from the original draft order
    """
    filtered_picks = {team: pos for team, pos in draft_order.items() if team in participating_teams} # Filter for the picks belong to participating teams
    return filtered_picks


def evaluate_protection(draft_order: dict, protected_range: range, protected_team: str, other_team: str) -> Tuple[str, int]:
    """
    Evaluates which team assumes ownership of a pick based on a range of protections

    Parameters:
    -----------
        draft_order (dict): the original order of the draft where keys are teams and items are pick values
        protected_range (range): the range where, should the protected pick fall, the team retains their pick
        protected_team (str): the abbreviated name of the team owning the pick
        other_team (str): the abbreviated name of the team receiving the pick outside of the protected range

    Returns:
    --------
        (Tuple[str, int] abbreviated name of the team with final ownership of the pick and the pick value itself
    """

    pick = prep_teams_and_picks(draft_order, [protected_team])[protected_team]  # Get the pick value for the protected team

    if pick in protected_range:
        # If pick lands in protected range, team keeps
        return (protected_team, pick)
    else:
        # If pick lands outside of the protected range, team conveys
        return (other_team, pick)


def evaluate_swap(draft_order: dict, participating_teams: List[str], current_team: str) -> Tuple[str, int]:
    """
    Evaluates whith team assumes ownership of a pick based on order of swaps and most/least favorable options

    Parameters:
    -----------
        draft_order (dict): the original order of the draft where keys are teams and items are pick values
        participating_teams (List[str]): the teams participating in order of who receives most to least favorable picks
        current_team (str): the team whose pick is being considered for the swap

    Returns:
    --------
        (Tuple[str, int]): the abbreviated name of the team with final ownership of the pick and the pick value itself
    """

    filtered_picks = prep_teams_and_picks(draft_order, participating_teams) # Filter for the picks belong to participating teams
    sorted_by_position = sorted(filtered_picks.items(), key=lambda x: x[1]) # Sort by draft order

    for i, obj in enumerate(sorted_by_position):
        if obj[0] == current_team:
            # Return which team receives the pick
            return (participating_teams[i], obj[1])