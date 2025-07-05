import random

teams = [
    "ATL", "BOS", "BRK", "CHA", "CLE", "CHI", "DAL", "DEN",
    "DET", "GSW", "HOU", "IND", "LAC", "LAL", "MEM", "MIA",
    "MIL", "MIN", "NOP", "NYK", "OKC", "ORL", "PHI", "PHX",
    "POR", "SAC", "SAS", "UTA", "TOR", "WAS"
]

random.shuffle(teams)
final_draft_order = {i + 1: team for i, team in enumerate(teams)}


def evaluate_swap(draft_order, participating_teams, current_team):
    """

    """
    picks = []
    participating_teams = ["WAS", "ATL", "UTA"]
    for i, team in draft_order.items():
        if team in participating_teams:
            picks.append((i, team))

    picks.sort(key=lambda x: x[0])  # Sort by draft order
    for i, obj in enumerate(picks):
        if obj[1] == current_team:
            print(participating_teams[i])