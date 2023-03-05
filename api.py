from nba_api.stats.static import players, teams
from nba_api.stats.endpoints import playergamelog, teamgamelog, commonallplayers
import os, pandas as data


# Find API player ID with full name.
def player_id_find(player_name):
    try:
        players.find_players_by_full_name(player_name)[0]['id']
    except:
        print("Player not found: " + player_name + "\n Please reload.")
    else:
        player_id = players.find_players_by_full_name(player_name)[0]['id']
        return player_id

def team_id_find(team_abbr):
    try:
        teams.find_team_by_abbreviation(team_abbr)['id']
    except:
        print("Team not found: " + team_abbr + "\n Please reload.")
    else:
        team_id = teams.find_team_by_abbreviation(team_abbr)['id']
        return team_id

def player_game_log(player_name):
    try:
        players.find_players_by_full_name(player_name)[0]['id']
    except:
        print("Player not found: " + player_name + "\nPlease retry.")
    else:
        player_log = playergamelog.PlayerGameLog(player_id=player_id_find(player_name)).get_data_frames()[0]
        filename = player_name + '.csv'
        pathname = '~/Desktop/sinix-model/csv/players/' + filename
        check = os.path.isfile(pathname)
        while not check:
            player_log.to_csv(pathname, index=False)
            # print("CSV load successful for " + player_name)
            return player_log


def team_game_log(team_abbr):
    try:
        teams.find_team_by_abbreviation(team_abbr)['id']
    except:
        print("Team not found: " + team_abbr + "\n Please reload.")
    else:
        team_log = teamgamelog.TeamGameLog(team_id=team_id_find(team_abbr)).get_data_frames()[0]
        filename = team_abbr + '.csv'
        pathname = '~/Desktop/sinix-model/csv/teams/' + filename
        check = os.path.isfile(pathname)
        while not check:
            team_log.to_csv(pathname, index=False)
            # print("CSV load successful for " + team_abbr)
            return team_log


def check_team(player_name):
    roster = commonallplayers.CommonAllPlayers(is_only_current_season=0)
    match = roster.get_data_frames()[0]
    team = data.Series(match[match['DISPLAY_FIRST_LAST'] == player_name]['TEAM_ABBREVIATION'])
    abbr = team.iloc[0]
    team_game_log(abbr)

