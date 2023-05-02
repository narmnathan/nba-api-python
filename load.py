import api
import os
import pandas as data
import time
from manager import CSV

CSV()


# Load player gamelog
def player_load(player):
    api.player_game_log(player)
    path = os.getcwd() + '/csv/players/' + player + '.csv'
    if os.path.exists(path):
        gamelog = data.read_csv(path)
        CSV.gamelog['player'] = gamelog
    CSV.prop['player'] = player
    api.check_team(player)


# Load alternate player gamelog (for injury filter)
def alt_load(player):
    api.player_game_log(player)
    path = os.getcwd() + '/csv/players/' + player + '.csv'
    if os.path.exists(path):
        gamelog = data.read_csv(path)
        CSV.gamelog['alt'] = gamelog
    CSV.prop['alt'] = player


# Load opposing team gamelog
def opp_load(opp):
    api.team_game_log(opp)
    path = os.getcwd() + '/csv/teams/' + opp + '.csv'
    if os.path.exists(path):
        opp_gamelog = data.read_csv(path)
        CSV.gamelog['opp'] = opp_gamelog
    CSV.prop['opp'] = opp


# Load team gamelog
def team_load(team):
    api.team_game_log(team)
    path = os.getcwd() + '/csv/teams/' + team + '.csv'
    if os.path.exists(path):
        team_gamelog = data.read_csv(path)
        CSV.gamelog['team'] = team_gamelog
    CSV.prop['team'] = team


# Main load function
def load(player, team, court, opp, prop_num, prop_type):
    player_load(player)
    time.sleep(.600)
    team_load(team)
    time.sleep(.600)
    CSV.prop['court'] = court
    opp_load(opp)
    time.sleep(.600)
    CSV.prop['num'] = prop_num
    CSV.prop['type'] = prop_type


def run(user_input):
    # define variables from user input
    input = user_input.split(" ")
    player = str(input[0]) + " " + str(input[1])
    team = input[2]
    court = input[3]
    opp = input[4]
    prop_num = input[5]
    prop_type = input[6]
    load(player, team, court, opp, prop_num, prop_type)
    print("Gamelogs successfully loaded for " + player)

# run('Jalen Brunson NYK @ CLE 22.5 PTS')