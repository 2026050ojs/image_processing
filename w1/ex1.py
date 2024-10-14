import cv2
#원본
if __name__ == '__main__':
    img  = cv2.imread('images/Lenna.jpg',cv2.IMREAD_UNCHANGED)
    cv2.imshow("Image",img)
    cv2.imwrite('Lena_1.bmp',img)
    cv2.imwrite('Lena_2.jpg',img)
# color image 
    cim = cv2.imread('images/Lenna.jpg',cv2.IMREAD_UNCHANGED)
    height, width, channel = img.shape
    print("height:{}, width: {}, channel: {}".format(height, width, channel))
# grayscale img
    img = cv2.imread('./Lena_2.jpg', cv2.IMREAD_GRAYSCALE)
    heigth, widgth = img.shape 
    print("height: {}, width: {}".format(heigth, width))
# binary
    src = cv2.imread('Lena_2.jpg', cv2.IMREAD_GRAYSCALE)
    cv2.imshow('src',src)
    _,dst = cv2.threshold(src, 160,255, cv2.THRESH_BINARY)
    cv2.imshow('dst',dst)
# binary inv

    
    cv2.waitKey(0)