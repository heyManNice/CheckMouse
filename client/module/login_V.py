# -*- coding: utf-8 -*-
"""
Created on Thu May 11 10:24:56 2023

@author: zk
"""

import re #导入re函数
class login_and_register: 
    '''
    功能：检验登陆以及注册格式合法性
    日期：Created on Thu May 11 10:24:56 2023
    '''
    def is_the_same(a,b):#检测是否相同
        if a==b:
            return True
        return False
    def mail_available(mail):#检测邮箱是否有效
        if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$",mail) != None:
            return True
        else:
            return False
    def is_Chinese(self,word):  #检测是否为中文
        count = 0
        for ch in word.encode('utf-8').decode('utf-8'):
            if '\u4e00' <= ch <= '\u9fff':
                return True
                count+=1
                break
            if count>=1:
                return True
            else:
                return False
    def password_verify(pwd = '测试密码'):#检测密码是否合法
            if re.match("^(?:(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])).*$",pwd)==None:
                return False
            else:
                if re.search(r"\W",pwd)==None:
                    return False
                else:
                    return True
    def phone_verify(num):#检测手机号是否合法
            if len(num) == 11 and num.isnumeric() is True:
                return True
            return False
    def username_verify(user_name):#检测用户名是否合法
        if len(user_name) >= 6 and login_and_register().is_Chinese(user_name) is False:
            return True
        else:
            return False
    def phone_or_username(usernameOrPhone = ''):#判断是手机还是用户名
        if login_and_register.phone_verify(usernameOrPhone) is True:#这个真代表是手机号
            return False                                            #是手机号所以输出false
        else:
            return True
        
    '''
    功能：检验登陆格式合法性
    usernameOrPhone = 输入的用户名或手机号
    password = 输入的密码
    日期：Created on Thu May 11 10:24:56 2023
    '''
    def login_verify(usernameOrPhone,password):
        #print('正在检查格式.......')
        if login_and_register.phone_or_username() is True:#true代表是用户名哦!!!!!
            #print("正在核查用户名格式")
            if login_and_register.username_verify(usernameOrPhone) is True:#
                #print("正在核查密码格式")
                if login_and_register.password_verify(password) is True:
                    #print('一眼丁真，鉴定为正确的格式')
                    return{"code":0,"msg":'一眼丁真，鉴定为正确的格式'}
                else:
                    #print('请重新输入密码！')
                    return {"code":1,"msg":'密码必须要有数字英文大小写特殊符号'}
            else:
                #print('请重新输入用户名！')
                return {"code":1,"msg":'用户名至少六个字符，不能是中文'}
        else:
            #print("正在核查手机号格式")
            if login_and_register.phone_verify(usernameOrPhone) is True:
                #print("正在核查密码格式")
                if login_and_register.password_verify(password) is True:
                    #print("正确！")
                    return{"code":0,"msg":'一眼丁真，鉴定为正确的格式'}
                else:
                    #print('请重新输入密码！')
                    return {"code":1,"msg":'密码必须要有数字英文大小写特殊符号'}
            else:
                return {"code":1,"msg":'你的手机怎么没有11位数字捏'}
    def register_format(username,password,confirmPW,mail):
        '''
        功能：检验注册格式合法性
        username = 输入的用户名
        password = 输入的密码
        confirmPW = 二次输入的密码
        mail = 输入的邮箱
        日期：Created on Thu May 11 10:24:56 2023
        ''' 
        if login_and_register.username_verify(username) is False:
            return {"code":1,"msg":'用户名至少六个字符，不能是中文'}
        elif login_and_register.password_verify(password) is False:
            return {"code":1,"msg":'密码必须要有数字英文大小写特殊符号'}
        elif login_and_register.is_the_same(password,confirmPW) is False:
            return {"code":1,"msg":'请确认密码是否相同！'}
        elif login_and_register.mail_available(mail) is False:
            return {"code":1,"msg":'请确认邮箱是否有效！'}
        else:
            return{"code":0,"msg":'一眼丁真，鉴定为正确的格式'}

            
        
            
###################################################################以下为测试使用
##############这里是测试用代码
#a = login_and_register.login_verify(usernameOrPhone1,password1)
#b = login_and_register.register_format(username2, password1, confirmPW1, mail1)
#print(a)
#print(b)

