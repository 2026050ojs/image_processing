import cv2
src = cv2.imread('lena_2.jpg',cv2.IMREAD_GRAYSCALE)
cv2.imshow('src',src)
#이진화
_, dst = cv2.threshold(src,160,255,cv2.THRESH_BINARY)
cv2.imshow('dst',dst)
_, dst = cv2.threshold(src,160,255,cv2.THRESH_BINARY_INV)
cv2.imshow('tbi',dst)
_, dst = cv2.threshold(src,160,255,cv2.THRESH_TRUNC)
cv2.imshow('ttr',dst)
_, dst = cv2.threshold(src,160,255,cv2.THRESH_TOZERO)
cv2.imshow('ttz',dst)
_, dst = cv2.threshold(src,160,255,cv2.THRESH_TOZERO_INV)
cv2.imshow('ttzi',dst)
cv2.waitKey(0)