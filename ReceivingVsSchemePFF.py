import time
import pymongo
from Team import Team
from selenium import webdriver
from OffPlayer import OffPlayer
from pymongo.server_api import ServerApi
from OffPlayerStats import OffPlayerStats
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def divByZeroCheck(a,b): return a / b if b else 0

def checkForElement(xPath):
    try:
        driver.find_element(By.XPATH, xPath)
    except:
        return False
    return True    

weeks = []; teamsNumb = []
for i in range(1,18): weeks.append(i)
for i in range(1,33): teamsNumb.append(i)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://premium.pff.com/nfl/positions/2023/SINGLE/receiving-scheme?team=1&week=1')
driver.implicitly_wait(10)
driver.maximize_window()

driver.find_element(By.XPATH, '//*[@id="react-root"]/div/header/div[3]/button').click()
driver.implicitly_wait(10)
driver.find_element(By.XPATH, '//*[@id="login-form_email"]').send_keys('navirzi@gmail.com')
driver.find_element(By.XPATH, '//*[@id="login-form_password"]').send_keys('#Supreme2525')
driver.find_element(By.XPATH, '//*[@id="sign-in"]').click()
time.sleep(1)

while checkForElement('/html/body/div/div/div/div/div[1]') and driver.find_element(By.XPATH, '/html/body/div/div/div/div/div[1]').text == "Recaptcha is required.":
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="login-form_password"]').send_keys('#Supreme2525')
    driver.find_element(By.XPATH, '//*[@id="sign-in"]').click()
    time.sleep(1)

client = pymongo.MongoClient("mongodb+srv://nickvirzi:Lm0KEcYruPQMoUnr@pff-analyzer.cd6jej9.mongodb.net/?retryWrites=true&w=majority", server_api=ServerApi('1'))
nflTeamsTable = client["NFLTeamsTable"]
teams = []

for team in teamsNumb:
    if team != 1:
        driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div[1]/div/div/div[3]/div/div[1]/div[1]/button[2]').click()
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div[1]/div/div/div[3]/div/div/div[1]/button').click()
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div[1]/div/div/div[3]/div/div/div[2]/div/div/div[2]/div[2]/div[1]/div/label[' + str(team) + ']').click()
        driver.implicitly_wait(10)

    curTeam = Team(driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div[1]/div/div/div[3]/div/div[1]/div[1]/button[1]/span[2]').text)

    for week in weeks: 
        if week != 1 or (week != 1 and team != 1):
            driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div[1]/div/div/div[1]/div[4]/div[1]').click()
            driver.implicitly_wait(10)
            driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div[1]/div/div/div[1]/div[4]/div[1]/div[2]/div/div/div[2]/div/label[' + str(week) + ']').click()
            driver.implicitly_wait(10)

        weeklyNameOrder = []

        try:
            table = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div[2]/div/div[3]/div/div/div[1]/div[2]/div/div[1]/div/div[1]/div')
            for tr in table.find_elements(By.CSS_SELECTOR, 'div.kyber-table-body__row'):
                for td in tr.find_elements(By.CSS_SELECTOR, 'div.kyber-table-body-cell--align-left'):
                    if td.text == '': break

                    weeklyNameOrder.append(td.text)
                    if any(player.name == td.text for player in curTeam.offensivePlayers): continue
                    curPlayer = OffPlayer(td.text, driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div[1]/div/div/div[3]/div/div[1]/div[1]/button[1]/span[2]').text)
                    curTeam.offensivePlayers.append(curPlayer)

            i = 0
            table = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div[2]/div/div[3]/div/div/div[1]/div[2]/div/div[1]/div/div[2]/div')
            for tr in table.find_elements(By.CSS_SELECTOR, 'div.kyber-table-body__row'):
                if tr.text == '': break
                index = [j for j,player in enumerate(curTeam.offensivePlayers) if player.name == weeklyNameOrder[i]][0]
                weekStats = OffPlayerStats(curTeam.offensivePlayers[index].name, curTeam.offensivePlayers[index].team)
                weekStats.week = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div[1]/div/div/div[1]/div[4]/div[1]/div[1]/button/span[2]').text

                k = 0
                for td in tr.find_elements(By.CSS_SELECTOR, 'div.kyber-table-body-cell'):
                    if i == len(weeklyNameOrder): break
                    tableDataText = td.text if td.text != '' else '0'

                    if k == 1: weekStats.position = tableDataText
                    elif k == 3: weekStats.teamAbrv = tableDataText
                    elif k == 6: weekStats.manTgts = float(tableDataText)
                    elif k == 7: weekStats.manRecs = float(tableDataText)
                    elif k == 9: weekStats.manYds = float(tableDataText)
                    elif k == 11: weekStats.manRecTDs = float(tableDataText)
                    elif k == 16: weekStats.manYdsPerRouteRun = float(tableDataText)
                    elif k == 29: weekStats.zoneTgts = float(tableDataText)
                    elif k == 30: weekStats.zoneRecs = float(tableDataText)
                    elif k == 32: weekStats.zoneYds = float(tableDataText)
                    elif k == 34: weekStats.zoneRecTDs = float(tableDataText)
                    elif k == 39: weekStats.zoneYdsPerRouteRun = float(tableDataText)

                    k += 1

                weekStats.manRoutesRun = round(divByZeroCheck(weekStats.manYds, weekStats.manYdsPerRouteRun))
                weekStats.manTgtsPerRouteRun = divByZeroCheck(weekStats.manTgts, weekStats.manRoutesRun)
                weekStats.manRecsPerRouteRun = divByZeroCheck(weekStats.manRecs, weekStats.manRoutesRun)
                weekStats.manYdsPerTarget = divByZeroCheck(weekStats.manYds, weekStats.manTgts)
                weekStats.manRecsPerTarget = divByZeroCheck(weekStats.manRecs, weekStats.manTgts)
                weekStats.zoneRoutesRun = round(divByZeroCheck(weekStats.zoneYds, weekStats.zoneYdsPerRouteRun))
                weekStats.zoneTgtsPerRouteRun = divByZeroCheck(weekStats.zoneTgts, weekStats.zoneRoutesRun)
                weekStats.zoneRecsPerRouteRun = divByZeroCheck(weekStats.zoneRecs, weekStats.zoneRoutesRun)
                weekStats.zoneYdsPerTarget = divByZeroCheck(weekStats.zoneYds, weekStats.zoneTgts)
                weekStats.zoneRecsPerTarget = divByZeroCheck(weekStats.zoneRecs, weekStats.zoneTgts)

                curTeam.offensivePlayers[index].weekByWeekStats.append(weekStats)
                curTeam.offensivePlayers[index].position = weekStats.position
                curTeam.offensivePlayers[index].teamAbrv = weekStats.teamAbrv
                curTeam.offensivePlayers[index].gamesPlayed2023 += curTeam.offensivePlayers[index].gamesPlayed2023
                
                i += 1

        except: continue

    nflTeamData = nflTeamsTable[curTeam.teamName]
    cloneTeam = curTeam.__dict__

    i = 0
    for player in curTeam.offensivePlayers:
        clonePlayer = player.__dict__
        clonePlayer["avgStats"] = player.avgStats.__dict__
        clonePlayer["totalStats"] = player.totalStats.__dict__

        k = 0
        for weekStats in player.weekByWeekStats:
            clonePlayer["weekByWeekStats"][k] = weekStats.__dict__
            k += 1

        cloneTeam["offensivePlayers"][i] = clonePlayer
        i += 1

    # nflTeamData.insert_one(cloneTeam)
    teams.append(curTeam)