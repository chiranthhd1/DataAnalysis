library(ggplot2)
movies <- read.csv("/media/chiranth/Documents/pdfs/EM622/class/class1/movies.csv")
View(movies)
#movies <- ggplot(data=movies)
#the plot function has been saved to movies_plot
movies_plot <- ggplot(data=movies)
#plotting a point graph whith x and y axesa as year and animation columns respect 
movies_plot + geom_point( aes(x=year, y = Animation))
#taking a subset of the main dataset which has year greater than 2000 and selecting only the year and animation column

# #year = subset(movies, year >= 2000, select=c(year, Animation)) 
# #ggplot(data=year) + geom_point( aes(x=year, y = Animation))
# #ggplot(data=year) + geom_bar( aes(x=year, y = Animation))
# '''
# title_anim = subset(movies, year >= 2000, select=c(year, title, Animation)) 
# View(title_anim)
# ggplot(data=year) + geom_bar( aes(x=title, y = year))
# View(title_anim)
# require(reshape2)
# title_anim$id <- rownames(title_anim) 
# d = melt(title_anim)
# View(title_anim)
# ggplot(data=year) + geom_bar( aes(x=title, y = year))
# View(d)
# ggplot(data=d) + geom_point( aes(x = value, y=title))
# anim = subset(movies, Animation = 1 , select=c(title,year, rating)) 
# View(anim)
# ggplot(data=anim) + geom_line( aes(x=year, y = rating ))
# anim_2005 = subset(movies, year >= 2000 & Animation == 1 , select=c(title,year, rating))
# View(anim_2005)
# ggplot(data=anim_2005) + geom_point( aes(x=year, y = rating ))
# ction = subset(movies, year >= 2000 & Action == 1 & rating >= 7 , select=c(title,year, rating))
# ggplot(data=ction) + geom_point( aes(x=year, y = rating ))
comed = subset(movies,Comedy== 1 & rating >= 7 , select=c(title,year, rating))
#ggplot(data=comed) + geom_histogram( aes(x=year),binwidth=2) 

ggplot(data=comed) + geom_histogram( aes(x=year),binwidth=2,breaks=seq(1920,2005, by =2),col="red",fill="blue")
# #gets the movie with ratingf 1 and which is action,com and documentary at the same tym
# actn_com_docu_and = subset(movies, Comedy == 1 & Action == 1 & Documentary ==1 & rating >= 7 , select=c(title,year,rating,Action,Comedy,Documentary))
# View(actn_com_docu)
# #gets the movie with ratingf 1 and which is any of action,com or documentary
#actn_com_docu = subset(movies, (Comedy == 1 | Action == 1 | Documentary ==1) & rating >= 7 , select=c(title,year,rating,Action,Comedy,Documentary))
#View(actn_com_docu)
#ggplot(data=comed) + geom_histogram( aes(x=year),binwidth=2,breaks=seq(1920,2005, by =2),col="red",fill="blue")+facet_wrap(~)

#likewise cmedy doing for other animation
anima1 = subset(movies,Animation== 1 & rating >= 7 , select=c(title,year, rating))
ggplot(data=anima1) + geom_histogram( aes(x=year),binwidth=2,breaks=seq(1920,2005, by =2),col="red",fill="blue")
#for docum3ntary
docu1 = subset(movies,Documentary== 1 & rating >= 7 , select=c(title,year, rating))
ggplot(data=docu1) + geom_histogram( aes(x=year),binwidth=2,breaks=seq(1920,2005, by =2),col="red",fill="blue")
#for romance
roman = subset(movies,Romance== 1 & rating >= 7 , select=c(title,year, rating))
ggplot(data=roman) + geom_histogram( aes(x=year),binwidth=2,breaks=seq(1920,2005, by =2),col="red",fill="blue")
#to get the best shortest movies in Animation
Anima_shortest = subset(movies,Animation == 1 & rating >= 8 & length <= 90 & length >20 , select=c(title,year,rating,length))
#ggplot(data=Anima_shortest) + geom_histogram( aes(x=year),binwidth=2,breaks=seq(1920,2005, by =2),col="red",fill="blue")
View(Anima_shortest) 
ggplot(data=Anima_shortest) + geom_point( aes(x=year, y = title))

#to get the best animated movies after2000
Anima_best2000 = subset(movies,Animation == 1 & rating >= 9, select=c(title,year,rating))
View(Anima_best2000)
ggplot(data=Anima_best2000) + geom_point( aes(x=rating, y = title)) + geom_vline(xintercept = 9:10, colour="green", linetype = "longdash")
#best action,anim,com,docu movies before 1990
act_best1990 = subset(movies,Action == 1 & year <= 1990 & rating >= 9, select=c(title,rating))
anim_best1990 = subset(movies,Animation == 1 & year <= 1990 & rating >= 9, select=c(title,rating))
com_best1990 = subset(movies,Comedy == 1 & year <= 1960 & rating >= 9, select=c(title,rating))
doc_best1990 = subset(movies,Documentary == 1 & year <= 1980 & rating >= 9, select=c(title,rating))
View(anim_best1990)
View(com_best1990)
View(doc_best1990)
ggplot(data=act_best1990) + geom_point( aes(x=rating, y = title), colour = "blue", size = 4)
ggplot(data=anim_best1990) + geom_point( aes(x=rating, y = title), colour = "red", size = 4)
ggplot(data=com_best1990) + geom_point( aes(x=rating, y = title), colour = "magenta", size = 4)
ggplot(data=doc_best1990) + geom_point( aes(x=rating, y = title), colour = "black", size = 4)
#ggplot(data=act_best1990) + geom_point( aes(x=rating, y = title))+ggplot(data=anim_best1990) + geom_point( aes(x=rating, y = title))+ggplot(data=com_best1990) + geom_point( aes(x=rating, y = title))+ggplot(data=doc_best1990) + geom_point( aes(x=rating, y = title))
