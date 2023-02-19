# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 21:37:15 2022

@author: Nico
"""

import PIL
import numpy as np

image_frames = []

months = np.arange(1, 491)

for i in months:
    new_frame = PIL.Image.open(r'C:\Users\Nico\Desktop\UBB\2022-2\Tesis\images_gif'+'\\'+ str(i)+'.jpg')
    image_frames.append(new_frame)
    
image_frames[0].save('temprature_timelapse.gif', format= 'GIF',
                     append_images= image_frames[1: ],
                     save_all= True, duration= 300,
                     loop= 0)