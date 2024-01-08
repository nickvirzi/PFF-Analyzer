import pymongo
from Team import Team
from OffPlayer import OffPlayer
from pymongo.server_api import ServerApi
from OffPlayerStats import OffPlayerStats

client = pymongo.MongoClient("mongodb+srv://nickvirzi:Lm0KEcYruPQMoUnr@pff-analyzer.cd6jej9.mongodb.net/?retryWrites=true&w=majority", server_api=ServerApi('1'))
nflTeamsTable = client["NFLTeamsTable"]
teamList = nflTeamsTable.list_collection_names()

offTeam = input("Enter offensive team: ")

oppPercentMan = .308
oppPercentZone = .692

highTDs = []

for teamName in teamList:
    team = nflTeamsTable[teamName]

    if teamName == offTeam:
        for data in team.find():
            for player in data['offensivePlayers']:
                manRR = 0 
                manYds = 0 
                manRecs = 0 
                manRecTDs = 0
                manTgts = 0
                manYdsPRR = 0 
                manRecsPRR = 0 
                manTgtsPRR = 0
                zoneRR = 0 
                zoneYds = 0 
                zoneRecs = 0 
                zoneRecTDs = 0
                zoneTgts = 0
                zoneYdsPRR = 0 
                zoneRecsPRR = 0 
                zoneTgtsPRR = 0
                gamesPlayed = len(player['weekByWeekStats'])
                last6WeeksStats = [stats for stats in player['weekByWeekStats'] if float(stats['week']) > 11]

                if len(last6WeeksStats) > 2:
                    for weekStats in last6WeeksStats:
                        manRR += float(weekStats['manRoutesRun'])
                        manYds += float(weekStats['manYds'])
                        manRecs += float(weekStats['manRecs']) 
                        manRecTDs += float(weekStats['manRecTDs'])
                        manTgts += float(weekStats['manTgts'])
                        manYdsPRR += float(weekStats['manYdsPerRouteRun'])
                        manRecsPRR += float(weekStats['manRecsPerRouteRun'])
                        manTgtsPRR += float(weekStats['manTgtsPerRouteRun'])
                        zoneRR += float(weekStats['zoneRoutesRun']) 
                        zoneYds += float(weekStats['zoneYds']) 
                        zoneRecs += float(weekStats['zoneRecs']) 
                        zoneRecTDs += float(weekStats['zoneRecTDs'])
                        zoneTgts += float(weekStats['zoneTgts'])
                        zoneYdsPRR += float(weekStats['zoneYdsPerRouteRun']) 
                        zoneRecsPRR += float(weekStats['zoneRecsPerRouteRun']) 
                        zoneTgtsPRR += float(weekStats['zoneTgtsPerRouteRun']) 

                    if manRecTDs == 2: highTDs.append([player['name'], manRecTDs])

                    totalRoutesRun = float(input("Enter " + player['name'] + "'s routes: "))
                    totalGames = float(input("Enter " + player['name'] + "'s games: "))
                    routesRunPerGame = (totalRoutesRun) / totalGames
                    expectedYds = (routesRunPerGame * (manYdsPRR / len(last6WeeksStats)) * oppPercentMan) + (routesRunPerGame * (zoneYdsPRR / len(last6WeeksStats)) * oppPercentZone)
                    expectedRecs = (routesRunPerGame * (manRecsPRR / len(last6WeeksStats)) * oppPercentMan) + (routesRunPerGame * (zoneRecsPRR / len(last6WeeksStats)) * oppPercentZone)
                    expectedTgts = (routesRunPerGame * (manTgtsPRR / len(last6WeeksStats)) * oppPercentMan) + (routesRunPerGame * (zoneTgtsPRR / len(last6WeeksStats)) * oppPercentZone)
                    print(player['name'] + " " + str(expectedTgts) + " Tgts")
                    print(player['name'] + " " + str(expectedRecs) + " Recs")
                    print(player['name'] + " " + str(expectedYds) + " Yds")

print(highTDs)
