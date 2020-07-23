# -*- coding: utf-8 -*-
from selenium import webdriver
driver = webdriver.Chrome('./chromedriver')
driver.get(
    'https://www.alimi.or.kr/api/a/vacant/selectApiVacant.do')
driver.implicitly_wait(1)
table = driver.find_element_by_class_name('search_list')
tableBody = table.find_element_by_tag_name('tbody')
tablerow = tableBody.find_elements_by_tag_name('tr')
for index, value in enumerate(tablerow):
    if index != 0:
        addDate = value.find_elements_by_tag_name('td')[2].text
        print(addDate)
