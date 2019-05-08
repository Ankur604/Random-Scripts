__author__ = 'Ankur303'
from selenium import webdriver
from time import sleep
import os

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
DRIVER_BIN = os.path.join(PROJECT_ROOT, "chromedriver")


try:
	url = 'https://cgifederal.secure.force.com/ApplicantHome'
	email_obj_name = 'Unauthorized:SiteTemplate:siteLogin:loginComponent:loginForm:username'
	pass_obj_name = 'Unauthorized:SiteTemplate:siteLogin:loginComponent:loginForm:password'
	check_box_obj_name = 'Unauthorized:SiteTemplate:siteLogin:loginComponent:loginForm:j_id172'
	email = 'Please paste your email here'
	password = 'Please paste your password here'
	captcha_text_obj_name = 'Unauthorized:SiteTemplate:siteLogin:loginComponent:loginForm:recaptcha_response_field'
	login_button_name = 'Unauthorized:SiteTemplate:siteLogin:loginComponent:loginForm:loginButton'
	driver = webdriver.Chrome(executable_path = DRIVER_BIN)
	driver.get(url)
	sleep(3)
except Exception as e:
	print e


try:
	print "Im here"
	captcha = raw_input("Enter the captcha : ")
	email_text_box = driver.find_element_by_name(email_obj_name)
	email_text_box.send_keys(email)
	pass_text_box = driver.find_element_by_name(pass_obj_name)
	pass_text_box.send_keys(password)
	check_box = driver.find_element_by_name(check_box_obj_name)
	check_box.click()
	captcha_text_box = driver.find_element_by_name(captcha_text_obj_name)
	captcha_text_box.send_keys(captcha)
	login_button = driver.find_element_by_name(login_button_name)
	login_button.click()
except Exception as e:
	raise e

try:
	sleep(10)	
	while (1):
		desired_value = driver.find_element_by_class_name('leftPanelText')
		desired_text = desired_value.text
		if desired_text.find('April') != -1:
			break
		driver.refresh()
		sleep(10)
	print "Found it"
	driver.get('https://cgifederal.secure.force.com/scheduleappointment')
	driver.execute_script("window.open('https://www.youtube.com/watch?v=n_GFN3a0yj0', 'new_window')")
except Exception as e:
	raise e
	
