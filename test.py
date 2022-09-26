# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 14:49:23 2022

@author: Max Schwinn
"""


from openpyxl import load_workbook
from osgeo import gdal
import numpy as np


#> open tiff file
tiff_t0 = gdal.Open("C:\\wheels\\Waldfl_m2_2018_6x6.tif")

#> read geographical information
# t0
geo_t0 = tiff_t0.GetGeoTransform()
proj_t0 = tiff_t0.GetProjection()
band_t0 = tiff_t0.GetRasterBand(1)
xsize_t0 = band_t0.XSize
ysize_t0 = band_t0.YSize

#> create array and close tiff
arr_t0 = band_t0.ReadAsArray()
tiff_t0 = None

print(geo_t0, "haha")

#import sys
#sys.path.append('C:\\ProgramData\\Anaconda3\\lib\\site-packages\\GDAL-3.4.3.dist-info')
#print(sys.path)
