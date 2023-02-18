from nba_api.stats.static import players
from nba_api.stats.endpoints import playergamelog
import os


# Find API player ID with full name.
def id_find(player_name):
    try:
        players.find_players_by_full_name(player_name)[0]['id']
    except:
        print("Player not found: " + player_name + "\n Please reload.")
    else:
        id = players.find_players_by_full_name(player_name)[0]['id']
        return id


def game_log(player_name):
    try:
        players.find_players_by_full_name(player_name)[0]['id']
    except:
        print("Player not found: " + player_name + "\nPlease retry.")
    else:
        log = playergamelog.PlayerGameLog(player_id=id_find(player_name)).get_data_frames()[0]
        filename = player_name + '.csv'
        pathname = '~Desktop/sinix-model/' + filename
        check = os.path.isfile(pathname)
        while not check:
            log.to_csv(filename, index=False)
            print("CSV load successful for " + player_name)
            return log



