import api, testing

# Store player names to retrieve respective CSVs
# player_names = []

# Create function to load player_names with input
player_input = input("Enter player names to retrieve with full names separated by commas. \ne.g.: Anthony Edwards, LeBron James, Joel Embiid\n")
player_names = player_input.split(", ")
for name in player_names:
    api.player_game_log(name)

team_input = input("Enter team abbreviations to retrieve separated by commas. \ne.g.: BKN, ATL, TOR\n")
team_abbrs = team_input.split(", ")

for team in team_abbrs:
    api.team_game_log(team)










