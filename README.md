# 欢迎补充与更新


-----
* [入门教程](https://bop.mol.uno/)
* [系统学习Python](http://www.runoob.com/python3/python3-tutorial.html)
* [官方示例代码（最新）](https://github.com/appium/appium/tree/master/sample-code/python)
* [unittest官方文档](https://docs.python.org/3/library/unittest.html)
* [从零开始学自动化测试](https://cloud.tencent.com/developer/column/2319/tag-0)
* [toast消息](https://cloud.tencent.com/developer/article/1087083)

### 文件说明
~~* start.py
一些测试方法的示例，看不明白的可以查看login/login.py~~
* helper.py
一些公用方法
* selector.py
查找元素的示例，包括生成测试报告的使用方式
* login/login.py
登录（退出登录）测试
* HTMLTestRunner_PY3.py
带有饼图的测试报告，打印信息会输出在测试报告中
* HTMLTestReportCN.py
没有饼图的测试报告
### 生成测试报告需要使用命令执行py文件
* python selector.py

#### 通过命令行更新代码（本地代码没有修改的情况下操作）
* git remote -v 查看远程关联仓库地址名称
* origin  http://git.jxsg.local/zhangmm/jxsg_android_test.git (fetch)
* origin  http://git.jxsg.local/zhangmm/jxsg_android_test.git (push)
* git pull origin master 这样就可以更新代码，默认是master（远程分支名称）
* 如果不清楚远程分支名称，可以使用git branch -r 查看远程分支名称
