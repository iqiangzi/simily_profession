#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/13 13:25
# @Author  : Nxy
# @Site    : 
# @File    : BasePage.py
# @Software: PyCharm
from testCase import MyUnit
from selenium import webdriver
class BasePage(object):
    '''
    页面基础类，用于所有页面的继承
    '''
    burl ="http://168.160.192.92:8080/fuhe24-manage"
    def __init__(self,selenium_driver,base_url= burl,parent=None):
        self.base_url = base_url
        self.driver = selenium_driver
        self.timeout = 30
        self.parent = parent

    def _open(self,url):
        url = self.base_url +url
        self.driver.get(url)

    def find_element(self,*loc):
        return self.driver.find_element(*loc)

    def find_elements(self,*loc):
        return self.driver.find_elements(*loc)

    def open(self,url):
        self._open(url)

    def script(self,src):
        return self.driver.execute_script(src)
    #处理弹出窗口，注意是确认窗口
    def confirm_window(self):
        return self.driver.switch_to.alert().text
    #frame转换
    def user_login_switch(self,id):
        self.driver.switch_to.frame(id)
    #跳到最外层窗口
    def user_switch_default(self):
        self.driver.switch_to.default_content()

if __name__=='__main__':
    s = BasePage(selenium_driver=webdriver.Firefox())
    s._open("/")
    webdriver.Firefox().quit()