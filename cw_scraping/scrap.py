import re
import chromedriver_binary
from selenium import webdriver
from bs4 import BeautifulSoup

import datetime

import settings

# 設定値
LOGIN_URL = 'https://crowdworks.jp/login'
SCRAP_URL = 'https://crowdworks.jp/public/jobs/recommendations/recommend_for_you'

REC_CATE = 'システム開発'
REC_LEVEL = '普通'
REC_LEN = '普通'
REC_TYPE = '継続'

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
        # bs4に託す
        soup = BeautifulSoup(driver.page_source, "html.parser")
        # 依頼の全体要素をリストに格納
        recommend_works = soup.select('li[data-job_offer_id]')

        work_infos = []
        work_infos += 'id,title,category,price,post_num,deadline\n'

        for work in recommend_works:
            work_id = work['data-job_offer_id']
            work_a_links = work.find_all('a')
            work_bolds = work.find_all('b')

            work_title = work_a_links[0].text.strip()
            work_category = work_a_links[1].text.strip()

            work_price = re.sub(r'[ 　\t\n,]*','', work_bolds[0].text)
            work_post_num = work_bolds[1].text.strip()
            work_deadline = work_bolds[2].text.strip()

            # 情報を書き込み
            work_infos += '{0},{1},{2},{3},{4},{5}\n'.format(work_id, work_title, work_category, work_price, work_post_num, work_deadline)

        dt_now = datetime.datetime.now().strftime('%Y-%m-%d')
        csv_name = './scrap_data/{0}_{1}_{2}_{3}_{4}.csv'.format(REC_CATE, REC_LEVEL, REC_LEN, REC_TYPE, dt_now)
        with open(csv_name, 'w', encoding='utf-8') as f:
            f.write(''.join(work_infos))
        
        print('process complete!')
        return 0

if __name__ == '__main__':
    scrap = ScrapeWithLogin(LOGIN_URL)
    scrap.login()
    scrap.scrap(SCRAP_URL)
