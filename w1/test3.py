import cv2

if __name__ == '__main__':
    img = cv2.imread('images/person_dark.jpg',cv2.IMREAD_GRAYSCALE)
    _,dst = cv2.threshold(img, 110,255,cv2.THRESH_TOZERO)
    cv2.imshow('binary img',dst)
    cv2.waitKey(0)