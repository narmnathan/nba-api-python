import pandas as data, numpy as np
import os, load

class Variables:
    gamelog = load.CSV.gamelogs['player']
    team_gamelog = load.CSV.gamelogs['team']
    # player stats.py
    min = gamelog['MIN'].mean()
    pts = gamelog['PTS'].mean()
    reb = gamelog['REB'].mean()
    oreb = gamelog['OREB'].mean()
    dreb = gamelog['DREB'].mean()
    oreb_ratio = oreb / reb
    dreb_ratio = dreb / reb
    ast = gamelog['AST'].mean()
    stl = gamelog['STL'].mean()
    blk = gamelog['BLK'].mean()
    tov = gamelog['TOV'].mean()
    pf = gamelog['PF'].mean()
    fgm = gamelog['FGM'].mean()
    fga = gamelog['FGA'].mean()
    fg3m = gamelog['FG3M'].mean()
    fg3a = gamelog['FG3A'].mean()
    fg_pct = gamelog['FG_PCT'].mean()
    fg3_pct = gamelog['FG3_PCT'].mean()
    fg3_ratio = fg3m / fgm
    ftm = gamelog['FTM'].mean()
    fta = gamelog['FTA'].mean()
    ft_pct = gamelog['FT_PCT'].mean()
    # team stats.py
    tm_min = team_gamelog['MIN'].mean()
    tm_pts = team_gamelog['PTS'].mean()
    tm_reb = team_gamelog['REB'].mean()
    tm_oreb = team_gamelog['OREB'].mean()
    tm_dreb = team_gamelog['DREB'].mean()
    tm_oreb_ratio = tm_oreb / tm_reb
    tm_dreb_ratio = tm_dreb / tm_reb
    tm_ast = team_gamelog['AST'].mean()
    tm_stl = team_gamelog['STL'].mean()
    tm_blk = team_gamelog['BLK'].mean()
    tm_tov = team_gamelog['TOV'].mean()
    tm_pf = team_gamelog['PF'].mean()
    tm_fgm = team_gamelog['FGM'].mean()
    tm_fga = team_gamelog['FGA'].mean()
    tm_fg3m = team_gamelog['FG3M'].mean()
    tm_fg3a = team_gamelog['FG3A'].mean()
    tm_fg_pct = team_gamelog['FG_PCT'].mean()
    tm_fg3_pct = team_gamelog['FG3_PCT'].mean()
    tm_fg3_ratio = tm_fg3m / tm_fgm
    tm_ftm = team_gamelog['FTM'].mean()
    tm_fta = team_gamelog['FTA'].mean()
    tm_ft_pct = team_gamelog['FT_PCT'].mean()

logs = Variables()


def court(type):
    if type == 'HOME':
        logs.gamelog = logs.gamelog[logs.gamelog['MATCHUP'].str.contains('vs.')]
    elif type == 'AWAY':
        logs.gamelog = logs.gamelog[logs.gamelog['MATCHUP'].str.contains('@')]


def opponent(opp):
    logs.gamelog = logs.gamelog[logs.gamelog['MATCHUP'].str.contains(opp)]


def last(games):
    logs.gamelog = logs.gamelog.loc[0:games]

def min(avg, type):
    if type == 'MIN':
       logs.gamelog = logs.gamelog[(logs.gamelog['MIN'] > avg)]
    elif type == 'MAX':
        logs.gamelog = logs.gamelog[(logs.gamelog['MIN'] < avg)]

def without(player):
    load.alt_load(player)
    alt_gamelog = load.CSV.gamelogs['alt']
    dates = np.array(alt_gamelog['GAME_DATE'])
    logs.gamelog = logs.gamelog[~logs.gamelog['GAME_DATE'].isin(dates)]

