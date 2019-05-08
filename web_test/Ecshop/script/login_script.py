from common.base import open_browser
from page.login_page import LoginPage, login_url


class LoginScript:
    def __init__(self,driver):
        """导入浏览器和实例化page类"""
        self.login_page = LoginPage(driver)
        self.login_page.open_url(login_url)

    def login_flow(self, username, password):
        """
        点击登录不记住密码
        :param username:
        :param password:
        :return:
        """
        self.login_page.input_username(username)
        self.login_page.input_password(password)
        self.login_page.click_submit()

    def login_flow_remember(self, username, password):
        """
        点击登录记住密码
        :param username:
        :param password:
        :return:
        """
        self.login_page.input_username(username)
        self.login_page.input_password(password)
        self.login_page.click_remember()
        self.login_page.click_submit()

    def is_success_login(self, username):
        """
        判断登录是否成功
        :return:
        """
        login_success_loc = ("class name", "f4_b")
        result = self.login_page.is_text_in_element(login_success_loc, username)
        return result
    def password_question(self):
        """密码问题找回密码"""
        self.login_page.click_password_qeustion()
    def email(self):
        """邮件找回密码"""
        self.login_page.click_email()
    def message(self):
        """短信验证找回密码"""
        self.login_page.click_message()
    def home_page(self):
        """首页"""
        self.login_page.click_home_page()
    def now_register(self):
        """立即注册"""
        self.login_page.click_register()



if __name__ == '__main__':
    driver = open_browser()
    login = LoginScript(driver)
    username = '诸葛亮'
    password = 'Test123456'
    login.login_flow(username, password)


