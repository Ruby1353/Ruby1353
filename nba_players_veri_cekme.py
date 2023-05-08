import requests
import pandas as pd
from bs4 import BeautifulSoup

# Web sayfasından veri çekme
url = 'https://www.nba.com/players'
r = requests.get(url)

# BeautifulSoup kullanarak veri kazıma
soup = BeautifulSoup(r.content, 'html.parser')

# class="list-group" olan tüm <ul> elementlerini bulalım
list_groups = soup.find ('div', {'class': 'PlayerList_playerTable__Jno0k'})
list_rows = list_groups.find_all("tr")

data = []
for row in list_rows:
    data.append([td.get_text(strip=True) for td in row.find_all("td")])
    
df = pd.DataFrame(data, columns=["PLAYER","TEAM", "NUMBER", "POSITION", "HEIGHT", "WEIGHT", "LAST ATTENDED", "COUNTRY"])



    
