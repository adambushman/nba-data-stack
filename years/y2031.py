"""
NBA Draft Year 2031
This file contains functions to determine the ownership of the 2031 NBA Draft picks.
Additionally, there exist constants for swap favorability.
"""


from utils import evaluate_swap


SWAP_FAVORABILITY = {
    "01": ["SAC", "SAS"]
}


def ATL_2031_r1(draft_order, prior_pick_history, context={}):
    """
    Atlanta has not traded their 2031 pick. They keep it regardless of position.
    """
    return "ATL"


def BOS_2031_r1(draft_order, prior_pick_history, context={}):
    """
    Boston has not traded their 2031 pick. They keep it regardless of position.
    """
    return "BOS"


def BRK_2031_r1(draft_order, prior_pick_history, context={}):
    """
    Brooklyn has not traded their 2031 pick. They keep it regardless of position.
    """
    return "BRK"


def CHA_2031_r1(draft_order, prior_pick_history, context={}):
    """
    Carlotte has not traded their 2031 pick. They keep it regardless of position.
    """
    return "CHA"


def CHI_2031_r1(draft_order, prior_pick_history, context={}):
    """
    Chicago has not traded their 2031 pick. They keep it regardless of position.
    """
    return "CHI"


def CLE_2031_r1(draft_order, prior_pick_history, context={}):
    """
    Cleveland has not traded their 2031 pick. They keep it regardless of position.
    """
    return "CLE"


def DAL_2031_r1(draft_order, prior_pick_history, context={}):
    """
    Dallas has not traded their 2031 pick. They keep it regardless of position.
    """
    return "DAL"


def DEN_2031_r1(draft_order, prior_pick_history, context={}):
    """
    Denver has not traded their 2031 pick. They keep it regardless of position.
    """
    return "DEN"


def DET_2031_r1(draft_order, prior_pick_history, context={}):
    """
    Detroit has not traded their 2031 pick. They keep it regardless of position.
    """
    return "DET"


def GSW_2031_r1(draft_order, prior_pick_history, context={}):
    """
    Golden State has not traded their 2031 pick. They keep it regardless of position.
    """
    return "GSW"


def HOU_2031_r1(draft_order, prior_pick_history, context={}):
    """
    Houston has not traded their 2031 pick. They keep it regardless of position.
    """
    return "HOU"


def IND_2031_r1(draft_order, prior_pick_history, context={}):
    """
    Indiana has not traded their 2031 pick. They keep it regardless of position.
    """
    return "IND"


def LAC_2031_r1(draft_order, prior_pick_history, context={}):
    """
    LA Clippers has not traded their 2031 pick. They keep it regardless of position.
    """
    return "LAC"


def LAL_2031_r1(draft_order, prior_pick_history, context={}):
    """
    LA Lakers has not traded their 2031 pick. They keep it regardless of position.
    """
    return "LAL"


def MEM_2031_r1(draft_order, prior_pick_history, context={}):
    """
    Memphis has not traded their 2031 pick. They keep it regardless of position.
    """
    return "MEM"


def MIA_2031_r1(draft_order, prior_pick_history, context={}):
    """
    Miami has not traded their 2031 pick. They keep it regardless of position.
    """
    return "MIA"


def MIL_2031_r1(draft_order, prior_pick_history, context={}):
    """
    Milwaukee has not traded their 2031 pick. They keep it regardless of position.
    """
    return "MIL"


def MIN_2031_r1(draft_order, prior_pick_history, context={}):
    """
    Minnesota traded their 2031 pick. Current owner is Sacramento.
        - Pick is unprotected.
        - MIN -> SAS: this was the Rob Dillingham trade
        - SAS -> SAC: this was the De'Aaron Fox trade
    """
    return "SAC"


def NOP_2031_r1(draft_order, prior_pick_history, context={}):
    """
    New Orleans has not traded their 2031 pick. They keep it regardless of position.
    """
    return "NOP"


def NYK_2031_r1(draft_order, prior_pick_history, context={}):
    """
    New York has traded their 2031 pick. Current owner is Brooklyn.
        - Pick is unprotected.
        - NYK -> BRK: this was the Mikal Bridges trade.
    """
    return "NYK"


def OKC_2031_r1(draft_order, prior_pick_history, context={}):
    """
    Oklahoma City has not traded their 2031 pick. They keep it regardless of position.
    """
    return "OKC"


def ORL_2031_r1(draft_order, prior_pick_history, context={}):
    """
    Orlando has not traded their 2031 pick. They keep it regardless of position.
    """
    return "ORL"


def PHI_2031_r1(draft_order, prior_pick_history, context={}):
    """
    Philadelphia has not traded their 2031 pick. They keep it regardless of position.
    """
    return "PHI"


def PHX_2031_r1(draft_order, prior_pick_history, context={}):
    """
    Phoenix has traded their 2031 pick. Current owner is Utah.
        - Pick is unprotected.
        - PHX -> UTA: this was the trade acquiring multiple least favorable swaps.
    """
    return "PHX"


def POR_2031_r1(draft_order, prior_pick_history, context={}):
    """
    Portland has not traded their 2031 pick. They keep it regardless of position.
    """
    return "POR"


def SAC_2031_r1(draft_order, prior_pick_history, context={}):
    """
    Sacramento has not traded their 2031 pick. They participate in swap rights with San Antonio.
        -   SAC <-> SAS: this was the De'Aaron Fox trade.
        -   SAC owns the most favorable swap rights with SAS.
    """
    current_team = "SAC"
    participating_teams = SWAP_FAVORABILITY["01"]
    ownership = evaluate_swap(draft_order, participating_teams, current_team)
    return "SAC"


def SAS_2031_r1(draft_order, prior_pick_history, context={}):
    """
    San Antonio has not traded their 2031 pick. They keep it regardless of position.
    """
    return "SAS"


def TOR_2031_r1(draft_order, prior_pick_history, context={}):
    """
    Toronto has not traded their 2031 pick. They keep it regardless of position.
    """
    return "TOR"


def UTA_2031_r1(draft_order, prior_pick_history, context={}):
    """
    Utah has not traded their 2031 pick. They keep it regardless of position.
    """
    return "UTA"


def WAS_2031_r1(draft_order, prior_pick_history, context={}):
    """
    Washington has not traded their 2031 pick. They keep it regardless of position.
    """
    return "WAS"



"""
ROUND 2 PICKS
"""