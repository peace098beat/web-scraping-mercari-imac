# docker run -d -p 4444:4444 -v /dev/shm:/dev/shm selenium/standalone-chrome:3.141.59-xenon

from selenium import webdriver
from selenium.webdriver.common.by import By

# x. Chrome の起動オプションを設定する
options = webdriver.ChromeOptions()
options.add_argument('--headless')

# x. ブラウザの新規ウィンドウを開く
print('connectiong to remote browser...')
driver = webdriver.Remote(
    command_executor='http://localhost:4444/wd/hub',
    desired_capabilities=options.to_capabilities(),
    options=options,
)

# 1. Qiita の Chanmoro のプロフィールページにアクセスする
driver.get('https://qiita.com/Chanmoro')
print(driver.current_url)
# > https://qiita.com/Chanmoro

# 2. 「最近の記事」に表示されている記事一覧の 2 ページ目に移動する
driver.find_element(By.XPATH, '//a[@rel="next" and text()="2"]').click()
print(driver.current_url)
# > https://qiita.com/Chanmoro?page=2

# 3. 2 ページ目の一番最初に表示されている記事のタイトルを URL を取得する
article_links = driver.find_elements(By.XPATH, '//div[@class="ItemLink__title"]/a')
print(article_links[0].text)
# > Python - 関数を文字列から動的に呼び出す
print(article_links[0].get_attribute('href'))
# > https://qiita.com/Chanmoro/items/9b0105e4c18bb76ed4e9

# x. ブラウザを終了する
driver.quit()