import pandas as pd


# Return Value Description
# ---------------------------------------------------------------------------------
# [original_team, original_pick_no, send_team, from_team, from_pick_no]

# original_team: the team who owned the pick at its inception
# original_pick_no: the pick number given it is still owned by the orignal team
# send_team: if populated, the original team's pick is sent to the new team; if blank, it belongs to the original team
# from_team: if populated, it's a swap wherein the original receives this team's pick; if blank, the original team receives nothing
# from_pick_no:
    # if from_team is blank, then it defaults to zero
    # if from_team is populated, then it's the swapped pick number

####################
# ATLANTA          #
# Checked 10/02/23 #
####################

def atl24r1():
    ATL = team_finishes.get("ATL")
    # [original_team, original_pick_no, send_team, from_team, from_pick_no]
    return ["ATL", ATL, "", "", 0]

def atl25r1():
    ATL = team_finishes.get("ATL")
    # [original_team, original_pick_no, send_team, from_team, from_pick_no]
    return ["ATL", ATL, "SAS", "", 0]

def atl26r1():
    ATL = team_finishes.get("ATL")
    SAS = team_finishes.get("SAS")

    # [original_team, original_pick_no, send_team, from_team, from_pick_no]
    if ATL < SAS:
        return ["ATL", ATL, "SAS", "SAS", SAS]
    else:
        return ["ATL", ATL, "", "", 0]

def atl27r1():
    ATL = team_finishes.get("ATL")
    # [original_team, original_pick_no, send_team, from_team, from_pick_no]
    return ["ATL", ATL, "SAS", "", 0]

def atl28r1():
    ATL = team_finishes.get("ATL")
    # [original_team, original_pick_no, send_team, from_team, from_pick_no]
    return ["ATL", ATL, "", "", 0]

def atl29r1():
    ATL = team_finishes.get("ATL")
    # [original_team, original_pick_no, send_team, from_team, from_pick_no]
    return ["ATL", ATL, "", "", 0]

def atl30r1():
    ATL = team_finishes.get("ATL")
    # [original_team, original_pick_no, send_team, from_team, from_pick_no]
    return ["ATL", ATL, "", "", 0]


####################
# BOSTON           #
# Checked 10/02/23 #
####################

def bos24r1():
    BOS = team_finishes.get("BOS")
    # [original_team, original_pick_no, send_team, from_team, from_pick_no]
    return ["BOS", BOS, "", "", 0]

def bos25r1():
    BOS = team_finishes.get("BOS")
    # [original_team, original_pick_no, send_team, from_team, from_pick_no]
    return ["BOS", BOS, "", "", 0]

def bos26r1():
    BOS = team_finishes.get("BOS")
    # [original_team, original_pick_no, send_team, from_team, from_pick_no]
    return ["BOS", BOS, "", "", 0]

def bos27r1():
    BOS = team_finishes.get("BOS")
    # [original_team, original_pick_no, send_team, from_team, from_pick_no]
    return ["BOS", BOS, "", "", 0]

def bos28r1():
    BOS = team_finishes.get("BOS")
    SAS = team_finishes.get("SAS")

    # [original_team, original_pick_no, send_team, from_team, from_pick_no]
    if BOS == 1:
        return ["BOS", BOS, "", "", 0]
    else:
        if BOS < SAS:
            return ["BOS", BOS, "SAS", "SAS", SAS]
        else:
            return ["BOS", BOS, "", "", 0]

def bos29r1():
    BOS = team_finishes.get("BOS")
    # [original_team, original_pick_no, send_team, from_team, from_pick_no]
    return ["BOS", BOS, "POR", "", 0]

def bos30r1():
    BOS = team_finishes.get("BOS")
    # [original_team, original_pick_no, send_team, from_team, from_pick_no]
    return ["BOS", BOS, "", "", 0]


####################
# BROOKLYN         #
# Checked 10/02/23 #
####################

def bkn24r1():
    BKN = team_finishes.get("BKN")
    return ["BKN", BKN, "HOU", "", 0]

def bkn25r1():
    BKN = team_finishes.get("BKN")
    HOU = team_finishes.get("HOU")
    LAC = team_finishes.get("LAC")
    OKC = team_finishes.get("OKC")

    pick = max(HOU, BKN, OKC)

    if pick == HOU:
        team = "HOU"
    elif pick == BKN:
        team = "BKN"
    else:
        team = "OKC"

    if HOU in range(1,10):
        # [original_team, original_pick_no, send_team, from_team, from_pick_no]
        return ["BKN", BKN, "", "", 0]
    else:
        if HOU > LAC:
            return ["BKN", BKN, team, team, max(HOU, BKN, OKC)]
        else:
            return ["BKN", BKN, "HOU", "HOU", HOU]

def bkn26r1():
    BKN = team_finishes.get("BKN")
    # [original_team, original_pick_no, send_team, from_team, from_pick_no]
    return ["BKN", BKN, "HOU", "", 0]

def bkn27r1():
    HOU = team_finishes.get("HOU")
    BKN = team_finishes.get("BKN")

    if BKN < HOU:
        # [original_team, original_pick_no, send_team, from_team, from_pick_no]
        return ["BKN", BKN, "HOU", "HOU", HOU]
    else:
        return ["BKN", BKN, "", "", 0]

def bkn28r1():
    BKN = team_finishes.get("BKN")
    PHI = team_finishes.get("PHI")
    PHX = team_finishes.get("PHX")

    if PHI in range(9,30):
        pick = min(BKN, PHI, PHX)
    else:
        pick = min(BKN, PHX)
    
    if pick == BKN:
        team = "BKN"
    elif pick == PHI:
        team = "PHI"
    else:
        team = "PHX"

    # [original_team, original_pick_no, send_team, from_team, from_pick_no]
    return ["BKN", BKN, team, team, pick]


def bkn29r1():
    BKN = team_finishes.get("BKN")
    # [original_team, original_pick_no, send_team, from_team, from_pick_no]
    return ["BKN", BKN, "", "", 0]

def bkn30r1():
    BKN = team_finishes.get("BKN")
    # [original_team, original_pick_no, send_team, from_team, from_pick_no]
    return ["BKN", BKN, "", "", 0]


####################
# CHARLOTTE        #
# Checked 10/02/23 #
####################

def cha24r1():
    CHA = team_finishes.get("CHA")

    if CHA in range(1, 14):
        # [original_team, original_pick_no, send_team, from_team, from_pick_no]
        return ["CHA", CHA, "", "", 0]
    else:
        return ["CHA", CHA, "SAS", "", 0]

def cha25r1():
    CHA = team_finishes.get("CHA")

    if cha24r1()[0] == "SAS":
        # [original_team, original_pick_no, send_team, from_team, from_pick_no]
        return ["CHA", CHA, "", "", 0]
    else:
        if CHA in range(1, 14):
            return ["CHA", CHA, "", "", 0]
        else:
            return ["CHA", CHA, "SAS", "", 0]

def cha26r1():
    CHA = team_finishes.get("CHA")
    # [original_team, original_pick_no, send_team, from_team, from_pick_no]
    return ["CHA", CHA, "", "", 0]

def cha27r1():
    CHA = team_finishes.get("CHA")
    # [original_team, original_pick_no, send_team, from_team, from_pick_no]
    return ["CHA", CHA, "", "", 0]

def cha28r1():
    CHA = team_finishes.get("CHA")
    # [original_team, original_pick_no, send_team, from_team, from_pick_no]
    return ["CHA", CHA, "", "", 0]

def cha29r1():
    CHA = team_finishes.get("CHA")
    # [original_team, original_pick_no, send_team, from_team, from_pick_no]
    return ["CHA", CHA, "", "", 0]

