movies <- read.csv("/media/chiranth/Documents/pdfs/EM622/class/class1/movies.csv")
library(ggplot2)

action_0_3 <- subset(movies, Action==1 & rating<=3, select=c(title))
action_rows <- nrow(action_0_3)

animation_0_3<-subset(movies, Animation==1 & rating<=3, select=c(title))
animation_rows <- nrow(animation_0_3)

comedy_0_3 <- subset(movies, Comedy==1&rating<=3, select=c(title))
comedy_rows <- nrow(comedy_0_3)

drama_0_3 <- subset(movies, Drama==1&rating<=3, select=c(title))
drama_rows <- nrow(drama_0_3)

documentary_0_3 <- subset(movies, Documentary==1&rating<=3, select=c(title))
documentary_rows <- nrow(documentary_0_3)

romance_0_3 <- subset(movies, Romance==1&rating<=3, select=c(title))
romance_rows <- nrow(romance_0_3)

short_0_3 <- subset(movies, Short==1&rating<=3, select=c(title))
short_rows <- nrow(short_0_3)

all_values_0_3 <- c(action_rows, animation_rows, comedy_rows, drama_rows, documentary_rows, romance_rows, short_rows)
all_values_0_3
names <- c("Action", "Animation", "Comedy", "Drama", "Documentary", "Romance", "Short")
graph <- data.frame(names, all_values_0_3)
graph


action_3_7 <- subset(movies, Action==1 & rating>3 & rating<=7, select=c(title))
action_rows1 <- nrow(action_3_7)

animation_3_7<-subset(movies, Animation==1 & rating>3 & rating<=7, select=c(title))
animation_rows1 <- nrow(animation_3_7)

comedy_3_7 <- subset(movies, Comedy==1&rating>3&rating<=7, select=c(title))
comedy_rows1 <- nrow(comedy_3_7)

drama_3_7 <- subset(movies, Drama==1&rating>3&rating<=7, select=c(title))
drama_rows1 <- nrow(drama_3_7)

documentary_3_7 <- subset(movies, Documentary==1&rating>3&rating<=7, select=c(title))
documentary_rows1 <- nrow(documentary_3_7)

romance_3_7 <- subset(movies, Romance==1&rating>3&rating<=7, select=c(title))
romance_rows1 <- nrow(romance_3_7)

short_3_7 <- subset(movies, Short==1&rating>3&rating<=7, select=c(title))
short_rows1 <- nrow(short_3_7)

all_values_3_7 <- c(action_rows1, animation_rows1, comedy_rows1, drama_rows1, documentary_rows1, romance_rows1, short_rows1)
all_values_3_7
graph1 <- data.frame(names, all_values_3_7)

action_7_10 <- subset(movies, Action==1 & rating>7 & rating<=10, select=c(title))
action_rows2 <- nrow(action_7_10)

animation_7_10<-subset(movies, Animation==1 & rating>7 & rating<=10, select=c(title))
animation_rows2 <- nrow(animation_7_10)

comedy_7_10 <- subset(movies, Comedy==1&rating>7&rating<=10, select=c(title))
comedy_rows2 <- nrow(comedy_7_10)

drama_7_10 <- subset(movies, Drama==1&rating>7&rating<=10, select=c(title))
drama_rows2 <- nrow(drama_7_10)

documentary_7_10 <- subset(movies, Documentary==1&rating>7&rating<=10, select=c(title))
documentary_rows2 <- nrow(documentary_7_10)

romance_7_10 <- subset(movies, Romance==1&rating>7&rating<=10, select=c(title))
romance_rows2 <- nrow(romance_7_10)

short_7_10 <- subset(movies, Short==1&rating>7&rating<=10, select=c(title))
short_rows2 <- nrow(short_7_10)

all_values_7_10 <- c(action_rows2, animation_rows2, comedy_rows2, drama_rows2, documentary_rows2, romance_rows2, short_rows2)
all_values_7_10
graph2 <- data.frame(names, all_values_3_7)

ggplot(data=graph) + geom_point(aes(x=names, y=all_values_0_3), size=5, colour="red") + geom_point(aes(x=names,y=all_values_3_7), size=5, colour="blue") + geom_point(aes(x=names,y=all_values_7_10), size=5, colour="green") + labs(title = "No of movies in a particular Genre in particular rating", x = "GENRE", y="No of Movies")
