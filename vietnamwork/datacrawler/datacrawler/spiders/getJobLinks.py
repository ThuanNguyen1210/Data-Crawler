# from selenium import webdriver
# import os
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import TimeoutException
# from selenium.webdriver.common.by import By
# import time

# try:
#         f = open("joblinks.txt")
#         os.remove("joblinks.txt")
# except:
#         pass
# time.sleep(2)

# driver = webdriver.Chrome(executable_path="C:\\Webdriver\\chromedriver.exe")  # Please add the path containing your webdriver here
# driver.maximize_window()
# driver.get("https://www.vietnamworks.com/dang-nhap?from=home-v2&type=login")

# username_textbox = driver.find_element_by_id("email")
# username_textbox.send_keys('thuannguyen121000@gmail.com')

# password_textbox = driver.find_element_by_id("login__password")
# password_textbox.send_keys('01658424179Aa')

# login_button = driver.find_element_by_id("button-login")
# login_button.submit()

# driver.get("https://www.vietnamworks.com/tim-viec-lam/tat-ca-viec-lam")
# # time.sleep(2)
# first = True
# while True:
#         driver.execute_script("window.scrollTo(0, 1080)") 
        
#         WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'job-title')))
#         jobs= driver.find_elements_by_class_name('job-title')
#         job_links = []
#         salaries_ele = driver.find_elements_by_css_selector('span.salary')
#         salaries = []
#         for i in range(len(jobs)):
#                 print(jobs[i].get_attribute('href'))
#                 job_links += [jobs[i].get_attribute('href')]
#         for i in range(len(salaries_ele)):
#                 salaries += [salaries_ele[i].text]
#         # Save data in jobslink.json
#         with open('joblinks.txt', 'a') as f:
#                 for link in job_links:
#                         f.write(link + '\n')
#         with open('salary.txt', 'a', encoding='utf-8') as s:
#                 for sal in salaries:
#                         s.write(sal + '\n')
#         if first == True:
#                 time.sleep(2)
#                 first = False
#         # time.sleep(5)
#         try:
#                 time.sleep(1)
#                 button = driver.find_element_by_xpath("//a[contains(@class, 'page-link') and text() = '>']").click()
#                 continue
#         except:
#                 break
# # Close the browser 
# # driver.close()
