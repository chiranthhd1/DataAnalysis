txhou <- read.csv("G:/pdfs/EM622/class/class2/tx-house-sales.csv")
smallest_average_price = min(txhou$avgprice, na.rm=FALSE)
smallest_average_price
smallest_average_price = min(subset(txhou, select=avgprice))
smallest_average_price
all_attri = subset(txhou, avgprice == 26700)
head(all_attri)
avg_price2 = (subset(txhou, year >=2000 & year <=2002, select =c(avgprice) ))
head(avg_price2)
arr__avf_price2 = arrange(avg_price2,)
smallest_average_price = subset(txhou, is.na(avgprice)==FALSE)
