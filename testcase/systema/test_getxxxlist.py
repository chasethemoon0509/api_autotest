from api.systema import GetXXXListApi
from util import loga
import pytest
from util.get_test_data import get_data_from_yaml


# 测试类
class TestGetXXXList:
    # 用例1，无条件默认查询，获取 XXX 的列表
    def test_getlist(self):
        instance = GetXXXListApi.GetXXXListApi()
        # 发请求
        request_result = instance.request()
        # 断言
        request_result[1].eq(expected='99', real=request_result[0]['total'], msg='所有类型的 XXX 总数有 99 个')
        loga('测试类：TestGetXXXList').info('pass')

    # 用例2，设置类型条件，查询 XXX 的列表
    def test_getlist_with_type(self):
        instance = GetXXXListApi.GetXXXListApi()
        # 假设是以 json 传参，查询 type 为 1 的结果
        instance.update_param({'type': 1})
        # 发请求
        request_result = instance.request()
        request_result[1].eq(expected='44', real=request_result[0]['total'], msg='类型为 1 的 XXX 数量有 44 个')

    # 用例3，参数化
    @pytest.mark.parametrize('type', get_data_from_yaml(which_system='systema'))
    def test_getlist_with_xxx(self, type):
        pass

    ...

