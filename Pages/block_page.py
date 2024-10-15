from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Initialize WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait =  WebDriverWait(driver, 20)

class BlockTrasanctions:
    URL = "https://blockstream.info/block/000000000000000000076c036ff5119e5a5a74df77abf64203473364509f7732"

    def __init__(self, driver):
        self.driver = driver
        self.wait =  WebDriverWait(self.driver, 10)
        

    def open(self):
        self.driver.get(self.URL)
        self.driver.maximize_window()
        

    def validate_heading(self, locator_tuple):
        element = self.wait.until(EC.visibility_of_element_located((locator_tuple)))
        return element.text
    
