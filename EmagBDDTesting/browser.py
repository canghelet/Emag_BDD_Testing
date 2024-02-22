import unittest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service


class Browser(unittest.TestCase):
    service = Service(executable_path='C:\BrowserDrivers\geckodriver.exe')
    options = webdriver.FirefoxOptions()
    driver = webdriver.Firefox(service=service, options=options)
    driver.implicitly_wait(10)
    driver.set_page_load_timeout(10)
    driver.maximize_window()
    driver.delete_all_cookies()

    def close(self):
        self.driver.delete_all_cookies()
        self.driver.close()