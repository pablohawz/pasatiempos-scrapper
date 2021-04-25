import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
# driver = webdriver.Firefox()
# driver.get("http://refraneirogalego.com/")

# elem = driver.find_elements_by_class_name('entry-title')
# elem.clear()


# driver.close()


def get_refranes(verbose, slp_time):
    '''Gathers jobs as a dataframe, scraped from Glassdoor'''

    # Initializing the webdriver
    options = webdriver.FirefoxOptions()

    # Uncomment the line below if you'd like to scrape without a new Chrome window every time.
    options.add_argument('headless')

    # Change the path to where chromedriver is in your home folder.
    driver = webdriver.Firefox(options=options)
    driver.set_window_size(1120, 1000)

    refranes = []
    page = 1
    # If true, should be still looking for new jobs.
    while page < 19:

        url = f"http://refraneirogalego.com/page/{page}"
        driver.get(url)

        # Let the page load. Change this number based on your internet speed.
        # Or, wait until the webpage is loaded, instead of hardcoding it.
        time.sleep(slp_time)

        # Going through each job in this page
        try:
            bookmarks = driver.find_elements_by_xpath('.//a[@rel="bookmark"]')
        except NoSuchElementException:
            bookmarks = []

        for bookmark in bookmarks:
            if verbose:
                print("Refran: {}".format(bookmark.text))

            if bookmark.text != "":
                refranes.append({'Refran': bookmark.text})

        page += 1

    # This line converts the dictionary object into a pandas DataFrame.
    return pd.DataFrame(refranes)


df = get_refranes(True, 2)

df.to_csv('refranes.csv', index=False)
