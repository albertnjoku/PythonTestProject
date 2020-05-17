from selenium import webdriver
import logging
from selenium.webdriver.common.keys import Keys

logging.basicConfig(filename=".\\logMessage.log", level=logging.DEBUG)
logger = logging.getLogger()


def test_title():
    driver = webdriver.Chrome()
    driver.get("http://www.python.org")
    assert "Python" in driver.title
    logger.info("log message")
    elem = driver.find_element_by_name("q")
    elem.clear()
    elem.send_keys("pycon")
    elem.send_keys(Keys.RETURN)
    assert "No results found." not in driver.page_source
    driver.close()
