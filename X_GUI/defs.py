import cv2
import math
import numpy as np

def sikaku(img,xy1,xy2,color):
    xy3=(xy1[0]+1,xy1[1]+1)
    xy4=(xy2[0]-1,xy2[1]-1)
    cv2.rectangle(img,xy1,xy2,(0,0,0),-1)
    cv2.rectangle(img,xy3,xy4,color,-1)
    return img


def move()
"""
def rec_X(img,xy,PI,size,color):
    a=1

def sankaku(img,xy1,xy2,xy3,color):
    h,w=img.shape[:2]
    im2_shape=(img.shape[0]*10,img.shape[1]*10,3)
    img2=np.zeros(im2_shape,dtype=np.uint8)
    im2_rec2=(int(im2_shape[0]*0.6),int(im2_shape[1]*0.6))
    im2_rec1=(im2_shape[0]-im2_rec2[0],im2_shape[1]-im2_rec2[1])
    cv2.rectangle(img2,im2_rec1,im2_rec2,color)
    affine=cv2.getRotationMatrix2D(())


def fri(size):
    root2=math.sqrt(2)
    size_image=(int(size[0]*root2),int(size[1]*root2),3)

    robo=np.zeros(size_image,dtype=np.uint8)
"""