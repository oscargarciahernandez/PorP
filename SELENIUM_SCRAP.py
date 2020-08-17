#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 23:41:14 2020

@author: ai5
"""


import requests
import re
import pandas as pd
import os
import datetime as dt
import numpy as np
import sys



def CREAR_SELENIUM_DRIVER(PATH_DOWNLOAD= os.getcwd()):
       '''
       JODER, NO SE COMO COJONES LO TIENE HECHO PARA ME HAN JODIDO, SOLAMENTE
       SE ME OCURRE USAR SELINUM PARA ESTA MIERDA DE PAGINA WEB... OTRA DE LAS 
       OPCIONES ES USAR SU REST-API EN UN FUTURO, PERO SOLAMENTE DAN ACCESO AL 
       ULTIMO DATO
       
       BLESS
       '''
       if not os.path.exists(PATH_DOWNLOAD):
           os.mkdir(PATH_DOWNLOAD)
       from selenium import webdriver
       
       
       #PARAMETROS FIREFOX
       profile = webdriver.FirefoxProfile()
       profile.set_preference('browser.download.folderList', 2) # custom location
       profile.set_preference('browser.download.manager.showWhenStarting', False)
       profile.set_preference('browser.download.dir', PATH_DOWNLOAD)
       profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'application/pdf')
       profile.set_preference( "pdfjs.disabled", True )
       
       DRIVER=webdriver.Firefox(profile, executable_path='geckodriver')
       return(DRIVER)


PAPERS= pd.read_csv('PAPERS_TO_DOWNLOAD.csv')
PATH_TO_DOWNLOAD= sys.argv[1]


DRIVER= CREAR_SELENIUM_DRIVER(PATH_DOWNLOAD=PATH_TO_DOWNLOAD)
for i in np.arange(0,len(PAPERS['Title'])):

    DRIVER.get('https://sci-hub.tw/')
    DRIVER.find_element_by_css_selector("#input > form:nth-child(1) > input:nth-child(2)").send_keys(PAPERS['Title'][i]) # PULSO EL BOTOM MONTH
    DRIVER.find_element_by_css_selector("#open").click() # PULSO EL BOTOM MONTH
    #DRIVER.find_element_by_css_selector("#buttons > ul:nth-child(1) > li:nth-child(1) > a:nth-child(1)").click()

while True:
    DOWNLOADED_FILES= [item for item in os.listdir(PATH_TO_DOWNLOAD) if '.part' in item]
    if len(DOWNLOADED_FILES)==0:
        break
        
DRIVER.close()                              

