import requests
from util import loga


def basic_request(requset_data):
    items = {key: requset_data[key] for key in requset_data.keys() if requset_data[key] is not None}
    try:
        r = requests.request(items.get('method'), items.get('url'), **{key: items[key] for key in items.keys() if key not in ['mehtod', 'url']})
        loga().info(f'接口：{r.url} 请求成功')
        return r
    except Exception as e:
        loga().exception(f'发送请求时出现异常错误 {e}')




