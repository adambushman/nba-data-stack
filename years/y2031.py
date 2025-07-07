"""
NBA Draft Year 2031
This file contains functions to determine the ownership of the 2031 NBA Draft picks.
Additionally, there exist constants for swap favorability.

Last Confirmed : July 2025
"""


from years.utils  import (
  evaluate_protection
  , evaluate_swap
  , evaluate_pick_history
)
from typing import Optional, Tuple


SWAP_FAVORABILITY = {
    # Ordered most to least favorable
    "01": ["SAC", "SAS"]
}


def ATL_2031_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}) -> Tuple[str, int]:
    """
    Atlanta has not traded their 2031 pick. They keep it regardless of position.
    """
    pick = draft_order["ATL"]
    return ("ATL", pick)


def BOS_2031_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}) -> Tuple[str, int]:
    """
    Boston has not traded their 2031 pick. They keep it regardless of position.
    """
    pick = draft_order["BOS"]
    return ("BOS", pick)


def BRK_2031_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}) -> Tuple[str, int]:
    """
    Brooklyn has not traded their 2031 pick. They keep it regardless of position.
    """
    pick = draft_order["BRK"]
    return ("BRK", pick)


def CHA_2031_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}) -> Tuple[str, int]:
    """
    Carlotte has not traded their 2031 pick. They keep it regardless of position.
    """
    pick = draft_order["CHA"]
    return ("CHA", pick)


def CHI_2031_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}) -> Tuple[str, int]:
    """
    Chicago has not traded their 2031 pick. They keep it regardless of position.
    """
    pick = draft_order["CHI"]
    return ("CHI", pick)


def CLE_2031_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}) -> Tuple[str, int]:
    """
    Cleveland has not traded their 2031 pick. They keep it regardless of position.
    """
    pick = draft_order["CLE"]
    return ("CLE", pick)


def DAL_2031_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}) -> Tuple[str, int]:
    """
    Dallas has not traded their 2031 pick. They keep it regardless of position.
    """
    pick = draft_order["DAL"]
    return ("DAL", pick)


def DEN_2031_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}) -> Tuple[str, int]:
    """
    Denver has not traded their 2031 pick. They keep it regardless of position.
    """
    pick = draft_order["DEN"]
    return ("DEN", pick)


def DET_2031_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}) -> Tuple[str, int]:
    """
    Detroit has not traded their 2031 pick. They keep it regardless of position.
    """
    pick = draft_order["DET"]
    return ("DET", pick)


def GSW_2031_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}) -> Tuple[str, int]:
    """
    Golden State has not traded their 2031 pick. They keep it regardless of position.
    """
    pick = draft_order["GSW"]
    return ("GSW", pick)


def HOU_2031_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}) -> Tuple[str, int]:
    """
    Houston has not traded their 2031 pick. They keep it regardless of position.
    """
    pick = draft_order["HOU"]
    return ("HOU", pick)


def IND_2031_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}) -> Tuple[str, int]:
    """
    Indiana has not traded their 2031 pick. They keep it regardless of position.
    """
    pick = draft_order["IND"]
    return ("IND", pick)


def LAC_2031_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}) -> Tuple[str, int]:
    """
    LA Clippers has not traded their 2031 pick. They keep it regardless of position.
    """
    pick = draft_order["LAC"]
    return ("LAC", pick)


def LAL_2031_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}) -> Tuple[str, int]:
    """
    LA Lakers has not traded their 2031 pick. They keep it regardless of position.
    """
    pick = draft_order["LAL"]
    return ("LAL", pick)


def MEM_2031_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}) -> Tuple[str, int]:
    """
    Memphis has not traded their 2031 pick. They keep it regardless of position.
    """
    pick = draft_order["MEM"]
    return ("MEM", pick)


def MIA_2031_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}) -> Tuple[str, int]:
    """
    Miami has not traded their 2031 pick. They keep it regardless of position.
    """
    pick = draft_order["MIA"]
    return ("MIA", pick)


