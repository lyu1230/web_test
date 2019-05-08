import unittest

import ddt

from common.base import open_browser, Base
from common.operation_excel import OperationExcel
from script.login_script import LoginScript

operation = OperationExcel('./data/test_data.xlsx')
test_data = operation.get_data_info()


@ddt.ddt
class TestLogin(unittest.TestCase):
    def setUp(self):
        """打开浏览器"""
        self.driver = open_browser()
        self.login = LoginScript(self.driver)
        self.base = Base(self.driver)

    @ddt.data(*test_data)
    def test_login(self, data):
        """登录不记住密码"""
        self.login.login_flow(data['username'], data['password'])
        # 验证登录是否成功
        result = self.login.is_success_login(data['username'])
        self.assertEqual(result, data['expect'])

    def tearDown(self):
        """关闭浏览器"""
        self.base.close_browser()


if __name__ == '__main__':
    unittest.main()
