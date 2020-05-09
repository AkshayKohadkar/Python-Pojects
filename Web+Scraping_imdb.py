#!/usr/bin/env python
# coding: utf-8

# # Web Scraping:
# 1. Import the libraries and classes:
#     - urllib request.
#     - BeautifulSoup.
# 2. Steps:
# 
# 
#     a. html upload.
#     b. html parser.
#     c. Extraction of data from web page.
#     d. Transformation into required file: csv.


# Import useful libraries and classes.
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

#html upload
my_url=  "https://www.imdb.com/list/ls020525837/"
uClient= uReq(my_url)
page_html= uClient.read()
uClient.close()

#html parser
page_soup= soup(page_html)
page_soup

#read class from web page.
containers= page_soup.findAll("div", {"class": "lister-item mode-detail"})
print(len(containers))



filename= "imdb_m.csv"
f= open(filename, "w")

headers= "Name; Year; Runtime \n"
f.write(headers)

for container in containers:
    name= container.img["alt"]
    year_mov= container.findAll("span", {"class": "lister-item-year"})
    year=str(year_mov[0].text)[1:-1]
    runtime_mov= container.findAll("span", {"class": "runtime"})
    runtime=runtime_mov[0].text
    
    print(name + ";" + year + ";" + runtime +  "\n")
    f.write(name + ";" + year + ";" + runtime  + "\n")
    

    
f.close()

