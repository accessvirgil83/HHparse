# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 00:49:53 2023

@author: rs
"""

import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import time
import base64
from selenium.webdriver.common.keys import Keys
import pandas as pd

x='<your password>'
driver = uc.Chrome()
url='https://spb.hh.ru/account/login?backurl=%2Fsearch%2Fresume%3Ftext%3D%25D0%25B2%25D0%25BE%25D0%25B4%25D0%25B8%25D1%2582%25D0%25B5%25D0%25BB%25D1%258C%2B%25D1%2581%2B%25D0%25BB%25D0%25B8%25D1%2587%25D0%25BD%25D1%258B%25D0%25BC%2B%25D0%25B0%25D0%25B2%25D1%2582%25D0%25BE%25D0%25BC%25D0%25BE%25D0%25B1%25D0%25B8%25D0%25BB%25D0%25B5%25D0%25BC&hhtmFrom=resume_search_result'
driver.get(url)
driver.find_element(By.XPATH,"//a[contains(@title, 'Мой Мир@mail.ru')]").click()
driver.find_element(By.XPATH,"//input[contains(@id, 'login')]").send_keys("rs-allection@mail.ru")
driver.find_element(By.XPATH,"//input[contains(@id, 'password')]").send_keys(x)
driver.find_element(By.XPATH,"//input[contains(@id, 'password')]").send_keys(Keys.ENTER)
url='https://spb.hh.ru/search/resume?area=1&area=232&area=2019&exp_period=all_time&items_on_page=100&logic=normal&no_magic=true&order_by=relevance&ored_clusters=true&pos=full_text&text=%D0%92%D0%BE%D0%B4%D0%B8%D1%82%D0%B5%D0%BB%D1%8C+%D1%81+%D0%BB%D0%B8%D1%87%D0%BD%D1%8B%D0%BC+%D0%B0%D0%B2%D1%82%D0%BE%D0%BC%D0%BE%D0%B1%D0%B8%D0%BB%D0%B5%D0%BC&search_period=30'
#url='https://spb.hh.ru/search/resume?text=%D0%92%D0%BE%D0%B4%D0%B8%D1%82%D0%B5%D0%BB%D1%8C+%D1%81+%D0%BB%D0%B8%D1%87%D0%BD%D1%8B%D0%BC+%D0%B0%D0%B2%D1%82%D0%BE%D0%BC%D0%BE%D0%B1%D0%B8%D0%BB%D0%B5%D0%BC&area=1&area=232&area=2019&ored_clusters=true&order_by=relevance&search_period=0&logic=normal&pos=full_text&exp_period=all_time&hhtmFrom=resume_search_result'
driver.get(url)
main=driver.find_elements(By.XPATH,"//div[contains(@class, 'resume-search-item__header')]")
count=0
m = driver.find_elements(By.XPATH,"//a[contains(@class, 'serp-item__title')]")
n = driver.find_elements(By.XPATH,"//div[contains(@class, 'bloko-text bloko-text_large bloko-text_strong')]")
k = driver.find_elements(By.XPATH,"//span[contains(@data-qa, 'job-search-status')]")
q = driver.find_elements(By.XPATH,"//div[contains(@data-qa, 'resume-serp__resume-excpirience-sum')]/span")
x= driver.find_elements(By.XPATH,"//span[contains(@class, 'date--cHInIjOdiyfDqTabYRkp date_highlight--AGBCI_xIPc7rwB4GqUST')]/span")
arr=[]
for i1,i2,i3,i4,i5 in zip(m,n,k,q,x):
    count+=1
    d=dict()
    d["ID"]=str(count)
    d["Url"]=i1.get_attribute('href')
    d["Title"]=i1.text
    d["Price"]=i2.text
    d["Status"]=i3.text
    d["Level"]=i4.text
    d["Last visit"]=i5.text
    
df =pd.DataFrame(arr)
df.to_csv(r'C:\Users\rs\msk_data1.csv', index= True)
