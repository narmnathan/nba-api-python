import requests, csv
from bs4 import BeautifulSoup


# to-do: make regression equation with advanced metrics -- strength metric from -1 to 1
#        add FTM, FTA, FT%
def props(url, data_id):
    # calls dataset from url
    page = requests.get(url=url)
    soup = BeautifulSoup(page.content, "html.parser")
    # parses with BeautifulSoup
    gameLast = soup.find(id=data_id)
    # date
    date = gameLast.find('td', {'data-stat': 'date_game'})
    # print("DATE: " + date.text)
    # team
    team = gameLast.find('td', {'data-stat': 'team_id'})
    # print("TEAM: " + team.text)
    # opp
    opp = gameLast.find('td', {'data-stat': 'opp_id'})
    # print("OPP: " + opp.text)
    # mp -- minutes played
    minutes = gameLast.find('td', {'data-stat': 'mp'})
    # print("MIN: " + minutes.text)
    # w/l
    winloss = gameLast.find('td', {'data-stat': 'game_result'})
    # print(winloss.text)
    # fg/fga (fg%)
    fgm = gameLast.find('td', {'data-stat': 'fg'})
    fga = gameLast.find('td', {'data-stat': 'fga'})
    fgp = gameLast.find('td', {'data-stat': 'fg_pct'})
    # print("FGM/FGA: " + str(fgm.text) + "/" + str(fga.text) + " (" + str(fgp.text) + ")")
    # 3pm/3pa (3p%)
    tpm = gameLast.find('td', {'data-stat': 'fg3'})
    tpa = gameLast.find('td', {'data-stat': 'fg3a'})
    tpp = gameLast.find('td', {'data-stat': 'fg3_pct'})
    # print("3PM/3PA: " + str(tpm.text) + "/" + str(tpa.text) + " (" + str(tpp.text) + ")")
    # points
    points = gameLast.find('td', {'data-stat': 'pts'})
    # print("PTS: " + points.text)
    # assists
    assists = gameLast.find('td', {'data-stat': 'ast'})
    # print("AST: " + assists.text)
    # rebounds
    rebounds = gameLast.find('td', {'data-stat': 'trb'})
    # print("REB: " + rebounds.text)
    # steals
    steals = gameLast.find('td', {'data-stat': 'stl'})
    # print("STL: " + steals.text)
    # blocks
    blocks = gameLast.find('td', {'data-stat': 'blk'})
    # print("BLK: " + blocks.text)
    # turnovers
    tov = gameLast.find('td', {'data-stat': 'tov'})
    # print("TOV: " + tov.text)
    with open('players.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['DATE', 'OPP', 'W/L', 'MIN', 'PTS', 'FGM', 'FGA', 'FG%', '3PM', '3PA', '3P%', 'REB', 'AST', 'STL', 'BLK', 'TOV'])
        writer.writerow([date.text, opp.text, winloss.text, minutes.text, points.text, fgm.text, fga.text, fgp.text, tpm.text, tpa.text, tpp.text, rebounds.text, assists.text, steals.text, blocks.text, tov.text])



props('https://www.basketball-reference.com/players/j/jokicni01/gamelog/2023', 'pgl_basic.565')


# have to figure out a way to automate getting the url and getting the id
# might just make a script and manually do it for now

