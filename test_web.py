from selenium import webdriver  
import time  
from selenium.webdriver.common.keys import Keys
import allure

class Testweb:
	### Input Username ###
	def test_gmail(self):
		self.driver = webdriver.Remote(desired_capabilities=webdriver.DesiredCapabilities.CHROME, command_executor='http://127.0.0.1:4444/wd/hub')
		self.driver.maximize_window() 
		self.driver.get("https://www.gmail.com")  
		self.driver.maximize_window()  
		#delete the cookies  
		self.driver.delete_all_cookies()  
		#identify the user name text box and enter the value  
		self.driver.find_element_by_id("identifierId").send_keys("fajarmaulana240699@gmail.com")  
		time.sleep(2)  
		#click on the next button  
		self.driver.find_element_by_xpath("//div[@class='VfPpkd-RLmnJb'][1]").click()  
		time.sleep(3)  
		status = self.driver.find_element_by_xpath("//div[@class='rr0DNb'][1]").is_displayed()
		if status == True:
			assert True
		else:
			assert False
		self.driver.close()

	### Klik Button ###
	#def click(tags, ids):
	#	driver.find_element_by_xpath(f"//{tags}[@class='{ids}'][1]").click()  
	#	time.sleep(2)

	### Klik Button By Value ###
	#def click_new(tags2, ids2):
	#	driver.find_element_by_xpath(f"//{tags2}[contains(text(),'{ids2}')][1]").click()  

