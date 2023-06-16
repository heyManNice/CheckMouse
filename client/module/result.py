import os
class show:
    def on_closed(self):
        print("退出程序")
        os._exit(0)
    def __init__(self,myweb,dpi):
        self.w=dpi.zoomPx(1000)
        self.h=dpi.zoomPx(740)
        self.win = myweb.create_window(js_api=self,title="恭喜",url='../source/result.ht',resizable=False,width=self.w,height=self.h,on_top=True)
        self.win.events.closed+=self.on_closed
        #myweb.start()
    def finish(self):
        self.win.destroy()
        print("完成")