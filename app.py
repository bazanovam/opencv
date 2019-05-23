import cv2
import time
import logging


def rotate():
    angle = 1
    while 1:
        logger = logging.getLogger('route.logger')
        logger.info('Connection to database successful') 

        # read image as grey scale
        img = cv2.imread('1.jpg')
        # get image height, width
        (h, w) = img.shape[:2]
        # calculate the center of the image
        center = (w / 2, h / 2)
        
        scale = 1.0
        
        M = cv2.getRotationMatrix2D(center, angle, scale)
        rotated = cv2.warpAffine(img, M, (h, w))
        writeStatus = cv2.imwrite("1.jpg", rotated)
        

        if writeStatus is True:
            print("image written")
            hs = open("hst.txt","a")
            hs.write(str(angle)+'\n')
            hs.close() 
        else:
            print("problem") # or raise exception, handle problem, etc.

        angle += 2
        time.sleep(2)

if __name__ == '__main__':
    rotate()