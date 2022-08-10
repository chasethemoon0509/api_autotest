"""
    pytest 的 conftest 文件，定义某些拓展功能
"""
import pytest


@pytest.fixture
def query_mysql(db, sql):
    """
    连接指定数据库，进行查询，返回数据
    :param db:
    :param sql:
    :return:
    """
    # 连接
    # 执行 sql 语句
    # 关闭连接
    # 返回数据
    pass


@pytest.fixture
def pytest_runtest_makereport():
    """
    pytest 内置钩子函数，获取测试结果

    :return:
    """
    pass


def pytest_addoption(parser):
    """
    添加自定义命令，--runwhich，表示运行哪个项目

    :param parser:
    :return:
    """

    parser.addoption('--runwhich',
                     action='store',
                     default='all',
                     choices=['systema', 'systemb', '...', 'allsystem'],
                     help='指定运行哪个项目的测试用例')


@pytest.fixture
def get_runwhich(request):
    """
    获取命令 --runwhich 的值
    :return:
    """
    which = request.config.getoption('--runwhich')
    return which