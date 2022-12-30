from typing import Collection, List
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver

class Browser:
    """Provide access to a singleton instance of a Selenium web driver.

    Methods:
    get_browser(cls)  class method that returns a singleton instance of a WebDriver
    """
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver: WebDriver = webdriver.Chrome(options=options)

    @classmethod
    def get_browser(cls) -> webdriver:
        """Return a singleton instance of a WebDriver.

        Returns:
        A WebDriver instance.
        """
        return cls.driver



def find_link(url: str, link_text: str) -> str:
    """Search a web page for a hyperlink with link text that exactly matches link_text.  

    :param url: URL of the web page to scan
    :param link_text: the text of a hyperlink to search for
    :return: string form of the first matching hyperlink URL or None if no match
    :raises ValueError: if the url is not valid

    Note: Selenium does not provide access to the HTTP response code,
    so it is difficult to detect when a page does not exist.
    For this assignment, your code will return None in that case.
    """
    browser = Browser.get_browser()
    try:
        browser.get(url)
    except WebDriverException:
        raise ValueError("Invalid URL")
    elements: List[WebElement] = browser.find_elements(By.LINK_TEXT, link_text)
    return elements[0].get_attribute('href') or None


def find_links(url: str) -> Collection[str]:
    """Return the URLs of all hyperlinks found inside of <a> tags
    on a page. The returned collection of hyperlinks should be unique.

    :param url: URL of the web page to scan
    :return: collection of matching urls
    :raises ValueError: if the url is not valid
    """
    browser = Browser.get_browser()
    try:
        browser.get(url)
    except WebDriverException:
        raise ValueError("Invalid URL")
    elements: Collection[str] = {
            link.get_attribute('href') for link in browser.find_elements(By.TAG_NAME, 'a')
            if link.get_attribute('href')  is not None
            }

    return elements or None
