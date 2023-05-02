from load import alt_load
import numpy as np
from manager import CSV, Filtered


class Variables:
    gamelog = CSV.gamelog['player']
    team_gamelog = CSV.gamelog['team']
    opp_gamelog = CSV.gamelog['opp']
    # Player stats
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
    # Team stats
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
    # Opponent stats
    opp_min = opp_gamelog['MIN'].mean()
    opp_pts = opp_gamelog['PTS'].mean()
    opp_reb = opp_gamelog['REB'].mean()
    opp_oreb = opp_gamelog['OREB'].mean()
    opp_dreb = opp_gamelog['DREB'].mean()
    opp_oreb_ratio = opp_oreb / opp_reb
    opp_dreb_ratio = opp_dreb / opp_reb
    opp_ast = opp_gamelog['AST'].mean()
    opp_stl = opp_gamelog['STL'].mean()
    opp_blk = opp_gamelog['BLK'].mean()
    opp_tov = opp_gamelog['TOV'].mean()
    opp_pf = opp_gamelog['PF'].mean()
    opp_fgm = opp_gamelog['FGM'].mean()
    opp_fga = opp_gamelog['FGA'].mean()
    opp_fg3m = opp_gamelog['FG3M'].mean()
    opp_fg3a = opp_gamelog['FG3A'].mean()
    opp_fg_pct = opp_gamelog['FG_PCT'].mean()
    opp_fg3_pct = opp_gamelog['FG3_PCT'].mean()
    opp_fg3_ratio = opp_fg3m / opp_fgm
    opp_ftm = opp_gamelog['FTM'].mean()
    opp_fta = opp_gamelog['FTA'].mean()
    opp_ft_pct = opp_gamelog['FT_PCT'].mean()


Variables()
Filtered()


def reset():
    Filtered.gamelog['player'] = Variables.gamelog
    Filtered.gamelog['team'] = Variables.team_gamelog
    Filtered.gamelog['opponent'] = Variables.opp_gamelog


def homecourt(type):
    if type == 'HOME':
        Filtered.gamelog['player'] = Variables.gamelog[Variables.gamelog['MATCHUP'].str.contains('vs.')]
    elif type == 'AWAY':
        Filtered.gamelog['player'] = Variables.gamelog[Variables.gamelog['MATCHUP'].str.contains('@')]


def opponent(opp):
    Filtered.gamelog['player'] = Variables.gamelog[Variables.gamelog['MATCHUP'].str.contains(opp)]


def last(games):
    Filtered.gamelog['player'] = Variables.gamelog.loc[0:(games - 1)]
    Filtered.gamelog['opponent'] = Variables.opp_gamelog.loc[0:(games - 1)]
    Filtered.gamelog['team'] = Variables.team_gamelog.loc[0:(games - 1)]


def minutes(num, type):
    if type == 'MIN':
        Filtered.gamelog['player'] = Variables.gamelog[(Variables.gamelog['MIN'] > num)]
    elif type == 'MAX':
        Filtered.gamelog['player'] = Variables.gamelog[(Variables.gamelog['MIN'] < num)]


def without(player):
    alt_load(player)
    alt_gamelog = CSV.gamelog['alt']
    dates = np.array(alt_gamelog['GAME_DATE'])
    Filtered.gamelog['player'] = Variables.gamelog[~Variables.gamelog['GAME_DATE'].isin(dates)]

