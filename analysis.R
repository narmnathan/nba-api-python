setwd("~/sinix-model/")
library(dplyr)
player_name <- NULL;
filename <- NULL;
gamelog <- NULL;
player_input <- NULL;
filter_input <- NULL;
###############################################################################

# SETUP
new_player <- function(player_input) {
  # name <- readline(prompt="Enter player name: ")
  player_name <<- player_input
  filename <<- paste(player_name, ".csv", sep="")
  if (file.exists(filename) == FALSE) {
    print("File not found! Reload")
  } else {
    gamelog <<- read.csv(filename)
    return("Successfully loaded")
  }
}
# FILTERS

# filter by home or away
filter_court <- function() {
  court <- readline(prompt="Enter filter [HOME/AWAY]: ")
  if (court == "HOME") {
    gamelog <<- filter(gamelog, grepl('vs.', MATCHUP))
  } else if (court == "AWAY") {
    gamelog <<- filter(gamelog, grepl('@', MATCHUP))
  }
  return(gamelog)
}

filter_opponent <- function() {
  opponent <- readline(prompt="What opponent to filter? e.g. DAL, NYK, TOR: ")
  gamelog <<- filter(gamelog, grepl(opponent, MATCHUP))
  return(gamelog)
}

# last games
filter_last <- function() {
  number <- readline(prompt="How many past games to filter? e.g. 5 for last 5 games: ")
  gamelog <<- gamelog[1:number, ]
  return(gamelog)
}

filter_min <- function() {
  minmax <- readline(prompt="Filtering max/min minutes played? [MAX/MIN]: ")
  if (minmax == "MIN") {
    minimum <- readline(prompt="Minimum # of minutes played? ")
    gamelog <<- filter(gamelog, MIN > minimum)
  } else if (minmax == "MAX") {
    maximum <- readline(prompt="Maximum # of minutes played? ")
    gamelog <<- filter(gamelog, MIN < maximum)
  }
  return(gamelog)
}

# resets gamelog without filters
reset <- function() {
  gamelog <<- read.csv(filename)
  print("Gamelog reset.")
  menu()
}

# RETRIEVALS

# gamelog
view_gamelog <- function() {
  print(gamelog)
}

#  name of player
name <- function() {
  name <- data.frame (
    NAME = c(player_name)
  )
  print(name)
  return(name)
}

# averages of points, rebounds, assists
avg_pra <- function() {
  pts <- mean(gamelog$PTS)
  reb <- mean(gamelog$REB)
  ast <- mean(gamelog$AST)
  avg_pra <- data.frame (
    PTS = c(pts),
    REB = c(reb),
    AST = c(ast)
  )
  print(avg_pra)
  return(avg_pra)
}

# all rebound averages and ratio of offensive/defensive rebounds to total rebounds
avg_reb_type <- function() {
  reb <- mean(gamelog$REB)
  oreb <- mean(gamelog$OREB)
  dreb <- mean(gamelog$DREB)
  oreb_pct <- oreb/reb
  dreb_pct <- dreb/reb
  avg_reb_type <- data.frame (
    REB = c(reb),
    OREB_PCT = c(oreb_pct),
    DREB_PCT = c(dreb_pct)
  )
  print(avg_reb_type)
  return(avg_reb_type)
}

# all field goal averages made and ratio of threes made to field goals made 
avg_fg_type <- function() {
  fgm <- mean(gamelog$FGM)
  fga <- mean(gamelog$FGA)
  fg3m <- mean(gamelog$FG3M)
  fg3a <- mean(gamelog$FG3A)
  fg_pct <- mean(gamelog$FG_PCT)
  fg3_pct <- mean(gamelog$FG3_PCT)
  fg3_ratio <- fg3m/fgm 
  avg_fg_type <- data.frame (
    FGM = c(fgm),
    FGA = c(fga),
    FG3M = c(fg3m),
    FG3A = c(fg3a),
    FG_PCT = c(fg_pct),
    FG3_PCT = c(fg3_pct),
    FG3_RATIO = c(fg3_ratio)
  )
  print(avg_fg_type)
  return(avg_fg_type)
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
    analysis_menu()
  } else {
    print("Key not recognized.")
    menu()
  }
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
analysis_menu <- function() {
  input <- readline(prompt="Enter:
  AVERAGES:
  [P] -- pts/reb/ast
  [F] -- field goal types and percentages
  [R] -- rebound types and percentages
  ")
  if (input == "P") {
    avg_pra()
    menu()
  } else if (input == "F") {
    avg_fg_type()
    menu()
  } else if (input == "R") {
    avg_reb_type()
    menu()
  } else {
    print("Key not recognized.")
    menu()
  }
}

###############################################################################
run()


