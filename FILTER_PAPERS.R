library(here)
library(stringr)
library(magrittr)
library(dplyr)

PAPERS_FOLDER<-list.dirs(here::here('perish_search/'),full.names = TRUE) %>% 
  .[str_detect(., 'SAVONIUS')]

PAPERS_DF<- PAPERS_FOLDER %>% list.files(full.names = TRUE) %>% 
  lapply(read.csv) %>% bind_rows()


GS<- PAPERS_DF %>% dplyr::filter(str_detect(Title, 'wind')) 


GS %>% write.csv('PAPERS_TO_DOWNLOAD.csv')

Sys.setenv(RETICULATE_PYTHON="/home/ai5/anaconda3/bin/python")
library(reticulate)
reticulate::py_config()
system(paste('python SELENIUM_SCRAP.py', PAPERS_FOLDER))

#reticulate::source_python('SELENIUM_SCRAP.py')
