import re

from bs4 import BeautifulSoup

from Configs.MysqlTool import SaveToMysql
from Configs.Config import BASE_URL, MAX_PAGES
from Configs.WebObtain import *


def main():
    # 获取数据
    for page in range(1, MAX_PAGES + 1):
        # 获取网页源码，在本地和网页中都找一遍
        PageUrl = GetUrlByPage(BASE_URL, page)
        html = GetHtmlByLocal(PageUrl)

        # 解析网页源码，获取并保存数据
        GetDataByHtml(html)


# 从html中获取并保存数据
def GetDataByHtml(html):
    soup = BeautifulSoup(html, "html.parser")
    for item in soup.find_all("div", class_="abstract-item clearfix"):
        data = dict()
        item = str(item) # 把列表项源码转换成字符串

        # 创建正则表达式对象用于获取想要的信息
        findTitle = re.compile(r'<div class="list-item-desc-top"><a.*>(.*)</a>.*</div>')  # 店名
        findLink = re.compile(r'<a class="abstract-pic grey" href="(.*?)".*>.*</a>')  # 店家详情链接
        findScore = re.compile(r'<div class="item-eval-info clearfix"><div class="rate-stars">.*</div><span>(.*?)<!-- -->分</span><span class="highlight">.*</span></div>') # 评分
        findCommentNum = re.compile(r'<span class="highlight">(.*?)<!-- -->人评论</span>') # 评论数量
        findPrice = re.compile(r'<div class="item-price-info"><span>人均 ¥ <!-- -->(.*?)</span> </div>')

        try:
            title = re.findall(findTitle, item)[0]
            data['title'] = title
        except:
            print('Title Error')
            data['title'] = ''

        try:
            link = re.findall(findLink, item)[0]
            data['link'] = link
        except:
            print('Link Error')
            data['link'] = ''

        try:
            score = re.findall(findScore, item)[0]
            data['score'] = score
        except:
            print('Score Error')
            data['score'] = ''

        try:
            commentNum = re.findall(findCommentNum, item)[0]
            data['comment_num'] = commentNum
        except:
            print('Comment Num Error')
            data['comment_num'] = ''

        try:
            price = re.findall(findPrice, item)[0]
            data['price'] = price
        except:
            print('Price Error')
            data['price'] = ''

        # 保存获取的数据
        print(data)
        SaveToMysql(data)


if __name__ == '__main__':
    main()
