import json

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


# 不登录进入网站
def OpenWebBySelenium(url):
    browser = GetChromeBrowser()
    browser.get(url)
    return browser


# 手动登录进入网站
def LoginWebByYourself(url):
    browser = GetChromeBrowser()
    browser.get(url)
    input('If you are already logged in, press enter to continue...')
    return browser


# 通过Cookie登录任意网站（未完成不可使用）
def LoginWebByCookie(url):
    browser = GetChromeBrowser()
    browser.get(url)

    #从cookies.txt文件读取cookies
    f2 = open("Configs/Utils/cookies.txt")
    cookies = json.loads(f2.read())

    #使用cookies登录
    for cook in cookies:
        browser.add_cookie(cook)

    #刷新页面
    browser.refresh()
    return browser


# 保存登录用的Cookie
def SaveMyCookie(url):
    browser = LoginWebByYourself(url)

    # 获取cookie
    cookies = browser.get_cookies()

    # cookie保存到cookies.txt文件
    f = open("Configs/Utils/cookies.txt", "w")
    f.write(json.dumps(cookies))


# 传入浏览器对象、账号和密码登录美团
def LoginMeiTuanByMessage(url, usr, pwd):
    # 打开网页
    browser = GetChromeBrowser()
    browser.get(url)

    print('登录信息录入中...')
    # 点击授权按钮
    agreeButton = browser.find_element(By.ID, 'user-agreement-wrap-text-circle')
    agreeButton.click()

    # 输入账号
    accountInput = browser.find_element(By.ID, 'login-email')
    accountInput.send_keys(usr)

    # 输入密码
    accountInput = browser.find_element(By.ID, 'login-password')
    accountInput.send_keys(pwd)

    # 点击登录
    print('录入完成，正在登录...')
    loginButton = browser.find_element(By.NAME, 'commit')
    loginButton.click()
    # try:
    #     print('清除弹窗中...')
    #     brower.switch_to.alert.accept()
    # except Exception:
    #     print('无弹窗')

    return browser


# 获取Chrome浏览器对象方法
def GetChromeBrowser():
    options = Options()
    # 隐藏：正在受到自动软件的控制的状态
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)

    browser = webdriver.Chrome(executable_path='venv/Scripts/chromedriver.exe', options=options)

    # 修改 webdriver 值
    browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"
    })

    return browser


# 更新网页网址
def UpdateUrl(browser, url):
    browser.get(url)


# 滚动到页面顶端
def ScrollTop(browser):
    js = "window.scrollTo(0,0)"
    browser.execute_script(js)


if __name__ == '__main__':
    pass