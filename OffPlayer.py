from OffPlayerStatsAvg import OffPlayerStatsAvg
from OffPlayerStatsTotal import OffPlayerStatsTotal

class OffPlayer:
    def __init__(self, name, team):
        self.name = name
        self.team = team
        self.avgStats = OffPlayerStatsAvg(name, team)
        self.totalStats = OffPlayerStatsTotal(name, team)
        self.teamAbrv = None
        self.position = None
        self.gamesPlayed2023 = 0
        self.weekByWeekStats = []