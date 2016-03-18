library(Quandl)
library(ggplot2)

stock_appl <- Quandl("GOOG/NASDAQ_APP",start_date="2015-01-01")[,c("Date","Close")]
data <- Quandl("LSE/SHRE", api_key="whoLQdbsSiGWzcY73hrB")
