#coding=utf-8

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
wait = WebDriverWait(browser, 10)
def search():
    browser.get('https://www.zhihu.com')
    input = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#Popover1-toggle"))
    )
    submit = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#root > div > div:nth-child(2) > header > div.AppHeader-inner > div.SearchBar > div > form > div > div > div > div > button > span > svg"))
    )
    input.send_keys('留学生')
    submit.click()




def main():
    search()

if __name__=='__main__':
    main()






