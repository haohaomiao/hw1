from cgi import test
import unittest

from app.checkers.user import register_params_check


class BasicTestCase(unittest.TestCase):
    '''
    TODO: 在这里补充注册相关测试用例
    '''
    def test_register_params_check(self):
    # 正常测例 
        # 1.username和password长度为下边界done
        self.assertEqual(register_params_check({'username':'test1',
                                                'password':'Test1_12',
                                                'nickname':'nickname',
                                                'url':'https://baidu.com',
                                                'mobile':'+86.123456789012',
                                                'magic_number':'114514'}),("ok",True))
        # 2.username和password长度为上边界done
        self.assertEqual(register_params_check({'username':'testtesttes1',
                                                'password':'Test1_test12345',
                                                'nickname':'nickname',
                                                'url':'https://baidu.com',
                                                'mobile':'+86.123456789012',
                                                'magic_number':'114514'}),("ok",True))
    # username异常测例
        # 1.缺少username字段done
        self.assertEqual(register_params_check({
                                                'password':'Test1_12',
                                                'nickname':'nickname',
                                                'url':'https://baidu.com',
                                                'mobile':'+86.123456789012',
                                                'magic_number':'114514'}),("username",False))
        # 2.lenth < 5done
        self.assertEqual(register_params_check({'username':'test',
                                                'password':'Test1_12',
                                                'nickname':'nickname',
                                                'url':'https://baidu.com',
                                                'mobile':'+86.123456789012',
                                                'magic_number':'114514'}),("username",False))
        # 3.len > 12done
        self.assertEqual(register_params_check({'username':'test1test1123',
                                                'password':'Test1_12',
                                                'nickname':'nickname',
                                                'url':'https://baidu.com',
                                                'mobile':'+86.123456789012',
                                                'magic_number':'114514'}),("username",False))
        # 4.缺少字母done
        self.assertEqual(register_params_check({'username':'12345',
                                                'password':'Test1_12',
                                                'nickname':'nickname',
                                                'url':'https://baidu.com',
                                                'mobile':'+86.123456789012',
                                                'magic_number':'114514'}),("username",False))
        # 5.缺少数字done
        self.assertEqual(register_params_check({'username':'testa',
                                                'password':'Test1_12',
                                                'nickname':'nickname',
                                                'url':'https://baidu.com',
                                                'mobile':'+86.123456789012',
                                                'magic_number':'114514'}),("username",False))
        # 6.字母在数字后面
        self.assertEqual(register_params_check({'username':'1test',
                                                'password':'Test1_12',
                                                'nickname':'nickname',
                                                'url':'https://baidu.com',
                                                'mobile':'+86.123456789012',
                                                'magic_number':'114514'}),("username",False))
    # password异常测例
        # 1.缺少password
        self.assertEqual(register_params_check({'username':'test1',
                                                'nickname':'nickname',
                                                'url':'https://baidu.com',
                                                'mobile':'+86.123456789012',
                                                'magic_number':'114514'}),("password",False))
        # 2.len<8
        self.assertEqual(register_params_check({'username':'test1',
                                                'password':'Test1_1',
                                                'nickname':'nickname',
                                                'url':'https://baidu.com',
                                                'mobile':'+86.123456789012',
                                                'magic_number':'114514'}),("password",False))
        # 3.len>15
        self.assertEqual(register_params_check({'username':'test1',
                                                'password':'Test1_1290123456',
                                                'nickname':'nickname',
                                                'url':'https://baidu.com',
                                                'mobile':'+86.123456789012',
                                                'magic_number':'114514'}),("password",False))
        # 4.缺少A
        self.assertEqual(register_params_check({'username':'test1',
                                                'password':'test1_12',
                                                'nickname':'nickname',
                                                'url':'https://baidu.com',
                                                'mobile':'+86.123456789012',
                                                'magic_number':'114514'}),("password",False))
        # 5.缺少a
        self.assertEqual(register_params_check({'username':'test1',
                                                'password':'TEST1_12',
                                                'nickname':'nickname',
                                                'url':'https://baidu.com',
                                                'mobile':'+86.123456789012',
                                                'magic_number':'114514'}),("password",False))
        # 6.缺少数字
        self.assertEqual(register_params_check({'username':'test1',
                                                'password':'Testa_bc',
                                                'nickname':'nickname',
                                                'url':'https://baidu.com',
                                                'mobile':'+86.123456789012',
                                                'magic_number':'114514'}),("password",False))
        # 7.缺少标点
        self.assertEqual(register_params_check({'username':'test1',
                                                'password':'Test1a12',
                                                'nickname':'nickname',
                                                'url':'https://baidu.com',
                                                'mobile':'+86.123456789012',
                                                'magic_number':'114514'}),("password",False))
        # 8.出现其它标点
        self.assertEqual(register_params_check({'username':'test1',
                                                'password':'Test1%12',
                                                'nickname':'nickname',
                                                'url':'https://baidu.com',
                                                'mobile':'+86.123456789012',
                                                'magic_number':'114514'}),("password",False))
    # nickname异常测例
        # 1.缺失nickname
        self.assertEqual(register_params_check({'username':'test1',
                                                'password':'Test1_12',
                                                'url':'https://baidu.com',
                                                'mobile':'+86.123456789012',
                                                'magic_number':'114514'}),("nickname",False))
    # url异常测例
        # 1.url缺失
        self.assertEqual(register_params_check({'username':'test1',
                                                'password':'Test1_12',
                                                'nickname':'nickname',
                                                'mobile':'+86.123456789012',
                                                'magic_number':'114514'}),("url",False))
        # 2.协议错误
        self.assertEqual(register_params_check({'username':'test1',
                                                'password':'Test1_12',
                                                'nickname':'nickname',
                                                'url':'htps://baidu.com',
                                                'mobile':'+86.123456789012',
                                                'magic_number':'114514'}),("url",False))
        self.assertEqual(register_params_check({'username':'test1',
                                                'password':'Test1_12',
                                                'nickname':'nickname',
                                                'url':'https123://baidu.com',
                                                'mobile':'+86.123456789012',
                                                'magic_number':'114514'}),("url",False))
        self.assertEqual(register_params_check({'username':'test1',
                                                'password':'Test1_12',
                                                'nickname':'nickname',
                                                'url':'baidu.com',
                                                'mobile':'+86.123456789012',
                                                'magic_number':'114514'}),("url",False))
        # 3.域名 长度过长
        self.assertEqual(register_params_check({'username':'test1',
                                                'password':'Test1_12',
                                                'nickname':'nickname',
                                                'url':'https://baidu.com.baidu.com.baidu.com.baiduaa.com',
                                                'mobile':'+86.123456789012',
                                                'magic_number':'114514'}),("url",False))
        # 4.域名 最后一段纯数字
        self.assertEqual(register_params_check({'username':'test1',
                                                'password':'Test1_12',
                                                'nickname':'nickname',
                                                'url':'https://baidu.123',
                                                'mobile':'+86.123456789012',
                                                'magic_number':'114514'}),("url",False))
        # 5.域名 连字符为首尾字符
        self.assertEqual(register_params_check({'username':'test1',
                                                'password':'Test1_12',
                                                'nickname':'nickname',
                                                'url':'https://baidu.-com',
                                                'mobile':'+86.123456789012',
                                                'magic_number':'114514'}),("url",False))
