import csv
from main import props


# load headers
def load(player):
    with open(player + '.csv', 'w', newline='') as file:  # rename to player
        writer = csv.writer(file)
        writer.writerow(
            ['DATE', 'OPP', 'W/L', 'MIN', 'PTS', 'FGM', 'FGA', 'FG%', '3PM', '3PA', '3P%', 'REB', 'AST', 'STL', 'BLK',
             'TOV'])

load('curry')
props('https://www.basketball-reference.com/players/c/curryst01/gamelog/2023', 'pgl_basic.858', 'curry')


