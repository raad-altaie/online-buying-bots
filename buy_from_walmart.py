from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


import requests
import time


item_link = 'https://www.walmart.com/ip/Sony-PlayStation-5-Video-Game-Console/363472942'

max_buying_price = 500

first_name = 'John'
last_name = 'Doe'
email = 'john.doe@example.com'
phone = '818-379-6722'
address_line_one = '1600 Amphitheatre Pkwy'
city = 'Mountain View'
state = 'California'
zip_code = '94043'
credit_card_number = '4872475635924104'
credit_card_exp_month = '05'
credit_card_exp_year = '27'
credit_card_cvv = '957'



def buy_from_walmart():
    driver.get(item_link)

    got_item = False

    while got_item == False:

        if driver.find_elements_by_xpath('//*[(text()="Add to cart")]'):

            # Check the price
            price_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,'#price > div > span.hide-content.display-inline-block-m > span > span.visuallyhidden')))
            price = float(price_element.text.replace('$', ''))

            if price > float(max_buying_price):
                print("Item is more expensive than max_buying_price")
                time.sleep(60)
                driver.refresh()
                continue


            # Add to cart
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME,'spin-button-children'))).click()

            WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, '//*[(text()="Check out")]'))).click()
            WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, '//*[(text()="Continue without account")]'))).click()
            WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, '//*[(text()="Continue")]'))).click()


            # Fill in the info
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID,'firstName'))).send_keys(first_name)
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID,'lastName'))).send_keys(last_name)
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID,'phone'))).send_keys(phone)
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID,'email'))).send_keys(email)
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID,'addressLineOne'))).send_keys(address_line_one)

            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID,'city'))).clear()
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID,'city'))).send_keys(city)

            Select(WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID,'state')))).select_by_visible_text(state)
            
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID,'postalCode'))).clear()
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID,'postalCode'))).send_keys(zip_code)


            # Click Continue after enter the info
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[(text()="Continue")]'))).click()


            # Payment info
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID,'creditCard'))).send_keys(credit_card_number)
            Select(WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID,'month-chooser')))).select_by_visible_text(credit_card_exp_month)
            Select(WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID,'year-chooser')))).select_by_visible_text(credit_card_exp_year)            
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID,'cvv'))).send_keys(credit_card_cvv)

            # Place order
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[(text()="Review your order")]'))).click()
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[(text()="Place order")]'))).click()
            got_item = True
            print('YOU GOT THE ITEM!! YAY!')


        else:
            # refresh every 60 seconds 
            time.sleep(60)
            driver.refresh()
            print('Refresh Page')



if __name__ == '__main__':
    # Load chrome
    driver = webdriver.Chrome(executable_path='./chromedriver')
    buy_from_walmart()
