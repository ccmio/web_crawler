from urllib.parse import urlencode
from pyquery import PyQuery as pq
import requests
base_url = 'https://m.weibo.cn/api/container/getIndex?'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) \
    Chrome/77.0.3865.90 Safari/537.36',
    'Referer': 'https://m.weibo.cn/u/2830678474'
}
print("just for test!")

def get_one_page(offset):
    params = {
        'type': 'uid',
        'value': '2830678474',
        'containerid' : '1076032830678474',
        'page': offset
    }
    rest_url = urlencode(params)
    url = base_url + rest_url
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
    except:
        print('error', requests.ConnectionError.args)


def parse_one_page(page_json):
    if page_json:
        items = page_json.get('data').get('cards')
        for item in items:
            item = item.get('mblog')
            yield {
                '日期': item.get('created_at'),
                '内容': pq(item.get('text')).text(),
                '点赞数': item.get('attitudes_count'),
                '评论数': item.get('comments_count'),
                '设备': item.get('source')
            }


def main(offset):
    page_json = get_one_page(offset)
    for item in parse_one_page(page_json):
        print(item)


if __name__ == '__main__':
    for i in range(10):
        main(i)
