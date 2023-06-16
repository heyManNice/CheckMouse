import group_name
class show():
    def get_name(self):
        return group_name.random_letters()
    def __init__(self,myweb,dpi):
        self.win = myweb.create_window(js_api=self,title="检鼠",url='../source/bootUI.ht',resizable=False,width=dpi.zoomPx(800),height=dpi.zoomPx(800),on_top=True,frameless=True,transparent=True)
        myweb.start()
    """启动窗口调用函数api的类"""
    def finish(self):
        self.win.destroy()
        print("启动完成")
    
if __name__ == '__main__':
    print("测试环境")