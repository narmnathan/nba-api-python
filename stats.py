import pandas as data
import load, filters

class Gamelogs:
    prop = load.CSV.prop
    player = load.CSV.gamelogs['player']
    team = load.CSV.gamelogs['team']
    opp = load.CSV.gamelogs['opp']

stats = filters.Variables()
Gamelogs()

def gamelog(type):
    if type == 'PLAYER':
        print(Gamelogs.player)
    elif type == 'TEAM':
        print(Gamelogs.team)
    elif type == 'OPP':
        print(Gamelogs.opp)

def basic():
    frame = {Gamelogs.prop['player']: [stats.pts, stats.reb, stats.ast, stats.blk, stats.tov, stats.pf]}
    index = ['PTS', 'REB', 'AST', 'BLK', 'TOV', 'PF']
    table = data.DataFrame(frame, index=index)
    print(table)


def reb_type():
    frame = {Gamelogs.prop['player']: [stats.reb, stats.oreb, stats.dreb, stats.oreb_ratio, stats.dreb_ratio]}
    index = ['REB', 'OREB', 'DREB', 'OREB_RATIO', 'DREB_RATIO']
    table = data.DataFrame(frame, index=index)
    print(table)


def fg_type():
    frame = {Gamelogs.prop['player']: [stats.fgm, stats.fga, stats.fg_pct,
                                 stats.fg3m, stats.fg3a, stats.fg3_pct, stats.fg3_ratio,
                                 stats.ftm, stats.fta, stats.ft_pct]}
    index = ['FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FG3_RATIO', 'FTM', 'FTA', 'FT_PCT']
    table = data.DataFrame(frame, index=index)
    print(table)


def tm_advanced():
    ast_pct = (100 * stats.ast) / (((stats.min / (stats.tm_min / 5)) * stats.tm_fgm) - stats.fgm)
    ast_to_ratio = stats.ast / stats.tov
    efg_pct = ((stats.fgm + 0.5 * stats.fg3m) / stats.fga)
    tsa = (stats.fga + (0.44 * stats.fta))
    tm_tsa = (stats.tm_fga + (0.44 * stats.tm_fta))
    tov_pct = (100 * stats.tov) / (tsa + stats.tov)
    ts_pct = (stats.pts / (2 * tsa))
    usg_pct = (100 * (tsa + stats.tov) * (stats.tm_min / 5)) / (stats.min * (tm_tsa + stats.tm_tov))
    frame = {
        Gamelogs.prop['player'] + ": " + Gamelogs.prop['team']: [ast_pct, ast_to_ratio, efg_pct, tsa, tov_pct, ts_pct, usg_pct]}
    index = ['AST%', 'AST/TO', 'eFG%', 'TSA', 'TOV%', 'TS%', 'USG%']
    table = data.DataFrame(frame, index=index)
    print(table)

