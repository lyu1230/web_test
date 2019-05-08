# 添加测试文件目录
import HTMLTestRunnerPlugins
import time
import unittest





case_dir = './case'

# 添加测试报告目录
report_dir = './report'

# 命名测试报告文件名---测试报告文件名格式为时间+HTMLReport
# 制作时间格式
now = time.strftime('%Y-%m-%d %H-%M-%S')
report_file = open(report_dir + '\\' + now + 'HTMLReport.html', 'wb')

# 创建测试套件
discover = unittest.defaultTestLoader.discover(case_dir, pattern='*test_login.py')

# 穿件runner
runner = HTMLTestRunnerPlugins.HTMLTestRunner(
                                                title='Ecshop 自动化测试',
                                                description='登录演示',
                                                stream=report_file,
                                                verbosity=2

)
runner.run(discover)
report_file.close()
