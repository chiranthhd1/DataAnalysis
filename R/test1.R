library(dplyr)
DHS_Daily_Report <- read.csv("/media/chiranth/Documents/pdfs/EM622/class/HW2/DHS_Daily_Report.csv")
myfunc <- function(x,y){DHS_Daily_Report[DHS_Daily_Report$Date.of.Census >= x & DHS_Daily_Report$Date.of.Census <= y,]}

DATE1 <- as.Date("03/31/2016", format = "%m/%d/%y")
DATE2 <- as.Date("03/1/2016", format = "%m/%d/%y")

Test1 <- myfunc(DATE1,DATE2)   
