setwd("~/Desktop/sinix-model/")
library(dplyr)
player_name <- NULL;
team_name <- NULL;
filename <- NULL;
team_filename <- NULL;
gamelog <- NULL;
team_gamelog <- NULL;
player_input <- NULL;
filter_input <- NULL;
###############################################################################

# SETUP
new_player <- function(player_input) {
  player_name <<- player_input
  filename <<- paste(player_name, ".csv", sep="")
  if (file.exists(filename) == FALSE) {
    print("File not found! Reload")
    run()
  } else {
    gamelog <<- read.csv(filename)
    return("Player successfully loaded")
  }
}
new_team <- function(team_input) {
  team_name <<- team_input
  team_filename <<- paste(team_name, ".csv", sep="")
  if (file.exists(filename) == FALSE) {
    print("File not found! Reload")
    run()
  } else {
    team_gamelog <<- read.csv(team_filename)
    return("Team successfully loaded")
  }
}
# FILTERS

# filter by home or away
filter_court <- function() {
  court <- readline(prompt="Enter filter [HOME/AWAY]: ")
  if (court == "HOME") {
    gamelog <<- filter(gamelog, grepl('vs.', MATCHUP))
    team_gamelog <<- filter(team_gamelog, grepl('vs.', MATCHUP))
  } else if (court == "AWAY") {
    gamelog <<- filter(gamelog, grepl('@', MATCHUP))
    team_gamelog <<- filter(team_gamelog, grepl('@', MATCHUP))
  }
  # return(gamelog)
}

filter_opponent <- function() {
  opponent <- readline(prompt="What opponent to filter? e.g. DAL, NYK, TOR: ")
  gamelog <<- filter(gamelog, grepl(opponent, MATCHUP))
  team_gamelog <<- filter(team_gamelog, grepl(opponent, MATCHUP))
  # return(gamelog)
}

# last games
filter_last <- function() {
  number <- readline(prompt="How many past games to filter? e.g. 5 for last 5 games: ")
  gamelog <<- gamelog[1:number, ]
  team_gamelog <<- team_gamelog[1:number, ]
  # return(gamelog)
}

filter_min <- function() {
  minmax <- readline(prompt="Filtering max/min minutes played? [MAX/MIN]: ")
  if (minmax == "MIN") {
    minimum <- readline(prompt="Minimum # of minutes played? ")
    gamelog <<- filter(gamelog, MIN > minimum)
    team_gamelog <<- filter(team_gamelog, MIN > minimum)
  } else if (minmax == "MAX") {
    maximum <- readline(prompt="Maximum # of minutes played? ")
    gamelog <<- filter(gamelog, MIN < maximum)
    team_gamelog <<- filter(team_gamelog, MIN < maximum)
  }
  # return(gamelog)
}

# resets gamelog without filters
reset <- function() {
  gamelog <<- read.csv(filename)  
  print("Gamelog reset.")
  team_gamelog <<- read.csv(team_filename)
  print("Team gamelog reset.")
  menu()
}

# RETRIEVALS
# averages are defined by filters -- use filters before running stat retrievals!

# gamelog
view_gamelog <- function() {
  print(gamelog)
}

# team gamelog
view_team_gamelog <- function () {
  print(team_gamelog)
}

#  name of player
player <- function() {
  player <- data.frame (
    NAME = c(player_name),
    TEAM = c(team_name)
  )
  print(player)
}

# averages of basic statistics found in gamelog
basic <- function() {
  min <- mean(gamelog$MIN) # avg min
  pts <- mean(gamelog$PTS) # avg pts
  reb <- mean(gamelog$REB) # avg reb
  ast <- mean(gamelog$AST) # avg ast
  stl <- mean(gamelog$STL) # avg stl
  blk <- mean(gamelog$BLK) # avg blk
  tov <- mean(gamelog$TOV) # avg tov
  pf <- mean(gamelog$PF) # avg player fouls
  basic <- data.frame (
    MIN = c(min),
    PTS = c(pts),
    REB = c(reb),
    AST = c(ast),
    STL = c(stl),
    BLK = c(blk),
    TOV = c(tov),
    PF = c(pf)
  )
  print(basic)
}

