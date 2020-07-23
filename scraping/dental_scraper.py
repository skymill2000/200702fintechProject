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


def getAIAData(name, birth, gender):
    driver = webdriver.Chrome('./chromedriver')
    scrapingResult = {
        'company': "라이나",
        'price': 0,
        'contents': []
    }
    driver.get(
        'https://www.aia.co.kr/ko/our-products/medical-protection/non-par-denteal-health-plan.html#')


def getLinaData(name, birth, gender):
    driver = webdriver.Chrome('./chromedriver')
    scrapingResult = {
        'company': "라이나",
        'price': 0,
        'contents': []
    }
    driver.get('https://direct.lina.co.kr/product/ess/dtc01/easy')
    textBox = driver.find_element_by_xpath('//*[@id="birthday"]')
    textBox.send_keys(birth)
    if gender == 1:
        femaleBtn = driver.find_element_by_xpath('//*[@id="main_btn_female"]')
        femaleBtn.click()
    else:
        maleBtn = driver.find_element_by_xpath('//*[@id="main_btn_male"]')
        maleBtn.click()
    resultBtn = driver.find_element_by_xpath(
        '//*[@id="btn_direct_dental_cal"]')
    resultBtn.click()
    htmlResult = driver.find_element_by_xpath('//*[@id="mo_amount_span"]').text
    resultValue = rePlaceData(htmlResult)
    scrapingResult['price'] = resultValue
    driver.implicitly_wait(1)
    detailBtn = driver.find_element_by_xpath('//*[@id="openLayerplanPonA2"]')
    detailBtn.click()
    tableBody = driver.find_element_by_xpath(
        '//*[@id="planPonA2"]/div/div[2]/div/div/table[1]').find_element_by_tag_name('tbody')
    rows = tableBody.find_elements_by_tag_name("tr")
    contentsList = []
    for index, value in enumerate(rows):
        if index != 0:
            print(value.find_elements_by_tag_name('th')[0].text)
            contentsList.append(value.find_elements_by_tag_name('th')[
                                0].text)
    scrapingResult['contents'] = contentsList
    return scrapingResult
