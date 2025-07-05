"""
NBA Draft Year 2032
This file contains functions to determine the ownership of the 2032 NBA Draft picks.
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
    # "01": ["SAC", "SAS"],
}


"""
ROUND 1 PICKS
"""
def ATL_2032_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}, context: Optional[dict] = {}):
    """
    Atlanta has not traded their 2032 pick. They keep it regardless of position.
    """
    return "ATL"


def BOS_2032_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}, context: Optional[dict] = {}):
    """
    Boston has not traded their 2032 pick. They keep it regardless of position.
    """
    return "BOS"


def BRK_2032_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}, context: Optional[dict] = {}):
    """
    Brooklyn has not traded their 2032 pick. They keep it regardless of position.
    """
    return "BRK"


def CHA_2032_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}, context: Optional[dict] = {}):
    """
    Carlotte has not traded their 2032 pick. They keep it regardless of position.
    """
    return "CHA"


def CHI_2032_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}, context: Optional[dict] = {}):
    """
    Chicago has not traded their 2032 pick. They keep it regardless of position.
    """
    return "CHI"


def CLE_2032_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}, context: Optional[dict] = {}):
    """
    Cleveland has not traded their 2032 pick. They keep it regardless of position.
    """
    return "CLE"


def DAL_2032_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}, context: Optional[dict] = {}):
    """
    Dallas has not traded their 2032 pick. They keep it regardless of position.
    """
    return "DAL"


def DEN_2032_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}, context: Optional[dict] = {}):
    """
    Denver has traded their 2032 pick to Brooklyn.
      - This was the "Cam Johnson/Michael Porter Jr." trade.
      - This pick is owned by Brooklyn regardless of position.
    """
    return "BRK"


def DET_2032_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}, context: Optional[dict] = {}):
    """
    Detroit has not traded their 2032 pick. They keep it regardless of position.
    """
    return "DET"


def GSW_2032_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}, context: Optional[dict] = {}):
    """
    Golden State has not traded their 2032 pick. They keep it regardless of position.
    """
    return "GSW"


def HOU_2032_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}, context: Optional[dict] = {}):
    """
    Houston has not traded their 2032 pick. They keep it regardless of position.
    """
    return "HOU"


def IND_2032_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}, context: Optional[dict] = {}):
    """
    Indiana has not traded their 2032 pick. They keep it regardless of position.
    """
    return "IND"


def LAC_2032_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}, context: Optional[dict] = {}):
    """
    LA Clippers has not traded their 2032 pick. They keep it regardless of position.
    """
    return "LAC"


def LAL_2032_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}, context: Optional[dict] = {}):
    """
    LA Lakers has not traded their 2032 pick. They keep it regardless of position.
    """
    return "LAL"


def MEM_2032_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}, context: Optional[dict] = {}):
    """
    Memphis has not traded their 2032 pick. They keep it regardless of position.
    """
    return "MEM"


def MIA_2032_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}, context: Optional[dict] = {}):
    """
    Miami has not traded their 2032 pick. They keep it regardless of position.
    """
    return "MIA"


def MIL_2032_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}, context: Optional[dict] = {}):
    """
    Milwaukee has not traded their 2032 pick. They keep it regardless of position.
    """
    return "MIL"


def MIN_2032_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}, context: Optional[dict] = {}):
    """
    Minnesota has not traded their 2032 pick. They keep it regardless of position.
    """
    return "MIN"


def NOP_2032_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}, context: Optional[dict] = {}):
    """
    New Orleans has not traded their 2032 pick. They keep it regardless of position.
    """
    return "NOP"


def NYK_2032_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}, context: Optional[dict] = {}):
    """
    New York has not traded their 2032 pick. They keep it regardless of position.
    """
    return "NYK"


def OKC_2032_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}, context: Optional[dict] = {}):
    """
    Oklahoma City has not traded their 2032 pick. They keep it regardless of position.
    """
    return "OKC"


def ORL_2032_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}, context: Optional[dict] = {}):
    """
    Orlando has not traded their 2032 pick. They keep it regardless of position.
    """
    return "ORL"


def PHI_2032_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}, context: Optional[dict] = {}):
    """
    Philadelphia has not traded their 2032 pick. They keep it regardless of position.
    """
    return "PHI"


def PHX_2032_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}, context: Optional[dict] = {}):
    """
    Phoenix has not traded their 2032 pick. They keep it regardless of position.
    """
    return "PHX"


def POR_2032_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}, context: Optional[dict] = {}):
    """
    Portland has not traded their 2032 pick. They keep it regardless of position.
    """
    return "POR"


def SAC_2032_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}, context: Optional[dict] = {}):
    """
    Sacramento has not traded their 2032 pick. They keep it regardless of position.
    """
    return "SAC"


def SAS_2032_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}, context: Optional[dict] = {}):
    """
    San Antonio has not traded their 2032 pick. They keep it regardless of position.
    """
    return "SAS"


def TOR_2032_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}, context: Optional[dict] = {}):
    """
    Toronto has not traded their 2032 pick. They keep it regardless of position.
    """
    return "TOR"


def UTA_2032_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}, context: Optional[dict] = {}):
    """
    Utah has not traded their 2032 pick. They keep it regardless of position.
    """
    return "UTA"


def WAS_2032_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}, context: Optional[dict] = {}):
    """
    Washington has not traded their 2032 pick. They keep it regardless of position.
    """
    return "WAS"



"""
ROUND 2 PICKS
"""