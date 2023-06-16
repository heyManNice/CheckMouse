import json_database
import text
class show:
    def __init__(self,myweb,dpi):
        self.myweb=myweb
        self.dpi=dpi
        self.isFull=False
        self.w=dpi.zoomPx(1000)
        self.h=dpi.zoomPx(600)
        self.win = myweb.create_window(js_api=self,title="主页",url='../source/index.ht',resizable=False,width=self.w,height=self.h)
        myweb.start()
    def fullscreen(self):
        self.win.toggle_fullscreen()
        self.isFull = ~self.isFull
        if ~self.isFull :
            self.win.resize(self.w,self.h)
        return 0
    def database_get(self):
        return json_database.select()
    def database_set(self,data):
        return json_database.insert(data)
    def start(self):
        text.show(self.myweb,self.dpi,self.win)
        #self.win.hide()
        return 0