import numpy as np
import cv2

type=1

def sikaku(img,xy1,xy2,color):
    xy3=(xy1[0]+1,xy1[1]+1)
    xy4=(xy2[0]-1,xy2[1]-1)
    cv2.rectangle(img,xy1,xy2,(0,0,0),-1)
    cv2.rectangle(img,xy3,xy4,color,-1)
    return img


def sikaku_D(img,xy,color):
    xy1=(700-xy,700-xy)
    xy2=(700+xy,700+xy)
    img=sikaku(img,xy1,xy2,color)
    return img

def zones(img,xy):
    reds=((700-xy,700-xy),(700+xy,700))
    blues=((700-xy,700),(700+xy,700+xy))

    Line=((700-xy,700-2),(700+xy,700+2))

    global R_Z
    global B_Z
    global Cen


    img=sikaku(img,reds[0],reds[1],R_Z)
    img=sikaku(img,blues[0],blues[1],B_Z)

    img=sikaku(img,Line[0],Line[1],Cen)

    return img

def mirrar_ob(img,xy,sizes,color1,color2):
    xy=(xy[0]+100,xy[1]+100)
#    sizes=(sizes[0]-1,sizes[1]-1)

    ob=((xy[0],xy[1]),(xy[0]+sizes[0],xy[1]+sizes[1]))
    ob_m=((1400-ob[1][0],1400-ob[1][1]),(1400-xy[0],1400-xy[1]))

    print(ob)
    print(ob_m)

    img=sikaku(img,ob[0],ob[1],color1)
    img=sikaku(img,ob_m[0],ob_m[1],color2)
    return img

def pole(img,xy,type):
    global Pole
    xy=(100+xy[0],100+xy[1])

    r1=5
    r2=15
    if type==3:
        r1=8
        r2=15

    xy2=(1400-xy[0],1400-xy[1])

    cv2.circle(img,xy,r2,(0,0,0),-1)
    cv2.circle(img,xy,r2-1,Pole,-1)
    cv2.circle(img,xy,r1,(0,0,0),-1)
    cv2.circle(img,xy,r1-1,Pole,-1)

    cv2.circle(img,xy2,r2,(0,0,0),-1)
    cv2.circle(img,xy2,r2-1,Pole,-1)
    cv2.circle(img,xy2,r1,(0,0,0),-1)
    cv2.circle(img,xy2,r1-1,Pole,-1)



    return img



img_T=np.ones((1400,1400,3),dtype=np.uint8).T

img_T[0]*=128
img_T[1]*=0
img_T[2]*=64

img=img_T.T


#myteam is blue
if type==1:
    R_Z=(118,129,255)
    B_Z=(255,231,143)
    F=(43,121,245)
    Cen=(43,121,245)
    Water=(255,200,90)
    Ring=(255,255,255)
    Re_T=(0,255,255)
    S_R_Z=(3,20,255)
    S_B_Z=(245,38,11)
    Brid=(128,128,128)
    Pole=(55,175,212)
#myteam is red
if type==2:
    R_Z=(255,231,143)
    B_Z=(118,129,255)
    F=(43,121,245)
    Cen=(43,121,245)
    Water=(255,200,90)
    Ring=(255,255,255)
    Re_T=(0,255,255)
    S_R_Z=(245,38,11)
    S_B_Z=(3,20,255)
    Brid=(128,128,128)
    Pole=(55,175,212)


#grass
img=sikaku_D(img,600,F)
img=zones(img,595)
img=sikaku_D(img,400,F)
img=sikaku_D(img,397,Water)
img=zones(img,340)
img=sikaku_D(img,150,Cen)

#areas
img=mirrar_ob(img,(5,5),(50,50),Ring,Ring)
img=mirrar_ob(img,(1200-55,5),(50,50),Ring,Ring)
img=mirrar_ob(img,(600-75,5),(150,100),S_R_Z,S_B_Z)
img=mirrar_ob(img,(5,600-50-2),(50,50),Re_T,Re_T)
img=mirrar_ob(img,(200,600-97-2),(60,97),Brid,Brid)
img=mirrar_ob(img,(600-50,600-150-50),(100,50),Ring,Ring)

#objects
#img=pole(img,(500,500),1)
#img=pole(img,(550,500),3)
oku1=5+195+60+20
oku2=600-150+20
oku3=600
img=pole(img,(oku3,oku3),3)
img=pole(img,(oku1,oku1),1)
img=pole(img,(1200-oku1,oku1),1)
img=pole(img,(600,oku1),1)
img=pole(img,(600-150+20,oku2),1)
img=pole(img,(600+150-20,oku2),1)




cv2.imwrite("./map.png",img)