##scrapes nba.com/stats

#import the libraries
from bs4 import BeautifulSoup
import requests
import numpy
import pyodbc
import pandas as pd
#from datetime import *
#from dateutil.relativedelta import *

nba_months = ['october', 'november', 'december', 'january', 'feburary', 'march', 'april', 'june']

nba_seasons = []
blank_months = []

for i in range(2000, 2020):
    nba_seasons.append(str(i))

for season in nba_seasons:
    for month in nba_months:
        #get_shedule('https://www.basketball-reference.com/leagues/NBA_',season,'_games-',month,'.html')
        url = ('https://www.basketball-reference.com/leagues/NBA_'+season+'_games-'+month+'.html')
        print(url)
        req = requests.get(url)
        html = req.text
        try:
            tables = pd.read_html(html)
            print(tables)
        except:
            blank_months.append(url)
            print('no tables found at ' + url)
for month in blank_months:
    print(month+'\n')

### proof that this works...
#url = 'https://www.basketball-reference.com/leagues/NBA_2018_games-october.html'
#req = requests.get(url)
#html = req.text
#tables = pd.read_html(html)
#print(tables)
### end proof

#https://www.basketball-reference.com/leagues/NBA_2018_games-october.html