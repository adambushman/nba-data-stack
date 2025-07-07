"""
NBA Draft Year 2026
This file contains functions to determine the ownership of the 2026 NBA Draft picks.
Additionally, there exist constants for swap favorability.

Last Confirmed : July 2025
"""


from years.utils  import (
  evaluate_protection
  , evaluate_swap
  , evaluate_pick_history
)
from typing import Optional


SWAP_FAVORABILITY = {
    # Ordered most to least favorable
    # "01": ["SAC", "SAS"],
}


"""
ROUND 1 PICKS
"""
def ATL_2026_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}):
    """
    Atlanta has not traded their 2026 pick. They keep it regardless of position.
    """
    pick = draft_order["ATL"]
    return ("ATL", pick)


def BOS_2026_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}):
    """
    Boston has not traded their 2026 pick. They keep it regardless of position.
    """
    pick = draft_order["BOS"]
    return ("BOS", pick)


def BRK_2026_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}):
    """
    Brooklyn has not traded their 2026 pick. They keep it regardless of position.
    """
    pick = draft_order["BRK"]
    return ("BRK", pick)


def CHA_2026_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}):
    """
    Carlotte has not traded their 2026 pick. They keep it regardless of position.
    """
    pick = draft_order["CHA"]
    return ("CHA", pick)


def CHI_2026_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}):
    """
    Chicago has not traded their 2026 pick. They keep it regardless of position.
    """
    pick = draft_order["CHI"]
    return ("CHI", pick)


def CLE_2026_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}):
    """
    Cleveland has not traded their 2026 pick. They keep it regardless of position.
    """
    pick = draft_order["CLE"]
    return ("CLE", pick)


def DAL_2026_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}):
    """
    Dallas has not traded their 2026 pick. They keep it regardless of position.
    """
    pick = draft_order["DAL"]
    return ("DAL", pick)


def DEN_2026_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}):
    """
    Denver has traded their 2026 pick to Brooklyn.
      - This was the "Cam Johnson/Michael Porter Jr." trade.
      - This pick is owned by Brooklyn regardless of position.
    """
    pick = draft_order["DEN"]
    return ("DEN", pick)


def DET_2026_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}):
    """
    Detroit has not traded their 2026 pick. They keep it regardless of position.
    """
    pick = draft_order["DET"]
    return ("DET", pick)


def GSW_2026_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}):
    """
    Golden State has not traded their 2026 pick. They keep it regardless of position.
    """
    pick = draft_order["GSW"]
    return ("GSW", pick)


def HOU_2026_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}):
    """
    Houston has not traded their 2026 pick. They keep it regardless of position.
    """
    pick = draft_order["HOU"]
    return ("HOU", pick)


def IND_2026_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}):
    """
    Indiana has not traded their 2026 pick. They keep it regardless of position.
    """
    pick = draft_order["IND"]
    return ("IND", pick)


def LAC_2026_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}):
    """
    LA Clippers has not traded their 2026 pick. They keep it regardless of position.
    """
    pick = draft_order["LAC"]
    return ("LAC", pick)


def LAL_2026_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}):
    """
    LA Lakers has not traded their 2026 pick. They keep it regardless of position.
    """
    pick = draft_order["LAL"]
    return ("LAL", pick)


def MEM_2026_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}):
    """
    Memphis has not traded their 2026 pick. They keep it regardless of position.
    """
    pick = draft_order["MEM"]
    return ("MEM", pick)


def MIA_2026_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}):
    """
    Miami has not traded their 2026 pick. They keep it regardless of position.
    """
    pick = draft_order["MIA"]
    return ("MIA", pick)


def MIL_2026_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}):
    """
    Milwaukee has not traded their 2026 pick. They keep it regardless of position.
    """
    pick = draft_order["MIL"]
    return ("MIL", pick)


def MIN_2026_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}):
    """
    Minnesota has not traded their 2026 pick. They keep it regardless of position.
    """
    pick = draft_order["MIN"]
    return ("MIN", pick)


def NOP_2026_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}):
    """
    New Orleans has not traded their 2026 pick. They keep it regardless of position.
    """
    pick = draft_order["NOP"]
    return ("NOP", pick)


def NYK_2026_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}):
    """
    New York has not traded their 2026 pick. They keep it regardless of position.
    """
    pick = draft_order["NYK"]
    return ("NYK", pick)


def OKC_2026_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}):
    """
    Oklahoma City has not traded their 2026 pick. They keep it regardless of position.
    """
    pick = draft_order["OKC"]
    return ("OKC", pick)


def ORL_2026_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}):
    """
    Orlando has not traded their 2026 pick. They keep it regardless of position.
    """
    pick = draft_order["ORL"]
    return ("ORL", pick)


def PHI_2026_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}):
    """
    Philadelphia has not traded their 2026 pick. They keep it regardless of position.
    """
    pick = draft_order["PHI"]
    return ("PHI", pick)


def PHX_2026_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}):
    """
    Phoenix has not traded their 2026 pick. They keep it regardless of position.
    """
    pick = draft_order["PHX"]
    return ("PHX", pick)


def POR_2026_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}):
    """
    Portland has not traded their 2026 pick. They keep it regardless of position.
    """
    pick = draft_order["POR"]
    return ("POR", pick)


def SAC_2026_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}):
    """
    Sacramento has not traded their 2026 pick. They keep it regardless of position.
    """
    pick = draft_order["SAC"]
    return ("SAC", pick)


def SAS_2026_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}):
    """
    San Antonio has not traded their 2026 pick. They keep it regardless of position.
    """
    pick = draft_order["SAS"]
    return ("SAS", pick)


def TOR_2026_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}):
    """
    Toronto has not traded their 2026 pick. They keep it regardless of position.
    """
    pick = draft_order["TOR"]
    return ("TOR", pick)


def UTA_2026_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}):
    """
    Utah has not traded their 2026 pick. They keep it regardless of position.
    """
    pick = draft_order["UTA"]
    return ("UTA", pick)


def WAS_2026_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}):
    """
    Washington has not traded their 2026 pick. They keep it regardless of position.
    """
    pick = draft_order["WAS"]
    return ("WAS", pick)



"""
ROUND 2 PICKS
"""