def cha30r1():
    CHA = team_finishes.get("CHA")
    # [original_team, original_pick_no, send_team, from_team, from_pick_no]
    return ["CHA", CHA, "", "", 0]


####################
# CHICAGO          #
# Checked 10/02/23 #
####################

def chi24r1():
    CHI = team_finishes.get("CHI")
    # [original_team, original_pick_no, send_team, from_team, from_pick_no]
    return ["CHI", CHI, "", "", 0]

def chi25r1():
    CHI = team_finishes.get("CHI")

    if CHI in range(1, 10):
        # [original_team, original_pick_no, send_team, from_team, from_pick_no]
        return ["CHI", CHI, "", "", 0]
    else:
        return ["CHI", CHI, "SAS", "", 0]

def chi26r1():
    CHI = team_finishes.get("CHI")

    if chi25r1()[0] == "SAS":
        # [original_team, original_pick_no, send_team, from_team, from_pick_no]
        return ["CHI", CHI, "", "", 0]
    else:
        if CHI in range(1, 8):
            return ["CHI", CHI, "", "", 0]
        else:
            return ["CHI", CHI, "SAS", "", 0]

def chi27r1():
    CHI = team_finishes.get("CHI")

    if chi25r1()[0] == "SAS" or chi26r1()[0] == "SAS":
        # [original_team, original_pick_no, send_team, from_team, from_pick_no]
        return ["CHI", CHI, "", "", 0]
    else:
        if CHI in range(1, 8):
            return ["CHI", CHI, "", "", 0]
        else:
            return ["CHI", CHI, "SAS", "", 0]

def chi28r1():
    CHI = team_finishes.get("CHI")
    # [original_team, original_pick_no, send_team, from_team, from_pick_no]
    return ["CHI", CHI, "", "", 0]

def chi29r1():
    CHI = team_finishes.get("CHI")
    # [original_team, original_pick_no, send_team, from_team, from_pick_no]
    return ["CHI", CHI, "", "", 0]

def chi30r1():
    CHI = team_finishes.get("CHI")
    # [original_team, original_pick_no, send_team, from_team, from_pick_no]
    return ["CHI", CHI, "", "", 0]


#####################
# CLEVELAND         #
# Checked 10/02/23  #
#####################

def cle24r1():
    CLE = team_finishes.get("CLE")
    # [original_team, original_pick_no, send_team, from_team, from_pick_no]
    return ["CLE", CLE, "", "", 0]

def cle25r1():
    CLE = team_finishes.get("CLE")
    # [original_team, original_pick_no, send_team, from_team, from_pick_no]
    return ["CLE", CLE, "UTA", "", 0]

def cle26r1():
    CLE = team_finishes.get("CLE")
    UTA = team_finishes.get("UTA")
    MIN = team_finishes.get("MIN")

    if UTA in range(1, 8) | uta24r1()[0] == "OKC" | uta25r1()[0] == "OKC":
        pick = min(UTA, CLE, MIN)

        if pick == UTA | pick == MIN:
             # [original_team, original_pick_no, send_team, from_team, from_pick_no]
            return ["CLE", CLE, "", "", 0]
        else:
            return ["CLE", CLE, "UTA", "UTA", UTA]
    else:
        return ["CLE", CLE, "", "", 0]

def cle27r1():
    CLE = team_finishes.get("CLE")
    # [original_team, original_pick_no, send_team, from_team, from_pick_no]
    return ["CLE", CLE, "UTA", "", 0]

def cle28r1():
    UTA = team_finishes.get("UTA")
    CLE = team_finishes.get("CLE")

    if UTA < CLE:
        # [original_team, original_pick_no, send_team, from_team, from_pick_no]
        return ["CLE", CLE, "", "", 0]
    else:
        return ["CLE", CLE, "UTA", "UTA", UTA]

def cle29r1():
    CLE = team_finishes.get("CLE")
    # [original_team, original_pick_no, send_team, from_team, from_pick_no]
    return ["CLE", CLE, "UTA", "", 0]

def cle30r1():
    CLE = team_finishes.get("CLE")
    # [original_team, original_pick_no, send_team, from_team, from_pick_no]
    return ["CLE", CLE, "", "", 0]


####################
# DALLAS           #
# Checked 10/02/23  #
####################

def dal24r1():
    DAL = team_finishes.get("DAL")
    if DAL in range(1,10):
        # [original_team, original_pick_no, send_team, from_team, from_pick_no]
        return ["DAL", DAL, "", "", 0]
    else:
        return ["DAL", DAL, "NYK", "", 0]

def dal25r1():
    DAL = team_finishes.get("DAL")
    if dal24r1()[0] == "NYK":
        # [original_team, original_pick_no, send_team, from_team, from_pick_no]
        return ["DAL", DAL, "", "", 0]
    else:
        if DAL in range(1,10):
            return ["DAL", DAL, "", "", 0]
        else:
            return ["DAL", DAL, "NYK", "", 0]
        
def dal26r1():
    DAL = team_finishes.get("DAL")
    # [original_team, original_pick_no, send_team, from_team, from_pick_no]
    return ["DAL", DAL, "", "", 0]
        
def dal27r1():
    DAL = team_finishes.get("DAL")
    # [original_team, original_pick_no, send_team, from_team, from_pick_no]
    return ["DAL", DAL, "", "", 0]
        
def dal28r1():
    DAL = team_finishes.get("DAL")
    # [original_team, original_pick_no, send_team, from_team, from_pick_no]
    return ["DAL", DAL, "", "", 0]
        
def dal29r1():
    DAL = team_finishes.get("DAL")
    # [original_team, original_pick_no, send_team, from_team, from_pick_no]
    return ["DAL", DAL, "BKN", "", 0]
        
def dal30r1():
    DAL = team_finishes.get("DAL")
    SAS = team_finishes.get("SAS")

    if DAL < SAS:
        # [original_team, original_pick_no, send_team, from_team, from_pick_no]
        return ["DAL", DAL, "", "", 0]
    else:
        return ["DAL", DAL, "", "", 0]


####################
# DENVER           #
# Checked 10/02/23 #
####################

def den24r1():
    DEN = team_finishes.get("DEN")
    # [original_team, original_pick_no, send_team, from_team, from_pick_no]
    return ["DEN", DEN, "", "", 0]

def den25r1():
    DEN = team_finishes.get("DEN")
    
    if team_finishes.get("DEN") in range(1,5):
        # [original_team, original_pick_no, send_team, from_team, from_pick_no]
        return ["DEN", DEN, "", "", 0]
    else:
        return ["DEN", DEN, "ORL", "", 0]

def den26r1():
    DEN = team_finishes.get("DEN")

    if den25r1()[0] == "ORL":
        # [original_team, original_pick_no, send_team, from_team, from_pick_no]
        return ["DEN", DEN, "", "", 0]
    else:
        if DEN in range(1,5):
            return ["DEN", DEN, "", "", 0]
        else:
            return ["DEN", DEN, "ORL", "", 0]

def den27r1():
    DEN = team_finishes.get("DEN")
    if den25r1()[0] == "ORL" or den26r1()[0] == "ORL":
        if DEN in range(1,5):
            # [original_team, original_pick_no, send_team, from_team, from_pick_no]
            return ["DEN", DEN, "", "", 0]
        else:
            return ["DEN", DEN, "OKC", "", 0]
    else:
        if DEN in range(1,5):
            return ["DEN", DEN, "", "", 0]
        else:
            return ["DEN", DEN, "ORL", "", 0]

def den28r1():
    DEN = team_finishes.get("DEN")
    if (den25r1()[0] == "ORL" or den26r1()[0] == "ORL") and den27r1()[0] == "OKC":
        # [original_team, original_pick_no, send_team, from_team, from_pick_no]
        return ["DEN", DEN, "", "", 0]
    else:
        if DEN in range(1,5):
            return ["DEN", DEN, "", "", 0]
        else:
            return ["DEN", DEN, "OKC", "", 0]

