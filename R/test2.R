avg_subset= subset(averages, select = c(date,children_average,adult_average,total_average))
View(avg_subset)
avg_plot <- ggplot(data=avg_subset)
avg_plot + geom_point( aes(x=date, y = children_average))
