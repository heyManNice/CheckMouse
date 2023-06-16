"""
功能:项目程序入口
日期:2023年3月17日
"""
import webview
import bootUI
import warn
import dpi
import login
import json_database
import index


if __name__ == '__main__':
    alldata = json_database.select()
    bootUI.show(webview,dpi)
    if(alldata["system"]["haveLogin"]==0):
        if(alldata["system"]["haveupdata"]==0):
            warn.show(webview,dpi)
            alldata["system"]["haveupdata"]=1
            json_database.insert(alldata)
        login.show(webview,dpi)
        pass
    alldata = json_database.select()
    if(alldata["system"]["haveLogin"]==0):
        exit()
    print("登录成功")
    index.show(webview,dpi)