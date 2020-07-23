# -*- coding: utf-8 -*-
import re
from selenium import webdriver
driver = webdriver.Chrome('./chromedriver')


def rePlaceData(value):
    numbers = re.findall("\d+", value)
    result = ""
    for i in numbers:
        decodedNumber = i
        result += decodedNumber
    return result


driver.get(
    'https://direct.lina.co.kr/product/ess/dtc01/easy')
birthInput = driver.find_element_by_xpath('//*[@id="birthday"]')
maleBtn = driver.find_element_by_xpath('//*[@id="main_btn_male"]')
resultBtn = driver.find_element_by_xpath('//*[@id="btn_direct_dental_cal"]')

birthInput.send_keys('890119')
maleBtn.click()
resultBtn.click()
driver.implicitly_wait(3)
htmlResult = driver.find_element_by_xpath('//*[@id="mo_amount_span"]').text
resultValue = rePlaceData(htmlResult)
detailBtn = driver.find_element_by_xpath('//*[@id="openLayerplanPonA2"]')
detailBtn.click()
table = driver.find_element_by_xpath(
    '//*[@id="planPonA2"]/div/div[2]/div/div/table[1]/tbody')
tableRow = table.find_elements_by_tag_name('tr')
for index, value in enumerate(tableRow):
    title = value.find_elements_by_tag_name('th')[0].text
    print(title)

print(htmlResult)
