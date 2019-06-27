import os
import re
import random
import sys
from time import *

from PIL import Image

ZCTZ=Image.open('再次挑战.PNG','r')#坐标1741，990到2004，990
TG=Image.open('跳过.PNG','r')#坐标2015，43到2140，43
DJ=Image.open('点击屏幕继续.PNG','r')#1006,964到1248，964
CG=Image.open('闯关.PNG','r')#1478，872到1722，872

a=ZCTZ.load()#获取图片像素点za
b=TG.load()#跳过
c=DJ.load()#点击屏幕
d=CG.load()#闯关

def tap_screen(x, y):
    """calculate real x, y according to device resolution."""
    base_x, base_y = 2248, 1080
    real_x = int(x / base_x * device_x)
    real_y = int(y / base_y * device_y)
    os.system('adb shell input tap {} {}'.format(real_x, real_y))

def pull_screenshot(): #定义 截取手机屏幕 并 发送截图到电脑 函数
 	os.system('adb shell screencap -p /sdcard/auto.png') #发送 截屏命令 到手机
 	os.system('adb pull /sdcard/auto.png .') 
def check(xx,yy,x1,y1,x2,y2):
	k=0
	for i in range(x1,x2):
		for j in range(y1,y2):
			if xx[i,j]==yy[i,j]:
				k=k+1
	if k>=50:
		return 1
	else:
		return 0

pull_screenshot()
SCREEN=Image.open('auto.png','r')
w,h=SCREEN.size
device_x, device_y = w, h
money=0	
JS1=0
JS2=0

# temp=eval(input('请将手机横置刘海在左侧,并打开usb调试和模拟点击，确认请输入1，否则输入2'))
# while 1:
# 	if temp==1:
# 		break
# 	else:
# 		temp=eval(input("请输入"))

while 1:
	pull_screenshot()	#pull_screenshot()
	SCREEN=Image.open('auto.png','r')
	e=SCREEN.load()
	TF=0
	if check(e,d,1490,850,1700,900)==1:#检测是否为闯关
		tap_screen(1600,872)
		print('闯关')
		JS1=perf_counter()
		sleep(10)
	elif check(e,c,990,947,1256,990)==1:#检测是否为点击屏幕继续
		tap_screen(1100,964)
		print('点击屏幕继续')
		sleep(2)
	elif check(e,b,2036,27,2121,63)==1:#检测跳过
		tap_screen(2073,983)
		sleep(0.1)
		tap_screen(2073,970)
		print('跳过')
		TF=TF+1
		if TF%3:
			pass
		else:
			sleep(20)
	elif check(e,a,1800,970,2027,1025)==1:
		tap_screen(1800,990)
		money=money+1
		JS2=perf_counter()
		print('再次挑战'+'已刷金币：',money*56,"本次耗时：{:.0f}min{:.0f}s".format((JS2-JS1)//60,round((JS2-JS1)%60,2)))
		JS1=0
		JS2=0	
		sleep(2)
	else:
		pass
