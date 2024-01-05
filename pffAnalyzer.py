from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://www.pff.com/')
driver.maximize_window()

driver.implicitly_wait(2)
driver.find_element(By.XPATH, '//*[@id="app"]/div[3]/div/nav/div[4]/div/a').click()

driver.implicitly_wait(2)
driver.find_element(By.XPATH, '//*[@id="login-form_email"]').send_keys('navirzi@gmail.com')
driver.find_element(By.XPATH, '//*[@id="login-form_password"]').send_keys('#Supreme2525')
driver.find_element(By.XPATH, '//*[@id="sign-in"]').click()

class Reciever:
    def __init__(self,name):
        self.name = name

    team = None
    manYrdsPerTgt = None
    manRecsPerTgt = None
    manTgtsPerGame = None
    zoneYrdsPerTgt = None
    zoneRecsPerTgt = None
    zoneTgtsPerGame = None
    
class Defense:
    def __init__(self,team):
        self.team = team

    manYrdsPerTgt = None
    manRecsPerTgt = None
    manTgtsPerGame = None
    manPercentage = None
    zoneYrdsPerTgt = None
    zoneRecsPerTgt = None
    zoneTgtsPerGame = None
    zonePercentage = None
    totYdsAllowed = None
    totTgtsAllowed = None

    players = []