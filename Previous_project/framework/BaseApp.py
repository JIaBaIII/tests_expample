import time

from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from config import URL


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = URL

    def find_element(self, locator):
        time.sleep(0.005)
        elem = WebDriverWait(self.driver, 5). \
            until(ec.presence_of_element_located(locator), message=f"Can't find element by locator {locator}")

        def apply_style(s):
            self.driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", elem, s)

        original_style = elem.get_attribute('style')
        apply_style("border: 6px double lightseagreen; "
                    "border-image-outset: 10px; box-shadow: 5px -5px 26px 2px #917CB7, "
                    "10px 10px 22px 0px #000000, 0px 0px 53px 5px #02BBFF;")
        time.sleep(0.15)
        apply_style(original_style)
        return elem

    def find_elements(self, locator):
        time.sleep(0.05)
        return WebDriverWait(self.driver, 5). \
            until(ec.presence_of_all_elements_located(locator), message=f"Can't find elements by locator {locator}")

    def click_on_element(self, locator):
        time.sleep(0.05)
        elem = WebDriverWait(self.driver, 5). \
            until(ec.presence_of_element_located(locator), message=f"Can't click on element by locator {locator}")

        def apply_style(s):
            self.driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", elem, s)
        original_style = elem.get_attribute('style')
        i = 20
        while 100 > i > 0:
            if 60 > i:
                apply_style("border: 2px ridge mediumblue; "
                            f"box-shadow: 0px 0px 45px {-35 + i}px rgba(102, 0, 255, 0.99), "
                            f"inset 0px 0px 35px {-40 + i}px rgba(255, 195, 127, 0.99); ")
                i += 1
            if 80 > i >= 60:
                apply_style(f"border: 3px ridge mediumblue; "
                            f"box-shadow: 0px 0px 30px {-60 + i}px rgba(255, 255, 255, 0.99),"
                            f"inset 0px 0px {90- i}px {80 - i}px rgba(255, 195, 127, 0.99), "
                            f"0px 0px 45px 25px rgba(102, 0, 255, 0.99); ")
                i += 1
                # time.sleep(0.001)
            if 100 > i >= 80:
                apply_style(f"box-shadow: 0px 0px 20px {-80 + i}px rgba(255, 255, 255, 0.99), "
                            f"0px 0px {i - 35}px {90 - i}px rgba(102, 0, 255, 0.99); ")
                i += 1
                time.sleep(0.00001)
        time.sleep(0.00001)
        apply_style(original_style)
        elem.click()
        return time.sleep(0.1)

    def staleness_of_element(self, element, time_wait):
        return WebDriverWait(
            self.driver, time_wait).until(ec.staleness_of(element),
                                          message=f" The element ({element}) is still attached to the DOM")

    def highlight(self, elem):
        """Highlights (blinks) a Selenium Webdriver element"""

        def apply_style(s):
            self.driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", elem, s)

        original_style = elem.get_attribute('style')
        apply_style("border: 7px double lightseagreen; "
                    "border-image-outset: 10px; box-shadow: 5px -5px 26px 2px #917CB7, "
                    "10px 10px 22px 0px #000000, 0px 0px 53px 5px #02BBFF;")
        time.sleep(0.2)
        apply_style(original_style)

    def highlight_click(self, elem):
        """Highlights (blinks) a Selenium Webdriver element"""

        def apply_style(s):
            self.driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", elem, s)

        original_style = elem.get_attribute('style')
        apply_style("border: 7px ridge darkviolet;")

        i = 20
        while 100 > i > 0:
            if 60 > i > 0:
                apply_style("border: 3px ridge mediumblue; "
                            f"box-shadow: 0px 0px 41px {-80 + i}px rgba(102, 0, 255, 0.99), "
                            f"inset 0px 0px 15px {-40+ i}px rgba(255, 195, 127, 0.99); ")
            i += 1
            if 80 > i >= 60:
                apply_style("border: 3px ridge mediumblue; "
                            f"box-shadow: 0px 0px 15px {-55 + i}px rgba(102, 0, 255, 0.99); ")
                i += 1
                time.sleep(0.000001)
                if 100 > i >= 80:
                    apply_style("border: 3px ridge mediumblue; "
                                f"box-shadow: 0px 0px {-35 + i}px {85 - i}px rgba(102, 0, 255, 0.99); ")
                    i += 1
                    time.sleep(0.00001)

        apply_style(original_style)
        elem.click()
        return time.sleep(0.1)

    def go_to_site(self, endpoint=''):
        return self.driver.get(self.base_url + endpoint)
