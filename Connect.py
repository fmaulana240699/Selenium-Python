from selenium import webdriver  
import time  
from selenium.webdriver.common.keys import Keys



### Input Username ###
def input(identity, username):
	driver.find_element_by_id(identity).send_keys(username) 
	time.sleep(2) 

### Klik Button ###
def click(tags, ids):
	driver.find_element_by_xpath(f"//{tags}[@class='{ids}'][1]").click()  
	time.sleep(2)

### Klik Button By Value ###
def click_new(tags2, ids2):
	driver.find_element_by_xpath(f"//{tags2}[contains(text(),'{ids2}')][1]").click()  



ip="172.168.100.65"
url="https://www.gmail.com"
driver = webdriver.Remote(desired_capabilities=webdriver.DesiredCapabilities.FIREFOX, command_executor=f'http://{ip}:4445/wd/hub')
#driver = webdriver.Chrome() 
driver.maximize_window() 
driver.get(url)  

input("identifierId", "fajarmaulana240699@gmail.com")
click("div", "VfPpkd-RLmnJb")
driver.close()  
print("Testing Successfuly")