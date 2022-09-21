from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.firefox.service import Service



s = Service('C:\Program Files (x86)\geckodriver.exe')
driver = webdriver.Firefox(service=s)
driver.get("https://www.icloud.com/")
WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.ID,"aid-auth-widget-iFrame")))
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "account_name_text_field"))).send_keys("email")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "account_name_text_field"))).send_keys(Keys.ENTER)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'password_text_field'))).send_keys("password")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'password_text_field'))).send_keys(Keys.ENTER)

#WebDriverWait(driver, 6).until(EC.frame_to_be_available_and_switch_to_it((By.ID,"aid-auth-widget-iFrame")))
#WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'didnt-get-code')))


#So far code works except for thepart where it actually returns that the login was successful when there is 2 fact authentication
heading_name=driver.find_element(By.CLASS_NAME, value ="button-link si-link ax-outline.tk-subbody.lite-theme-override.other-option-popover-link")
if (heading_name.text=="Didn’t get a verification code?"):
    print("Login successful")
else:
    print("Login failed")