def den29r1():
    DEN = team_finishes.get("DEN")
    if den27r1()[0] == "OKC" or den28r1()[0] == "OKC":
        # [original_team, original_pick_no, send_team, from_team, from_pick_no]
        return ["DEN", DEN, "", "", 0]
    else:
        if DEN in range(1,5):
            return ["DEN", DEN, "", "", 0]
        else:
            return ["DEN", DEN, "OKC", "", 0]

def den30r1():
    DEN = team_finishes.get("DEN")
    if den27r1()[0] == "OKC" or den28r1()[0] == "OKC" or den29r1()[0] == "OKC":
        # [original_team, original_pick_no, send_team, from_team, from_pick_no]
        return ["DEN", DEN, "", "", 0]
    else:
        if DEN in range(1,5):
            return ["DEN", DEN, "", "", 0]
        else:
            return ["DEN", DEN, "OKC", "", 0]


####################
# DETROIT          #
# Checked 10/02/23 #
####################

def det24r1():
    DET = team_finishes.get("DET")
    if DET in range(1,18):
        # [original_team, original_pick_no, send_team, from_team, from_pick_no]
        return ["DET", DET, "", "", 0]
    else:
        return ["DET", DET, "NYK", "", 0]

def det25r1():
    DET = team_finishes.get("DET")
    if det24r1()[0] == "NYK":
        # [original_team, original_pick_no, send_team, from_team, from_pick_no]
        return ["DET", DET, "", "", 0]
    else:
        if DET in range(1,13):
            return ["DET", DET, "", "", 0]
        else:
            return ["DET", DET, "NYK", "", 0]

def det26r1():
    DET = team_finishes.get("DET")
    if det24r1()[0] == "NYK" or det25r1()[0] == "NYK":
        # [original_team, original_pick_no, send_team, from_team, from_pick_no]
        return ["DET", DET, "", "", 0]
    else:
        if DET in range(1,11):
            return ["DET", DET, "", "", 0]
        else:
            return ["DET", DET, "NYK", "", 0]

def det27r1():
    DET = team_finishes.get("DET")
    if det24r1()[0] == "NYK" or det25r1()[0] == "NYK" or det26r1()[0] == "NYK":
        # [original_team, original_pick_no, send_team, from_team, from_pick_no]
        return ["DET", DET, "", "", 0]
    else:
        if DET in range(1,9):
            return ["DET", DET, "", "", 0]
        else:
            return ["DET", DET, "NYK", "", 0]
        
def det28r1():
    DET = team_finishes.get("DET")
    # [original_team, original_pick_no, send_team, from_team, from_pick_no]
    return ["DET", DET, "", "", 0]
        
def det29r1():
    DET = team_finishes.get("DET")
    # [original_team, original_pick_no, send_team, from_team, from_pick_no]
    return ["DET", DET, "", "", 0]
        
def det30r1():
    DET = team_finishes.get("DET")
    # [original_team, original_pick_no, send_team, from_team, from_pick_no]
    return ["DET", DET, "", "", 0]


####################
# GOLDEN STATE     #
# Checked 10/02/23 #
####################

def gsw24r1():
    GSW = team_finishes.get("GSW")

    if GSW in range(1, 4):
        # [original_team, original_pick_no, send_team, from_team, from_pick_no]
        return ["GSW", GSW, "", "", 0]
    else:
        return ["GSW", GSW, "POR", "", 0]

def gsw25r1():
    GSW = team_finishes.get("GSW")

    if gsw24r1()[0] == "POR":
        # [original_team, original_pick_no, send_team, from_team, from_pick_no]
        return ["GSW", GSW, "", "", 0]
    else:
        if GSW in range(1, 4):
            return ["GSW", GSW, "", "", 0]
        else:
            return ["GSW", GSW, "POR", "", 0]

def gsw26r1():
    GSW = team_finishes.get("GSW")
    # [original_team, original_pick_no, send_team, from_team, from_pick_no]
    if gsw24r1()[0] == "POR" or gsw25r1()[0] == "POR":
        return ["GSW", GSW, "", "", 0]
    else:
        return ["GSW", GSW, "POR", "", 0]
    
def gsw27r1():
    GSW = team_finishes.get("GSW")
    # [original_team, original_pick_no, send_team, from_team, from_pick_no]
    return ["GSW", GSW, "", "", 0]
    
def gsw28r1():
    GSW = team_finishes.get("GSW")
    # [original_team, original_pick_no, send_team, from_team, from_pick_no]
    return ["GSW", GSW, "", "", 0]
    
def gsw29r1():
    GSW = team_finishes.get("GSW")
    # [original_team, original_pick_no, send_team, from_team, from_pick_no]
    return ["GSW", GSW, "", "", 0]
    
def gsw30r1():
    GSW = team_finishes.get("GSW")
    
    if GSW in range(1, 20):
        # [original_team, original_pick_no, send_team, from_team, from_pick_no]
        return ["GSW", GSW, "", "", 0]
    else:
        return ["GSW", GSW, "WAS", "", 0]


####################
# HOUSTON          #
# Checked 10/02/23 #
####################

def hou24r1():
    HOU = team_finishes.get("HOU")
    UTA = team_finishes.get("UTA")
    OKC = team_finishes.get("OKC")
    LAC = team_finishes.get("LAC")

    if HOU in range(1,4):
        # [original_team, original_pick_no, send_team, from_team, from_pick_no]
        return ["HOU", HOU, "", "", 0]
    else:
        if UTA in range(11,30):
            if HOU > UTA and HOU > LAC and HOU > OKC:
                return ["HOU", HOU, "IND", "", 0]
            else:
                return ["HOU", HOU, "OKC", "", 0]
        else:
            if HOU > LAC and HOU > OKC:
                return ["HOU", HOU, "IND", "", 0]
            else:
                return ["HOU", HOU, "OKC", "", 0]

def hou25r1():
    HOU = team_finishes.get("HOU")
    BKN = team_finishes.get("BKN")
    LAC = team_finishes.get("LAC")
    OKC = team_finishes.get("OKC")

    pick = min(HOU, max(BKN, OKC))
    if pick == HOU:
        team = "HOU"
    elif pick == BKN:
        team = "BKN"
    else:
        team = "OKC"

    if HOU in range(1,10):
        # [original_team, original_pick_no, send_team, from_team, from_pick_no]
        return ["HOU", HOU, "", "", 0]
    else:
        if HOU > LAC:
            return ["HOU", HOU, team, team, pick]
        else:
            if HOU > BKN and HOU > OKC:
                return ["HOU", HOU, "OKC", "", 0]


def hou26r1():
    HOU = team_finishes.get("HOU")

    if HOU in range(1,4):
        # [original_team, original_pick_no, send_team, from_team, from_pick_no]
        return ["HOU", HOU, "", "", 0]
    else:
        return ["HOU", HOU, "OKC", "", 0]
    
def hou27r1():
    HOU = team_finishes.get("HOU")
    BKN = team_finishes.get("BKN")

    if HOU < BKN:
        # [original_team, original_pick_no, send_team, from_team, from_pick_no]
        return ["HOU", HOU, "", "", 0]
    else:
        return ["HOU", HOU, "BKN", "BKN", BKN]
    
def hou28r1():
    HOU = team_finishes.get("HOU")
    # [original_team, original_pick_no, send_team, from_team, from_pick_no]
    return ["HOU", HOU, "", "", 0]
    
def hou29r1():
    HOU = team_finishes.get("HOU")
    # [original_team, original_pick_no, send_team, from_team, from_pick_no]
    return ["HOU", HOU, "", "", 0]
    
