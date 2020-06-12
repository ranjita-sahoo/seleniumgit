from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_elements_by_name("name")
#river.find_element_by_id("exampleCheck1").click()
#driver.find_element_by_css_selector("input[name='name']").send_keys("Rahul")
print(driver.find_element_by_css_selector("[class*='alert-success']").find_element_by_link_text("Success! The Form has been submitted successfully!."))