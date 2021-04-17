from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


import requests
import time


item_link = 'https://www.walmart.com/ip/Sony-PlayStation-5-Video-Game-Console/363472942'


first_name = 'Test'
last_name = 'Test'
email = 'test@test.com'
phone = '8008080000'
address_line_one = '123 Main St'
city = 'San Diego'
state = 'California'
zip_code = '920000'
credit_card_number = '4872475635924104'
credit_card_exp_month = '05'
credit_card_exp_year = '27'
credit_card_cvv = '957'



def buy_from_walmart():
    driver.get(item_link)

    got_item = False

    while got_item == False:

        if driver.find_elements_by_xpath('//*[(text()="Add to cart")]'):

            add_to_cart = WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.CLASS_NAME,'spin-button-children')))
            add_to_cart.click()


            time.sleep(2)
            WebDriverWait(driver,15).until(EC.presence_of_element_located((By.XPATH, '//*[(text()="Check out")]'))).click()
            WebDriverWait(driver,15).until(EC.presence_of_element_located((By.XPATH, '//*[(text()="Continue without account")]'))).click()
            WebDriverWait(driver,15).until(EC.presence_of_element_located((By.XPATH, '//*[(text()="Continue")]'))).click()

            time.sleep(2)


            driver.find_element_by_id("firstName").send_keys(first_name)
            driver.find_element_by_id("lastName").send_keys(last_name)
            driver.find_element_by_id("phone").send_keys(phone)
            driver.find_element_by_id("email").send_keys(email)
            driver.find_element_by_id("addressLineOne").send_keys(address_line_one)
            

            driver.find_element_by_id('city').clear()
            driver.find_element_by_id("city").send_keys(city)


            Select(driver.find_element_by_id("state")).select_by_visible_text(state)

            driver.find_element_by_id("postalCode").clear()
            driver.find_element_by_id("postalCode").send_keys(zip_code) 
            
            WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[(text()="Continue")]'))).click()
            time.sleep(2)

            driver.find_element_by_id("creditCard").send_keys(credit_card_number)
            Select(driver.find_element_by_id("month-chooser")).select_by_visible_text(credit_card_exp_month)
            Select(driver.find_element_by_id("year-chooser")).select_by_visible_text(credit_card_exp_year)
            driver.find_element_by_id("cvv").send_keys(credit_card_cvv)



            WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[(text()="Review your order")]'))).click()
            WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[(text()="Place order")]'))).click()
            got_item = True
            print('GOT THE ITEM!! YAY!')


        else:
            # refresh every 60 seconds 
            time.sleep(60)
            driver.refresh()
            print('Refresh Page')



if __name__ == '__main__':
    # Load chrome
    driver = webdriver.Chrome(executable_path='./chromedriver')
    buy_from_walmart()
