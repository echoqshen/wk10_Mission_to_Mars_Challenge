from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
import datetime as dt
import requests
from webdriver_manager.chrome import ChromeDriverManager
import time

# executable_path = {'executable_path': ChromeDriverManager().install()}
# browser = Browser('chrome', **executable_path, headless=True)

### function which returns a dictionary of titles and URLS for images 

def hemisphere(browser):
     
     ### our webpage 
    hemisphere_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    ### visit the webpage with chrome 
    browser.visit(hemisphere_url)


    ## wait a bit . make sure the browser has retrieved the page
    time.sleep(2)

     ### create a data set ( a list ) to store the returned crap 
    imageURLS = []


    ### there are 4 images ( we know this !!! )
    for i in range(4):
        
        ### find all the links with enhanced in the text. ( could be doen outside loop )
        links_found = browser.links.find_by_partial_text('Enhanced')
        print(links_found)
        ## wait a bit 
        time.sleep(2)
        ### click on the link 
        links_found[i].click()

        #soup = soup(browser.html, 'html.parser')
        #title = (soup.find('title').text).replace(' Enhanced', '')
        ### find the title text 
        title = browser.find_by_css("h2.title").text
        print("title")
        print(title)

        #mydiv = soup.find("div", {"class": "downloads"})
        # #find the full image

        ## not used ?? 
        #html_soup = soup(browser.html, 'html.parser')
        #im = soup.find('a', text='Sample')
        # #get the images url
        #img_url = im['href']

        # find the link of the image 
        element = browser.links.find_by_text('Sample').first
        ## get the url of the link 
        img_url = element['href']
        
        ## put the img link and title for this moon into the result array/list
        # #make a dictionary and append to the list
        imageURLS.append({'title': title, 'img_url': img_url})

        #go back in the browser to check next moon 
        browser.back()
        #print("imgURLS")
        #print(imageURLS)
        ## return results back from our function 
    browser.quit()
    return(imageURLS)

    

### TEST OUR FUNCTION 
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)
print(hemisphere(browser))


##### SAMPLE RESULTS LIST :::: 


# [{'title': 'Cerberus Hemisphere Enhanced',
#  'img_url': 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg'},
#   {'title': 'Schiaparelli Hemisphere Enhanced',
#    'img_url': 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg'}, 
#    {'title': 'Syrtis Major Hemisphere Enhanced',
#     'img_url': 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg'},
#      {'title': 'Valles Marineris Hemisphere Enhanced', 'img_url':
#  'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg'}]