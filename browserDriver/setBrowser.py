#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/02/12 9:38
# @Author  : Nxy
# @Site    :
# @File    : setBrowser.py
# @Software: PyCharm

''' 在测试中启动浏览器'''
from selenium import webdriver
class setBrowser ():

    """
    练习启动各种浏览器：Firefox， Chrome， IE
    练习启动各种浏览器的同时加载插件：Firefox， Chrome， IE
    """
    def startFirefox (self):
        """这里启动firefox 有别于python2 ，需要用户自行下载驱动
        在地址： https://github.com/mozilla/geckodriver/releases/tag/v0.11.1
        将下载后的文件解压放在firefox 的安装目录下，并将firefox【 的按住那个目录配置在path中
        重新打开 项目即可启动firefox"""
        driver = webdriver.Firefox ()
        return driver

    '''
    打开chrome浏览器
    driverPath： chrome 浏览器的驱动放置位置
    '''
    def startChrome (self, driverPath):
        driver = webdriver.Chrome (driverPath)  # 调用chrome浏览器
        return driver
    '''
    打开ie浏览器，目前win10 系统是 Microsoft Edge
    而不是ie 所以该方法在win10 不可用
    driverPath： ie 浏览器的驱动放置位置
    '''
    def startIE (self,driverPath):
        driver = webdriver.Ie (driverPath)
        return driver
if __name__ == '__main__':
    b = setBrowser ()
    # driver = b.startChromeNoUrl("E:\\PyCharm_Workspace\\TestFrame\\com\\browserDriver\\chromedriver.exe")
    # driver.get("http://www.jd.com")
    # b.getElementDisplay(driver,'xpath','//*[@id="ttbar-login"]/a[1]')
    # b.startIE("http://www.baidu.com","E:\\PyCharm_Workspace\\TestFrame\\com\\browserDriver\\IEDriverServer.exe")
    d= b.startFirefox ()
    d.get("http://www.baidu.com")
   #  b.startChrome("http://www.baidu.com","E:\\PyCharm_Workspace\\TestFrame\\com\\browserDriver\\chromedriver.exe")
