import login_V
import code
import json_database

yzm_pictures = {"car": ["1.png", "2.png", "3.png", "4.png", "5.png","6.png", "7.png", "8.png", "9.png", "10.png"],
            "bus": ["11.png", "12.png", "13.png", "14.png", "15.png","16.png", "17.png", "18.png", "19.png", "20.png"],
            "bicycle": ["21.png", "22.png", "23.png", "24.png", "25.png","26.png", "27.png", "28.png", "29.png", "30.png"],
            "AcademicBuilding": ["31.png", "32.png", "33.png", "34.png", "35.png","36.png", "37.png", "38.png", "39.png", "40.png"],
            }  # 每类图片配十张照片，多少类再议

class show():
    def __init__(self,myweb,dpi):
        self.win = myweb.create_window(js_api=self,title="检鼠",url='../source/login.ht',resizable=False,width=dpi.zoomPx(400),height=dpi.zoomPx(600))
        myweb.start()
    """启动窗口调用函数api的类"""
    def finish(self):
        self.win.destroy()
        print("完成")
    def database_get(self):
        return json_database.select()
    def database_set(self,data):
        return json_database.insert(data)
    def get_Vcode(self):
        return code.getVeri(yzm_pictures.copy())
    def login(self,usernameOrphone,password):
        return login_V.login_and_register.login_verify(usernameOrphone,password)
    def regi(self,username, password, confirmPW1, mail):
        return login_V.login_and_register.register_format(username, password, confirmPW1, mail)
    
if __name__ == '__main__':
    print("测试环境")