import chromedriver_binary
from selenium import webdriver

import settings


class ScrapeLoginAuthSite():
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.url = "WEBSITE_URL"
        #chrome driver -headless mode
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        self.driver = webdriver.Chrome(options=options)
