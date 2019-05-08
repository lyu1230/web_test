from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def open_browser(browser='chrome'):
    """打开浏览器"""
    driver = None
    if browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    elif browser == 'ie':
        driver = webdriver.Ie()
    else:
        print("请输入正确浏览器,例如,chrome,firefox,ie")
    return driver


class Base():
    def __init__(self, driver):
        """初始化方法"""
        self.driver = driver

    def open_url(self, url):
        """打开网页"""
        self.driver.get(url)
        # 窗口最大化
        self.driver.maximize_window()

    def find_element(self, locator, timeout=10):
        """定位一个元素"""

        element = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
        return element

    def find_elements(self, locator, timeout=10):
        """
        定位一组元素
        :param locator:
        :param timeout:
        :return:
        """
        elements = WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))
        return elements

    def click_element(self, locator, timeout=10):
        """
        元素点击
        :param locator:
        :param timeout:最大等待时间
        :return:
        """
        element = self.find_element(locator=locator, timeout=timeout)
        element.click()

    def send_keys(self,locator,text,timeout=10):
        """元素输入"""
        element=self.find_element(locator=locator,timeout=timeout)
        element.clear()
        element.send_keys(text)
    def is_text_in_element(self,locator,text,timeout=10):
        """
        判断文本是否存在元素中,是则返回True,不是则返回false
        :param locator: 定位器
        :param text: 判断文本
        :param timeout:
        :return:
        """
        try:
            result=WebDriverWait(self.driver,timeout=timeout).until(EC.text_to_be_present_in_element(locator,text))
            return result
        except:
            return False

    def is_value_in_element(self,locator,value,timeout):
        """
        判断value是否存在元素中,是则返回True,不是则返回false
        :param locator:
        :param value:
        :param timeout:
        :return:
        """
        try:
            result=WebDriverWait(self.driver,timeout=timeout).until(EC.text_to_be_present_in_element_value(locator,value))
            return result
        except:
            return False
    def close_browser(self):
        """
        关闭浏览器
        :return:
        """
        self.driver.quit()

if __name__ == '__main__':
    pass
