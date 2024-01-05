class OffPlayerStatsTotal:
    def __init__(self, name, team):
        self.name = name
        self.team = team
        self.teamAbrv = None
        self.position = None

        #Per Game Totals For The Season
        self.tgts = None #Receiving Grades
        self.recs = None #Receiving Grades
        self.yds = None #Receiving Grades
        self.recTDs = None #Receiving Grades
        self.routesRun = None #Receiving Grades
        self.tgtsPerRouteRun = None #Calc From Receiving Grades
        self.recsPerRouteRun = None #Calc From Receiving Grades
        self.ydsPerRouteRun = None #Receiving Grades
        self.ydsPerTarget = None #Calc From Receiving Grades
        self.recsPerTarget = None #Calc From Receiving Grades

        #Man Per Game Totals For The Season
        self.manTgts = None #Receiving vs Scheme
        self.manRecs = None #Receiving vs Scheme
        self.manYds = None #Receiving vs Scheme
        self.manRecTDs = None #Receiving vs Scheme
        self.manRoutesRun = None #Calc From Receiving vs Scheme
        self.manTgtsPerRouteRun = None #Calc From Receiving vs Scheme
        self.manRecsPerRouteRun = None #Calc From Receiving vs Scheme
        self.manYdsPerRouteRun = None #Receiving vs Scheme
        self.manYdsPerTarget = None #Calc From Receiving vs Scheme
        self.manRecsPerTarget = None #Calc From Receiving vs Scheme

        #Zone Per Game Totals For The Season
        self.zoneTgts = None #Receiving vs Scheme
        self.zoneRecs = None #Receiving vs Scheme
        self.zoneYds = None #Receiving vs Scheme
        self.zoneRecTDs = None #Receiving vs Scheme
        self.zoneRoutesRun = None #Calc From Receiving vs Scheme
        self.zoneTgtsPerRouteRun = None #Calc From Receiving vs Scheme
        self.zoneRecsPerRouteRun = None #Calc From Receiving vs Scheme
        self.zoneYdsPerRouteRun = None #Receiving vs Scheme
        self.zoneYdsPerTarget = None #Calc From Receiving vs Scheme
        self.zoneRecsPerTarget = None #Calc From Receiving vs Scheme