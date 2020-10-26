import os
import requests
from hashlib import md5
from urllib.parse import urlencode
from multiprocessing.pool import Pool

base_url = 'https://www.toutiao.com/api/search/content/?'

print("just for test2")
def get_one_page(offset):
    params = {
        'app_name': 'web_search',
        'offset': offset,
        'format': 'json',
        'keyword': '街拍',
        'autoload': 'true',
        'count': '20',
        'en_qc': '1',
        'cur_tab': '1',
        'from': 'search_tab',
        'pd': 'synthesis',
        'timestamp': '1570272638029'
    }
    url = base_url + urlencode(params)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
    except:
        print('抓取失败')


def parse_one_page(json):
    items = json.get('data')
    for item in items:
        title = item.get('title')
        list_item = item.get('image_list')
        if list_item:
            for image in list_item:
                yield {
                    'url': image.get('url'),
                    'title': title
                }


def save_image(item):
    root_path = 'toutiao/' + item.get('title')
    if not os.path.exists(root_path):
        os.makedirs(root_path)
    try:
        image = requests.get(item.get('url'))
        if image.status_code == 200:
            image_path = '{0}/{1}.{2}'.format(root_path, md5(image.content).hexdigest(), 'jpg')
            if not os.path.exists(image_path):
                with open(image_path, 'wb') as f:
                    f.write(image.content)
                    print('下载成功')
            else:
                print('图片已存在')
    except:
        print('下载图片出错')


def main(offset):
    json = get_one_page(offset)
    for item in parse_one_page(json):
        print(item)
        save_image(item)


if __name__ == '__main__':
    pool = Pool()
    pool.map(main, [i*20 for i in range(0, 2)])
    pool.close()
    pool.join()
