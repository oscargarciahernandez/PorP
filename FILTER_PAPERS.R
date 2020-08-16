library(here)
library(stringr)
library(magrittr)
library(dplyr)

PAPERS_FOLDER<- '/home/ai5/shared_folder_virtualbox/perish/Nueva carpeta/'

PAPERS_DF<- PAPERS_FOLDER %>% list.files(full.names = TRUE) %>% 
  lapply(read.csv) %>% bind_rows()
GS<- PAPERS_DF %>% dplyr::filter(str_detect(Title, 'wind')) 
GS %>% write.csv('/home/ai5/GS_API/PAPERS_TO_DOWNLOAD.csv')
