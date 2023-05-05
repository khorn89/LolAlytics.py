from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import csv

driver = webdriver.Chrome()
url = "https://lolalytics.com/lol/tierlist/"

file = open("TierlistPatch.csv", 'w')
writer = csv.writer(file)

driver.get(url)
local_class = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='root']/div[6]/div/div")))
element_class = local_class.get_attribute("class")

#List of attributes that are getting scrapped.
name=[]
winRate=[]
pickRate=[]

#write header rows
writer.writerow(['Champion Name', 'Win rate', 'Pick Rate'])

content = driver.page_source
soup = BeautifulSoup(content)

for row in soup.find('div', attrs={'class': element_class}).find_all('div', recursive=False):
    columns = row.find_all('div')
    name = columns[1].text
    winRate = columns[6].text
    pickRate = columns[3].text

    print(f'{name} - {winRate} - {pickRate}')
    writer.writerow([name, winRate, pickRate])

driver.close()
