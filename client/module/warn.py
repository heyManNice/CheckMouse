"""
功能:弹出一个提示窗口
子程序:否
日期:2023年3月26日
"""

class show():
    """窗口调用函数api的类"""
    def __init__(self,myweb,dpi) -> None:
        self.win= myweb.create_window(title="检鼠",url='../source/warn.ht',js_api=self,resizable=False,width=dpi.zoomPx(320),height=dpi.zoomPx(170),on_top=True)
        myweb.start()
    def yes(self):
        """
        功能:提示框点击确定执行的代码
        日期:2023年3月26日
        """
        self.win.destroy()
        print("确定")
    def no(self):
        """
        功能:提示框点击不取消执行的代码
        日期:2023年3月26日
        """
        print("不取消")

if __name__ == '__main__':
    print("调试模式")