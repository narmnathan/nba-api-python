setwd("~/Desktop/sinix-model")
library(dplyr)
player_name = readline(prompt="Enter player name: ") # stores player name
filename <- paste(player_name, ".csv", sep="") # retrieves csv from working directory
gamelog <- read.csv(filename) # stores gamelog into R

# FILTER

# last games
filter_last <- function(number) {
  reset()
  gamelog <<- gamelog[1:number, ]
}

# resets gamelog to full size
reset <- function() {
  gamelog <- read.csv(filename)
}

# RETRIEVAL

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
avg_reb_pct <- function() {
  reb <- mean(gamelog$REB)
  oreb <- mean(gamelog$OREB)
  dreb <- mean(gamelog$DREB)
  oreb_pct <- oreb/reb
  dreb_pct <- dreb/reb
  avg_reb_pct <- data.frame (
    REB = c(reb),
    OREB_PCT = c(oreb_pct),
    DREB_PCT = c(dreb_pct)
  )
  return(avg_reb_pct)
}

# all field goal averages made and ratio of threes made to field goals made 
avg_fg_pct <- function() {
  fgm <- mean(gamelog$FGM)
  fga <- mean(gamelog$FGA)
  fg3m <- mean(gamelog$FG3M)
  fg3a <- mean(gamelog$FG3A)
  fg_pct <- mean(gamelog$FG_PCT)
  fg3_pct <- mean(gamelog$FG3_PCT)
  fg3_ratio <- fg3m/fgm 
  avg_fg_pct <- data.frame (
    FGM = c(fgm),
    FGA = c(fga),
    FG3M = c(fg3m),
    FG3A = c(fg3a),
    FG_PCT = c(fg_pct),
    FG3_PCT = c(fg3_pct),
    FG3_RATIO = c(fg3_ratio)
  )
  return(avg_fg_pct)
}

