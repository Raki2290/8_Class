from selenium import webdriver
#from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome()
driver.get("https://www.flipkart.com/")
driver.maximize_window()
driver.implicitly_wait(30)
driver.find_element_by_xpath("//button[@class='_2AkmmA _29YdH8']").click()
element = driver.find_element_by_xpath("//span [text()='Men']")
webdriver.ActionChains(driver).move_to_element(element).click(element).perform()
