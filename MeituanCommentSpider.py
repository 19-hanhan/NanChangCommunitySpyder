import random
import time

from selenium.webdriver.common.by import By

from Configs.Config import BASE_URL
from Configs.MysqlTool import GetColFromMysql, SaveToMysql
from Configs.SeleniumTool import LoginWebByCookie, OpenWebBySelenium, LoginWebByYourself, UpdateUrl, ScrollTop, SaveMyCookie


def main():
    ### 打开浏览器 ###
    browser = LoginWebByCookie('https://nc.meituan.com/')

    commentList = GetColFromMysql('detail')
    # print(commentList)
    for commentUrl in commentList:
        UpdateUrl(browser, commentUrl) # 刷新到新的评论

        while True:
            if browser.current_url != commentUrl:
                input('The current page is not in the data list, please do it manually')

            # 获取当前页数据
            ScrollTop(browser)
            time.sleep(random.randint(1, 5))
            GetData(browser, commentUrl)
            # return

            # 判断是否有下一页
            try:
                time.sleep(random.randint(1, 5))
                turnPageButton = browser.find_element(By.XPATH, r'//span[@class="iconfont icon-btn_right"]')
                # print(browser.title)
                turnPageButton.click()
            except:
                break


# 获取并保存数据
def GetData(browser, commentUrl):
    commentList = browser.find_elements(By.XPATH, '//div[@class="com-cont"]/div/div[@class="list clear"]')
    # print(commentList)
    for commentItem in commentList:
        data = dict()

        data['url'] = commentUrl

        try:
            commentName = commentItem.find_element(By.CLASS_NAME, 'name')
            data['username'] = commentName.text
        except:
            data['username'] = ''

        try:
            commentContext = commentItem.find_element(By.CLASS_NAME, 'desc')
            data['context'] = commentContext.text
        except:
            data['context'] = ''

        try:
            commentTime = commentItem.find_element(By.CLASS_NAME, 'date')
            data['time'] = commentTime.text
        except:
            data['time'] = ''

        print(data)
        SaveToMysql(data)


if __name__ == '__main__':
    main()
    # SaveMyCookie('https://passport.meituan.com/account/unitivelogin')