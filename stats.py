import pandas as pd
from manager import CSV, Filtered


class Gamelogs:
    prop = CSV.prop


class Stats:
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


Stats()
Gamelogs()  # no way to simplify this ?


# problem: gamelog class doesn't adjust for filters. to adjust and show correct stats
# per filters: knowing gamelogs change per filter, need a method to change gamelog variables per filter.
# so last 10 games will change the gamelog assignment to Filtered.player['last'] instead of CSV.gamelog['player']

def change(param):
    match param:
        case "COURT":
            Stats.gamelog = Filtered.player['court']
        case "OPP":
            Stats.gamelog = Filtered.player['against']
        case "LAST":
            Stats.gamelog = Filtered.player['last']
        case "MIN":
            Stats.gamelog = Filtered.player['minutes']
        case "WITHOUT":
            Stats.gamelog = Filtered.player['without']


def basic():
    frame = {" ": [Stats.pts, Stats.reb, Stats.ast, Stats.blk, Stats.tov, Stats.pf]}
    index = ['PTS', 'REB', 'AST', 'BLK', 'TOV', 'PF']
    table = pd.DataFrame(frame, index=index)
    print(table)
    md = table.to_markdown()
    return md


def reb_type():
    frame = {" ": [Stats.reb, Stats.oreb, Stats.dreb, Stats.oreb_ratio, Stats.dreb_ratio]}
    index = ['REB', 'OREB', 'DREB', 'OREB_RATIO', 'DREB_RATIO']
    table = pd.DataFrame(frame, index=index)
    md = table.to_markdown()
    return md


def fg_type():
    frame = {" ": [Stats.fgm, Stats.fga, Stats.fg_pct,
                   Stats.fg3m, Stats.fg3a, Stats.fg3_pct, Stats.fg3_ratio,
                   Stats.ftm, Stats.fta, Stats.ft_pct]}
    index = ['FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FG3_RATIO', 'FTM', 'FTA', 'FT_PCT']
    table = pd.DataFrame(frame, index=index)
    md = table.to_markdown()
    return md


def tm_advanced():
    ast_pct = (100 * Stats.ast) / (((Stats.min / (Stats.tm_min / 5)) * Stats.tm_fgm) - Stats.fgm)
    ast_to_ratio = Stats.ast / Stats.tov
    efg_pct = ((Stats.fgm + 0.5 * Stats.fg3m) / Stats.fga)
    tsa = (Stats.fga + (0.44 * Stats.fta))
    tm_tsa = (Stats.tm_fga + (0.44 * Stats.tm_fta))
    tov_pct = (100 * Stats.tov) / (tsa + Stats.tov)
    ts_pct = (Stats.pts / (2 * tsa))
    usg_pct = (100 * (tsa + Stats.tov) * (Stats.tm_min / 5)) / (Stats.min * (tm_tsa + Stats.tm_tov))
    frame = {
        Gamelogs.prop['player'] + ": " + Gamelogs.prop['team']: [ast_pct, ast_to_ratio, efg_pct, tsa, tov_pct, ts_pct,
                                                                 usg_pct]}
    index = ['AST%', 'AST/TO', 'eFG%', 'TSA', 'TOV%', 'TS%', 'USG%']
    table = pd.DataFrame(frame, index=index)
    md = table.to_markdown()
    return md


def opp_advanced():
    tm_poss = 0.5 * ((Stats.tm_fga + 0.4 * Stats.tm_fta - 1.07 * (Stats.tm_oreb / (Stats.tm_oreb + Stats.opp_dreb)) * (
            Stats.tm_fga - Stats.tm_fgm) + Stats.tm_tov) + (Stats.opp_fga + 0.4 * (Stats.opp_fta) - 1.07 * (
            Stats.opp_oreb / (Stats.opp_oreb + Stats.tm_dreb) * (Stats.opp_fga - Stats.opp_fgm) + Stats.opp_tov)))
    opp_poss = 0.5 * ((Stats.opp_fga + 0.4 * Stats.opp_fta - 1.07 * (
            Stats.opp_oreb / (Stats.opp_oreb + Stats.tm_dreb)) * (
                               Stats.opp_fga - Stats.opp_fgm) + Stats.opp_tov) + (
                              Stats.tm_fga + 0.4 * (Stats.tm_fta) - 1.07 * (
                              Stats.tm_oreb / (Stats.tm_oreb + Stats.opp_dreb) * (
                              Stats.tm_fga - Stats.tm_fgm) + Stats.tm_tov)))
    oreb_pct = (100 * (Stats.oreb * (Stats.tm_min / 5))) / (Stats.min * (Stats.tm_oreb + Stats.opp_dreb))
    dreb_pct = (100 * (Stats.dreb * (Stats.tm_min / 5))) / (Stats.min * (Stats.tm_dreb + Stats.opp_oreb))
    blk_pct = (100 * ((Stats.blk) * (Stats.tm_min / 5))) / (Stats.tm_min * (Stats.opp_fga - Stats.opp_fg3a))
    stl_pct = (100 * (Stats.stl * (Stats.tm_min / 5))) / (Stats.min * opp_poss)
    frame = {
        Gamelogs.prop['player'] + ": " + Gamelogs.prop['team'] + " " + Gamelogs.prop['court'] + " " + Gamelogs.prop[
            'opp']: [oreb_pct, dreb_pct, blk_pct, stl_pct]}
    index = ['OREB%', 'DREB%', 'BLK%', 'STL%']
    table = pd.DataFrame(frame, index=index)
    md = table.to_markdown()
    return md
