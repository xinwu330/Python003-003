from selenium import webdriver
import time

try:
    browser = webdriver.Chrome(executable_path='my_local_path/chromedriver.exe')
    
    browser.get('https://shimo.im/login?from=home')
    time.sleep(1)

    browser.find_element_by_xpath('//*[@name="mobileOrEmail"]').send_keys('kill******1234@126.com')
    browser.find_element_by_xpath('//*[@name="password"]').send_keys('********')
    time.sleep(1)
    browser.find_element_by_xpath('//*[@class="sm-button submit sc-1n784rm-0 bcuuIb"]').click()

    cookies = browser.get_cookies()
    print(cookies)
    time.sleep(3)

except Exception as e:
    print(e)
else:    
    browser.close()