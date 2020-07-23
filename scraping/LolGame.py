# -*- coding: utf-8 -*-
from selenium import webdriver

driver = webdriver.Chrome('./chromedriver')
driver.get('https://kr.leagueoflegends.com/ko-kr/')

idInput = driver.find_element_by_css_selector(
    '#riotbar-account > div:nth-child(1) > a')
idInput.click()
id = driver.find_element_by_css_selector(
    'body > div > div > div > div.grid.grid-direction__row.grid-page-web__content > div.grid.grid-direction__column.grid-page-web__wrapper > div > div.grid.grid-align-center.grid-justify-space-between.grid-fill.grid-direction__column.grid-panel-web__content.grid-panel__content > div > div > div > div:nth-child(1) > div > input')
id.send_keys('')
password = driver.find_element_by_css_selector(
    'body > div > div > div > div.grid.grid-direction__row.grid-page-web__content > div.grid.grid-direction__column.grid-page-web__wrapper > div > div.grid.grid-align-center.grid-justify-space-between.grid-fill.grid-direction__column.grid-panel-web__content.grid-panel__content > div > div > div > div.field.password-field.field--animate > div > input')
password.send_keys('')
button = driver.find_element_by_css_selector(
    'body > div > div > div > div.grid.grid-direction__row.grid-page-web__content > div.grid.grid-direction__column.grid-page-web__wrapper > div > button')
button.click()
