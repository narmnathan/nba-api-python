import requests
from bs4 import BeautifulSoup


# to-do: make regression equation with advanced metrics -- strength metric from -1 to 1
def props(url, data_id):
    # calls dataset from url
    page = requests.get(url=url)
    soup = BeautifulSoup(page.content, "html.parser")
    # parses with BeautifulSoup
    gameLast = soup.find(id=data_id)
    # date
    date = gameLast.find('td', {'data-stat': 'date_game'})
    print("DATE: " + date.text)
    # team
    team = gameLast.find('td', {'data-stat': 'team_id'})
    print("TEAM: " + team.text)
    # opp
    opp = gameLast.find('td', {'data-stat': 'opp_id'})
    print("OPP: " + opp.text)
    # mp -- minutes played
    minutes = gameLast.find('td', {'data-stat': 'mp'})
    print("MIN: " + minutes.text)
    # w/l
    winloss = gameLast.find('td', {'data-stat': 'game_result'})
    print(winloss.text)
    # fg/fga (fg%)
    fg = gameLast.find('td', {'data-stat': 'fg'})
    fga = gameLast.find('td', {'data-stat': 'fga'})
    fgp = gameLast.find('td', {'data-stat': 'fg_pct'})
    print("FGM/FGA: " + str(fg.text) + "/" + str(fga.text) + " (" + str(fgp.text) + ")")
    # 3pm/3pa (3p%)
    tpm = gameLast.find('td', {'data-stat': 'fg3'})
    tpa = gameLast.find('td', {'data-stat': 'fg3a'})
    tpp = gameLast.find('td', {'data-stat': 'fg3_pct'})
    print("3PM/3PA: " + str(tpm.text) + "/" + str(tpa.text) + " (" + str(tpp.text) + ")")
    # points
    points = gameLast.find('td', {'data-stat': 'pts'})
    print("PTS: " + points.text)
    # assists
    assists = gameLast.find('td', {'data-stat': 'ast'})
    print("AST: " + assists.text)
    # rebounds
    rebounds = gameLast.find('td', {'data-stat': 'trb'})
    print("REB: " + rebounds.text)
    # steals
    steals = gameLast.find('td', {'data-stat': 'stl'})
    print("STL: " + steals.text)
    # blocks
    blocks = gameLast.find('td', {'data-stat': 'blk'})
    print("BLK: " + blocks.text)
    # turnovers
    tov = gameLast.find('td', {'data-stat': 'tov'})
    print("TOV: " + tov.text)


