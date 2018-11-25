# from urllib.request import urlopen
# from bs4 import BeautifulSoup
#
# html=urlopen('https://docs.python.org/3/library/urllib.request.html#module-urllib.request')
# bs_obj=BeautifulSoup(html.read(),'html.parser')
# text_list=bs_obj.find_all('a','reference internal')
# for text in text_list:
#     print(text.get_text())
#
# html.close()

#爬去网易云音乐播放量达到500万的歌单
from selenium import webdriver
import csv
# import sys
# import io
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')

url='https://music.163.com/#/discover/playlist'

driver=webdriver.PhantomJS()

csv_file=open('playlist.csv','w',newline='')
writer=csv.writer(csv_file)
writer.writerow(['标题','播放数','链接'])

while url !='javascript:void(0)':
    driver.get(url)
    driver.switch_to.frame('contentFrame')
    data=driver.find_element_by_id('m-pl-container').find_elements_by_tag_name('li')

    for i in range(len(data)):
        nb=data[i].find_element_by_class_name('nb').text
        if '万' in nb and int(nb.split('万')[0])>500:
            msk=data[i].find_element_by_css_selector('a.msk')

            writer.writerow([msk.get_attribute('title'), nb, msk.get_attribute('href')])

    url=driver.find_element_by_css_selector('a.zbtn.znxt').get_attribute('href')
csv_file.close()
