import pytest
from Pages.block_page import BlockTrasanctions
from selenium.webdriver.common.by import By

def test_heading(driver):
    page = BlockTrasanctions(driver)
    page.open()
    heading = page.validate_heading((By.XPATH, f"//*[@class = 'font-h3']"))
    assert "25 of 2875 Transactions" == heading

