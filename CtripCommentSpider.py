import time

from selenium.webdriver.common.by import By

from Configs.Config import BASE_URL
from Configs.MysqlTool import GetColFromMysql, SaveToMysql
from Configs.SeleniumTool import LoginWebByCookie, OpenWebBySelenium, LoginWebByYourself, UpdateUrl, ScrollTop


def main():
    ### 打开浏览器 ###
    browser = OpenWebBySelenium('https://you.ctrip.com/')

    commentList = GetColFromMysql('link')
    for commentUrl in commentList:
        UpdateUrl(browser, commentUrl) # 刷新到新的景点评论

        while True:
            # 获取当前页数据
            ScrollTop(browser)
            GetData(browser, commentUrl)
            # return

            # 判断是否有下一页
            try:
                time.sleep(1)
                turnPageButton = browser.find_element(By.XPATH, r'//li[@title="下一页" and @class=" ant-pagination-next"]/span/a')
                # print(browser.title)
                turnPageButton.click()
            except:
                break


# 获取并保存数据
def GetData(browser, commentUrl):
    commentList = browser.find_elements(By.CLASS_NAME, 'commentItem')
    for commentItem in commentList:
        data = dict()

        data['url'] = commentUrl

        try:
            commentName = commentItem.find_element(By.CLASS_NAME, 'userName')
            data['username'] = commentName.text
        except:
            data['username'] = ''

        try:
            commentContext = commentItem.find_element(By.CLASS_NAME, 'commentDetail')
            data['context'] = commentContext.text
        except:
            data['context'] = ''

        try:
            commentTime = commentItem.find_element(By.CLASS_NAME, 'commentTime')
            data['time'] = commentTime.text
        except:
            data['time'] = ''

        print(data)
        SaveToMysql(data)


if __name__ == '__main__':
    main()