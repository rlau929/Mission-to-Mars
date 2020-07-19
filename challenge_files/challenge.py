# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
import datetime as dt
def scrape_all():
    browser = Browser("chrome", executable_path="chromedriver", headless=True)

    # Run all scraping functions and store results in a dictionary
    data = {
        "che_image": cerberus_hemisphere_enhanced(browser),
        "she_image": schiaparelli_hemisphere_enhanced(browser),
        "smhe_image": syrtis_major_hemisphere_enhanced(browser),
        "vmhe_image": valles_marineris_hemisphere_enhanced(browser)
    }

    # Stop webdriver and return data
    browser.quit()
    return data
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
def cerberus_hemisphere_enhanced(browser):
    # Visit URL
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)
    img_url = f'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg'
    return img_url

#----------------------------------------------------------------------------------  
def schiaparelli_hemisphere_enhanced(browser):
    # Visit URL
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)
    img_url = f'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg'
    return img_url
#---------------------------------------------------------------------------------- 
def syrtis_major_hemisphere_enhanced(browser):
    # Visit URL
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)
    img_url = f'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg'
    return img_url
#---------------------------------------------------------------------------------- 
def valles_marineris_hemisphere_enhanced(browser):
    # Visit URL
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)
    img_url = f'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg'
    return img_url