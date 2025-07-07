from years.utils import (
  prep_teams_and_picks
  , evaluate_protection
  , evaluate_swap
  , evaluate_pick_history
  , generate_pick_history
)


test_draft_order = {
    'DET': 1
  , 'CLE': 2
  , 'NYK': 3
  , 'POR': 4
  , 'GSW': 5
  , 'UTA': 6
  , 'OKC': 7
  , 'CHI': 8
  , 'SAS': 9
  , 'LAL': 10
  , 'TOR': 11
  , 'DEN': 12
  , 'WAS': 13
  , 'CHA': 14
  , 'SAC': 15
  , 'PHI': 16
  , 'LAC': 17
  , 'ATL': 18
  , 'IND': 19
  , 'ORL': 20
  , 'BOS': 21
  , 'DAL': 22
  , 'MIA': 23
  , 'MIL': 24
  , 'MIN': 25
  , 'BRK': 26
  , 'HOU': 27
  , 'NOP': 28
  , 'MEM': 29
  , 'PHX': 30
  }

test_pick_history = {
  '2025': {'UTA': 1},
  '2026': {'UTA': 2},
  '2027': {'UTA': 3},
  '2028': {'SAS': 28},
  '2029': {'UTA': 10},
  '2030': {'PHX': 9},
  '2031': {'UTA': 12},
}


def test_prep_teams_and_picks():
    """
    Test the prep_teams_and_picks function to ensure it correctly filters and formats team picks
    """

    teams = ["UTA", "OKC", "CIN"]  # CIN not in draft_order
    result = prep_teams_and_picks(test_draft_order, teams)

    # Assertions
    assert len(test_draft_order.keys()) == 30 # All 30 teams present
    assert len(result.keys()) == 2  # Only UTA and OKC should be included
    assert result == {"UTA": 6, "OKC": 7} # Output should match the expected values


def test_evaluate_protection_pick_is_protected():
    """
    Test the evaluate_protection function to ensure it correctly identifies when a pick is protected
    """

    protected_range = range(1, 5)  # Picks 1 to 4 are protected
    protected_team = "MIN"
    other_team = "UTA"

    owner, pick = evaluate_protection(test_draft_order, protected_range, protected_team, other_team)
    assert (owner, pick) == ("UTA", 25)


def test_evaluate_protection_pick_conveys():
    protected_range = range(1, 4) # Picks 1 to 3 are protected
    protected_team = "CLE"
    other_team = "UTA"

    owner, pick = evaluate_protection(test_draft_order, protected_range, protected_team, other_team)
    assert (owner, pick) == ("CLE", 2)


def test_evaluate_swap_basic_ordering():
    """
    Test the evaluate_swap function to ensure it correctly evaluates swap rights based on draft order
    """

    participating_1 = ["UTA", "NYK", "PHX"]
    participating_2 = ["BRK", "MIN"]
    participating_3 = ["DET", "PHX"]

    # Most favorable goes to UTA (5), then NYK (8), then PHX (12)
    assert evaluate_swap(test_draft_order, participating_1, "UTA") == ("NYK", 6) # UTA's pick goes to NYK
    assert evaluate_swap(test_draft_order, participating_2, "BRK") == ("MIN", 26) # BRK's pick goes to MIN
    assert evaluate_swap(test_draft_order, participating_3, "PHX") == ("PHX", 30) # PHX keeps their own pick


def test_generate_pick_history():
    """
    Test the generate_pick_history function to ensure it generates a valid pick history for a team
    """

    history = generate_pick_history("UTA", 2032)

    assert list(history.keys()) == ['2025', '2026', '2027', '2028', '2029', '2030', '2031']
    count_uta = 0
    for val in history.values():
        assert isinstance(val, dict)
        assert isinstance(list(val.keys())[0], str)
        assert isinstance(list(val.items())[0][1], int)
        count_uta += 1 if "UTA" in list(val.items())[0] else 0

    assert count_uta >= 3  # UTA should have at least 3 picks they've retained in their history


def test_evaluate_pick_history():
    """
    Test the evaluate_pick_history function to ensure it correctly evaluates the pick history and who receives ownership
    """

    team = "UTA"
    owed_team = "SAS"
    history = evaluate_pick_history(test_draft_order, test_pick_history, team, owed_team)

    assert isinstance(history, tuple)
    assert history[0] == team  # Pick belongs to UTA since previously conveyed


def test_evaluate_selective_pick_history():
    """
    Test the evaluate_pick_history function to ensure it correctly evaluates the pick history in select prior years
    """

    team = "UTA"
    owed_team = "SAS"
    prior_years_1 = 3
    history_1 = evaluate_pick_history(test_draft_order, test_pick_history, team, owed_team, prior_years_1)
    prior_years_2 = range(2025, 2030)  # From 2025 to 2029
    history_2 = evaluate_pick_history(test_draft_order, test_pick_history, team, owed_team, prior_years_2)

    assert isinstance(history_1, tuple)
    assert history_1[0] == owed_team  # Pick belongs to UTA since previously conveyed
    assert isinstance(history_2, tuple)
    assert history_2[0] == owed_team  # Pick belongs to UTA since previously conveyed