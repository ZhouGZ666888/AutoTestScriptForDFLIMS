import unittest
from functools import wraps


def CustomSkip(func):
    @wraps(func)
    def wrappend(self):
        if self._outcome.result.failures or self._outcome.result.errors:
            raise unittest.SkipTest(func.__name__, self._outcome.result.failures[0][0]._testMethodName)
        func(self)

    return wrappend




def skip_dependon(depend=""):
    """
    存在依赖关系的用例，依赖用例失败，则被依赖用例跳过执行
    :param depend: 依赖的用例函数名，默认为空
    :return: wraper_func
    """
    def wraper_func(test_func):
        @wraps(test_func)  # @wraps：避免被装饰函数自身的信息丢失
        def inner_func(self):
            if depend == test_func.__name__:
                raise ValueError("{} cannot depend on itself".format(depend))
            # print("self._outcome", self._outcome.__dict__)
            # 此方法适用于python3.4 +
            # 如果是低版本的python3，请将self._outcome.result修改为self._outcomeForDoCleanups
            # 如果你是python2版本，请将self._outcome.result修改为self._resultForDoCleanups
            failures = str([fail[0] for fail in self._outcome.result.failures])
            errors = str([error[0] for error in self._outcome.result.errors])
            skipped = str([error[0] for error in self._outcome.result.skipped])
            flag = (depend in failures) or (depend in errors) or (depend in skipped)
            if failures.find(depend) != -1:
                # 输出结果 [<__main__.TestDemo testMethod=test_login>]
                # 如果依赖的用例名在failures中，则判定为失败，以下两种情况同理
                # find()方法：查找子字符串，若找到返回从0开始的下标值，若找不到返回 - 1
                test = unittest.skipIf(flag, "{} failed".format(depend))(test_func)
            elif errors.find(depend) != -1:
                test = unittest.skipIf(flag, "{} error".format(depend))(test_func)
            elif skipped.find(depend) != -1:
                test = unittest.skipIf(flag, "{} skipped".format(depend))(test_func)
            else:
                test = test_func
            return test(self)
        return inner_func
    return wraper_func


class TestDemo1(unittest.TestCase):

    def test_login(self):
        print("test_login")
        self.assertEqual(1, 2)  # 这里让登录判断为失败

    @skip_dependon(depend="test_login")  # 此用例依赖于第一个用例
    def test_logout(self):
        print("test_logout")
        self.assertEqual(1, 1)

    @skip_dependon(depend="test_logout")  # 此用例依赖于第二个用例
    def test_1(self):
        print("test1")

    @skip_dependon(depend="test_1")  # 此用例依赖于第三个用例
    def test_2(self):
        print("test2")




class TestDemo(unittest.TestCase):

    def test_1(self):
        print('第一个测试用例')

    @CustomSkip
    def test_a(self):
        self.assertEqual(1, 2)

    @CustomSkip
    def test_b(self):
        print('测试用例bbbbb')
        self.assertEqual(1, 3)

    @CustomSkip
    def test_c(self):
        print('测试用例ccccc')


if __name__ == '__main__':
    unittest.main()
