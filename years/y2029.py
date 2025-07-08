"""
NBA Draft Year 2029
This file contains functions to determine the ownership of the 2029 NBA Draft picks.
Additionally, there exist constants for swap favorability.

Last Confirmed : July 2025
"""


from years.utils import (
  generate_team_order
  , evaluate_protection
  , evaluate_swap
  , evaluate_pick_history
)
from typing import Optional
import copy


SWAP_FAVORABILITY = {
    # Ordered most to least favorable
    1: {"participants": ["UTA", "CLE", "MIN"], "owed_teams": ["UTA", "UTA", "CHA"]},
    2: {"participants": ["POR", "BOS", "MIL"], "owed_teams": ["POR", "WAS", "POR"]},
    3: {"participants": ["HOU", "PHX", "DAL"], "owed_teams": ["HOU", "HOU", "BRK"]},
    4: {"participants": ["PHI", "LAC"], "owed_teams": ["PHI", "LAC"]},
    5: {"participants": ["MEM", "ORL"], "owed_teams": ["MEM", "ORL"]},
}


"""
ROUND 1 PICKS
"""
def ATL_2029_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}):
    """
    Atlanta has not traded their 2029 pick. They keep it regardless of position.
    """
    pick = draft_order["ATL"]
    return ("ATL", pick)


def BOS_2029_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}):
    """
    Boston has traded their 2029 pick. They owe to either Washington or Portland, calculated by favorability with Milwaukee and Portland.
        - Boston is unprotected; this is the Jrue Holiday trade
        - Milwaukee is unprotected; this is the Damian Lillard trade
        - Portland keeps the most and least favorable picks; other goes to Washington
            - Washington pick is the Deni Avidja trade
    """
    participating_teams = SWAP_FAVORABILITY[2]

    ownership = evaluate_swap(draft_order, participating_teams, "BOS")
    return ownership


def BRK_2029_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}):
    """
    Brooklyn has not traded their 2029 pick. They keep it regardless of position.
    """
    pick = draft_order["BRK"]
    return ("BRK", pick)


def CHA_2029_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}):
    """
    Carlotte has not traded their 2029 pick. They keep it regardless of position.
    """
    pick = draft_order["CHA"]
    return ("CHA", pick)


def CHI_2029_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}):
    """
    Chicago has not traded their 2029 pick. They keep it regardless of position.
    """
    pick = draft_order["CHI"]
    return ("CHI", pick)


def CLE_2029_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}):
    """
    Cleveland has traded to their 2029 pick. They participate with Minnesota and Utah.
        - Cleveland is unprotected; this is the Donovan Mitchell trade
        - Minnesota is protected 1-5; this is the Rudy Gobert trade
        - Utah keeps the two most favorable picks; other goes to Charlotte
            - Charlotte pick is the Mark Williams trade
    """
    min_pick = draft_order["MIN"]
    participating_teams = copy.deepcopy(SWAP_FAVORABILITY[1])

    if min_pick in range(1, 6):
        # Minnesota keeps their pick (doesn't participate in swap)
        participating_teams["participants"].remove("MIN")

    ownership = evaluate_swap(draft_order, participating_teams, "CLE")
    return ownership


def DAL_2029_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}):
    """
    Phoenix has traded their 2029 pick. They owe conditionally with Phoenix and Dallas to either Houston or.
        - Phoenix is unprotected; this is the Kevin Durant to BKN
        - Dallas is unprotected; this is the Kyrie Irving trade
        - Houston keeps the two most favorable picks; other goes to Washington
            - Brooklyn pick is the James Harden trade
    """
    participating_teams = SWAP_FAVORABILITY[3]

    ownership = evaluate_swap(draft_order, participating_teams, "DAL")
    return ownership


def DEN_2029_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}):
    """
    Denver has traded their 2029 pick to Brooklyn.
      - This was the "Cam Johnson/Michael Porter Jr." trade.
      - This pick is owned by Brooklyn regardless of position.
    """
    pick = draft_order["DEN"]
    return ("DEN", pick)


