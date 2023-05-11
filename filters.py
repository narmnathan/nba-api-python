from load import alt_load
import numpy as np
from manager import CSV, Filtered


class Logs:
    gamelog = CSV.gamelog['player']
    team_gamelog = CSV.gamelog['team']
    opp_gamelog = CSV.gamelog['opp']


Logs()
Filtered()


def court(type):
    if type == 'HOME':
        Filtered.player['court'] = Logs.gamelog[Logs.gamelog['MATCHUP'].str.contains('vs.')]
        # Filtered.team['court'] = Logs.team_gamelog[Logs.team_gamelog['MATCHUP'].str.contrains('vs.')]
    elif type == 'AWAY':
        Filtered.player['court'] = Logs.gamelog[Logs.gamelog['MATCHUP'].str.contains('@')]
        # Filtered.team['court'] = Logs.team_gamelog[Logs.team_gamelog['MATCHUP'].str.contrains('@')]



def opponent(opp):
    Filtered.player['against'] = Logs.gamelog[Logs.gamelog['MATCHUP'].str.contains(opp)]
    # Filtered.team['against'] = Logs.team_gamelog[Logs.team_gamelog['MATCHUP'].str.contains(opp)]



def last(games):
    Filtered.player['last'] = Logs.gamelog.loc[0:(games - 1)]
    # Filtered.team['last'] = Logs.team_gamelog.loc[0:(games - 1)]
    # Filtered.opp['last'] = Logs.opp_gamelog.loc[0:(games - 1)]


def minutes(num, type):
    if type == 'MIN':
        Filtered.player['minutes'] = Logs.gamelog[(Logs.gamelog['MIN'] > num)]
    elif type == 'MAX':
        Filtered.player['minutes'] = Logs.gamelog[(Logs.gamelog['MIN'] < num)]


def without(player):
    alt_load(player)
    alt_gamelog = CSV.gamelog['alt']
    dates = np.array(alt_gamelog['GAME_DATE'])
    Filtered.player['without'] = Logs.gamelog[~Logs.gamelog['GAME_DATE'].isin(dates)]
    # Filtered.team['without'] = Logs.team_gamelog[~Logs.team_gamelog['GAME_DATE'].isin(dates)]
