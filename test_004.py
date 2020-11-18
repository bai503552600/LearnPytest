'''
fixture作用域
默认是function级别的。 有function、module、class、session级别
'''
import pytest

@pytest.fixture(scope='class') #每个类调用一次，在类中首次调用这个fixture的时候执行前置，类方法执行完执行后置
def login():
    print("系统登录")  #前置
    yield
    print("退出登录")  #后置

class Test_Query():
    def test_case1(self):
        print("测试查询1")
    def test_case2(self,login):
        print("测试查询2")
    def test_case3(self):
        print("测试查询3")

class Test_Delete():
    def test_csae1(self,login):
        print("测试删除1")
    def test_csae2(self):
        print("测试删除2")
    def test_csae3(self):
        print("测试删除3")

