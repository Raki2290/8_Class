from selenium import webdriver
driver= webdriver.Chrome()
driver.get("file:///C:/Users/Indium%20Software/Desktop/WebTable.html")
driver.maximize_window()
driver.implicitly_wait(30)

ele= driver.find_elements_by_xpath('/html/body/table/tbody/tr[1]')
print(ele)