#!/usr/bin/python
# -*- coding:utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Uiauto(object):
    # driver不能放在函数内部，应为函数结束后就会回收函数占用空间，导致打开的网页闪退
    driver = webdriver.Chrome()

    def login(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("http://mywifi.mercku.tech/")
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "has-icon"))
        ).send_keys("22222222")


if __name__ == '__main__':
    Uiauto().login()
