# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 15:49:32 2019

@author: Maple
"""

import os 
import ndjson
import matplotlib.pyplot as plt
import numpy as np


F = 'data'
files = os.listdir(F)

# load from file-like objects
file_p = F + '\\' + files[4]
with open(file_p) as f:
    data = ndjson.load(f)
    
# %%
word = data[0]['word']
pic_strokes = data[0]['drawing']        

# %% Plot image from strokes
Picture = np.zeros([150, 260])
for s in pic_strokes:
    plt.plot(s[0], s[1], 'k')
    Picture

# %% Check if the line have intersections with any other lines
for idx, val in enumerate(pic_strokes[:-1][:]):
    stroke1 = pic_strokes[idx]
    stroke2 = pic_strokes[idx+1]
    
    s1x = stroke1[0]
    s2x = stroke2[0]
    
    s1y = stroke1[1]
    s2y = stroke2[1]
    
    yint = [pos for pos in s1x if pos in s2x]
    xint = [pos for pos in s1y if pos in s2y]
    
    if not yint and not xint:
        print('No intersection Between lines')
    else:
        print('Line does have intersection')


# %% Subplot of various doodles
dim = 4;
fig, ax = plt.subplots(dim,dim, figsize=(8,6), constrained_layout = True)
fig.suptitle('Doodles of ' + word)
xl = np.shape(ax)[0]
yl = np.shape(ax)[1]
i = 0
j = 0
for p in data[0:xl*yl]:
    strokes = p['drawing']
    for s in strokes:
        ax[i][j].plot(s[0], s[1], 'k')
        ax[i][j].axis('off')
    i = i+1
    if i == xl:
        i = 0
        j = j+1

# %% 
fig = plt.figure()
fig.add_subplot(111)

theta = np.arange(0, 2*np.pi + 0.1, 0.1)
r = 1
X = r*np.cos(theta)
Y = r*np.sin(theta)
plt.plot(X,Y)
plt.axis('off')
fig.canvas.draw()

Dat = np.array(fig.canvas.renderer._renderer)

fig2 = plt.figure()
plt.imshow(Dat)
plt.axis('off')


































    
