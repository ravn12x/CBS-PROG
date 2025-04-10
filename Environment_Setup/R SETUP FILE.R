#this file contains all the basic commands for installing the necessary R packages-
#required by the Quantitative part of the QQM course

install.packages("tidyverse")
install.packages("rvest")
install.packages("bibliometrix")
install.packages("ggplot2")

#running the lines above should result in the full suite of necessarry packages being installed

library(bibliometrix)

biblioshiny()

#running the 2 lines above should allow you to start Bibliometrix on your localhost (it starts the program)