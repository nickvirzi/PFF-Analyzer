import time
from Team import Team
from OffPlayer import OffPlayer
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

weeks = []; teamsNumb = []
for i in range(1,17): weeks.append(i)
for i in range(1,32): teamsNumb.append(i)

driver.get('https://premium.pff.com/nfl/positions/2023/SINGLE/receiving-scheme?team=1&week=1')
driver.implicitly_wait(10)
driver.maximize_window()

driver.find_element(By.XPATH, '//*[@id="react-root"]/div/header/div[3]/button').click()
driver.implicitly_wait(10)
driver.find_element(By.XPATH, '//*[@id="login-form_email"]').send_keys('navirzi@gmail.com')
driver.find_element(By.XPATH, '//*[@id="login-form_password"]').send_keys('#Supreme2525')
driver.find_element(By.XPATH, '//*[@id="sign-in"]').click()
driver.implicitly_wait(10)

teams = []

for team in teamsNumb:
    if team != 1:
        driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div[1]/div/div/div[3]/div/div[1]/div[1]/button[1]/span[2]').click()
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div[1]/div/div/div[3]/div/div[1]/div[2]/div/div/div[2]/div[2]/div[1]/div/label[' + str(team) + ']').click()
        driver.implicitly_wait(10)

    curTeam = Team(driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div[1]/div/div/div[3]/div/div[1]/div[1]/button[1]/span[2]').text)

    for week in weeks: 
        if week != 1:
            driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div[1]/div/div/div[1]/div[4]/div[1]').click()
            driver.implicitly_wait(10)
            driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div[1]/div/div/div[1]/div[4]/div[1]/div[2]/div/div/div[2]/div/label[' + str(week) + ']').click()
            driver.implicitly_wait(10)

        table = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div[2]/div/div[3]/div/div/div[1]/div[2]/div/div[1]/div/div[1]/div')
        for tr in table.find_elements(By.CSS_SELECTOR, 'div.kyber-table-body__row'):
            for td in tr.find_elements(By.CSS_SELECTOR, 'div.kyber-table-body-cell--align-left'):
                if td.text == '': break

                playerName = td.text
                curPlayer = OffPlayer(playerName)
                curTeam.offensivePlayers.append(curPlayer)

        i = 0
        table = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div[2]/div/div[3]/div/div/div[1]/div[2]/div/div[1]/div/div[2]/div')
        for tr in table.find_elements(By.CSS_SELECTOR, 'div.kyber-table-body__row'):

            k = 0
            for td in tr.find_elements(By.CSS_SELECTOR, 'div.kyber-table-body-cell'):
                if k == 4: curTeam.offensivePlayers[i].tgts = td.text
                
                k += 1
            
            i += 1

        time.sleep(5)

    teams.append(curTeam)




driver.implicitly_wait(10)
time.sleep(20)