def DET_2029_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}):
    """
    Detroit has not traded their 2029 pick. They keep it regardless of position.
    """
    pick = draft_order["DET"]
    return ("DET", pick)


def GSW_2029_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}):
    """
    Golden State has not traded their 2029 pick. They keep it regardless of position.
    """
    pick = draft_order["GSW"]
    return ("GSW", pick)


def HOU_2029_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}):
    """
    Houston has not traded their 2029 pick. They participate in swaps with Brooklyn, concerning Phoenix and Dallas.
        - Phoenix is unprotected; this is the Kevin Durant
        - Dallas is unprotected; this is the Kyrie Irving trade
        - Houston keeps the two most favorable picks; other goes to Washington
            - Brooklyn pick is the James Harden trade
    """
    participating_teams = SWAP_FAVORABILITY[3]

    ownership = evaluate_swap(draft_order, participating_teams, "HOU")
    return ownership


def IND_2029_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}):
    """
    Indiana has not traded their 2029 pick. They keep it regardless of position.
    """
    pick = draft_order["IND"]
    return ("IND", pick)


def LAC_2029_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}):
    """
    LA Clippers has traded rights to swap their 2029 pick. They owe conditional swap rights to Philadelphia
        - LA Clippers is protected 1-3; this is the James Harden trade
    """
    la_pick = draft_order["LAC"]
    protected = range(1,4) # Protected 1-3
    participating_teams = copy.deepcopy(SWAP_FAVORABILITY[4])

    if la_pick in protected:
        return ("LAC", la_pick)

    ownership = evaluate_swap(draft_order, participating_teams, "LAC")
    return ownership


def LAL_2029_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}):
    """
    LA Lakers has not traded their 2029 pick. They keep it regardless of position.
    """
    pick = draft_order["LAL"]
    return ("LAL", pick)


def MEM_2029_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}):
    """
    Memphis has not traded their 2029 pick, but owns conditional swap rights with Orlando.
        - ORL protected 1-2; this is the Desmond Bane trade
    """
    pick = draft_order["MEM"]
    orl_pick = draft_order["ORL"]
    protected = range(1,3) # Protected 1-2
    participating_teams = SWAP_FAVORABILITY[5]

    if orl_pick in protected:
        return ("MEM", pick)

    ownership = evaluate_swap(draft_order, participating_teams, "MEM")
    return ownership


def MIA_2029_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}):
    """
    Miami has not traded their 2029 pick. They keep it regardless of position.
    """
    pick = draft_order["MIA"]
    return ("MIA", pick)


def MIL_2029_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}):
    """
    Milwaukee has traded their 2029 pick. They owe to either Washington or Portland, calculated by favorability with Boston and Portland.
        - Boston is unprotected; this is the Jrue Holiday trade
        - Milwaukee is unprotected; this is the Damian Lillard trade
        - Portland keeps the most and least favorable picks; other goes to Washington
            - Washington pick is the Deni Avidja trade
    """
    participating_teams = SWAP_FAVORABILITY[2]

    ownership = evaluate_swap(draft_order, participating_teams, "MIL")
    return ownership


def MIN_2029_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}):
    """
    Minnesota has traded to their 2029 pick. They participate with Cleveland and Utah.
        - Cleveland is unprotected; this is the Donovan Mitchell trade
        - Minnesota is protected 1-5; this is the Rudy Gobert trade
        - Utah keeps the two most favorable picks; other goes to Charlotte
            - Charlotte pick is the Mark Williams trade
    """
    min_pick = draft_order["MIN"]
    participating_teams = copy.deepcopy(SWAP_FAVORABILITY[1])

    if min_pick in range(1, 6):
        # Minnesota keeps their pick (doesn't participate in swap)
        return ("MIN", min_pick)

    ownership = evaluate_swap(draft_order, participating_teams, "MIN")
    return ownership


def NOP_2029_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}):
    """
    New Orleans has not traded their 2029 pick. They keep it regardless of position.
    """
    pick = draft_order["NOP"]
    return ("NOP", pick)


