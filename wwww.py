from selenium import webdriver
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
import poplib
from email.parser import Parser
from pymongo import MongoClient

wd = webdriver.Chrome("/usr/local/bin/chromedriver")
wd.implicitly_wait(300)

wd.get('https://mbd.baidu.com/newspage/data/landingsuper?context=%7B%22nid%22%3A%22news_9698210431272618710%22%7D&n_type=0&p_from=1')

time.sleep(5)

#将滚动条移动到页面的底部
js="var q=document.documentElement.scrollTop=100000"
wd.execute_script(js)
time.sleep(3)