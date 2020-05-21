from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import csv

driver = webdriver.Chrome()
url = "https://lolalytics.com/lol/tierlist/"

file = open("TierlistPatch10.10.csv", 'w')
writer = csv.writer(file)

driver.get(url)
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='root']/div[9]/div[2]")))

#List of attributes that are getting scrapped.
name=[]
winRate=[]
pickRate=[]

#write header rows
writer.writerow(['Champion Name', 'Win rate', 'Pick Rate'])

content = driver.page_source
soup = BeautifulSoup(content)

for row in soup.find('div', 'tierlist wrapper').find_all('div', recursive=False):
    columns = row.find_all('div')
    name = columns[3].text
    winRate = columns[8].text
    pickRate = columns[10].text

    print(f'{name} - {winRate} - {pickRate}')
    writer.writerow([name, winRate, pickRate])

driver.close()

