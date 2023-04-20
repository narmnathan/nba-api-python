import api
import os
import pandas as data
import time
from variables import CSV

# dictionaries all other modules refer to

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
    time.sleep(.600)
    team_load(team)
    time.sleep(.600)
    CSV.prop['court'] = court
    opp_load(opp)
    time.sleep(.600)
    CSV.prop['num'] = prop_num
    CSV.prop['type'] = prop_type
    CSV.vars = player + team + court + opp + prop_num + prop_type


def run(user_input):
    # define variables from user input
    dict = user_input.split(" ")
    player = str(dict[0]) + " " + str(dict[1])
    team = dict[2]
    court = dict[3]
    opp = dict[4]
    prop_num = dict[5]
    prop_type = dict[6]
    load(player, team, court, opp, prop_num, prop_type)
    CSV.vars = dict
    print("Gamelogs successfully loaded")