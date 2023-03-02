from selenium import webdriver
from selenium.webdriver.common.by import By
import logging
logging.basicConfig(filename = "assert.log",level=logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')



driver = webdriver.Chrome()
driver.get(r"https://www2.daad.de/deutschland/studienangebote/international-programmes/en/result/?q=computer%20science&degree%5B%5D=1&lang%5B%5D=4&fos=&cert=&admReq=&langExamPC=&langExamLC=&langExamSC=&langDeAvailable=&langEnAvailable=&modStd%5B%5D=&cit%5B%5D=&tyi%5B%5D=&ins%5B%5D=&fee=&bgn%5B%5D=&dat%5B%5D=&prep_subj%5B%5D=&prep_degree%5B%5D=&sort=4&dur=&subjects%5B%5D=&limit=10&offset=&display=list")
driver.implicitly_wait(30)
try:
    acceptTermButton = driver.find_element(By.CLASS_NAME, 'qa-cookie-consent-accept-all')
    acceptTermButton.click()
except:
    pass
courseListDivs = driver.find_elements(By.CLASS_NAME, 'c-ad-carousel--list')


for courseDiv in courseListDivs:
    element = courseDiv.find_element(By.TAG_NAME , "a")
    logging.debug(str(element))
    element.click()
    driver.back()

driver.quit()