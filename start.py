# -*- coding:utf-8- -*-
"""
Author:Yang Sheng-rong
Date:2023年09月10日
Email:3118393236@qq.com
"""
# 导入Python自带的os模块
import os

# 导入第三方模块
import numpy as np
import pygame
from PIL import ImageGrab

# 初始化混音器
pygame.mixer.init()
# 持续监听
while True:
    img = np.array(ImageGrab.grab())  # 获取屏幕像素
    if img.sum() > 1370702574:  # 像素总和超过 85%纯白就启动
        pygame.mixer.music.load("start.mp3")  # 音乐路径
        pygame.mixer.music.play()  # 播放音乐
        os.system(r"D:\QQMusic\QQMusic1942.19.49.58\QQMusic.exe")  # 替换成原神启动路径
        print("Start.........!")
