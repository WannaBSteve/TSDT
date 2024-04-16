from selenium import webdriver

# 创建 Chrome WebDriver 实例
browser = webdriver.Chrome()

browser.get('http://localhost:8000')

assert 'Django' in browser.page_source