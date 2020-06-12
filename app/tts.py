from selenium import webdriver
from selenium.webdriver.support import select

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://login.salesforce.com/")
driver.find_element_by_css_selector("#username").send_keys("Rahul")
driver.find_element_by_css_selector(".password").send_keys("Sushree")
driver.find_element_by_link_text("Forgot Your Password?").click()

#dropdown = select(driver.find_element_by_id())

driver.get_screenshot_as_file("scrn.png")