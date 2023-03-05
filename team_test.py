import pandas as data
import os
from nba_api.stats.endpoints import commonallplayers

df = commonallplayers.CommonAllPlayers(is_only_current_season=0)

dd = df.get_data_frames()[0]


abbr = dd[['TEAM_ABBREVIATION']][dd['DISPLAY_FIRST_LAST'] == 'Jayson Tatum']

print(abbr)