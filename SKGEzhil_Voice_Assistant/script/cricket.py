import requests
from bs4 import BeautifulSoup

from SKGEzhil_Voice_Assistant.script.speech_engine import talk


def cricket_score():
    url = "https://www.cricbuzz.com/cricket-match/live-scores"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html5lib')
    table = soup.find('div', attrs={'id': 'page-wrapper'})
    team = table.find('a', attrs={'class': 'text-hvr-underline text-bold'})
    try:
        print((team.text.replace(',', '')).replace('vs', 'versus'))
        talk((team.text.replace(',', '')).replace('vs', 'versus'))
        team_1 = ((team.text.replace(',', '')).split('vs'))[0]
        team_2 = ((team.text.replace(',', '')).split('vs'))[1]
        print('Team 1: ' + team_1)
        print('Team 2:' + team_2)
        bat_team_select = table.find('div', attrs={'class': 'cb-text-live'})
        absolute_team_1 = team_1.replace(' ', '')
        absolute_team_2 = team_2.replace(' ', '')
        bat_area = table.find('div', attrs={'class': 'cb-hmscg-bat-txt'})
        bat_team = bat_area.find('div', attrs={'class': 'cb-ovr-flo cb-hmscg-tm-nm'})
        if absolute_team_1[0] == bat_team.text[0]:
            print(team_1 + ' is batting')
            batting_team = team_1
        elif 'RSA' in bat_team.text:
            print('South Africa is batting')
            batting_team = 'south africa'
        else:
            print(team_2 + ' is batting')
            batting_team = team_2
        talk(batting_team + ' is batting now')
        for score_1 in table.findAll('div', attrs={'class': 'cb-hmscg-bat-txt'}):
            score = score_1.find('div', attrs={'style': 'display:inline-block; width:140px'})
            real_score = score.text.replace('-', ' for ')
            print(real_score)
            if '(' not in real_score:
                talk(real_score + 'wickets')
            else:
                talk(real_score)
            break
    except Exception as e:
        print(e)
        print('No live matches now')
