"""
NBA Draft Year 2030
This file contains functions to determine the ownership of the 2030 NBA Draft picks.
Additionally, there exist constants for swap favorability.
"""


from years.utils  import (
  prep_teams_and_picks
  , evaluate_protection
  , evaluate_swap
)
from typing import Optional


SWAP_FAVORABILITY = {
    # Ordered most to least favorable
    "01": ["WAS", "MEM", "PHX"],
    "O2": ["SAS", "DAL", "MIN"]
}


def ATL_2030_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}, context: Optional[dict] = {}):
    """
    Atlanta has not traded their 2030 pick. They keep it regardless of position.
    """
    return "ATL"


def BOS_2030_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}, context: Optional[dict] = {}):
    """
    Boston has not traded their 2030 pick. They keep it regardless of position.
    """
    return "BOS"


def BRK_2030_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}, context: Optional[dict] = {}):
    """
    Brooklyn has not traded their 2030 pick. They keep it regardless of position.
    """
    return "BRK"


def CHA_2030_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}, context: Optional[dict] = {}):
    """
    Carlotte has not traded their 2030 pick. They keep it regardless of position.
    """
    return "CHA"


def CHI_2030_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}, context: Optional[dict] = {}):
    """
    Chicago has not traded their 2030 pick. They keep it regardless of position.
    """
    return "CHI"


def CLE_2030_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}, context: Optional[dict] = {}):
    """
    Cleveland has not traded their 2030 pick. They keep it regardless of position.
    """
    return "CLE"


def DAL_2030_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}, context: Optional[dict] = {}):
    """
    Dallas has not traded their 2030 pick. They keep it regardless of position.
    """
    return "DAL"


def DEN_2030_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}, context: Optional[dict] = {}):
    """
    Denver has not traded their 2030 pick. They keep it regardless of position.
    """
    return "DEN"


def DET_2030_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}, context: Optional[dict] = {}):
    """
    Detroit has not traded their 2030 pick. They keep it regardless of position.
    """
    return "DET"


def GSW_2030_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}, context: Optional[dict] = {}):
    """
    Golden State has not traded their 2030 pick. They keep it regardless of position.
    """
    return "GSW"


def HOU_2030_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}, context: Optional[dict] = {}):
    """
    Houston has not traded their 2030 pick. They keep it regardless of position.
    """
    return "HOU"


def IND_2030_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}, context: Optional[dict] = {}):
    """
    Indiana has not traded their 2030 pick. They keep it regardless of position.
    """
    return "IND"


def LAC_2030_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}, context: Optional[dict] = {}):
    """
    LA Clippers has not traded their 2030 pick. They keep it regardless of position.
    """
    return "LAC"


def LAL_2030_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}, context: Optional[dict] = {}):
    """
    LA Lakers has not traded their 2030 pick. They keep it regardless of position.
    """
    return "LAL"


def MEM_2030_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}, context: Optional[dict] = {}):
    """
    Memphis has traded swap rights to their 2031 pick.
        - MEM <-> WAS: this was the Marcus Smart trade
        - MEM owns the middle favorable, after WAS but before PHX
    """
    current_team = "MEM"
    participating_teams = SWAP_FAVORABILITY["01"]
    ownership = evaluate_swap(participating_teams, current_team)
    return ownership


def MIA_2030_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}, context: Optional[dict] = {}):
    """
    Miami has not traded their 2030 pick. They keep it regardless of position.
    """
    return "MIA"


def MIL_2030_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}, context: Optional[dict] = {}):
    """
    Milwaukee has not traded their 2030 pick. They keep it regardless of position.
    """
    return "MIL"


def MIN_2030_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}, context: Optional[dict] = {}):
    """
    Minnesota traded their 2030 pick. Current owner is Sacramento.
        - Pick is unprotected.
        - MIN -> SAS: this was the Rob Dillingham trade
        - SAS -> SAC: this was the De'Aaron Fox trade
    """
    return "SAC"


def NOP_2030_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}, context: Optional[dict] = {}):
    """
    New Orleans has not traded their 2030 pick. They keep it regardless of position.
    """
    return "NOP"


def NYK_2030_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}, context: Optional[dict] = {}):
    """
    New York has traded their 2030 pick. Current owner is Brooklyn.
        - Pick is unprotected.
        - NYK -> BRK: this was the Mikal Bridges trade.
    """
    return "NYK"


def OKC_2030_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}, context: Optional[dict] = {}):
    """
    Oklahoma City has not traded their 2030 pick. They keep it regardless of position.
    """
    return "OKC"


def ORL_2030_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}, context: Optional[dict] = {}):
    """
    Orlando has not traded their 2030 pick. They keep it regardless of position.
    """
    return "ORL"


def PHI_2030_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}, context: Optional[dict] = {}):
    """
    Philadelphia has not traded their 2030 pick. They keep it regardless of position.
    """
    return "PHI"


def PHX_2030_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}, context: Optional[dict] = {}):
    """
    Phoenix has traded swap rights to their 2031 pick.
        - PHX <-> WAS: this was the Bradley Beal trade
        - PHX owns the least favorable, then MEM, then PHX with most favorable
    """
    current_team = "PHX"
    participating_teams = SWAP_FAVORABILITY["01"]
    ownership = evaluate_swap(participating_teams, current_team)
    return ownership


def POR_2030_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}, context: Optional[dict] = {}):
    """
    Portland has not traded their 2030 pick. They keep it regardless of position.
    """
    return "POR"


def SAC_2030_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}, context: Optional[dict] = {}):
    """
    Sacramento has not traded their 2030 pick. They participate in swap rights with San Antonio.
        -   SAC <-> SAS: this was the De'Aaron Fox trade.
        -   SAC owns the most favorable swap rights with SAS.
    """
    current_team = "SAC"
    participating_teams = SWAP_FAVORABILITY["01"]
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
    min_pick = None


    current_team = "SAS"
    participating_teams = SWAP_FAVORABILITY["02"]
    ownership = evaluate_swap(participating_teams, current_team)
    return ownership


def TOR_2030_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}, context: Optional[dict] = {}):
    """
    Toronto has not traded their 2030 pick. They keep it regardless of position.
    """
    return "TOR"


def UTA_2030_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}, context: Optional[dict] = {}):
    """
    Utah has not traded their 2030 pick. They keep it regardless of position.
    """
    return "UTA"


def WAS_2030_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}, context: Optional[dict] = {}):
    """
    Washington has not traded their 2030 pick. They participate in swap rights with Memphis and Phoenix.
        - WAS <-> PHX: this was the Bradley Beal trade
        - WAS <-> MEM: this was the Marcus Smart trade
        - WAS owns most favorable, then MEM, then PHX with least favorable
    """
    current_team = "WAS"
    participating_teams = SWAP_FAVORABILITY["01"]
    ownership = evaluate_swap(participating_teams, current_team)
    return ownership



"""
ROUND 2 PICKS
"""