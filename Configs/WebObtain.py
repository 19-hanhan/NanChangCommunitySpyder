import random
import re
import time

import requests

from Configs.OtherTools import GetMd5
from Configs.MysqlTool import SaveWeb
from Configs.Config import HEADERS, COOKIE, TIMEOUT, HTML_SAVE_URL


# 获取网页源代码
def GetHtml(url):
    cookies = {i.split('=')[0]: i.split('=')[1] for i in COOKIE.split('; ')}
    html = requests.get(url, headers=HEADERS, cookies=cookies, timeout=TIMEOUT).text
    return html


# 从本地获取网页源码
def GetHtmlByLocal(url):
    html = ''
    try:  # 爬过了就直接用
        f = open(HTML_SAVE_URL + GetMd5(url) + '.html', 'r', encoding='utf-8')
        html = f.read()
    except:  # 没爬过就爬一下
        time.sleep(2)
        print('未获取过[{}]源码，重新爬取'.format(url))
        html = GetHtml(url)
        SaveWeb(url, html)  # 保存到本地
        time.sleep(random.randint(1, 5))
    return html


# 根据地址和页码获取当前页url
# （根据网页规则变化）
def GetUrlByPage(url, page):
    return url + 'p-cs300021-nanchang-jingdian-1-' + str(page)


if __name__ == '__main__':
    pass
