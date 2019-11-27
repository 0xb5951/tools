import chromedriver_binary
from selenium import webdriver

import settings

# 設定値
LOGIN_URL = 'https://crowdworks.jp/login'
SCRAP_URL = 'https://crowdworks.jp/public/jobs/recommendations/recommend_for_you'

class ScrapeWithLogin():
    def __init__(self, url):
        self.email = settings.LOGIN_EMAIL
        self.password = settings.LOGIN_PASS
        self.url = url
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        self.driver = webdriver.Chrome(options=options)
    
    def login(self):
        driver = self.driver
        #Login window
        print("open login window...\n")
        driver.get(self.url)
        username_box = driver.find_element_by_id("username")
        username_box.send_keys(self.email)
        password_box = driver.find_element_by_id("password")
        password_box.send_keys(self.password)
        driver.find_element_by_name("commit").click()

        # ログインチェック
        if "https://crowdworks.jp/dashboard" not in driver.current_url:
            print("Login Fail")
            raise Exception('Error.')
        print('Login Succcess')
        return

    def scrap(self, url):
        driver = self.driver
        # 対象ページに移動
        driver.get(url)
        # 依頼の全体要素をリストに格納
        recommend_works = driver.find_elements_by_css_selector('li[data-job_offer_id]')
        print(recommend_works)
        return

if __name__ == '__main__':
    scrap = ScrapeWithLogin(LOGIN_URL)
    scrap.login()
    scrap.scrap(SCRAP_URL)
