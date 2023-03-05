import pandas as data
import os
class Load:
    # load gamelogs for player, team, and opponent
    player_name = input("Enter player name: \n")
    player_path = os.getcwd() + '/csv/players/' + player_name + '.csv'
    if os.path.exists(player_path):
        gamelog = data.read_csv(player_path)
    else:
        print("Player not found! Reload")
    team_abbr = input("Enter team abbreviation: \n")
    team_path = os.getcwd() + '/csv/teams/' + team_abbr + '.csv'
    if os.path.exists(player_path):
        team_gamelog = data.read_csv(team_path)
    else:
        print("Team not found! Reload")

    # filter gamelogs


