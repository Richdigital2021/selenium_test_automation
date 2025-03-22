import time
from selenium import webdriver
from selenium.webdriver.common.by import By

#Variable Declaration
wait = 5
url = "https://automationplayground.com/crm/login.html"
Email_Address = "richy@gmail.com"
password = "123456"
first_name = "John"
last_name = "Kelvin"
city = "Houston"
state_of_origin = "Texas"

# Initializing my Browser
driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()
time.sleep(wait)

# Sign in to the web page
Email_Id = driver.find_element(By.ID, "email-id")
Email_Id.send_keys(Email_Address)

Password = driver.find_element(By.ID,"password")
Password.send_keys(password)

Submit_Id = driver.find_element(By.ID, "submit-id")
Submit_Id.click()
time.sleep(wait)

# Adding new customer
NewCustomer = driver.find_element(By.ID, "new-customer")
NewCustomer.click()

CustomerEmail = driver.find_element(By.ID, "EmailAddress")
CustomerEmail.send_keys("newcustomer@gmail.com")

CustomerFirstName = driver.find_element(By.ID, "FirstName")
CustomerFirstName.send_keys(first_name)

CustomerLastName = driver.find_element(By.ID, "LastName")
CustomerLastName.send_keys(last_name)

City = driver.find_element(By.ID, "City")
City.send_keys(city)

State = driver.find_element(By.ID, "StateOrRegion")
State.send_keys(state_of_origin)

Gender = driver.find_element(By.NAME, "gender")
Gender.click()
time.sleep(wait)

# Selecting the Promo code
PromoName = driver.find_element(By.NAME, "promos-name")
PromoName.send_keys("promos-yes")
#time.sleep(wait)

#Submiting the form
Submit = driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
Submit.click()
time.sleep(wait)