import requests
import re
import json
print("a")
def get_one_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }
    respongse = requests.get(url=url, headers=headers)
    if respongse.status_code == 200:
        return respongse
    else:
        return None


def info_extract(text):
    patterns = re.compile(
        'board-index-(\d+).*?title="(.*?)".*?data-src="(.*?)@.*?star">\s*(.*?)\s*</p>.*?releasetime">(.*?)</p>.*?integer">(.*?)<.*?(\d)',
        re.S)
    info = re.findall(patterns, text)
    print('info:', info)
    for item in info:
        yield {
            '排名': item[0],
            '电影名': item[1],
            '海报': item[2],
            '主演': item[3][3:],
            '上映时间': item[4][5:],
            '猫眼评分': item[5]+item[6]
        }


def main(offset):
    url = 'http://maoyan.com/board/4'+'?offset='+str(offset)
    doc = get_one_page(url)
    with open('./maoyan_film.txt', 'a') as f:
        for item in info_extract(doc.text):
            f.write(json.dumps(item, ensure_ascii=False) + '\n')


if __name__ == '__main__':
    for i in range(10):
        main(i*10)
