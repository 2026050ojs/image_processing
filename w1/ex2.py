import cv2
#원본
if __name__ == '__main__':
    image = cv2.imread('images/Lenna.jpg',cv2.IMREAD_UNCHANGED)
    cv2.imshow('original', image)
    cv2.imwrite('Original_Lenna.jpg', image)
#grayscale image
    gray_image = cv2.imread('images/Lenna.jpg',cv2.IMREAD_GRAYSCALE)
    cv2.imshow('grayscale', gray_image)
    cv2.imwrite('grayscale_Lenna.jpg',gray_image)
#color
    IMREAD_COLOR = cv2.imread('images/Lenna.jpg',cv2.IMREAD_COLOR)
    cv2.imshow('IMREAD_COLOR', IMREAD_COLOR)
    cv2.imwrite('IMREAD_COLOR_Lenna.jpg',IMREAD_COLOR) 
#gray2   
    IMREAD_REDUCED_GRAYSCALE_2 = cv2.imread('images/Lenna.jpg',cv2.IMREAD_REDUCED_GRAYSCALE_2)
    cv2.imshow('IMREAD_REDUCED_GRAYSCALE_2', IMREAD_REDUCED_GRAYSCALE_2)
    cv2.imwrite('IMREAD_REDUCED_GRAYSCALE_2_Lenna.jpg',IMREAD_REDUCED_GRAYSCALE_2)    
#gray4
    IMREAD_REDUCED_GRAYSCALE_4 = cv2.imread('images/Lenna.jpg',cv2.IMREAD_REDUCED_GRAYSCALE_4)
    cv2.imshow('IMREAD_REDUCED_GRAYSCALE_4', IMREAD_REDUCED_GRAYSCALE_4)
    cv2.imwrite('IMREAD_REDUCED_GRAYSCALE_4_Lenna.jpg',IMREAD_REDUCED_GRAYSCALE_4)    
#gray8  
    IMREAD_REDUCED_GRAYSCALE_8 = cv2.imread('images/Lenna.jpg',cv2.IMREAD_REDUCED_GRAYSCALE_8)
    cv2.imshow('IMREAD_REDUCED_GRAYSCALE_8', IMREAD_REDUCED_GRAYSCALE_8)
    cv2.imwrite('IMREAD_REDUCED_GRAYSCALE_8_Lenna.jpg',IMREAD_REDUCED_GRAYSCALE_8)    
#reduced color2   
    IMREAD_REDUCED_COLOR_2 = cv2.imread('images/Lenna.jpg',cv2.IMREAD_REDUCED_COLOR_2)
    cv2.imshow('IMREAD_REDUCED_COLOR_2', IMREAD_REDUCED_COLOR_2)  
    cv2.imwrite('IMREAD_REDUCED_COLOR_2_Lenna.jpg',IMREAD_REDUCED_COLOR_2)    
#reduced color4    
    IMREAD_REDUCED_COLOR_4 = cv2.imread('images/Lenna.jpg',cv2.IMREAD_REDUCED_COLOR_4)
    cv2.imshow('IMREAD_REDUCED_COLOR_4', IMREAD_REDUCED_COLOR_4)
    cv2.imwrite('IMREAD_REDUCED_COLOR_4_Lenna.jpg',IMREAD_REDUCED_COLOR_4)    
#reduced color8      
    IMREAD_REDUCED_COLOR_8 = cv2.imread('images/Lenna.jpg',cv2.IMREAD_REDUCED_COLOR_8)
    cv2.imshow('IMREAD_REDUCED_COLOR_8', IMREAD_REDUCED_COLOR_8)
    cv2.imwrite('IMREAD_REDUCED_COLOR_8_Lenna.jpg',IMREAD_REDUCED_COLOR_8)    

    cv2.waitKey(0)