# 手机号异常测例
        # 1.缺少手机号
        self.assertEqual(register_params_check({'username':'test1',
                                                'password':'Test1_12',
                                                'nickname':'nickname',
                                                'url':'https://baidu.com',
                                                'magic_number':'114514'}),("mobile",False))
        # 2.区号异常测例
        self.assertEqual(register_params_check({'username':'test1',
                                                'password':'Test1_12',
                                                'nickname':'nickname',
                                                'url':'https://baidu.com',
                                                'mobile':'86.123456789012',
                                                'magic_number':'114514'}),("mobile",False))
        self.assertEqual(register_params_check({'username':'test1',
                                                'password':'Test1_12',
                                                'nickname':'nickname',
                                                'url':'https://baidu.com',
                                                'mobile':'+786.123456789012',
                                                'magic_number':'114514'}),("mobile",False))
        # 3.手机号异常测例
        self.assertEqual(register_params_check({'username':'test1',
                                                'password':'Test1_12',
                                                'nickname':'nickname',
                                                'url':'https://baidu.com',
                                                'mobile':'+86.12345678901',
                                                'magic_number':'114514'}),("mobile",False))
        self.assertEqual(register_params_check({'username':'test1',
                                                'password':'Test1_12',
                                                'nickname':'nickname',
                                                'url':'https://baidu.com',
                                                'mobile':'+86.1234567890123',
                                                'magic_number':'114514'}),("mobile",False))
    # 幸运数字测例
        # 1.幸运数字缺失
        self.assertEqual(register_params_check({'username':'test1',
                                                'password':'Test1_12',
                                                'nickname':'nickname',
                                                'url':'https://baidu.com',
                                                'mobile':'+86.123456789012',
                                                'magic_number':''}),("ok",True))
        self.assertEqual(register_params_check({'username':'test1',
                                                'password':'Test1_12',
                                                'nickname':'nickname',
                                                'url':'https://baidu.com',
                                                'mobile':'+86.123456789012'}),("ok",True))
        


if __name__ == '__main__':
    unittest.main()
