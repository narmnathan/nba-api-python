setwd("~/Desktop/sinix-model/")
library(dplyr)
player_name <- NULL;
filename <- NULL;
gamelog <- NULL;

# SETUP
new_player <- function() {
  name <- readline(prompt="Enter player name: ")
  player_name <<- name
  filename <<- paste(name, ".csv", sep="")
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
}

# RETRIEVALS

#  name of player
name <- function() {
  name <- data.frame (
    NAME = c(player_name)
  )
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
  return(avg_fg_type)
}

new_player()
name()
avg_pra()
avg_reb_type()
avg_fg_type()
