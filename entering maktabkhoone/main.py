# to run the chosen browser:
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# can bypss the capcha test on Chrome
import undetected_chromedriver as uc

# used for searching html tags and interacting with them:
from selenium.webdriver.common.by import By

# so we can add interactive keys like Enter or etc...
from selenium.webdriver.common.keys import Keys
import time

# wait some time if the condition not met crash the program
from selenium.webdriver.support.ui import WebDriverWait
# sets the condition of the waiting
from selenium.webdriver.support import expected_conditions as EC

# to surpass the capcha test while searching
driver = uc.Chrome()

driver.get("https://google.com")

# to wait 5 secs until the web is located \
# and if it couldnt load the page in 5 secs it will crash the program
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CLASS_NAME, "gLFyf"))
)

input_element = driver.find_element(By.CLASS_NAME, "gLFyf")
input_element.clear() # --> to clear anything that was in the field
input_element.send_keys("maktab khoone" + Keys.ENTER)


WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "مکتب‌خونه | آکادمی آنلاین تخصص‌ها"))
)

link = driver.find_element(By.PARTIAL_LINK_TEXT, "مکتب‌خونه | آکادمی آنلاین تخصص‌ها")
link.click()

# waits and closed the program after 10secs.
time.sleep(10)
driver.quit()
