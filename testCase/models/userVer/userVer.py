#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-03-14 14:19:28
# @Author  : Nxy
# @Site    : 
# @File    : userVer.py
# @Software: PyCharm
from selenium import  webdriver
import unittest
from testCase.pageObj.basePage import BasePage
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from time import sleep
class UserVer(BasePage):
    #Action
    login_username_loc=(By.ID,"userid")
    login_password_loc=(By.ID,"password")
    login_button_loc=(By.XPATH,"/html/body/form/div[5]/div/div[1]/div[6]/input")
    user_login_success_href=(By.CSS_SELECTOR,"li.profile.single")
    #登录用户名
     #登录用户名
    def login_username(self,username):
        self.find_element(*self.login_username_loc).clear()
        self.find_element(*self.login_username_loc).send_keys(username)
    #登录密码
    def login_password(self,password):
        self.find_element(*self.login_password_loc).clear()
        self.find_element(*self.login_password_loc).send_keys(password)
    #登录按钮
    def login_button(self):
        self.find_element(*self.login_button_loc).click()
    #定义统一登录入口
    def user_login(self,username,password):
        '''获取的用户名密码登录'''
        self.open("")
        self.login_username(username)
        self.login_password(password)
        self.login_button()
        sleep(5)

    #用户登录成功
    def user_login_success(self):
        self.find_element(*self.user_login_success_href).click()

    user_error_remind_loc=(By.ID,"useridError")
    pawd_error_remind_loc=(By.ID,"passwordError")
    user_login_success_loc=(By.XPATH,"/html/body/div[1]/div[5]/div/div[2]/div/span[1]")


    #用户名错误提示
    def user_error_remind(self):
        return self.find_element(*self.user_error_remind_loc).text
    #密码错误提示
    def pawd_error_remind(self):
        return self.find_element(*self.pawd_error_remind_loc).text
    #登录成功后显示的用户名
    def user_login_success_verify(self):
        return self.find_element(*self.user_login_success_loc).text

    def userRegist(self):
        pass
    def forgetPwd(self):
        pass
    def userLogin(self):
        pass
