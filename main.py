from HTMLTestRunner import HTMLTestRunner # 运行器; 另外 HTMLTestRunner 为生成页面测试报告的工具
import  unittest
import os
tests = unittest.defaultTestLoader.discover(os.getcwd(),pattern="Test*.py")
# 使用运行器
runner = HTMLTestRunner.HTMLTestRunner(
    title="HKR登陆测试",
    description="HKR登陆详细测试【成功，失败】",
    verbosity=1,
    stream = open(file="HKR测试报告.html",mode="w+",encoding="utf-8")
)



runner.run(tests)