# advanced average statistics derived from player and team gamelogs
advanced <- function() {
  min <- mean(gamelog$MIN) # avg min
  pts <- mean(gamelog$PTS) # avg pts
  reb <- mean(gamelog$REB) # avg reb
  ast <- mean(gamelog$AST) # avg ast
  stl <- mean(gamelog$STL) # avg stl
  blk <- mean(gamelog$BLK) # avg blk
  tov <- mean(gamelog$TOV) # avg tov
  pf <- mean(gamelog$PF) # avg personal fouls
  fg <- mean(gamelog$FGM) # avg total fgs
  fg3m <- mean(gamelog$FG3M) # avg 3pm
  fga <- mean(gamelog$FGA) # avg fga
  fta <- mean(gamelog$FTA) # avg fta
  tm_min <- mean(team_gamelog$MIN) # team avg min
  tm_pts <- mean(team_gamelog$PTS) # team avg pts
  tm_reb <- mean(team_gamelog$REB) # team avg reb
  tm_ast <- mean(team_gamelog$AST) # team avg ast
  tm_stl <- mean(team_gamelog$STL) # team avg stl
  tm_blk <- mean(team_gamelog$BLK) # team avg blk
  tm_tov <- mean(team_gamelog$TOV) # team avg tov
  tm_pf <- mean(team_gamelog$PF) # team avg pf
  tm_fg <- mean(team_gamelog$FGM) # total team fgs
  tm_fga <- mean(team_gamelog$FGA) # total team fga
  tm_fta <- mean(team_gamelog$FTA) # total team fta
  ast_pct <- (100 * ast) / (((min / (tm_min / 5)) * tm_fg) - fg) # assist %
  ast_to_ratio <- ast/tov # ast/to ratio
  efg_pct <- ((fg + 0.5 * fg3m) / fga) # effective field goal %
  tsa <- (fga + (0.44 * fta)) # true shooting attempts
  tm_tsa <- (tm_fga + (0.44 * tm_fta))
  tov_pct <- (100 * tov) / (tsa + tov) # turnover %
  ts_pct <- (pts / (2 * tsa)) # true shooting %
  usg_pct <- (100 * (tsa + tov) * (tm_min / 5)) / (min * (tm_tsa + tm_tov))
  advanced <- data.frame (
    AST_PCT = c(ast_pct),
    AST_TO_RATIO = c(ast_to_ratio),
    eFG_PCT = c(efg_pct),
    TOV_PCT = c(tov_pct),
    TS_PCT = c(ts_pct),
    USG_PCT = c(usg_pct)
  )
  return(advanced)
}

# all rebound averages and ratio of offensive/defensive rebounds to total rebounds
reb_type <- function() {
  reb <- mean(gamelog$REB)
  oreb <- mean(gamelog$OREB)
  dreb <- mean(gamelog$DREB)
  oreb_ratio <- oreb/reb
  dreb_ratio <- dreb/reb
  reb_type <- data.frame (
    REB = c(reb),
    OREB = c(oreb),
    DREB = c(dreb),
    OREB_RATIO = c(oreb_ratio),
    DREB_RATIO = c(dreb_ratio)
  )
  print(reb_type)
}

# all field goal averages made and ratio of threes made to field goals made 
fg_type <- function() {
  fgm <- mean(gamelog$FGM)
  fga <- mean(gamelog$FGA)
  fg3m <- mean(gamelog$FG3M)
  fg3a <- mean(gamelog$FG3A)
  fg_pct <- mean(gamelog$FG_PCT)
  fg3_pct <- mean(gamelog$FG3_PCT)
  fg3_ratio <- fg3m/fgm
  ftm <- mean(gamelog$FTM)
  fta <- mean(gamelog$FTA)
  ft_pct <- mean(gamelog$FT_PCT)
  fg_type <- data.frame (
    FGM = c(fgm),
    FGA = c(fga),
    FG3M = c(fg3m),
    FG3A = c(fg3a),
    FG_PCT = c(fg_pct),
    FG3_PCT = c(fg3_pct),
    FG3_RATIO = c(fg3_ratio),
    FTM = c(ftm),
    FTA = c(fta),
    FT_PCT = c(ft_pct)
  )
  print(fg_type)
}
# RUN
run <- function() {
  welcome <- readline(prompt="Analyze new player? [Y/N]: ")
  if (welcome == "Y") {
    player_input <<- readline("Enter full name of player, e.g. Anthony Edwards, LeBron James, Anthony Davis: ")
    new_player(player_input)
    menu()
  } else {
    print("Key not recognized.")
    run()
  }
}

menu <- function() {
  input <- readline(prompt="Enter:
  [G] -- view gamelog
  [F] -- filters
  [A] -- analysis
  ")
  if (input == "G") {
    view_gamelog()
    menu()
  } else if (input == "F") {
    filter_menu()
  } else if (input == "A") {
    analysis()
    menu()
  } else {
    print("Key not recognized.")
    menu()
  }
}

analysis <- function() {
  avg_pra()
  avg_fg_type()
  avg_reb_type()
}

filter_menu <- function() {
  input <- readline(prompt="Enter:
  FILTERS:
  [C] -- filter by court
  [L] -- filter by last n games
  [O] -- filter by opponent
  [M] -- filter by minutes played
  [R] -- reset all filters
  ")
  if (input == "C") {
    filter_court()
    menu()
  } else if (input == "L") {
    filter_last()
    menu()
  } else if (input == "O") {
    filter_opponent()
    menu()
  } else if (input == "M") {
    filter_min()
    menu()
  } else if (input == "R") {
    reset()
    menu()
  } else {
    print("Key not recognized.")
    menu()
  }
}

###############################################################################
run()


