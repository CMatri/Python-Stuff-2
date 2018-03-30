import requests
from bs4 import BeautifulSoup

page = requests.get('http://www.ncaa.com/rankings/basketball-men/d1/ncaa-mens-basketball-rpi')

if page.status_code != 200:
    print('Fatal error: Could not download rankings.')
    exit()

soup = BeautifulSoup(page.content, 'html.parser')
table = soup.find('table', { 'class' : 'ncaa-rankings-table' }).find_all('tr')

rankings = []

for t in table[1:]:
    entry = list(t.children)
    rankings.append([entry[2].text, int(entry[0].text)])

success = []
fail = []

for i, team in enumerate(rankings):
    stats_page = requests.get('http://warrennolan.com/basketball/2018/team-sheet?team=' + team[0])
    d = BeautifulSoup(stats_page.content, 'html.parser').find('div', { 'id' : 'page-menu-middle' })
    
    if list(list(d)[1].children)[1].text.replace(' ', '') == '':
        fail.append(team)
    else:
        success.append(team)
    
    if int(i / len(rankings) * 100.) % 10 == 0: print(str(i / len(rankings) * 100)[:3] + '%')
    if stats_page.status_code != 200:
        print(team[0] + ' grab failed: ' + str(stats_page.status_code))

print("Success: ")
print(success)

print('-------------------------------------------------')

print("Fail: ")
print(fail)