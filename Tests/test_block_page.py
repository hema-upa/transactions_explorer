import pytest
from Pages.block_page import BlockTrasanctions
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait =  WebDriverWait(driver, 20)

def test_heading(driver):
    page = BlockTrasanctions(driver)
    page.open()
    heading = page.validate_heading((By.XPATH, f"//*[@class = 'font-h3']"))
    assert "25 of 2875 Transactions" == heading
def test_input_output(driver):
    page = BlockTrasanctions(driver)
    page.open()
    print(input_ouput_transaction())

