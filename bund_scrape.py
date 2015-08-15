from bs4 import BeautifulSoup
import requests
import csv

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

#table_headers = []
def get_scores():
    for tx in table.findAll('tr', {'class': "columns"}):
        table_headers = [th.text.strip().encode('utf-8') for th in tx.findAll('th') ] 

    with open('Bundesliga_Standings.csv', 'wb+') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames = table_headers, delimiter = ',')
        writer.writeheader()
        writer = csv.writer(csv_file)
        for trs in table.find_all('tr'):
            tds = trs.find_all('td')
            row = [elem.text.strip().encode('utf-8') for elem in tds]
            writer.writerow(row)

get_scores()



