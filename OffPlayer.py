from OffPlayerStatsAvg import OffPlayerStatsAvg
from OffPlayerStatsTotal import OffPlayerStatsTotal

class OffPlayer:
    def __init__(self, name):
        self.name = name
        self.avgStats = OffPlayerStatsAvg(name)
        self.totalStats = OffPlayerStatsTotal(name)
    
    team = None
    position = None
    gamesPlayed2023 = None
    weekByWeekStats = []