setwd('/Users/patrick/Dropbox/Summer 2015/Bund_Scrape/')

week_1 <- read.csv('Bundesliga_Standings_Week_1.csv')

week_1 <- week_1[, colSums(is.na(week_1)) != nrow(week_1)]

week_1 <- subset(week_1, select = c('POS', 'TEAM', 'P', 'W', 'D', 'L', 'F', 'A'))

week_1$week <- 1