import sys, os
import selenium
import selenium.webdriver as webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def search(yammerpage):
    driver = webdriver.Firefox()
    driver.get(yammerpage)
    try:
        login = driver.find_element_by_id('user_email')
        login.send_keys('matthew@apnic.net')
        login.send_keys(Keys.RETURN)
    except selenium.common.exceptions.NoSuchElementException, e:
        print e
        driver.close()
    except selenium.common.exceptions.WebDriverException, e:
        print e
        driver.close()

def setUp():
    try:
        driver = webdriver.Firefox()
        driver.get("http://www.yammer.com/#/apnic.net/uploaded_files/")
        driver.find_element_by_class_name("yj-public-page--header-login").click()
        driver.find_element_by_id("login").send_keys("matthew@apnic.net")
        driver.find_element_by_id("login").send_keys(Keys.RETURN)
        ldp = EC.presence_of_element_located((By.ID, "input_1"))
        WebDriverWait(driver, 10).until(ldp)
        driver.find_element_by_id("input_1").send_keys("matthew")
        driver.find_element_by_id("input_2").send_keys(passwd)
        driver.find_element_by_id("input_2").send_keys(Keys.RETURN)
        yammer = EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "PacNOG"))
        WebDriverWait(driver, 10).until(yammer)
        driver.find_element_by_partial_link_text("PacNOG").click()
        files = EC.presence_of_element_located((By.XPATH, '//a[@href="https://www.yammer.com/apnic.net/#/groups/11103342/files"]'))
        WebDriverWait(driver, 10).until(files)
        driver.find_element_by_xpath('//a[@href="https://www.yammer.com/apnic.net/#/groups/11103342/files"]').click()

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "yj-tabular-data-cont")))
        driver.find_element_by_partial_link_text('All File Types').click()
        driver.find_element_by_partial_link_text('Images').click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "yj-thumbnail-item")))

        print driver.find_element_by_xpath('//img[@class="yj-thumbnail-item-image"]').get_attribute('href')
        each  = []
        for each in driver.find_element_by_xpath('//img[@class="yj-thumbnail-item-image"]'):
            print each.get_attribute('src')
            #<img class="yj-thumbnail-item-image" src="https://www.yammer.com/api/v1/uploaded_files/96287818/version/96674866/thumbnail" alt="IMG_2476.JPG">
        else:
            print "failed"
    except selenium.common.exceptions.NoSuchElementException, e:
        print e
    except selenium.common.exceptions.WebDriverException, e:
        print e
    except TypeError, e:
        print e
passwd = raw_input("What is your password? :")
setUp()
