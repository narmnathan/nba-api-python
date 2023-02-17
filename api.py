from nba_api.stats.static import players
from nba_api.stats.endpoints import playergamelog
import os


# Find API player ID with full name.
def id_find(player_name):
    id = players.find_players_by_full_name(player_name)[0]['id']
    return id


def game_log(player_name):
    log = playergamelog.PlayerGameLog(player_id=id_find(player_name)).get_data_frames()[0]
    filename = player_name + '.csv'
    pathname = '~Desktop/sinix-model/' + filename
    check = os.path.isfile(pathname)
    while not check:
        log.to_csv(filename, index=False)
        return log



