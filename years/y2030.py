"""
NBA Draft Year 2030
This file contains functions to determine the ownership of the 2030 NBA Draft picks.
Additionally, there exist constants for swap favorability.
"""


from years.utils  import (
  prep_teams_and_picks
  , evaluate_protection
  , evaluate_swap
  , generate_team_order
)
from typing import Optional


SWAP_FAVORABILITY = {
    # Ordered most to least favorable
    1: ["WAS", "MEM", "PHX"],
    2: ["SAS", "DAL", "MIN"]
}


def ATL_2030_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}, context: Optional[dict] = {}):
    """
    Atlanta has not traded their 2030 pick. They keep it regardless of position.
    """
    pick = draft_order["ATL"]
    return ("ATL", pick)


def BOS_2030_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}, context: Optional[dict] = {}):
    """
    Boston has not traded their 2030 pick. They keep it regardless of position.
    """
    pick = draft_order["BOS"]
    return ("BOS", pick)


def BRK_2030_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}, context: Optional[dict] = {}):
    """
    Brooklyn has not traded their 2030 pick. They keep it regardless of position.
    """
    pick = draft_order["BRK"]
    return ("BRK", pick)


def CHA_2030_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}, context: Optional[dict] = {}):
    """
    Carlotte has not traded their 2030 pick. They keep it regardless of position.
    """
    pick = draft_order["CHA"]
    return ("CHA", pick)


def CHI_2030_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}, context: Optional[dict] = {}):
    """
    Chicago has not traded their 2030 pick. They keep it regardless of position.
    """
    pick = draft_order["CHI"]
    return ("CHI", pick)


def CLE_2030_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}, context: Optional[dict] = {}):
    """
    Cleveland has not traded their 2030 pick. They keep it regardless of position.
    """
    pick = draft_order["CLE"]
    return ("CLE", pick)


def DAL_2030_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}, context: Optional[dict] = {}):
    """
    Dalls has traded swap rights to their 2030 pick.
        -   DAL <-> SAS: this was the Grant Williams trade.
        -   SAS owns the most favorable, then DAL, then MIN with the least favorable
            -   MIN only participates if it's 2-30
    """
    protection = range(1, 2) # # Protected 1-1, unprotected 2-30
    min_pick_owner = evaluate_protection(draft_order, protection, "MIN", "SAS")
    participating_teams = SWAP_FAVORABILITY[2]

    if min_pick_owner == "MIN":
        # MIN retains its pick
        participating_teams.remove("MIN")

    # Otherwise, MIN remains in the swap
    ownership = evaluate_swap(draft_order, participating_teams, "DAL")
    return ownership


def DEN_2030_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}, context: Optional[dict] = {}):
    """
    Denver has not traded their 2030 pick. They keep it regardless of position.
    """
    pick = draft_order["DEN"]
    return ("DEN", pick)


def DET_2030_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}, context: Optional[dict] = {}):
    """
    Detroit has not traded their 2030 pick. They keep it regardless of position.
    """
    pick = draft_order["DET"]
    return ("DET", pick)


def GSW_2030_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}, context: Optional[dict] = {}):
    """
    Golden State has not traded their 2030 pick. They keep it regardless of position.
    """
    pick = draft_order["GSW"]
    return ("GSW", pick)


def HOU_2030_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}, context: Optional[dict] = {}):
    """
    Houston has not traded their 2030 pick. They keep it regardless of position.
    """
    pick = draft_order["HOU"]
    return ("HOU", pick)


def IND_2030_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}, context: Optional[dict] = {}):
    """
    Indiana has not traded their 2030 pick. They keep it regardless of position.
    """
    pick = draft_order["IND"]
    return ("IND", pick)


def LAC_2030_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}, context: Optional[dict] = {}):
    """
    LA Clippers has not traded their 2030 pick. They keep it regardless of position.
    """
    pick = draft_order["LAC"]
    return ("LAC", pick)


def LAL_2030_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}, context: Optional[dict] = {}):
    """
    LA Lakers has not traded their 2030 pick. They keep it regardless of position.
    """
    pick = draft_order["LAL"]
    return ("LAL", pick)


def MEM_2030_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}, context: Optional[dict] = {}):
    """
    Memphis has traded swap rights to their 2031 pick.
        - MEM <-> WAS: this was the Marcus Smart trade
        - MEM owns the middle favorable, after WAS but before PHX
    """
    current_team = "MEM"
    participating_teams = SWAP_FAVORABILITY[1]
    ownership = evaluate_swap(participating_teams, current_team)
    return ownership


def MIA_2030_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}, context: Optional[dict] = {}):
    """
    Miami has not traded their 2030 pick. They keep it regardless of position.
    """
    pick = draft_order["MIA"]
    return ("MIA", pick)


def MIL_2030_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}, context: Optional[dict] = {}):
    """
    Milwaukee has not traded their 2030 pick. They keep it regardless of position.
    """
    pick = draft_order["MIL"]
    return ("MIL", pick)


