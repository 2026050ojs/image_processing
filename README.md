# image_processing
## week1
### 과제 1
``` python
import cv2

if __name__ == '__main__':
# color image 
    img = cv2.imread('./images/Lenna.jpg',cv2.IMREAD_UNCHANGED)
    height, width, channell = img.shape
    print("height:{}, width: {}, channel: {}".format(heigth, width,channel))
# grayscale img
    img = cv2.imread(./Lenna.jpg, cv2.IMREAD_UNCHANGED)
    heigth, widgth
```