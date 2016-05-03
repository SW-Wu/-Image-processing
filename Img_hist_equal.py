# -*- coding: utf-8 -*-
'''
Author : S.W.
Publish time : 2016 / 5 / 3
'''

#  import matplotlib、numpy模組
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

img = mpimg.imread('Image.jpg') # 開啟圖片並讀取成矩陣模式
imgplot = plt.imshow(img, plt.gray()) # 利用plt模組顯示此灰階圖
imghist = plt.hist(img.flatten(),128) # 顯示此圖的Histogram

# 設定 Equalization 功能
def histeq(im, nbr_bins = 256):        
    imhist, bins = np.histogram(im.flatten(), nbr_bins, normed = True) # get image histogram
    cdf = imhist.cumsum() # cumulative distribution function
    cdf = 255 * cdf / cdf[-1] # normalize
    imeq = np.interp(im.flatten(), bins[:-1], cdf) # use linear interpolation of cdf to find new pixel values
    return imeq.reshape(im.shape), cdf

imgeq = histeq(img)[0]
imgeqhist = plt.hist(imgeq.flatten(),128) 
imgploteq = plt.imshow(imgeq, plt.gray()) # 對影像作 Histogram Equalization 處理並顯示


'''對影像進行 Arithmetic Operations'''

# 1. f(x) = x + 128 (將影像增亮)
add128 = img.copy()
add128[add128 > 127] = 127
add128 = add128 + 128
imgplot = plt.imshow(add128, plt.gray()) # 灰階圖
imghist = plt.hist(add128.flatten(),128) # Histogram
imgeq = histeq(add128)[0]
imgeqhist = plt.hist(imgeq.flatten(),128) # Histogram Equalization
imgploteq = plt.imshow(imgeq, plt.gray()) # Histogram Equalization 處理後的灰階圖

# 2.. f(x) = x/2 (將影像亮度砍半)
divide2 = img.copy()
divide2 = divide2 / 2
imgplot = plt.imshow(divide2, plt.gray()) # 灰階圖
imghist = plt.hist(divide2.flatten(),128) # Histogram
imgeq = histeq(divide2)[0]
imgeqhist = plt.hist(imgeq.flatten(),128) # Histogram Equalization
imgplot = plt.imshow(imgeq, plt.gray()) # Histogram Equalization 處理後的灰階圖

# 3.. f(x) = x - 128 (將影像檢暗)
subtract128 = img.copy()
subtract128[subtract128 < 128] = 128
subtract128 = subtract128 - 128
imgplot = plt.imshow(subtract128, plt.gray()) # 灰階圖
imghist = plt.hist(subtract128.flatten(),128) # Histogram
imgeq = histeq(subtract128)[0]
imgeqhist = plt.hist(imgeq.flatten(),128) # Histogram Equalization
imgplot = plt.imshow(imgeq, plt.gray()) # Histogram Equalization 處理後的灰階圖

# 4.. f(x) = 255 - x (負片)
inverse = img.copy()
inverse = 255 - inverse
imgplot = plt.imshow(inverse, plt.gray()) # 灰階圖
imghist = plt.hist(inverse.flatten(),128) # Histogram
imgeq = histeq(inverse)[0]
imgeqhist = plt.hist(imgeq.flatten(),128) # Histogram Equalization
imgplot = plt.imshow(imgeq, plt.gray()) # Histogram Equalization 處理後的灰階圖
