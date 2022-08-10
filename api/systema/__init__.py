"""
    系统/项目 a 的基础 api 构造
"""
from basic import BasicApi
from basic import basic_token


class SystemABasicApi(BasicApi):
    def set_token(self):
        self.request_data['header']['Authorization'] = basic_token.a_token


__all__ = ['SystemABasicApi']



