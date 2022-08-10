from abc import ABCMeta, abstractmethod


class Token(metaclass=ABCMeta):
    @abstractmethod
    def get_token(self):
        pass


# 实现系统 A 获取 token 的方法
class SystemAToken(Token):
    def get_token(self):
        pass


# 实现系统 B 获取 token 的方法
class SystemBToken(Token):
    def get_token(self):
        pass


...


# Singleton Module Class Instance
a_token = SystemAToken()
b_token = SystemBToken()