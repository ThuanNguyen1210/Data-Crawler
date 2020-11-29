from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Webdriver\\chromedriver.exe")  # Please add the path containing your webdriver here

driver.get("https://www.vietnamworks.com/tim-viec-lam/tat-ca-viec-lam")
driver.implicitly_wait(5)
jobs = driver.find_elements_by_css_selector('h3 a.job-title')
job_links = []

# Send to resquest to the web and find elements corresponding to each job
for i in range(len(jobs)):
        print(jobs[i].get_attribute('href'))
        job_links += [jobs[i].get_attribute('href')]

# Close the browser 
driver.close()

# Save data in jobslink.json
with open('joblinks.txt', 'w') as f:
        for link in job_links:
                f.write(link + '\n')