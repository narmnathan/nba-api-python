import numpy as np
from load import CSV, alt_load


class Variables:
    gamelog = CSV.gamelogs['player']
    team_gamelog = CSV.gamelogs['team']
    opp_gamelog = CSV.gamelogs['opp']
    # player stats
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
    # team stats
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
    # opponent stats
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


def homecourt(type):
    if type == 'HOME':
        Variables.gamelog = Variables.gamelog[Variables.gamelog['MATCHUP'].str.contains('vs.')]
    elif type == 'AWAY':
        Variables.gamelog = Variables.gamelog[Variables.gamelog['MATCHUP'].str.contains('@')]


def opponent(opp):
    Variables.gamelog = Variables.gamelog[Variables.gamelog['MATCHUP'].str.contains(opp)]


def last(games):
    Variables.gamelog = Variables.gamelog.loc[0:games]


def min(avg, type):
    if type == 'MIN':
        Variables.gamelog = Variables.gamelog[(Variables.gamelog['MIN'] > avg)]
    elif type == 'MAX':
        Variables.gamelog = Variables.gamelog[(Variables.gamelog['MIN'] < avg)]


def without(player):
    alt_load(player)
    alt_gamelog = CSV.gamelogs['alt']
    dates = np.array(alt_gamelog['GAME_DATE'])
    Variables.gamelog = Variables.gamelog[~Variables.gamelog['GAME_DATE'].isin(dates)]
