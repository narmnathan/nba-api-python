import pandas as data
import os, load

load = new_load.Load()


class Retrievals:
    # player stats
    min = load.gamelog['MIN'].mean()
    pts = load.gamelog['PTS'].mean()
    reb = load.gamelog['REB'].mean()
    oreb = load.gamelog['OREB'].mean()
    dreb = load.gamelog['DREB'].mean()
    oreb_ratio = oreb / reb
    dreb_ratio = dreb / reb
    ast = load.gamelog['AST'].mean()
    stl = load.gamelog['STL'].mean()
    blk = load.gamelog['BLK'].mean()
    tov = load.gamelog['TOV'].mean()
    pf = load.gamelog['PF'].mean()
    fgm = load.gamelog['FGM'].mean()
    fga = load.gamelog['FGA'].mean()
    fg3m = load.gamelog['FG3M'].mean()
    fg3a = load.gamelog['FG3A'].mean()
    fg_pct = load.gamelog['FG_PCT'].mean()
    fg3_pct = load.gamelog['FG3_PCT'].mean()
    fg3_ratio = fg3m / fgm
    ftm = load.gamelog['FTM'].mean()
    fta = load.gamelog['FTA'].mean()
    ft_pct = load.gamelog['FT_PCT'].mean()
    # team stats
    tm_min = load.team_gamelog['MIN'].mean()
    tm_pts = load.team_gamelog['PTS'].mean()
    tm_reb = load.team_gamelog['REB'].mean()
    tm_oreb = load.team_gamelog['OREB'].mean()
    tm_dreb = load.team_gamelog['DREB'].mean()
    tm_oreb_ratio = tm_oreb / tm_reb
    tm_dreb_ratio = tm_dreb / tm_reb
    tm_ast = load.team_gamelog['AST'].mean()
    tm_stl = load.team_gamelog['STL'].mean()
    tm_blk = load.team_gamelog['BLK'].mean()
    tm_tov = load.team_gamelog['TOV'].mean()
    tm_pf = load.team_gamelog['PF'].mean()
    tm_fgm = load.team_gamelog['FGM'].mean()
    tm_fga = load.team_gamelog['FGA'].mean()
    tm_fg3m = load.team_gamelog['FG3M'].mean()
    tm_fg3a = load.team_gamelog['FG3A'].mean()
    tm_fg_pct = load.team_gamelog['FG_PCT'].mean()
    tm_fg3_pct = load.team_gamelog['FG3_PCT'].mean()
    tm_fg3_ratio = tm_fg3m / tm_fgm
    tm_ftm = load.team_gamelog['FTM'].mean()
    tm_fta = load.team_gamelog['FTA'].mean()
    tm_ft_pct = load.team_gamelog['FT_PCT'].mean()
