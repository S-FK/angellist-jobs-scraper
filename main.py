# importing packages
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import csv
import os

driver = webdriver.Chrome(executable_path='./chromedriver')

# starting to fetch angel list
driver.get('https://angel.co/jobs')
print("page fetched")
time.sleep(20)
print ("woke up")

# finding the login button and pressing it
login = driver.find_element_by_class_name('styles_link__6tbl_')
login.send_keys(Keys.RETURN)
print("redirected to:", driver.title)

# finding email and password input fields and entering details
email = driver.find_element_by_id('user_email')
password = driver.find_element_by_id('user_password')
login_btn = driver.find_element_by_name('commit')

# put your login creds here
email.send_keys('')
password.send_keys('')
login_btn.send_keys(Keys.RETURN)

print('redirected to:', driver.title)

time.sleep(60)

jobs = driver.find_elements_by_class_name('styles_title__xpQDw')

print("Total jobs on this page:", len(jobs))

folder_name = f'Angel_jobs'
if not os.path.exists(folder_name):
        os.mkdir(folder_name)
csv_filename = f'internships.csv'
with open(os.path.join(folder_name, csv_filename), 'w', encoding='utf-8') as f:
        headers = ['Role', 'Company Name', 'Skills', 'Type', 'Compensation', 'Location', 'Description', 'Logo', 'Job Link']
        write = csv.writer(f, dialect='excel')
        write.writerow(headers)
        for job in jobs:
            job.click()
            time.sleep(10)
            job_role = job.text
            job_company = driver.find_element_by_css_selector("div[class^='styles_detail__moBEM styles_name__YTfJL']").text
            comp_dets = driver.find_element_by_css_selector("div[class^='styles_detail__moBEM styles_name__YTfJL']")
            company_logo = comp_dets.find_element_by_class_name('styles_avatar__2IVF7.styles_square__53UBi').get_attribute('src')
            try:
                job_skills = driver.find_element_by_class_name('styles_skillPillTags__Zv_Uv').text
            except:
                job_skills = ''
            try:
                job_compensation = driver.find_element_by_class_name('styles_compensation__QkJIm').text
            except:
                job_compensation = ''
            job_type = driver.find_element_by_xpath("//*[contains(text(), 'Internship') or contains(text(), 'Full Time')]").text
            job_description = driver.find_element_by_class_name('styles_component__WZ_oK').text
            job_location = driver.find_element_by_class_name('styles_component__Jnlux').text
            company_link = driver.find_element_by_css_selector("a[class^='styles_component__UCLp3 styles_defaultLink__eZMqw styles_logo__dAyAQ']").get_attribute('href')
            job_link = driver.current_url #company_link + '/jobs'

            new_data = [job_role, job_company, job_skills, job_type, job_compensation, job_location, job_description, company_logo, job_link]
            write.writerow(new_data)

            driver.back()



time.sleep(20)

driver.quit()