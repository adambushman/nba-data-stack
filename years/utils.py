from typing import Optional, Union, List, Tuple
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


def generate_pick_history(team: str, year_0: int) -> dict:
    """
    Generates a mock pick history for a team, simulating the picks they have made in previous drafts. Goes back 5 years.

    Parameters:
    -----------
        team (str): the abbreviated name of the team

    Returns:
    --------
        (dict): a dictionary where keys are years and values are dictionaries of receiving team and pick values
    """
    teams = [
        "ATL", "BOS", "BRK", "CHA", "CLE", "CHI", "DAL", "DEN",
        "DET", "GSW", "HOU", "IND", "LAC", "LAL", "MEM", "MIA",
        "MIL", "MIN", "NOP", "NYK", "OKC", "ORL", "PHI", "PHX",
        "POR", "SAC", "SAS", "UTA", "TOR", "WAS"
    ]
    teams.remove(team)  # Remove the team for which we are generating history
    random.shuffle(teams)  # Shuffle the teams to simulate randomness
    recent_conveyences = teams[:random.randint(1, 5)]  # Get 1-4 teams who recently had picks conveyed to them
    team_picks = [team] * (7 - len(recent_conveyences))  # Create a list of the team for each year
    team_picks.extend(recent_conveyences)  # Add the recent conveyences to the list
    random.shuffle(team_picks)  # Shuffle the picks to simulate randomness

    return {f"{year}": {team_picks[year_0 - 7 - year]: random.randint(1, 30)} for year in range(year_0 - 7, year_0)}


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


def evaluate_pick_history(draft_order: dict, pick_history: dict, current_team: str, owed_team: str, prior_years: Optional[Union[int, range]] = 7) -> Tuple[str, int]:
    """
    Evaluates the pick history for a team to determine if they own a pick or if it has been conveyed.

    Parameters:
    -----------
        pick_history (dict): past 5 years of pick history for a team
        current_team (str): the team whose pick is being evaluated
        owed_team (str): the team that may receive the pick if it has been conveyed
        prior_years (Optional[Union[int, range]]): the number of years to look back in the pick history to determine ownership; defaults to 7. Optionally, define with a range of years

    Returns:
    --------
        (Tuple[str, int]): the abbreviated name of the team with final ownership of the pick and the pick value itself
    """

    pick = draft_order[current_team]  # Get the pick value for the current team

    if isinstance(prior_years, range):
        eligible_years = reversed(list(pick_history.keys())[prior_years.start - 1:prior_years.stop - 1])
    else:
        eligible_years = reversed(list(pick_history.keys())[:prior_years])

    for year in eligible_years:
        if owed_team in pick_history[year].keys():
            # If the owed team is found in the pick history, team has conveyed the pick
            return (current_team, pick)

    # Team not found so team must now convey, if ensuing logic allows it
    return (owed_team, pick)