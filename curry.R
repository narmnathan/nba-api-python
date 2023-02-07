setwd("~/Desktop/sinix-model")
curry <- read.csv("curry.csv")
print(curry)
pts_avg <- mean(curry$PTS)
reb_avg <- mean(curry$REB)
ast_avg <- mean(curry$AST)
fgp_avg <- mean(curry$FGP)
tpp_avg <- mean(curry$TPP)
print(pts_avg)
print(reb_avg)
print(ast_avg)
print(fgp_avg)
print(tpp_avg)
curry_anal <- data.frame(NAME = "Stephen Curry",
                         PTS = c(pts_avg),
                         REB = c(reb_avg),
                         AST = c(ast_avg),
                         FGP = (fgp_avg),
                         TPP = (tpp_avg))
print(curry_anal)
setwd("~/Desktop/")
write.csv(curry_anal, "~/Desktop/sinix-model/curry_anal.csv", row.names = FALSE)
