from api.systema import SystemABasicApi


class GetXXXListApi(SystemABasicApi):
    def __init__(self):
        super(GetXXXListApi, self).__init__(method='get', url='https://www.示例网址.com/api/v1/getxxxList')


