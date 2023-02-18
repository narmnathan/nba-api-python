import api

# Store player names to retrieve respective CSVs
# player_names = []

# Create function to load player_names with input
input = input("Enter player names to retrieve with full names separated by commas. \ne.g.: Anthony Edwards, LeBron James, Joel Embiid\n")
player_names = input.split(", ")
# load = input("Enter desired player full names (followed by enter), then type 'load' to load CSVs.\n")
for name in player_names:
    api.game_log(name)








