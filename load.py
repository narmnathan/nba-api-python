import pandas as data
import os, api

# define dictionaries to load gamelogs into and call from other modules
class CSV:
    gamelogs = {}
    prop = {}


CSV()

# load main player gamelog
def player_load(player):
    api.player_game_log(player)
    path = os.getcwd() + '/csv/players/' + player + '.csv'
    if os.path.exists(path):
        gamelog = data.read_csv(path)
        CSV.gamelogs['player'] = gamelog
    CSV.prop['player'] = player
    api.check_team(player)

# load alternate player gamelog
def alt_load(player):
    api.player_game_log(player)
    path = os.getcwd() + '/csv/players/' + player + '.csv'
    if os.path.exists(path):
        gamelog = data.read_csv(path)
        CSV.gamelogs['alt'] = gamelog
    CSV.prop['alt'] = player

# load opponent gamelog
def opp_load(opp):
    api.team_game_log(opp)
    path = os.getcwd() + '/csv/teams/' + opp + '.csv'
    if os.path.exists(path):
        opp_gamelog = data.read_csv(path)
        CSV.gamelogs['opp'] = opp_gamelog
    CSV.prop['opp'] = opp

# load team gamelog
def team_load(team):
    api.team_game_log(team)
    path = os.getcwd() + '/csv/teams/' + team + '.csv'
    if os.path.exists(path):
        team_gamelog = data.read_csv(path)
        CSV.gamelogs['team'] = team_gamelog
    CSV.prop['team'] = team

# full load function for gamelog and prop dictionaries
def load(player, team, court, opp, prop_num, prop_type):
    player_load(player)
    team_load(team)
    CSV.prop['court'] = court
    opp_load(opp)
    CSV.prop['num'] = prop_num
    CSV.prop['type'] = prop_type
    print(player + ', ' + team + ' ' + court + ' ' + opp + ', ' + prop_num + ' ' + prop_type + ': gamelogs loaded')


# load('Jayson Tatum', 'BOS', '@', 'CLE', '8.5', 'reb')


