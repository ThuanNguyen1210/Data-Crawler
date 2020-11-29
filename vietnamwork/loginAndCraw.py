from selenium import webdriver
from getpass import getpass
import time
# Please create an account and login using that account
# username = input("Enter username: ")


# password = input("Enter password: ")

# Please add add the path containing your webdriver here
driver = webdriver.Chrome("C:\\Webdriver\\chromedriver.exe")
driver.get("https://www.vietnamworks.com/dang-nhap?from=home-v2&type=login")

# username_textbox = driver.find_element_by_id("email")
# username_textbox.send_keys(username)

# password_textbox = driver.find_element_by_id("login__password")
# password_textbox.send_keys(password)

# login_button = driver.find_element_by_id("button-login")
# login_button.submit()

driver.get("https://www.vietnamworks.com/tim-viec-lam/tat-ca-viec-lam")
# driver.implicitly_wait(500)

time.sleep(30)
jobs = driver.find_elements_by_class_name('job-title')

for i in range(len(jobs)):
    print(jobs[i].get_attribute('href'))
# print(list(jobs))
print("Number of Jobs: ", len(jobs))
# driver.close()

# Just return the first 9 jobs
