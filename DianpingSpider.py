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
    for item in soup.find_all("div", class_="tit"):
        data = dict()
        item = str(item) # 把列表项源码转换成字符串
        # print(item)

        # 创建正则表达式对象用于获取想要的信息
        findTitle = re.compile(r'<h4>(.*?)</h4>')  # 店名
        findLink = re.compile(r'<a.*data-click-name="shop_title_click".*href="(.*?)".*>')  # 店家详情链接

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

        # 保存获取的数据
        print(data)
        SaveToMysql(data)


if __name__ == '__main__':
    print("Work Start")
    main()
    print("Work Completed")
