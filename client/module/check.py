import result
class show:
    def __init__(self,myweb,dpi,parent):
        self.parent=parent
        self.myweb=myweb
        self.dpi=dpi
        self.w=dpi.zoomPx(1000)
        self.h=dpi.zoomPx(600)
        self.win = myweb.create_window(js_api=self,title="正在检测",url='../source/check.ht',resizable=False,width=self.w,height=self.h,fullscreen=True,transparent=True,on_top=True)
        #myweb.start()
    def finish(self):
        result.show(self.myweb,self.dpi)
        self.win.hide()
        #self.parent.show()
        print("完成")