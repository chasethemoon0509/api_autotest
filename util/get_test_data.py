

def get_data_from_yaml(which_system):
    """
    从 yaml 文件中读取数据，返回测试数据对象。
    为了避免重复读取文件，整个程序运行周期内只会读取文件一次，读取所有的数据，并将其存在 dir 属性中。
    后续再调用此方法时，不会再读取文件，而是返回 dir 属性中存储的数据对象，类型为字典

    :param which_system: 项目名，传什么项目名返回什么项目下维护的测试数据
    :return: 数据字典对象
    """
    pass


def get_data_from_excel(which_system):
    """
    和 get_data_from_yaml 函数类似

    :param which_system:
    :return:
    """
    pass


def get_data_from_csv(which_system):
    """
    和 get_data_from_yaml 函数类型
    :param which_system:
    :return:
    """
    pass