def hou30r1():
    HOU = team_finishes.get("HOU")
    # [original_team, original_pick_no, send_team, from_team, from_pick_no]
    return ["HOU", HOU, "", "", 0]


###################
# INDIANA         #
# Checked 9/26/23 #
###################

def ind24r1():
    IND = team_finishes.get("IND")
    # [original_team, original_pick_no, send_team, from_team, from_pick_no]
    return ["IND", IND, "", "", 0]

def ind25r1():
    IND = team_finishes.get("IND")
    # [original_team, original_pick_no, send_team, from_team, from_pick_no]
    return ["IND", IND, "", "", 0]

def ind26r1():
    IND = team_finishes.get("IND")
    # [original_team, original_pick_no, send_team, from_team, from_pick_no]
    return ["IND", IND, "", "", 0]

def ind27r1():
    IND = team_finishes.get("IND")
    # [original_team, original_pick_no, send_team, from_team, from_pick_no]
    return ["IND", IND, "", "", 0]

def ind28r1():
    IND = team_finishes.get("IND")
    # [original_team, original_pick_no, send_team, from_team, from_pick_no]
    return ["IND", IND, "", "", 0]

def ind29r1():
    IND = team_finishes.get("IND")
    # [original_team, original_pick_no, send_team, from_team, from_pick_no]
    return ["IND", IND, "", "", 0]

def ind30r1():
    IND = team_finishes.get("IND")
    # [original_team, original_pick_no, send_team, from_team, from_pick_no]
    return ["IND", IND, "", "", 0]


####################
# LA CLIPPERS      #
# Checked 10/02/23 #
####################

def lac24r1():
    LAC = team_finishes.get("LAC")
    HOU = team_finishes.get("HOU")
    UTA = team_finishes.get("UTA")
    OKC = team_finishes.get("OKC")

    picks = [LAC, OKC]

    if UTA in range(11,30):
        picks.append(UTA)
    
    if HOU in range(5,30):
        picks.append(HOU)

    picks.sort()

    if picks[len(picks)-1] == LAC:
        # [original_team, original_pick_no, send_team, from_team, from_pick_no]
        return ["LAC", LAC, "IND", "", 0]
    else:
        return ["LAC", LAC, "OKC", "", 0]

def lac25r1():
    LAC = team_finishes.get("LAC")
    OKC = team_finishes.get("OKC")

    if LAC < OKC:
        # [original_team, original_pick_no, send_team, from_team, from_pick_no]
        return ["LAC", LAC, "OKC", "OKC", OKC]
    else:
        return ["LAC", LAC, "", "", 0]
    
def lac26r1():
    LAC = team_finishes.get("LAC")
    # [original_team, original_pick_no, send_team, from_team, from_pick_no]
    return ["LAC", LAC, "OKC", "", 0]
    
def lac27r1():
    LAC = team_finishes.get("LAC")
    # [original_team, original_pick_no, send_team, from_team, from_pick_no]
    return ["LAC", LAC, "", "", 0]
    
def lac28r1():
    LAC = team_finishes.get("LAC")
    # [original_team, original_pick_no, send_team, from_team, from_pick_no]
    return ["LAC", LAC, "", "", 0]
    
def lac29r1():
    LAC = team_finishes.get("LAC")
    # [original_team, original_pick_no, send_team, from_team, from_pick_no]
    return ["LAC", LAC, "", "", 0]
    
def lac30r1():
    LAC = team_finishes.get("LAC")
    # [original_team, original_pick_no, send_team, from_team, from_pick_no]
    return ["LAC", LAC, "", "", 0]


####################
# LA LAKERS        #
# Checked 10/02/23 #
####################

def lal24r1():
    NOP_def = False
    LAL = team_finishes.get("LAL")

    if NOP_def:
        # [original_team, original_pick_no, send_team, from_team, from_pick_no]
        return ["LAL", LAL, "", "", 0]
    else:
        return ["LAL", LAL, "NOP", "", 0]
    
def lal25r1():
    LAL = team_finishes.get("LAL")

    if lal24r1()[0] == "NOP":
        # [original_team, original_pick_no, send_team, from_team, from_pick_no]
        return ["LAL", LAL, "", "", 0]
    else:
        return ["LAL", LAL, "NOP", "", 0]
    
def lal26r1():
    LAL = team_finishes.get("LAL")
    # [original_team, original_pick_no, send_team, from_team, from_pick_no]
    return ["LAL", LAL, "", "", 0]
    
def lal27r1():
    LAL = team_finishes.get("LAL")

    if LAL in range(1,4):
        # [original_team, original_pick_no, send_team, from_team, from_pick_no]
        return ["LAL", LAL, "", "", 0]
    else:
        return ["LAL", LAL, "UTA", "", 0]
    
def lal28r1():
    LAL = team_finishes.get("LAL")
    # [original_team, original_pick_no, send_team, from_team, from_pick_no]
    return ["LAL", LAL, "", "", 0]
    
def lal29r1():
    LAL = team_finishes.get("LAL")
    # [original_team, original_pick_no, send_team, from_team, from_pick_no]
    return ["LAL", LAL, "", "", 0]
    
def lal30r1():
    LAL = team_finishes.get("LAL")
    # [original_team, original_pick_no, send_team, from_team, from_pick_no]
    return ["LAL", LAL, "", "", 0]


####################
# MEMPHIS          #
# Checked 10/02/23 #
####################

def mem24r1():
    MEM = team_finishes.get("MEM")
    PHX = team_finishes.get("PHX")
    WAS = team_finishes.get("WAS")

    picks = [PHX]
    if WAS in range(1,12):
        picks.append(WAS)

    minn = min(MEM, max(picks))
    if minn == MEM:
        team = "MEM"
    elif minn == PHX:
        team = "PHX"
    else:
        team = "WAS"

    # [original_team, original_pick_no, send_team, from_team, from_pick_no]
    return ["MEM", MEM, team, team, minn]

def mem25r1():
    MEM = team_finishes.get("MEM")
    # [original_team, original_pick_no, send_team, from_team, from_pick_no]
    return ["MEM", MEM, "", "", 0]

def mem26r1():
    MEM = team_finishes.get("MEM")
    # [original_team, original_pick_no, send_team, from_team, from_pick_no]
    return ["MEM", MEM, "", "", 0]

def mem27r1():
    MEM = team_finishes.get("MEM")
    # [original_team, original_pick_no, send_team, from_team, from_pick_no]
    return ["MEM", MEM, "", "", 0]

def mem28r1():
    MEM = team_finishes.get("MEM")
    # [original_team, original_pick_no, send_team, from_team, from_pick_no]
    return ["MEM", MEM, "", "", 0]

def mem29r1():
    MEM = team_finishes.get("MEM")
    # [original_team, original_pick_no, send_team, from_team, from_pick_no]
    return ["MEM", MEM, "", "", 0]

def mem30r1():
    MEM = team_finishes.get("MEM")
    PHX = team_finishes.get("PHX")
    WAS = team_finishes.get("WAS")

    pick =  min(MEM, max(PHX, WAS))

    if pick == MEM:
        team = "MEM"
    elif pick == PHX:
        team = "PHX"
    else:
        team = "WAS"
    
    # [original_team, original_pick_no, send_team, from_team, from_pick_no]
    return ["MEM", MEM, team, team, pick]


####################
# MIAMI            #
# Checked 10/02/23 #
####################

def mia24r1():
    MIA = team_finishes.get("MIA")
    # [original_team, original_pick_no, send_team, from_team, from_pick_no]
    return ["MIA", MIA, "", "", 0]

def mia25r1():
    MIA = team_finishes.get("MIA")

    if MIA in range(1,14):
        # [original_team, original_pick_no, send_team, from_team, from_pick_no]
        return ["MIA", MIA, "", "", 0]
    else:
        return ["MIA", MIA, "OKC", "", 0]

