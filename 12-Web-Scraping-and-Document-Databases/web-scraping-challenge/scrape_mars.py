# Definng Function Scrape


from splinter import Browser
from bs4 import BeautifulSoup as BS
import requests
import pandas as pd
from datetime import datetime


def scrape():

    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)

    # Scraping the latest headline fron Nasa Mars website

    url = 'https://mars.nasa.gov/news'
    browser.visit(url)
    html = browser.html

    soup = BS(html, 'html.parser')
    LatestResult = soup.find(class_="slide")

    headlines = [x.find('div', class_="content_title").text.strip()
                 for x in LatestResult]
    description = [x.find(
        'div', class_="rollover_description_inner").text.strip() for x in LatestResult]

    for x in headlines:
        headline = x
        print(headline)

    for x in description:
        description = x
        print(description)

    News = {"Headline": headline, "Description": description}
    print(News)

    # JPL Mars Space Images - Featured Image

    url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url)
    browser.find_by_id('full_image').click()
    featured_image_url = browser.find_by_css('.fancybox-image').first['src']
    featured_image_url

    # Obtaining the latest tweet

    url = "https://twitter.com/marswxreport?lang=en"
    browser.visit(url)
    html = browser.html
    soup = BS(html, 'html.parser')
    LatestTweet = soup.find(class_="js-tweet-text-container").text.strip()
    print(LatestTweet)

    # Mars Facts

    url = 'https://space-facts.com/mars/'
    tables = pd.read_html(url)
    MARS_PLANET_PROFILE = tables[0].copy()
    MARS_PLANET_PROFILE.to_html('MarsFact.html', header=None, index=False)

    # Mars Hemispheres

    url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url)
    html = browser.html
    soup = BS(html, 'html.parser')
    results = soup.find_all('div', class_="item")
    hemisphere_image_urls = []

    for x in results:
        link = x.a["href"]
        url = (f"https://astrogeology.usgs.gov{link}")
        browser.visit(url)
        html = browser.html
        soup = BS(html, 'html.parser')
        links = soup.find('img', class_="wide-image")["src"]
        Title = soup.find('h2')
        title = (Title.text)
        print(title)
        print(f"https://astrogeology.usgs.gov{links}")
        case = {"title": title, 'image_url': (
            f"https://astrogeology.usgs.gov{links}")}
        hemisphere_image_urls.append(case)

    Now = datetime.now()

    # one Python dictionary containing all of the scraped data
    data = {"LastUpdate": Now, "LatestNews": News, "Featured_Image": featured_image_url, "Weather": LatestTweet, "HemisphereImages": hemisphere_image_urls
            }

    print("******")
    print(f"Data Scraping Completed on {Now}")
    return data

    browser.quit()
