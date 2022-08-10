import loguru


def loga(system_name=None):
    """
    日志收集器
    :param system_name: 标识，用于区分
    :return:
    """
    lg = loguru.logger
    lg.add(f'../log/{system_name}' + '{time}.log', rotation='00:00', enqueue=True, compression="zip", encoding="utf-8")
    return lg




