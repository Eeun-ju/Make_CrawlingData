from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from urllib.request import urlopen
from bs4 import BeautifulSoup
import time 
import openpyxl

excel_file = openpyxl.Workbook()
excel_sheet = excel_file.active
excel_sheet.append(['공감수','댓글수','제목','내용','주소'])

driver = webdriver.Chrome('크롬드라이브 위치')

driver.get('https://ajou.everytime.kr/login')
driver.find_element_by_name('userid').send_keys('자신의 id')
driver.find_element_by_name('password').send_keys('자신의 비밀번')
driver.find_element_by_tag_name('input').send_keys(Keys.RETURN)

time.sleep(2)
driver.find_element_by_xpath('//*[@id="submenu"]/div/div[2]/ul/li[1]').click()

time.sleep(2)
driver.find_element_by_css_selector('#container > div.wrap.articles > div.pagination > a').click()
 
time.sleep(1)

def save_data():
    driver.find_element_by_css_selector('#container > div.wrap.articles > div.pagination > a.next').click()
    time.sleep(0.5)
    
    res = driver.page_source
    soup = BeautifulSoup(res,"html.parser")
    
    data_name = soup.select('#container > div.wrap.articles > article > a > h2')
    data_num = soup.select('.vote')
    data_comment = soup.select('.comment')
    data_text = soup.select('#container > div.wrap.articles > article > a > p')
    data_url = soup.select('#container > div.wrap.articles > article > a')

    
    for num,comment,name,text,url in zip(data_num,data_comment,data_name,data_text,data_url):
        excel_sheet.append([int(num.get_text()),int(comment.get_text()),name.get_text(),text.get_text(),'https://everytime.kr'+url.get('href')])       

      
driver.find_element_by_xpath('//*[@id="sheet"]/ul/li[3]/a').click()

 
time.sleep(0.5)
for i in range(3):
    save_data()


