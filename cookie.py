from selenium import webdriver

driver = webdriver.PhantomJS()
driver.get('http://pythonscraping.com')
driver.implicitly_wait(1)
print(driver.get_cookies())

savedCookies = driver.get_cookies()
driver2 = webdriver.PhantomJS()
driver2.get('http://pythonscraping.com')
driver2.delete_all_cookies()
for cookie in savedCookies:
    driver.add_cookie(cookie)

driver2.get('http://pythonscraping.com')
driver2.implicitly_wait(1)
print(driver2.get_cookies())