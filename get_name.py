# -*- coding: utf-8 -*-  
import os
from PIL import Image
  
def file_name(file_dir):   
    for root, dirs, files in os.walk(file_dir):  
        for file in files:
            im = Image.open(file_dir+'/'+file)
            #print(file+'宽：%d,高：%d' % (im.size[0], im.size[1]))
            width = str(im.size[0])
            height = str(im.size[1])
            mes = width + 'x' + height
            with open('/home/one/data/alaska-tiff/jpg/tif_name1.txt', 'a+') as f:
                f.write(os.path.splitext(file)[0] +'|'+mes+'\n')
            #print(os.path.splitext(file)[0] + '\n')
                
    

file_name('/home/one/data/alaska-tiff/ALASKA_training_set_TIFF1')