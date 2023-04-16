import cv2
import numpy
import copy
import math
import numpy as np


def draw_img(img,img_robo,xy,PI):

    h,w=img.shape[:2]
    h_r,w_r=img_robo.shape[:2]
    size_image=(h,w,3)
    robo=np.zeros(size_image,dtype=np.uint8)


    img_go=copy.deepcopy(img)
    center=(int(w_r/2),int(h_r/2))
    affine=cv2.getRotationMatrix2D(center,PI,1.0)
    affine[0][2]+=int(  xy[0]-w_r/2  )
    affine[1][2]+=int(  xy[1]-h_r/2  )

    robo=cv2.warpAffine(img_robo,affine,(w,h))

    img_go+=robo
    return img_go


#"""

cv2.namedWindow("view1", cv2.WINDOW_NORMAL)
cv2.resizeWindow("view1", 640, 480)

def setX(X):
        global xy
        xy[0]=X
def setY(X):
        global xy
        xy[1]=X
def setPI(X):
        global PI
        PI=X


img=cv2.imread("./X_GUI/map.png")
xy=[700,1400-150]
phase=int(math.degrees(math.pi/2))
img_robo=cv2.imread("./X_GUI/rabbit.png")

cv2.createTrackbar("X",
                "view1",
                    xy[0],
                    1400,
                    setX)
cv2.createTrackbar("Y",
                "view1",
                    xy[1],
                    1400,
                    setY)
cv2.createTrackbar("Phase",
                "view1",
                    phase,
                    720,
                    setPI)


while True:
    
    img_go=draw_img(img,img_robo,xy,phase)
    cv2.imshow("view1",img_go)
    if cv2.waitKey(10) == 27:
        break
    cv2.destroyAllWindows

#"""