def mia26r1():
    MIA = team_finishes.get("MIA")

    if mia25r1()[0] == "OKC":
        # [original_team, original_pick_no, send_team, from_team, from_pick_no]
        return ["MIA", MIA, "", "", 0]
    else:
        return ["MIA", MIA, "OKC", "", 0]

def mia27r1():
    MIA = team_finishes.get("MIA")
    # [original_team, original_pick_no, send_team, from_team, from_pick_no]
    return ["MIA", MIA, "", "", 0]

def mia28r1():
    MIA = team_finishes.get("MIA")
    # [original_team, original_pick_no, send_team, from_team, from_pick_no]
    return ["MIA", MIA, "", "", 0]

def mia29r1():
    MIA = team_finishes.get("MIA")
    # [original_team, original_pick_no, send_team, from_team, from_pick_no]
    return ["MIA", MIA, "", "", 0]

def mia30r1():
    MIA = team_finishes.get("MIA")
    # [original_team, original_pick_no, send_team, from_team, from_pick_no]
    return ["MIA", MIA, "", "", 0]


####################
# MILWAUKEE        #
# Checked 10/02/23 #
####################

def mil24r1():
    MIL = team_finishes.get("MIL")
    NOP = team_finishes.get("NOP")

    if MIL < NOP:
        # [original_team, original_pick_no, send_team, from_team, from_pick_no]
        return ["MIL", MIL, "NOP", "", 0]
    else:
        return ["MIL", MIL, "", "", 0]
    
def mil25r1():
    MIL = team_finishes.get("MIL")

    if MIL in range(1,4):
        # [original_team, original_pick_no, send_team, from_team, from_pick_no]
        return ["MIL", MIL, "NOP", "", 0]
    else:
        return ["MIL", MIL, "NYK", "", 0]
    
def mil26r1():
    MIL = team_finishes.get("MIL")
    NOP = team_finishes.get("NOP")

    if MIL < NOP:
        # [original_team, original_pick_no, send_team, from_team, from_pick_no]
        return ["MIL", MIL, "NOP", "NOP", NOP]
    else:
        return ["MIL", MIL, "", "", 0]
    
def mil27r1():
    MIL = team_finishes.get("MIL")
    # [original_team, original_pick_no, send_team, from_team, from_pick_no]
    return ["MIL", MIL, "NOP", "", 0]

def mil28r1():
    MIL = team_finishes.get("MIL")
    POR = team_finishes.get("POR")

    if MIL < POR:
        # [original_team, original_pick_no, send_team, from_team, from_pick_no]
        return ["MIL", MIL, "POR", "POR", POR]
    else:
        return ["MIL", MIL, "", "", 0]

def mil29r1():
    MIL = team_finishes.get("MIL")
    # [original_team, original_pick_no, send_team, from_team, from_pick_no]
    return ["MIL", MIL, "POR", "", 0]

def mil30r1():
    MIL = team_finishes.get("MIL")
    POR = team_finishes.get("POR")

    if MIL < POR:
        # [original_team, original_pick_no, send_team, from_team, from_pick_no]
        return ["MIL", MIL, "POR", "POR", POR]
    else:
        return ["MIL", MIL, "", "", 0]

####################
# MINNESOTA        #
# Checked 10/02/23 #
####################

def min24r1():
    MIN = team_finishes.get("MIN")
    # [original_team, original_pick_no, send_team, from_team, from_pick_no]
    return ["MIN", MIN, "", "", 0]

def min25r1():
    MIN = team_finishes.get("MIN")
    # [original_team, original_pick_no, send_team, from_team, from_pick_no]
    return ["MIN", MIN, "UTA", "", 0]

def min26r1():
    MIN = team_finishes.get("MIN")

    # [original_team, original_pick_no, send_team, from_team, from_pick_no] 
    if MIN < team_finishes.get("UTA"):
        return ["MIN", MIN, "UTA", "", 0]
    else:
        return ["MIN", MIN, "", "", 0]
    
def min27r1():
    MIN = team_finishes.get("MIN")
    # [original_team, original_pick_no, send_team, from_team, from_pick_no]
    return ["MIN", MIN, "UTA", "", 0]

def min28r1():
    MIN = team_finishes.get("MIN")
    # [original_team, original_pick_no, send_team, from_team, from_pick_no]
    return ["MIN", MIN, "", "", 0]

def min29r1():
    MIN = team_finishes.get("MIN")

    if MIN in range(1,5):
        # [original_team, original_pick_no, send_team, from_team, from_pick_no]
        return ["MIN", MIN, "", "", 0]
    else:
        return ["MIN", MIN, "UTA", "", 0]

def min30r1():
    MIN = team_finishes.get("MIN")
    # [original_team, original_pick_no, send_team, from_team, from_pick_no]
    return ["MIN", MIN, "", "", 0]


####################
# NEW ORLEANS      #
# Checked 10/02/23 #
####################

def nop24r1():
    NOP = team_finishes.get("NOP")
    MIL = team_finishes.get("MIL")

    if NOP < MIL:
        # [original_team, original_pick_no, send_team, from_team, from_pick_no]
        return ["NOP", NOP, "", "", 0]
    else:
        return ["NOP", NOP, "MIL", "MIL", MIL]
    
def nop25r1():
    NOP = team_finishes.get("NOP")
    # [original_team, original_pick_no, send_team, from_team, from_pick_no]
    return ["NOP", NOP, "", "", 0]
    
def nop26r1():
    NOP = team_finishes.get("NOP")
    MIL = team_finishes.get("MIL")

    if NOP < MIL:
        # [original_team, original_pick_no, send_team, from_team, from_pick_no]
        return ["NOP", NOP, "", "", 0]
    else:
        return ["NOP", NOP, "MIL", "MIL", MIL]
    
def nop27r1():
    NOP = team_finishes.get("NOP")
    # [original_team, original_pick_no, send_team, from_team, from_pick_no]
    return ["NOP", NOP, "", "", 0]
    
def nop28r1():
    NOP = team_finishes.get("NOP")
    # [original_team, original_pick_no, send_team, from_team, from_pick_no]
    return ["NOP", NOP, "", "", 0]
    
def nop29r1():
    NOP = team_finishes.get("NOP")
    # [original_team, original_pick_no, send_team, from_team, from_pick_no]
    return ["NOP", NOP, "", "", 0]
    
def nop30r1():
    NOP = team_finishes.get("NOP")
    # [original_team, original_pick_no, send_team, from_team, from_pick_no]
    return ["NOP", NOP, "", "", 0]


####################
# NEW YORK         #
# Checked 10/02/23 #
####################
    
def nyk24r1():
    NYK = team_finishes.get("NYK")
    # [original_team, original_pick_no, send_team, from_team, from_pick_no]
    return ["NYK", NYK, "", "", 0]
    
def nyk25r1():
    NYK = team_finishes.get("NYK")
    # [original_team, original_pick_no, send_team, from_team, from_pick_no]
    return ["NYK", NYK, "", "", 0]
    
def nyk26r1():
    NYK = team_finishes.get("NYK")
    # [original_team, original_pick_no, send_team, from_team, from_pick_no]
    return ["NYK", NYK, "", "", 0]
    
def nyk27r1():
    NYK = team_finishes.get("NYK")
    # [original_team, original_pick_no, send_team, from_team, from_pick_no]
    return ["NYK", NYK, "", "", 0]
    
def nyk28r1():
    NYK = team_finishes.get("NYK")
    # [original_team, original_pick_no, send_team, from_team, from_pick_no]
    return ["NYK", NYK, "", "", 0]
    