def MIN_2030_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}, context: Optional[dict] = {}):
    """
    Minnesota has traded swap rights to their 2030 pick.
        -   MIN <-> SAS: this was the Rob Dillingham trade.
        -   SAS owns the most favorable, then DAL, then MIN with the least favorable
            -   MIN only participates if it's 2-30
    """
    protection = range(1, 2) # # Protected 1-1, unprotected 2-30
    min_pick_owner = evaluate_protection(draft_order, protection, "MIN", "SAS")
    participating_teams = SWAP_FAVORABILITY[2]

    if min_pick_owner == "MIN":
        # MIN retains its pick
        pick = draft_order["MIN"]
        return ("MIN", pick)

    # Otherwise, MIN remains in the swap
    ownership = evaluate_swap(draft_order, participating_teams, "MIN")
    return ownership


def NOP_2030_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}, context: Optional[dict] = {}):
    """
    New Orleans has not traded their 2030 pick. They keep it regardless of position.
    """
    pick = draft_order["NOP"]
    return ("NOP", pick)


def NYK_2030_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}, context: Optional[dict] = {}):
    """
    New York has traded their 2030 pick. Current owner is Brooklyn.
        - Pick is unprotected.
        - NYK -> BRK: this was the Mikal Bridges trade.
    """
    pick = draft_order["NYK"]
    return ("NYK", pick)


def OKC_2030_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}, context: Optional[dict] = {}):
    """
    Oklahoma City has not traded their 2030 pick. They keep it regardless of position.
    """
    pick = draft_order["OKC"]
    return ("OKC", pick)


def ORL_2030_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}, context: Optional[dict] = {}):
    """
    Orlando has not traded their 2030 pick. They keep it regardless of position.
    """
    pick = draft_order["ORL"]
    return ("ORL", pick)


def PHI_2030_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}, context: Optional[dict] = {}):
    """
    Philadelphia has not traded their 2030 pick. They keep it regardless of position.
    """
    pick = draft_order["PHI"]
    return ("PHI", pick)


def PHX_2030_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}, context: Optional[dict] = {}):
    """
    Phoenix has traded swap rights to their 2031 pick.
        - PHX <-> WAS: this was the Bradley Beal trade
        - PHX owns the least favorable, then MEM, then PHX with most favorable
    """
    current_team = "PHX"
    participating_teams = SWAP_FAVORABILITY[1]
    ownership = evaluate_swap(participating_teams, current_team)
    return ownership


def POR_2030_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}, context: Optional[dict] = {}):
    """
    Portland has not traded their 2030 pick. They keep it regardless of position.
    """
    pick = draft_order["POR"]
    return ("POR", pick)


def SAC_2030_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}, context: Optional[dict] = {}):
    """
    Sacramento has not traded their 2030 pick. They participate in swap rights with San Antonio.
        -   SAC <-> SAS: this was the De'Aaron Fox trade.
        -   SAC owns the most favorable swap rights with SAS.
    """
    current_team = "SAC"
    participating_teams = SWAP_FAVORABILITY[1]
    ownership = evaluate_swap(participating_teams, current_team)
    return ownership


def SAS_2030_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}, context: Optional[dict] = {}):
    """
    San Antonio has not traded their 2030 pick. They participate in swap rights with Dallas and Minnesota.
        -   SAS <-> MIN: this was the Rob Dillingham trade.
        -   SAS <-> DAL: this was the Grant Williams trade.
        -   SAS owns the most favorable, then DAL, then MIN with the least favorable
            -   MIN only participates if it's 2-30
    """
    protection = range(1, 2) # # Protected 1-1, unprotected 2-30
    min_pick_owner = evaluate_protection(draft_order, protection, "MIN", "SAS")
    participating_teams = SWAP_FAVORABILITY[2]

    if min_pick_owner == "MIN":
        # MIN retains its pick
        participating_teams.remove("MIN")

    # Otherwise, MIN remains in the swap
    ownership = evaluate_swap(draft_order, participating_teams, "SAS")
    return ownership


def TOR_2030_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}, context: Optional[dict] = {}):
    """
    Toronto has not traded their 2030 pick. They keep it regardless of position.
    """
    pick = draft_order["TOR"]
    return ("TOR", pick)


def UTA_2030_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}, context: Optional[dict] = {}):
    """
    Utah has not traded their 2030 pick. They keep it regardless of position.
    """
    pick = draft_order["UTA"]
    return ("UTA", pick)


def WAS_2030_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}, context: Optional[dict] = {}):
    """
    Washington has not traded their 2030 pick. They participate in swap rights with Memphis and Phoenix.
        - WAS <-> PHX: this was the Bradley Beal trade
        - WAS <-> MEM: this was the Marcus Smart trade
        - WAS owns most favorable, then MEM, then PHX with least favorable
    """
    current_team = "WAS"
    participating_teams = SWAP_FAVORABILITY[1]
    ownership = evaluate_swap(participating_teams, current_team)
    return ownership



"""
ROUND 2 PICKS
"""