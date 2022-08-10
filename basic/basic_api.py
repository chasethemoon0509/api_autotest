from basic_request import basic_request


class BasicApi:
    def __init__(self, method, url, param=None, data=None, json=None,):
        header = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36', 'Authorization': None}
        self.request_data = {
            'method': method,
            'url': url,
            'param': param,
            'data': data,
            'json': json,
            'header': header
        }

    def add_request_data(self, key, value):
        self.request_data[key] = value
        return self

    def update_param(self, new_value):
        self.request_data['param'] = new_value
        return self

    def update_data(self, new_value):
        self.request_data['data'] = new_value
        return self

    def update_json(self, new_value):
        self.request_data['json'] = new_value
        return self

    def request(self):
        r = basic_request(self.request_data)
        return r.json(), self

    def eq(self, expected, real, msg=None):
        assert real == expected, msg

    def ne(self, expected, real, msg=None):
        assert real != expected, msg

    def lt(self, a, b, msg=''):
        assert a < b, msg

    def le(self, a, b, msg=''):
        assert a <= b, msg

    def gt(self, a, b, msg=''):
        assert a > b, msg

    def ge(self, a, b, msg=''):
        assert a >= b, msg

    def contain(self, a, b, msg=''):
        assert a in b, msg




