class OffPlayerStats:
    def __init__(self, name):
        self.name = name

    team = None
    position = None

    #Per Game Totals
    tgts = None #Receiving Grades
    recs = None #Receiving Grades
    yds = None #Receiving Grades
    recTDs = None #Receiving Grades
    routesRun = None #Receiving Grades
    tgtsPerRouteRun = None #Calc From Receiving Grades
    recsPerRouteRun = None #Calc From Receiving Grades
    ydsPerRouteRun = None #Receiving Grades

    #Man Per Game Totals
    manTgts = None #Receiving vs Scheme
    manRecs = None #Receiving vs Scheme
    manYds = None #Receiving vs Scheme
    manRecTDs = None #Receiving vs Scheme
    manRoutesRun = None #Calc From Receiving vs Scheme
    manTgtsPerRouteRun = None #Calc From Receiving vs Scheme
    manRecsPerRouteRun = None #Calc From Receiving vs Scheme
    manYdsPerRouteRun = None #Receiving vs Scheme

    #Zone Per Game Totals
    zoneTgts = None #Receiving vs Scheme
    zoneRecs = None #Receiving vs Scheme
    zoneYds = None #Receiving vs Scheme
    zoneRecTDs = None #Receiving vs Scheme
    zoneRoutesRun = None #Calc From Receiving vs Scheme
    zoneTgtsPerRouteRun = None #Calc From Receiving vs Scheme
    zoneRecsPerRouteRun = None #Calc From Receiving vs Scheme
    zoneYdsPerRouteRun = None #Receiving vs Scheme