def nyk29r1():
    NYK = team_finishes.get("NYK")
    # [original_team, original_pick_no, send_team, from_team, from_pick_no]
    return ["NYK", NYK, "", "", 0]
    
def nyk30r1():
    NYK = team_finishes.get("NYK")
    # [original_team, original_pick_no, send_team, from_team, from_pick_no]
    return ["NYK", NYK, "", "", 0]


####################
# OKLAHOMA CITY    #
# Checked 10/02/23 #
####################
    
def okc24r1():
    OKC = team_finishes.get("OKC")
    # [original_team, original_pick_no, send_team, from_team, from_pick_no]
    return ["OKC", OKC, "", "", 0]

def okc25r1():
    OKC = team_finishes.get("OKC")
    HOU = team_finishes.get("HOU")

    if (HOU < OKC) and HOU in range(11,30):
        # [original_team, original_pick_no, send_team, from_team, from_pick_no]
        return ["OKC", OKC, "HOU", "HOU", HOU]
    else:
        return ["OKC", OKC, "", "", 0]
    
def okc26r1():
    OKC = team_finishes.get("OKC")
    # [original_team, original_pick_no, send_team, from_team, from_pick_no]
    return ["OKC", OKC, "", "", 0]
    
def okc27r1():
    OKC = team_finishes.get("OKC")
    # [original_team, original_pick_no, send_team, from_team, from_pick_no]
    return ["OKC", OKC, "", "", 0]
    
def okc28r1():
    OKC = team_finishes.get("OKC")
    # [original_team, original_pick_no, send_team, from_team, from_pick_no]
    return ["OKC", OKC, "", "", 0]
    
def okc29r1():
    OKC = team_finishes.get("OKC")
    # [original_team, original_pick_no, send_team, from_team, from_pick_no]
    return ["OKC", OKC, "", "", 0]
    
def okc30r1():
    OKC = team_finishes.get("OKC")
    # [original_team, original_pick_no, send_team, from_team, from_pick_no]
    return ["OKC", OKC, "", "", 0]


####################
# ORLANDO          #
# Checked 10/02/23 #
####################

def orl24r1():
    ORL = team_finishes.get("ORL")
    # [original_team, original_pick_no, send_team, from_team, from_pick_no]
    return ["ORL", ORL, "", "", 0]

def orl25r1():
    ORL = team_finishes.get("ORL")
    # [original_team, original_pick_no, send_team, from_team, from_pick_no]
    return ["ORL", ORL, "", "", 0]

def orl26r1():
    ORL = team_finishes.get("ORL")
    PHX = team_finishes.get("PHX")
    WAS = team_finishes.get("WAS")

    picks = [PHX]
    if WAS in range(1,8):
        picks.append(WAS)

    minn = min(ORL, max(picks))

    if minn == ORL:
        return ["ORL", ORL, "", "", 0]
    elif minn == PHX:
        return ["ORL", ORL, "PHX", "PHX", PHX]
    else:
        return ["ORL", ORL, "ORL", "ORL", ORL]

def orl27r1():
    ORL = team_finishes.get("ORL")
    # [original_team, original_pick_no, send_team, from_team, from_pick_no]
    return ["ORL", ORL, "", "", 0]

def orl28r1():
    ORL = team_finishes.get("ORL")
    # [original_team, original_pick_no, send_team, from_team, from_pick_no]
    return ["ORL", ORL, "", "", 0]

def orl29r1():
    ORL = team_finishes.get("ORL")
    # [original_team, original_pick_no, send_team, from_team, from_pick_no]
    return ["ORL", ORL, "", "", 0]

def orl30r1():
    ORL = team_finishes.get("ORL")
    # [original_team, original_pick_no, send_team, from_team, from_pick_no]
    return ["ORL", ORL, "", "", 0]


####################
# PHILADELPHIA     #
# Checked 10/02/23 #
####################

def phi24r1():
    PHI = team_finishes.get("PHI")
    # [original_team, original_pick_no, send_team, from_team, from_pick_no]
    return ["PHI", PHI, "", "", 0]

def phi25r1():
    PHI = team_finishes.get("PHI")

    if PHI in range(1,6):
        # [original_team, original_pick_no, send_team, from_team, from_pick_no]
        return ["PHI", PHI, "", "", 0]
    else:
        return ["PHI", PHI, "OKC", "", 0]

def phi26r1():
    PHI = team_finishes.get("PHI")

    if phi25r1()[0] == "OKC":
        # [original_team, original_pick_no, send_team, from_team, from_pick_no]
        return ["PHI", PHI, "", "", 0]
    else:
        if PHI in range(1,6):
            return ["PHI", PHI, "", "", 0]
        else:
            return ["PHI", PHI, "OKC", "", 0]

def phi27r1():
    PHI = team_finishes.get("PHI")

    if phi25r1()[0] == "OKC" or phi26r1()[0] == "OKC":
        if PHI in range(1,8):
            # [original_team, original_pick_no, send_team, from_team, from_pick_no]
            return ["PHI", PHI, "", "", 0]
        else:
            return ["PHI", PHI, "BKN", "", 0]
    else:
        if PHI in range(1,6):
            return ["PHI", PHI, "", "", 0]
        else:
            return ["PHI", PHI, "OKC", "", 0]

def phi28r1():
    BKN = team_finishes.get("BKN")
    PHX = team_finishes.get("PHX")
    WAS = team_finishes.get("WAS")
    PHI = team_finishes.get("PHI")

    if PHI in range(1,8):
        # [original_team, original_pick_no, send_team, from_team, from_pick_no]
        return ["PHI", PHI, "", "", 0]
    else:
        pick = max(BKN, PHX, PHI)
        
        if pick == PHI:
            alt_pick = min(PHI, WAS)
            if alt_pick == PHI:
                return ["PHI", PHI, "WAS", "", 0]
            else:
                return ["PHI", PHI, "", "", 0]
        else:
            return ["PHI", PHI, "BKN", "", 0]


def phi29r1():
    PHI = team_finishes.get("PHI")
    # [original_team, original_pick_no, send_team, from_team, from_pick_no]
    return ["PHI", PHI, "", "", 0]

def phi30r1():
    PHI = team_finishes.get("PHI")
    # [original_team, original_pick_no, send_team, from_team, from_pick_no]
    return ["PHI", PHI, "", "", 0]


#######
# PHX #
#######




###################
# PORTLAND        #
# Checked 9/26/23 #
###################

def por24r1():
    POR = team_finishes.get("POR")

    if POR in range(1,14):
        return ["POR", POR]
    else:
        return ["CHI", POR]

def por25r1():
    POR = team_finishes.get("POR")

    if por24r1() == "CHI":
        return ["POR", POR]
    else:
        if POR in range(1,14):
            return ["POR", POR]
        else:
            return ["CHI", POR]

def por26r1():
    POR = team_finishes.get("POR")

    if por24r1() == "CHI" or por25r1() == "CHI":
        return ["POR", POR]
    else:
        if POR in range(1,14):
            return ["POR", POR]
        else:
            return ["CHI", POR]

def por27r1():
    POR = team_finishes.get("POR")

    if por24r1() == "CHI" or por25r1() == "CHI" or por26r1() == "CHI":
        return ["POR", POR]
    else:
        if POR in range(1,14):
            return ["POR", POR]
        else:
            return ["CHI", POR]

def por28r1():
    POR = team_finishes.get("POR")

    if por24r1() == "CHI" or por25r1() == "CHI" or por26r1() == "CHI" or por27r1() == "CHI":
        return ["POR", POR]
    else:
        if POR in range(1,14):
            return ["POR", POR]
        else:
            return ["CHI", POR]
        
def por29r1():
    return ["POR", team_finishes.get("POR")]
        
def por30r1():
    return ["POR", team_finishes.get("POR")]


