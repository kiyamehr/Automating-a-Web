from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://orteil.dashnet.org/cookieclicker/")

cookie_id = "bigCookie"

WebDriverWait(driver, 60).until(
    # xpath uses a function to find the given text and calls a def(named: contains*) \
    # and that def gets a text() so it searches for aa text and the text in the next tuple
    EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'English')]"))
)

# press the english language:
language_select = driver.find_element(By.XPATH, "//*[contains(text(), 'English')]")
language_select.click()


WebDriverWait(driver, 60).until(
    EC.presence_of_element_located((By.ID, "bigCookie"))
    )


# if we dont add this cause of (my) super slow internet speed \
# the program will crash cause there is yet not a big cookie id found\
# so we wait for 10 secs more for it to fully load
time.sleep(10)

# press the big cookie:
big_cookie_click = driver.find_element(By.ID, "bigCookie")

product_price_prefix = "productPrice"
product_prefix = "product"
while True:
    big_cookie_click.click()
    
    # when reached a space '(" ")' seperate the two and pick out the first value
    cookies_count = driver.find_element(By.ID, "cookies").text.split(" ")[0] # to get the str of cookies
    
    # replacing ',' with an empty stirng
    cookies_count = int(cookies_count.replace(",", ""))
    
    # because we have 4 upgrades we want to iterate through:
    for i in range(4):
        product_price = driver.find_element(By.ID, product_price_prefix + str(i)).text.replace(",", "")
        
        if not product_price.isdigit():
            continue
        
        product_price = int(product_price)
        
        if cookies_count >= product_price:
            product = driver.find_element(By.ID, product_prefix + str(i))
            product.click()
            break

        
    print(cookies_count)
