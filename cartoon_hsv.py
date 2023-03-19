import cv2
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
from countors import drawcontour
red_low=np.array([0,120,20])
red_up=np.array([15,255,255])
encode_red=np.array([0,0,255])

orange_low=np.array([16,120,20])
orange_up=np.array([25,255,255])
encode_orange=np.array([0,128,255])

yellow_low=np.array([21,120,20])
yello_up=np.array([40,225,225])
encode_yellow=np.array([0,255,255])

ligth_green_low=np.array([41,120,20])
ligth_green_up=np.array([55,255,255])
encode_ligth_green=np.array([0,255,128])

dark_green_low=np.array([56,120,20])
dark_green_up=np.array([70,255,255])
encode_dark_green=np.array([0,153,0])

light_blue_low=np.array([71,0,20])
light_blue_up=np.array([100,255,255])
encode_light_blue=np.array([255,255,51])

dark_blue_low=np.array([101,0,20])
dark_blue_up=np.array([127,255,255])
encode_dark_blue=np.array([204,0,0])

purple_low=np.array([128,0,20])
purple_up=np.array([148,255,255])
encode_purple=np.array([204,0,204])

pink_low=np.array([149,40,20])
pink_up=np.array([180,255,255])
encode_pink=np.array([153,51,255])

#withe_low=np.array([0,0,200])
#withe_up=np.array([180,255,255])
withe_low=np.array([0,0,0])
withe_up=np.array([180,30,255])
encode_whithe=np.array([255,255,255])

#black_low=np.array([0,0,0])
#black_up=np.array([180,255,100])#30
black_low=np.array([0,0,0])
black_up=np.array([170,255,70])#30
encode_black=np.array([32,32,32])


X=np.array([
    [red_low,red_up,encode_red],
    [orange_low,orange_up,encode_orange],
    [yellow_low,yello_up,encode_yellow],
    [ligth_green_low,ligth_green_up,encode_ligth_green],
    [dark_green_low,dark_green_up,encode_dark_green],
    [light_blue_low,light_blue_up,encode_light_blue],
    [dark_blue_low,dark_blue_up,encode_dark_blue],
    [purple_low,purple_up,encode_purple],
    [pink_low,pink_up,encode_pink],
    #[withe_low,withe_up,encode_whithe],
    [black_low,black_up,encode_black]
    
])

def encode_color(pixel):
    mask=[]
    for color in X :
        thresh=cv2.inRange(pixel,color[0],color[1])
        img_hsv_i[thresh==255]=color[2]
        #img[(thresh==np.array[255,0,0])]=color[2]
        #mask.append(thresh)
    return img_hsv_i
img=cv2.imread("/home/atefeh/Desktop/image/s1/cartoon/pink.jpg")
img_hsv= cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
kernel = np.ones((3, 3), np.float32) / 9
#image = cv2.filter2D(img_hsv, -1, kernel)
image=cv2.GaussianBlur(img_hsv,(5,5),0)
img_hsv_i=255*np.ones_like(img)
h,w=img.shape[:2]
#for i in range (h):
    #for j in range(w):
#maskes=np.array(encode_color(img_hsv))
#res=np.sum(maskes,axis=0,dtype=np.uint8)


#res=cv2.bitwise_and(img,img,mask=res)
encode_color=encode_color(image)
final=drawcontour(img,encode_color)
#final=cv2.cvtColor(img_hsv_i,cv2.COLOR_HSV2BGR)
cv2.imwrite("ii.png",final)
cv2.waitKey(0)
cv2.destroyAllWindows()