###################
# SACRAMENTO      #
# Checked 9/26/23 #
###################

def sac24r1():
    SAC = team_finishes.get("SAC")

    if SAC in range(1,14):
        return ["SAC", SAC]
    else:
        return ["ATL", SAC]

def sac25r1():
    SAC = team_finishes.get("SAC")

    if sac24r1()[0] == "ATL":
        return ["SAC", SAC]
    else:
        if SAC in range(1,12):
            return ["SAC", SAC]
        else:
            return ["ATL", SAC]

def sac26r1():
    SAC = team_finishes.get("SAC")

    if sac24r1()[0] == "ATL" or sac25r1()[0] == "ATL":
        return ["SAC", SAC]
    else:
        if SAC in range(1,10):
            return ["SAC", SAC]
        else:
            return ["ATL", SAC]
        
def sac27r1():
    return ["SAC", team_finishes.get("SAC")]
        
def sac28r1():
    return ["SAC", team_finishes.get("SAC")]
        
def sac29r1():
    return ["SAC", team_finishes.get("SAC")]
        
def sac30r1():
    return ["SAC", team_finishes.get("SAC")]


###################
# SAN ANTONIO     #
# Checked 9/26/23 #
###################

def sas24r1():
    return ["SAS", team_finishes.get("SAS")]

def sas25r1():
    return ["SAS", team_finishes.get("SAS")]

def sas26r1():
    SAS = team_finishes.get("SAS")
    ATL = team_finishes.get("ATL")

    if SAS < ATL:
        return ["SAS", SAS]
    else:
        return ["SAS", ATL]

def sas27r1():
    return ["SAS", team_finishes.get("SAS")]

def sas28r1():
    return ["SAS", team_finishes.get("SAS")]

def sas29r1():
    return ["SAS", team_finishes.get("SAS")]

def sas30r1():
    SAS = team_finishes.get("SAS")
    DAL = team_finishes.get("DAL")

    if SAS < DAL:
        return ["SAS", SAS]
    else:
        return ["SAS", DAL]


###################
# TORONTO         #
# Checked 9/26/23 #
###################

def tor24r1():
    TOR = team_finishes.get("TOR")

    if TOR in range(1,6):
        return ["TOR", TOR]
    else:
        return ["SAS", TOR]

def tor25r1():
    TOR = team_finishes.get("TOR")

    if tor24r1()[0] == "SAS":
        return ["TOR", TOR]
    else:
        if TOR in range(1,6):
            return ["TOR", TOR]
        else:
            return ["SAS", TOR]

def tor26r1():
    TOR = team_finishes.get("TOR")

    if tor24r1()[0] == "SAS" or tor25r1()[0] == "SAS":
        return ["TOR", TOR]
    else:
        if TOR in range(1,6):
            return ["TOR", TOR]
        else:
            return ["SAS", TOR]
        
def tor27r1():
    return ["TOR", team_finishes.get("TOR")]
        
def tor28r1():
    return ["TOR", team_finishes.get("TOR")]
        
def tor29r1():
    return ["TOR", team_finishes.get("TOR")]
        
def tor30r1():
    return ["TOR", team_finishes.get("TOR")]


###################
# UTAH            #
# Checked 9/26/23 #
###################

def uta24r1():
    UTA = team_finishes.get("UTA")
    HOU = team_finishes.get("HOU")
    LAC = team_finishes.get("LAC")
    OKC = team_finishes.get("OKC")

    if UTA in range(1,10):
        return ["UTA", UTA]
    else:
        if UTA > HOU and UTA > LAC and UTA > OKC:
            return ["IND", UTA]
        else: 
            return ["OKC", UTA]

def uta25r1():
    UTA = team_finishes.get("UTA")

    if uta24r1()[0] != "UTA":
        return ["UTA", UTA]
    else:
        if UTA in range(1,10):
            return ["UTA", UTA]
        else:
            return ["OKC", UTA]

def uta26r1():
    UTA = team_finishes.get("UTA")
    CLE = team_finishes.get("CLE")
    MIN = team_finishes.get("MIN")

    if UTA in range(1,8):
        return ["UTA", min(UTA, CLE, MIN)]
    else:
        return ["OKC", min(UTA, CLE, MIN)]

def uta27r1():
    return ["UTA", team_finishes.get("UTA")]

def uta28r1():
    return ["UTA", team_finishes.get("UTA")]

def uta29r1():
    return ["UTA", team_finishes.get("UTA")]

def uta30r1():
    return ["UTA", team_finishes.get("UTA")]


###################
# WASHINGTON      #
# Checked 9/26/23 #
###################

def was24r1():
    WAS = team_finishes.get("WAS")
    PHX = team_finishes.get("PHX")

    if WAS in range(1,12):
        if WAS < PHX:
            return ["WAS", WAS]
        else:
            return ["WAS", PHX]
    else:
        return ["NYK", WAS]
    
def was25r1():
    WAS = team_finishes.get("WAS")

    if was24r1()[0] == "NYK":
        return ["WAS", WAS]
    else:
        if WAS in range(1,10):
            return ["WAS", WAS]
        else:
            return ["NYK", WAS]
        
def was26r1():
    WAS = team_finishes.get("WAS")
    PHX = team_finishes.get("PHX")

    if was24r1()[0] == "NYK" or was24r1()[0] == "NYK":
        if WAS < PHX:
            return ["WAS", WAS]
        else:
            return ["WAS", PHX]
    else:
        if WAS in range(1,8):
            if WAS < PHX:
                return ["WAS", WAS]
            else:
                return ["WAS", PHX]
        else:
            return ["NYK", WAS]
        
def was27r1():
    return ["WAS", team_finishes.get("WAS")]

def was28r1():
    WAS = team_finishes.get("WAS")
    BKN = team_finishes.get("BKN")
    PHX = team_finishes.get("PHX")
    PHI = team_finishes.get("PHI")

    picks = [BKN, PHX]
    if (phi25r1()[0] == "OKC" or phi26r1()[0] == "OKC") and phi27r1()[0] != "OKC":
        picks.append(PHI)
    
    return ["WAS", min(WAS, max(picks))]

def was29r1():
    return ["WAS", team_finishes.get("WAS")]

def was30r1():
    WAS = team_finishes.get("WAS")
    PHX = team_finishes.get("PHX")

    if WAS < PHX:
        return ["WAS", WAS]
    else:
        return ["WAS", PHX]


###########
# Execute #
###########

team_finishes = {
    'cha': 4,
    'BKN': 29,
    'BOS': 17,
    'CHA': 1,
    'CHI': 13,
    'CLE': 3,
    'DAL': 12,
    'DEN': 6,
    'DET': 8,
    'GSW': 19,
    'HOU': 28,
    'IND': 24,
    'LAC': 23,
    'LAL': 20,
    'MEM': 14,
    'MIA': 7,
    'MIL': 25,
    'MIN': 15,
    'NOP': 9,
    'NYK': 16,
    'OKC': 11,
    'ORL': 21,
    'PHI': 22,
    'PHX': 10,
    'POR': 2,
    'SAC': 5,
    'SAS': 26,
    'UTA': 18,
    'TOR': 27,
    'WAS': 30
}


df = pd.DataFrame({
    'original_team': [], 
    'original_pick_no': [], 
    'new_team': [], 
    'fron_team': [], 
    'new_pick_no': []
})


def push_row(df, fns):
    df.loc[len(df)] = fns()


