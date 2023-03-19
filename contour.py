import cv2 
def drawcontour(ori_img,en_img):
    imgray = cv2.cvtColor(ori_img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(imgray, 120, 255, 0)
    contours, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    smoothen_contours=[]
    factor=0.003
    for cnt in contours :
        epsilon = factor * cv2.arcLength(cnt,True)
        smoothen_contours.append(cv2.approxPolyDP(cnt,epsilon,True))
    cv2.drawContours(en_img, contours, -1, (0,0,0), 2)
    return en_img
