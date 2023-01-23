import requests, csv
from bs4 import BeautifulSoup


# to-do: make regression equation with advanced metrics -- strength metric from -1 to 1
#        add FTM, FTA, FT%
def props(url, data_id, player):
    # calls dataset from url
    page = requests.get(url=url)
    soup = BeautifulSoup(page.content, "html.parser")
    # parses with BeautifulSoup
    g_last = soup.find(id=data_id)
    # date
    g_date = g_last.find('td', {'data-stat': 'date_game'})
    date = g_date.text
    # print("DATE: " + date.text)
    # team
    g_team = g_last.find('td', {'data-stat': 'team_id'})
    team = g_team.text
    # print("TEAM: " + team.text)
    # opp
    g_opp = g_last.find('td', {'data-stat': 'opp_id'})
    opp = g_opp.text
    # print("OPP: " + opp.text)
    # mp -- minutes played
    g_minutes = g_last.find('td', {'data-stat': 'mp'})
    min = g_minutes.text
    # print("MIN: " + minutes.text)
    # w/l
    g_winloss = g_last.find('td', {'data-stat': 'game_result'})
    winloss = g_winloss.text
    # print(winloss.text)
    # fg/fga (fg%)
    g_fgm = g_last.find('td', {'data-stat': 'fg'})
    fgm = g_fgm.text
    g_fga = g_last.find('td', {'data-stat': 'fga'})
    fga = g_fga.text
    g_fgp = g_last.find('td', {'data-stat': 'fg_pct'})
    fgp = g_fgp.text
    # print("FGM/FGA: " + str(fgm.text) + "/" + str(fga.text) + " (" + str(fgp.text) + ")")
    # 3pm/3pa (3p%)
    g_tpm = g_last.find('td', {'data-stat': 'fg3'})
    tpm = g_tpm.text
    g_tpa = g_last.find('td', {'data-stat': 'fg3a'})
    tpa = g_tpa.text
    g_tpp = g_last.find('td', {'data-stat': 'fg3_pct'})
    tpp = g_tpp.text
    # print("3PM/3PA: " + str(tpm.text) + "/" + str(tpa.text) + " (" + str(tpp.text) + ")")
    # points
    g_points = g_last.find('td', {'data-stat': 'pts'})
    pts = g_points.text
    # print("PTS: " + points.text)
    # assists
    g_assists = g_last.find('td', {'data-stat': 'ast'})
    ast = g_assists.text
    # print("AST: " + assists.text)
    # rebounds
    g_rebounds = g_last.find('td', {'data-stat': 'trb'})
    reb = g_rebounds.text
    # print("REB: " + rebounds.text)
    # steals
    g_steals = g_last.find('td', {'data-stat': 'stl'})
    stl = g_steals.text
    # print("STL: " + steals.text)
    # blocks
    g_blocks = g_last.find('td', {'data-stat': 'blk'})
    blk = g_blocks.text
    # print("BLK: " + blocks.text)
    # turnovers
    g_tov = g_last.find('td', {'data-stat': 'tov'})
    tov = g_tov.text
    # print("TOV: " + tov.text)
    with open(player + '.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, opp, winloss, min, pts, fgm, fga, fgp, tpm, tpa, tpp, reb, ast, stl, blk, tov])

props('https://www.basketball-reference.com/players/j/jokicni01/gamelog/2023', 'pgl_basic.568', 'jokic')

# have to figure out a way to automate getting the url and getting the id
# might just make a script and manually do it for now
