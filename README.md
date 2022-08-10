## 整体设计描述

#### 接口组织

每一个接口都将作为一个类来组织。完整的接口继承关系有三层，分别是全局通用的接口类、项目单独的基础接口类、具体到项目中的实际功能接口类。

- BasicApi：封装在 basic 目录下的 basic_api 模块中。主要定义请求数据、参数修改方法、断言方法、请求方法。
- SystemABasicApi：表示项目 A 的基础接口类，放在 api 包中的 __init__.py 文件中，继承全局接口类 BasicApi，同时定义了添加 token 到请求数据字典中的方法。
- GetXXXListApi： 表示具体某个功能的接口，继承 SystemABasicApi 类，给父类传请求方法、接口地址。


#### 用例
用例保存在 `testcase` 包中，每个项目单独存放自己的接口。

一条用例的构成，首先实例化具体某个功能的接口类的对象，然后使用该对象调用请求方法，发送请求，最后再使用此实例对象调用断言方法，大体上分为这三步：

- 实例化要测试的接口类对象
- 使用对象调用修改参数方法、然后调用请求方法，发送请求
- 调用对象的断言方法进行断言

在代码中，大体表现如下：
```python
from api.systema import GetXXXListApi

# 测试类
class TestGetXXXList:
    # 用例/测试函数，无条件默认查询，获取 XXX 的列表
    def test_getlist(self):
        # 实例化接口类的对象
        instance = GetXXXListApi.GetXXXListApi()
        # 发请求
        request_result = instance.request()
        # 断言
        request_result[1].eq(expected='99', real=request_result[0]['total'], msg='所有类型的 XXX 总数有 99 个')
```

#### 封装请求方法

使用 `requests` 库可满足大部分需求，简要代码在 `basic` 包下的 `basic_request.py` 文件中。


#### Token 管理

多个项目有多个 `token`，使用抽象类规范代码，每个子类只要实现获取并返回 `token` 的方法即可，简要代码在 `basic` 目录下的 `basic_token.py` 文件中。

获得的 `token` 会在多个用例中使用，为了不重复登录获取 `token` ，同时也为了保持测试的连贯性，对于 `token` 需要实现单例模式。


#### 测试数据

提供了 `csv`、`excel`、`yaml` 三种数据存储方式，数据存储在 `testdata` 目录下。

同时在 `util` 包中提供了读取测试数据的方法，简要代码在 `get_test_data.py` 文件中。

在一次测试运行周期内，只会进行一次读取文件的操作，第一次读取数据之后，会把数据保存在 `dir` 属性中，在之后需要使用数据的地方直接从 `dir` 属性中读取即可。这样做是为了避免每次都对文件进行读取操作，节省测试时间。

测试数据将会使用 `pytest` 的 `@pytest.mark.parametrize` 装饰器进行参数化。

#### 日志

日志使用 `loguru` 库


#### `conftest`

拓展功能，定义 `fixture`，添加钩子函数，添加自定义命令


#### 自定义命令

定义区分项目、区分环境执行的命令，在执行时，根据命令的值，去执行哪个项目下的用例，哪个环境下的用例


#### 测试报告

测试报告使用 `pytest-html` 完全满足需求，且便于分发。`allure` 强大且美观，但是具体还是要看需要决定。


#### 测试结果通知

主要目的是把通知发送到工作群里，需要对接对于工作群应用的 `SDK` 或开放接口。

发送的消息主要是测试结果的简要统计，以及测试报告所在服务器的存储目录地址。

#### 持续集成

结合 `jenkins` 实现。区分环境制定不同的定时规则。






