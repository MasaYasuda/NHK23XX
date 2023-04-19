import pyrealsense2 as rs
import numpy as np
import cv2
import images4 as images3
import defs.H_change as H_c
import ReachAndPhase as RAP
import copy
from defs import movement as moves
from defs import IandD
from defs import go
from defs import lock_on

#import H_filter as Hf
#import defs.H_middle as hm

Hue=19
Hue_wide=2
pole_num=80
checkdef=[0,0,0]
typeofnow=0

#コールバック用関数
def Hue_center_def(X):
    global Hue
    global checkdef
    Hue=X
    checkdef[0]=1

def Hue_wide_def(X):
    global Hue_wide
    global checkdef
    Hue_wide=X
    checkdef[1]=1

def pole_num_def(X):
    global pole_num
    global checkdef
    pole_num=X
    checkdef[2]=1

def types(X):
    global typeofnow
    typeofnow=X

def go_def(X):
    global mode
    mode=X

def targets(event,x,y,flags,param):
    global stats
    global Target
    global Target_type
    global typeofnow

    if event==cv2.EVENT_LBUTTONDOWN:    
        Target,Target_type=lock_on.lock_on(stats[1:],Target,Target_type,typeofnow,x,y)



#画像インポートまではネット上のサンプルコードを流用して行いました
# カメラの設定
conf = rs.config()
# RGB
conf.enable_stream(rs.stream.color, 1280, 720, rs.format.bgr8, 30)
# 距離
#conf.enable_stream(rs.stream.depth, 1280, 720, rs.format.z16, 30)
# stream開始
pipe = rs.pipeline()
profile = pipe.start(conf)
cnt = 0



#H補正用画像
#画質変更で落ちるならここ！
img_Hfil=cv2.imread("./programs/images/H_filter.png")
h,w=img_Hfil.shape[:2]
H_fil=H_c.change_H(h,w)
#H_fil=Hf.filter(img_Hfil)



#windowの設定
cv2.namedWindow("view1", cv2.WINDOW_NORMAL)
cv2.resizeWindow("view1", 640, 480)

cv2.createTrackbar("Hue_center",
                   "view1",
                    19,
                    30,
                    Hue_center_def)
cv2.createTrackbar("Hue_wide",
                   "view1",
                    2,
                    10,
                    Hue_wide_def)
cv2.createTrackbar("Chose_poles",
                   "view1",
                    5,
                    10,
                    pole_num_def)
cv2.createTrackbar("Type",
                   "view1",
                    2,
                    3,
                    types)
cv2.createTrackbar("Go!",
                   "view1",
                    0,
                    1,
                    go_def)
cv2.setMouseCallback("view1",
                    targets)


#cv2.setMouseCallback("Win_a",
#                    averages)

print("setup ended")
















#ここから本編

mode=0
CON_PID_control=[0,0,0]

while True:
    #インポート
    frames = pipe.wait_for_frames()
    color_frame = frames.get_color_frame()
    img = np.asanyarray(color_frame.get_data())




    #画像処理
    img2, lines ,stats_nonuse,centroids_nonuse = images3.images_4return(img,H_fil,Hue,Hue_wide)
    #画面全体の塊認識をなくす
    stats=stats_nonuse[1:]
    centroids=centroids_nonuse[1:]

    






        #表示
    cv2.imshow("view1",img2)
    #print("End1")
    if cv2.waitKey(3) == 27:
        break
    cv2.destroyAllWindows

