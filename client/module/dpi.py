"""
功能:获取电脑系统的缩放比例
子程序:否
日期:2023年3月26日
"""

from win32 import win32api, win32gui, win32print
from win32.lib import win32con
from win32.win32api import GetSystemMetrics


def get_real_resolution():
    """
    功能:获取真实的分辨率
    日期:2023年3月26日
    """
    hDC = win32gui.GetDC(0)
    w = win32print.GetDeviceCaps(hDC, win32con.DESKTOPHORZRES)
    h = win32print.GetDeviceCaps(hDC, win32con.DESKTOPVERTRES)
    return w, h


def get_screen_size():
    """
    功能:获取缩放后的分辨率
    日期:2023年3月26日
    """
    w = GetSystemMetrics (0)
    h = GetSystemMetrics (1)
    return w, h
def get_Zoom():
    """
    功能:获取缩放倍率
    日期:2023年3月26日
    """
    real_resolution = get_real_resolution()
    screen_size = get_screen_size()
    screen_scale_rate = round(real_resolution[0] / screen_size[0], 2)
    return screen_scale_rate

zoom = get_Zoom()

def zoomPx(num):
    """
    功能:将输入的像素值转换为系统缩放后的像素
    num:像素值
    日期:2023年3月26日
    """
    return int(zoom*num)
if __name__ == '__main__':
    print("测试环境")
    print(get_Zoom())