"""
功能：用于筛选验证码图片的模块
子程序：否
日期：2023年5月14日
"""

import random

def getVeri(pictures):
    """
    功能：随机抽取组成验证码的九张图片
    参数：包涵全部图片的字典
    日期：2023年5月14日
    """
    PicList = []
    Right = []
    s1 = random.choice(list(pictures.keys()))
    r_num = random.randint(2, 5)
    f_num = 9-r_num
    len1 = len(pictures[s1])
    nums = random.sample(range(len1),r_num)
    for i in range(r_num):
        j = nums[i]
        PicList.append(pictures[s1][j])
        Right.append(pictures[s1][j])
    pictures.pop(s1)
    f_pics = list(pictures.values())
    len2 = len1*len(f_pics)
    f_nums = random.sample(range(len2),f_num)
    for i in range(f_num):
        r = int(f_nums[i]/10)
        c = int(f_nums[i]%10)
        PicList.append(f_pics[r][c])
    random.shuffle(PicList)
    yzm = {"em":s1,"PicList":PicList,"Right":Right}
    return yzm

#print(getVeri(yzm_pictures))
