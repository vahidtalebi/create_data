import cv2
import numpy as np
import os
import urllib.request

def store_raw_image():
    pos_image_links = open('pos_image_links', 'r')
    pos_image_urls = pos_image_links.readlines()

    if not os.path.exist('pos'):
        os.makedirs('pos')
        return None
    pic_num = 1
    for i in pos_image_urls:
        try:
            print i
            urllib.request.urlretrieve(i, 'pos/'+str(pic_num)+'.jpg')
            img = imread('pos/'+str(pic_num)+'.jpg')
            resize_image = cv2.resize(img, (100, 100))
            for j in names:
                cv2.flip(resize_image, j)
                cv2.writh

        except Exception as e:
            print str(e)
            return None