def MIL_2031_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}) -> Tuple[str, int]:
    """
    Milwaukee has not traded their 2031 pick. They keep it regardless of position.
    """
    pick = draft_order["MIL"]
    return ("MIL", pick)


def MIN_2031_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}) -> Tuple[str, int]:
    """
    Minnesota traded their 2031 pick. Current owner is Sacramento.
        - Pick is unprotected.
        - MIN -> SAS: this was the Rob Dillingham trade
        - SAS -> SAC: this was the De'Aaron Fox trade
    """
    pick = draft_order["MIN"]
    return ("SAC", pick)


def NOP_2031_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}) -> Tuple[str, int]:
    """
    New Orleans has not traded their 2031 pick. They keep it regardless of position.
    """
    pick = draft_order["NOP"]
    return ("NOP", pick)


def NYK_2031_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}) -> Tuple[str, int]:
    """
    New York has traded their 2031 pick. Current owner is Brooklyn.
        - Pick is unprotected.
        - NYK -> BRK: this was the Mikal Bridges trade.
    """
    pick = draft_order["NYK"]
    return ("BRK", pick)


def OKC_2031_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}) -> Tuple[str, int]:
    """
    Oklahoma City has not traded their 2031 pick. They keep it regardless of position.
    """
    pick = draft_order["OKC"]
    return ("OKC", pick)


def ORL_2031_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}) -> Tuple[str, int]:
    """
    Orlando has not traded their 2031 pick. They keep it regardless of position.
    """
    pick = draft_order["ORL"]
    return ("ORL", pick)


def PHI_2031_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}) -> Tuple[str, int]:
    """
    Philadelphia has not traded their 2031 pick. They keep it regardless of position.
    """
    pick = draft_order["PHI"]
    return ("PHI", pick)


def PHX_2031_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}) -> Tuple[str, int]:
    """
    Phoenix has traded their 2031 pick. Current owner is Utah.
        - Pick is unprotected.
        - PHX -> UTA: this was the trade acquiring multiple least favorable swaps.
    """
    pick = draft_order["PHX"]
    return ("UTA", pick)


def POR_2031_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}) -> Tuple[str, int]:
    """
    Portland has not traded their 2031 pick. They keep it regardless of position.
    """
    pick = draft_order["POR"]
    return ("POR", pick)


def SAC_2031_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}) -> Tuple[str, int]:
    """
    Sacramento has not traded their 2031 pick. They participate in swap rights with San Antonio.
        -   SAC <-> SAS: this was the De'Aaron Fox trade.
        -   SAC owns the most favorable swap rights with SAS.
    """
    current_team = "SAC"
    participating_teams = SWAP_FAVORABILITY["01"]
    ownership = evaluate_swap(participating_teams, current_team)
    return ownership


def SAS_2031_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}) -> Tuple[str, int]:
    """
    San Antonio has traded swap rights to their 2031 pick.
        -   SAS <-> SAC: this was the De'Aaron Fox trade.
        -   SAS owns the least favorable swap rights with SAC.
    """
    current_team = "SAS"
    participating_teams = SWAP_FAVORABILITY["01"]
    ownership = evaluate_swap(participating_teams, current_team)
    return ownership


def TOR_2031_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}) -> Tuple[str, int]:
    """
    Toronto has not traded their 2031 pick. They keep it regardless of position.
    """
    pick = draft_order["TOR"]
    return ("TOR", pick)


def UTA_2031_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}) -> Tuple[str, int]:
    """
    Utah has not traded their 2031 pick. They keep it regardless of position.
    """
    pick = draft_order["UTA"]
    return ("UTA", pick)


def WAS_2031_r1(draft_order: dict, prior_pick_history: Optional[dict] = {}) -> Tuple[str, int]:
    """
    Washington has not traded their 2031 pick. They keep it regardless of position.
    """
    pick = draft_order["WAS"]
    return "WAS"



"""
ROUND 2 PICKS
"""