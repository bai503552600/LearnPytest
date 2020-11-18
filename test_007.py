'''
1.接口测试场景比较难模拟，需要大量的工作才能完成
2.依赖第三方的接口，但是第三方的接口没有开发完成
测试环境不充分的情况下，怎么做接口测试？ 使用Mock来模拟
'''
import requests
import mock
import json


class Alipay:
    def zhifu(self, data):
        # 接口功能尚未开发完成。
        # 接口地址、get/post 、入参、返回值已经定义好，有对应的接口文档
        r = requests.post("http://zhifubao.com/pay", data=data).json()
        return r


class Tixian:
    def test_tixian(self, data):
        r = requests.post("http://jy001:8081/futureloan/mvc/api/member/withdraw", data=data).json()
        return r


class Chongzhi:
    def test_chongzhi(self, data):
        r = requests.post("http://jy001:8081/futureloan/mvc/api/member/recharge", data=data).json()
        return r


class TestMock:
    def test_alipay(self):
        # 对要模拟的类创建一个对象
        aliPay = Alipay()
        tixian = Tixian()
        chongzhi = Chongzhi()

        # 模拟zhifu的返回值为{"code":200,"msg":"支付成功"}
        # 接口完成后注掉该行
        # aliPay.zhifu = mock.Mock(return_value={"code": 200, "msg": "支付成功"})
        # 调用zhifu接口
        # data = {"OrderId": "215464", "Amount": 153.5, "Type": "支付宝"}
        # r = aliPay.zhifu(data)

        data = {"mobilephone": 18812345678, "amount": 100000}
        data2 = {"mobilephone": 18812345678, "amount": 1000}
        # chongzhi.test_chongzhi = mock.Mock(return_value={"code": 200, "msg": "充值成功"})
        tixian.test_tixian = mock.Mock(return_value={"code": 200, "msg": "取现成功"})
        r1 = chongzhi.test_chongzhi(data)

        assert r1['msg']=='充值成功'
        assert r1['code']=='10001'
        print(r1)


        r2 = tixian.test_tixian(data2)
        assert r2['msg'] == '取现成功'
        print(r2)

