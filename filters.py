import pandas as data
import vars, load

class Filters:
    load = new_load.Load()
    stats = vars.Retrievals()
    gamelog = load.gamelog
    team_gamelog = load.team_gamelog

    def __init__(self, team=None, opp=None, games=None, min=None):
        self.team = team
        self.opp = opp
        self.games = games
        self.min = min

    def court(team):
        if team == 'HOME':
            gamelog = data.gamelog.filter['MATCHUP'].str.match('vs.')
            team_gamelog = data.team_gamelog.filter['MATCHUP'].str.match('vs.')

        elif team == 'AWAY':
            gamelog = data.gamelog.filter['MATCHUP'].str.match('@')
            team_gamelog = data.team_gamelog.filter['MATCHUP'].str.match('@')



    def opponent(opp):
        gamelog = data.filter['MATCHUP'].str.match(opp)
        team_gamelog = data.filter['MATCHUP'].str.match(opp)


    #def last(games):


    #def min(min):

df = Filters(team='HOME', opp='LAC')

df.court()
df.opp()