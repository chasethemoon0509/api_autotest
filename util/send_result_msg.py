
# 调用 fixture，获取测试结果
def send_feishu_msg(pytest_runtest_makereport):
    """
    将测试结果发送到飞书群内

    :param pytest_runtest_makereport:
    :return:
    """
    # 获取钩子函数返回的测试结果
    # 提取测试结果，综合执行用例数，通过用例数，失败用例数，通过率，失败率、测试报告服务器地址等等
    # 调用飞书 SDK 发送到飞书群内


def send_work_weixin_msg(pytest_runtest_makereport):
    """
    将测试结果发送到飞书群内

    :param pytest_runtest_makereport:
    :return:
    """
    # 获取钩子函数返回的测试结果
    # 提取测试结果，综合执行用例数，通过用例数，失败用例数，通过率，失败率、测试报告服务器地址等等
    # 调用企业微信 SDK 发送到企业微信群内
    pass


...
