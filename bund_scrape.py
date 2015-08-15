from bs4 import BeautifulSoup
import requests
import csv
import time 
from datetime import *


'''
German Results
http://www.espnfc.us/german-bundesliga/10/table
'''

#Top Day Get
# def get_data_bundesliga():
#     home = soup.find_all('td', class_='team-name-home')
#     away = soup.find_all('td', class_='team-name-away')
#     result = soup.find_all('td', class_='match-result')
#     with open('bundesliga_results_2015.csv', 'wb+') as csv_file:
#             writer = csv.writer(csv_file)
        
#             for year in years:
#                 for month in months:
#                     for crime in crimes[month+str(year)]:
#                         #print crime.toArray()
#                         writer.writerow(crime.toArray())
#     for value in zip(home, result, away):
#         print('Home: ' + value[0].string + ' ' + value[1].string + ' Away: ' + value[2].string)

url = 'http://www.espnfc.us/german-bundesliga/10/table'
    
r  = requests.get(url)

data = r.text

soup = BeautifulSoup(data, "html.parser")

table = soup.find('table')
week = 1
today = date.today()
timechange = timedelta(days=7)
print today
week2 = datetime.strptime('08/17/15', "%m/%d/%y")
week3 = week2 + timechange
week4 = week3 + timedelta(days=7)
week5 = week4 + timedelta(days=7)
week6 = week5 + timedelta(days=7)
week7 = week6 + timedelta(days=7)
week8 = week7 + timedelta(days=7)
week9 = week8 + timedelta(days=7)
week10 = week9 + timedelta(days=7)
week11 = week10 + timedelta(days=7)
week12 = week11 + timedelta(days=7)
week13 = week12 + timedelta(days=7)
week14 = week13 + timedelta(days=7)
week15 = week14 + timedelta(days=7)
week16 = week15 + timedelta(days=7)
week17 = week16 + timedelta(days=7)
week18 = week17 + timedelta(days=7)
week19 = week18 + timedelta(days=7)
week20 = week19 + timedelta(days=7)
week21 = week20 + timedelta(days=7)
week22 = week21 + timedelta(days=7)

week_list = [week2, week3,week4,week5,week6,week7,week8 ,week9,   week10,  week11,  week12,  week13,  week14,  week15,  week16,  week17,  week18,  week19,  week20, week21, week22] 
for x in week_list:
    print x 
    if today == week2.date():
        week += 1
    print week




filename = 'Bundesliga_Standings_Week_' + str(week) + '.csv'

#table_headers = []
def get_scores():
    for tx in table.findAll('tr', {'class': "columns"}):
        table_headers = [th.text.strip().encode('utf-8') for th in tx.findAll('th') ] 

    with open(filename, 'wb+') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames = table_headers, delimiter = ',')
        writer.writeheader()
        writer = csv.writer(csv_file)
        for trs in table.find_all('tr'):
            tds = trs.find_all('td')
            row = [elem.text.strip().encode('utf-8') for elem in tds]
            writer.writerow(row)

get_scores()



