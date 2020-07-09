from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
#driver = webdriver.Firefox()

driver.get('https://www.baidu.com/')

#element_keyword = driver.find_element_by_id('kw')

#element_keyword.send_keys('宋曲')

element_search_button = driver.find_element_by_id('su')

print(element_search_button)