def NYK_2029_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}):
    """
    New York has not traded their 2029 pick. They keep it regardless of position.
    """
    pick = draft_order["NYK"]
    return ("NYK", pick)


def OKC_2029_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}):
    """
    Oklahoma City has not traded their 2029 pick. They keep it regardless of position.
    """
    pick = draft_order["OKC"]
    return ("OKC", pick)


def ORL_2029_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}):
    """
    Orlando has traded the right to conditionlly swap their 2029 pick with Memphis.
     - ORL protected 1-2; this is the Desmond Bane trade
    """
    pick = draft_order["ORL"]
    protected = range(1,3) # Protected 1-2
    participating_teams = SWAP_FAVORABILITY[5]

    if pick in protected:
        return ("ORL", pick)

    ownership = evaluate_swap(draft_order, participating_teams, "ORL")
    return ownership


def PHI_2029_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}):
    """
    Philadelphia has not traded their 2029 pick. They own conditional swap rights to LA Clippers
        - LA Clippers is protected 1-3; this is the James Harden trade
    """
    la_pick = draft_order["LAC"]
    protected = range(1,4) # Protected 1-3
    participating_teams = copy.deepcopy(SWAP_FAVORABILITY[4])

    if la_pick in protected:
        participating_teams["participants"].remove("LAC")

    ownership = evaluate_swap(draft_order, participating_teams, "PHI")
    return ownership


def PHX_2029_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}):
    """
    Phoenix has traded their 2029 pick. They owe conditionally with Phoenix and Dallas to either Houston or.
        - Phoenix is unprotected; this is the Kevin Durant to BKN
        - Dallas is unprotected; this is the Kyrie Irving trade
        - Houston keeps the two most favorable picks; other goes to Washington
            - Brooklyn pick is the James Harden trade
    """
    participating_teams = SWAP_FAVORABILITY[3]

    ownership = evaluate_swap(draft_order, participating_teams, "PHX")
    return ownership


def POR_2029_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}):
    """
    Portland has not traded their 2029 pick. They participate swaps with Washington, concerning Boston and Milwaukee.
        - Boston is unprotected; this is the Jrue Holiday trade
        - Milwaukee is unprotected; this is the Damian Lillard trade
        - Portland keeps the most and least favorable picks; other goes to Washington
            - Washington pick is the Deni Avidja trade
    """
    participating_teams = SWAP_FAVORABILITY[2]

    ownership = evaluate_swap(draft_order, participating_teams, "POR")
    return ownership



def SAC_2029_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}):
    """
    Sacramento has not traded their 2029 pick. They keep it regardless of position.
    """
    pick = draft_order["SAC"]
    return ("SAC", pick)


def SAS_2029_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}):
    """
    San Antonio has not traded their 2029 pick. They keep it regardless of position.
    """
    pick = draft_order["SAS"]
    return ("SAS", pick)


def TOR_2029_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}):
    """
    Toronto has not traded their 2029 pick. They keep it regardless of position.
    """
    pick = draft_order["TOR"]
    return ("TOR", pick)


def UTA_2029_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}):
    """
    Utah has not traded their 2029 pick. They participate swaps with Charlotte, concerning Cleveland and Minnesota.
        - Cleveland is unprotected; this is the Donovan Mitchell trade
        - Minnesota is protected 1-5; this is the Rudy Gobert trade
        - Utah keeps the two most favorable picks; other goes to Charlotte
            - Charlotte pick is the Mark Williams trade
    """
    min_pick = draft_order["MIN"]
    participating_teams = copy.deepcopy(SWAP_FAVORABILITY[1])

    if min_pick in range(1, 6):
        # Minnesota keeps their pick (doesn't participate in swap)
        participating_teams["participants"].remove("MIN")

    ownership = evaluate_swap(draft_order, participating_teams, "UTA")
    return ownership


def WAS_2029_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}):
    """
    Washington has not traded their 2029 pick. They keep it regardless of position.
    """
    pick = draft_order["WAS"]
    return ("WAS", pick)



"""
ROUND 2 PICKS
"""