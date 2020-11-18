import json
import pytest
import requests
import xlrd


# todo 打开excle
xl = xlrd.open_workbook(r'D:\bai\Fiddler_test\金融1.1.xlsx')
table = xl.sheets()[0]
rows = table.nrows
nums=[]
for i in range(15, 18):
    datas = {}
    data1 = table.cell(i, 7).value
    datas['casedata'] = data1
    data2 = table.cell(i, 9).value
    datas['expect'] = data2
    nums.append(datas)
# print(nums)

@pytest.fixture(params=nums)
# 测试执行过程
# @pytest.fixture(params=[{'casedata': {"mobilephone": 18812345678, "pwd": 12345687},
#                          'expect': {"status": 0, "code": "20111", "data": None, "msg": "用户名或密码错误"}},
#                         {'casedata': {"mobilephone": 18812345678, "pwd": 123456},
#                          'expect': {"status": 1, "code": "10001", "data": None, "msg": "登录成功"}}])
def register_data(request):
    return request.param

def test_001(register_data):
    url = "http://jy001:8081/futureloan/mvc/api/member/login"
    data3=register_data['casedata']
    # print(data3)
    data4=json.loads(data3)
    r1 = requests.post(url, data=data4)
    # data5=register_data['expect']

    assert r1.json() == register_data['expect']
    assert r1.status_code==200
    print(r1.json())

