import cv2
import copy
import math
import numpy as np

img=cv2.imread("./X_GUI/map.png")
xy=[700,1400-150]
PI=int(math.degrees(math.pi/2))

m_sizex=50.0
m_sizey=50.0
img_robo=cv2.imread("./X_GUI/rabbit.png")
h,w=img.shape[:2]
h_r,w_r=img_robo.shape[:2]
size_image=(h,w,3)
robo=np.zeros(size_image,dtype=np.uint8)

def setX(X):
    global xy
    xy[0]=X

def setY(X):
    global xy
    xy[1]=X
def setPI(X):
    global PI
    PI=X


cv2.namedWindow("view1", cv2.WINDOW_NORMAL)
cv2.resizeWindow("view1", 640, 480)

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
                    PI,
                    720,
                    setPI)



while True:

    img_go=copy.deepcopy(img)
    center=(int(w_r/2),int(h_r/2))
    affine=cv2.getRotationMatrix2D(center,PI,1.0)
#    affine[0][2]+=int(  (w_r-w)/2 +xy[0]  )
#    affine[1][2]+=int(  (h_r-w)/2 +xy[1]  )
    affine[0][2]+=int(  xy[0]-w_r/2  )
    affine[1][2]+=int(  xy[1]-h_r/2  )

    robo=cv2.warpAffine(img_robo,affine,(w,h))

    img_go+=robo

    cv2.imshow("view1",img_go)
    if cv2.waitKey(10) == 27:
        break
    cv2.destroyAllWindows
