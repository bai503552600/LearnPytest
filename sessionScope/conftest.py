'''
conftrst.py session 级别的fixture放在这个文件中，名字不能写错。

第一次调用这个fixture执行前置，目录下所有文件执行完，再执行后置。
conftest.py 文件有作用域，对统计目录以及子目录生效。
一个工程中可以有多个conftest.py文件
'''
import pytest

@pytest.fixture(scope='session')
def login():
    print("登录系统")  #前置
    yield
    print("退出登录")  #后置