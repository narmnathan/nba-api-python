import pandas as data
import os, api

class CSV:
    gamelogs = {}
    prop = {}

CSV()


def player_load(player):
    try:
        api.player_game_log(player)
    except:
        print("Could not load!")  # update
    else:
        path = os.getcwd() + '/csv/players/' + player + '.csv'
        if os.path.exists(path):
            gamelog = data.read_csv(path)  # define this within class and update
            CSV.gamelogs['player'] = gamelog
        api.check_team(player)


def opp_load(opp):
    api.team_game_log(opp)
    path = os.getcwd() + '/csv/teams/' + opp + '.csv'
    if os.path.exists(path):
        opp_gamelog = data.read_csv(path)
        CSV.gamelogs['opp'] = opp_gamelog


def team_load(team):
    api.team_game_log(team)
    path = os.getcwd() + '/csv/teams/' + team + '.csv'
    if os.path.exists(path):
        team_gamelog = data.read_csv(path)
        CSV.gamelogs['team'] = team_gamelog


def load(player, team, court, opp, prop_num, prop_type):
    player_load(player)
    team_load(team)
    CSV.prop['court'] = court
    opp_load(opp)
    CSV.prop['num'] = prop_num
    CSV.prop['type'] = prop_type
    print(player + ', ' + team + ' ' + court + ' ' + opp + ', ' + prop_num + ' ' + prop_type + ': gamelogs loaded')


load('Jayson Tatum', 'BOS', '@', 'CLE', '8.5', 'reb')
# find a way to connect player to team -- maybe dict with all teams and rosters?

# load('Jayson Tatum', 'CLE', '8.5', 'reb')
# goal -- load function updates