def eval_pick_protections():
    # ATLANTA
    push_row(df, atl24r1)
    push_row(df, atl25r1)
    push_row(df, atl26r1)
    push_row(df, atl27r1)
    push_row(df, atl28r1)
    push_row(df, atl29r1)
    push_row(df, atl30r1)
    # BROOKLYN
    push_row(df, bkn24r1)
    push_row(df, bkn25r1)
    push_row(df, bkn26r1)
    push_row(df, bkn27r1)
    push_row(df, bkn28r1)
    push_row(df, bkn29r1)
    push_row(df, bkn30r1)
    # BOSTON
    push_row(df, bos24r1)
    push_row(df, bos25r1)
    push_row(df, bos26r1)
    push_row(df, bos27r1)
    push_row(df, bos28r1)
    push_row(df, bos29r1)
    push_row(df, bos30r1)
    # CHARLOTTE
    push_row(df, cha24r1)
    push_row(df, cha25r1)
    push_row(df, cha26r1)
    push_row(df, cha27r1)
    push_row(df, cha28r1)
    push_row(df, cha29r1)
    push_row(df, cha30r1)
    # CHICAGO
    push_row(df, chi24r1)
    push_row(df, chi25r1)
    push_row(df, chi26r1)
    push_row(df, chi27r1)
    push_row(df, chi28r1)
    push_row(df, chi29r1)
    push_row(df, chi30r1)
    # CLEVELAND
    push_row(df, cle24r1)
    push_row(df, cle25r1)
    push_row(df, cle26r1)
    push_row(df, cle27r1)
    push_row(df, cle28r1)
    push_row(df, cle29r1)
    push_row(df, cle30r1)
    # DALLAS
    push_row(df, dal24r1)
    push_row(df, dal25r1)
    push_row(df, dal26r1)
    push_row(df, dal27r1)
    push_row(df, dal28r1)
    push_row(df, dal29r1)
    push_row(df, dal30r1)
    # DENVER
    push_row(df, den24r1)
    push_row(df, den25r1)
    push_row(df, den26r1)
    push_row(df, den27r1)
    push_row(df, den28r1)
    push_row(df, den29r1)
    push_row(df, den30r1)
    # DETROIT
    push_row(df, det24r1)
    push_row(df, det25r1)
    push_row(df, det26r1)
    push_row(df, det27r1)
    push_row(df, det28r1)
    push_row(df, det29r1)
    push_row(df, det30r1)
    # GOLDEN STATE
    push_row(df, gsw24r1)
    push_row(df, gsw25r1)
    push_row(df, gsw26r1)
    push_row(df, gsw27r1)
    push_row(df, gsw28r1)
    push_row(df, gsw29r1)
    push_row(df, gsw30r1)
    # HOUSTON
    push_row(df, hou24r1)
    push_row(df, hou25r1)
    push_row(df, hou26r1)
    push_row(df, hou27r1)
    push_row(df, hou28r1)
    push_row(df, hou29r1)
    push_row(df, hou30r1)
    # INDIANA
    push_row(df, ind24r1)
    push_row(df, ind25r1)
    push_row(df, ind26r1)
    push_row(df, ind27r1)
    push_row(df, ind28r1)
    push_row(df, ind29r1)
    push_row(df, ind30r1)
    # LA CLIPPERS
    push_row(df, lac24r1)
    push_row(df, lac25r1)
    push_row(df, lac26r1)
    push_row(df, lac27r1)
    push_row(df, lac28r1)
    push_row(df, lac29r1)
    push_row(df, lac30r1)
    # LA LAKERS
    push_row(df, lal24r1)
    push_row(df, lal25r1)
    push_row(df, lal26r1)
    push_row(df, lal27r1)
    push_row(df, lal28r1)
    push_row(df, lal29r1)
    push_row(df, lal30r1)
    # MEMPHIS
    push_row(df, mem24r1)
    push_row(df, mem25r1)
    push_row(df, mem26r1)
    push_row(df, mem27r1)
    push_row(df, mem28r1)
    push_row(df, mem29r1)
    push_row(df, mem30r1)
    # MIAMI
    push_row(df, mia24r1)
    push_row(df, mia25r1)
    push_row(df, mia26r1)
    push_row(df, mia27r1)
    push_row(df, mia28r1)
    push_row(df, mia29r1)
    push_row(df, mia30r1)
    # MILWAUKEE
    push_row(df, mil24r1)
    push_row(df, mil25r1)
    push_row(df, mil26r1)
    push_row(df, mil27r1)
    push_row(df, mil28r1)
    push_row(df, mil29r1)
    push_row(df, mil30r1)
    # MINNESOTA
    push_row(df, min24r1)
    push_row(df, min25r1)
    push_row(df, min26r1)
    push_row(df, min27r1)
    push_row(df, min28r1)
    push_row(df, min29r1)
    push_row(df, min30r1)
    # NEW ORLEANS
    push_row(df, nop24r1)
    push_row(df, nop25r1)
    push_row(df, nop26r1)
    push_row(df, nop27r1)
    push_row(df, nop28r1)
    push_row(df, nop29r1)
    push_row(df, nop30r1)
    # NEW YORK
    push_row(df, nyk24r1)
    push_row(df, nyk25r1)
    push_row(df, nyk26r1)
    push_row(df, nyk27r1)
    push_row(df, nyk28r1)
    push_row(df, nyk29r1)
    push_row(df, nyk30r1)
    # OKLAHOMA CITY
    push_row(df, okc24r1)
    push_row(df, okc25r1)
    push_row(df, okc26r1)
    push_row(df, okc27r1)
    push_row(df, okc28r1)
    push_row(df, okc29r1)
    push_row(df, okc30r1)
    # ORLANDO
    push_row(df, orl24r1)
    push_row(df, orl25r1)
    push_row(df, orl26r1)
    push_row(df, orl27r1)
    push_row(df, orl28r1)
    push_row(df, orl29r1)
    push_row(df, orl30r1)
    # PHILADELPHIA
    push_row(df, phi24r1)
    push_row(df, phi25r1)
    push_row(df, phi26r1)
    push_row(df, phi27r1)
    push_row(df, phi28r1)
    push_row(df, phi29r1)
    push_row(df, phi30r1)
    # PHOENIX
    push_row(df, phx24r1)
    push_row(df, phx25r1)
    push_row(df, phx26r1)
    push_row(df, phx27r1)
    push_row(df, phx28r1)
    push_row(df, phx29r1)
    push_row(df, phx30r1)
    # PORTLAND
    push_row(df, por24r1)
    push_row(df, por25r1)
    push_row(df, por26r1)
    push_row(df, por27r1)
    push_row(df, por28r1)
    push_row(df, por29r1)
    push_row(df, por30r1)
    # SACRAMENTO
    push_row(df, sac24r1)
    push_row(df, sac25r1)
    push_row(df, sac26r1)
    push_row(df, sac27r1)
    push_row(df, sac28r1)
    push_row(df, sac29r1)
    push_row(df, sac30r1)
    # SAN ANTONIO
    push_row(df, sas24r1)
    push_row(df, sas25r1)
    push_row(df, sas26r1)
    push_row(df, sas27r1)
    push_row(df, sas28r1)
    push_row(df, sas29r1)
    push_row(df, sas30r1)
    # UTAH
    push_row(df, uta24r1)
    push_row(df, uta25r1)
    push_row(df, uta26r1)
    push_row(df, uta27r1)
    push_row(df, uta28r1)
    push_row(df, uta29r1)
    push_row(df, uta30r1)
    # TORONTO
    push_row(df, tor24r1)
    push_row(df, tor25r1)
    push_row(df, tor26r1)
    push_row(df, tor27r1)
    push_row(df, tor28r1)
    push_row(df, tor29r1)
    push_row(df, tor30r1)
    # WASHINGTON
    push_row(df, was24r1)
    push_row(df, was25r1)
    push_row(df, was26r1)
    push_row(df, was27r1)
    push_row(df, was28r1)
    push_row(df, was29r1)
    push_row(df, was30r1)


eval_pick_protections()