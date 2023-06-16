import group_name
import os
import check
import time

class show:
    def __init__(self,myweb,dpi,parent):
        #self.state=state
        self.parent=parent
        self.myweb=myweb
        self.dpi=dpi
        self.isFull=False
        self.w=dpi.zoomPx(800)
        self.h=dpi.zoomPx(580)
        self.win = myweb.create_window(js_api=self,title="许可协议",url='../source/text.ht',resizable=False,width=self.w,height=self.h,text_select=True)
        #myweb.start()
    def finish(self):
        os.system("start .\source\check.bat")
        self.win.hide()
        self.parent.hide()
        time.sleep(2)
        check.show(self.myweb,self.dpi,self.parent)
        print("完成")
    def get_name(self):
        return group_name.random_letters()
