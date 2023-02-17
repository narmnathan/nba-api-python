anaylsis <- function(player_csv, name) {
    setwd("~/Desktop/sinix-model")
    player <- read.csv(player_csv)
    pts <- mean(player$PTS)
    rebs <- mean(player$REB)
    ast <- mean(player$AST)
    fgp <- mean(player$FGP)
    tpp <- mean(player$TPP)
    player_analysis <- data.frame(NAME = name,
                         PTS = c(pts),
                         REB = c(rebs),
                         AST = c(ast),
                         FGP = c(fgp),
                         TPP = c(tpp))
    

  print(player_analysis)
}   
anaylsis("curry.csv", "Stephen Curry")

