from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
chrome_options = webdriver.ChromeOptions()
import requests

OS_USERNAME = 'joshu'
chrome_options = chrome_options.add_argument(
                f"--user-data-dir=C:\Program Files (x86)\Google\Chrome\Application")

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

valorant_page = "https://tracker.gg/valorant/profile/riot/Otto%230tto/matches"
page = driver.get(valorant_page)

outside_KDA_path = '//*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[3]/div[2]/div[2]/div/div[2]/div[1]/div[2]/div/div[2]/div[1]'

outside_KDA = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, outside_KDA_path))).text

print(outside_KDA)



#I think this is the path to the data element I want to extract
'''
> div.trn-wrapper 
> div.trn-container 
> div 
> main 
> div.content.no-card-margin 
> div.site-container.trn-grid.trn-grid--vertical.trn-grid--small 
> div.trn-grid__sidebar-left 
> div:nth-child(2) 
> div 
> div.trn-gamereport-list.trn-gamereport-list--compact 
> div:nth-child(1) 
> div.trn-gamereport-list__group-entries 
> div.vmr.trn-match-row.trn-match-row--outcome-loss.cursor-pointer 
> div.vmr-stats.trn-match-row__section.trn-match-row__section--right.gap-4 
> div.trn-match-row__block.min-w-24 
> div.trn-match-row__text-value
'''