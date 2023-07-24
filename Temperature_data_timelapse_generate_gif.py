# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 21:37:15 2022

@author: Nico
"""

from PIL import Image
import numpy as np

image_frames = []

months = np.arange(1, 492)

for i in months:
    new_frame = Image.open(r'C:\\Users\\Nico\\Desktop\\UBB\\2022-2\\Tesis_windows\\tkinter\\img\\CR2MET_tmin_v2.0_mon_1979_2019_005deg'+'\\'+ str(i)+'.jpg')
    image_frames.append(new_frame)
    
image_frames[0].save('temprature_timelapse.gif', format= 'GIF',
                     append_images= image_frames[1: ],
                     save_all= True, duration= 300,
                     loop= 0)