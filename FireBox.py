# -*- coding: utf-8 -*-
"""
FireBOX

Created on Wed Feb 28 17:20:42 2018

@author: Eric Alterman
"""

import arcpy, numpy
#remember, this structure imports env as an object
from arcpy import env

arcpy.CheckOutExtension("Spatial")
arcpy.CheckOutExtension("3D")
#from arcpy.sa import *

path = r'C:\Users\Eric Alterman\Documents\FIREBOX'
arcpy.CheckOutExtension("Spatial")
env.workspace = path + '\data'
dem_path = env.workspace + '\USGS_NED_13_n41w106_ArcGrid'
#env.workspace = os.getcwd()+'/demo'
env.overwriteOutput = 1

theme = 'results.gdbAOI_image.tif'
dem = dem_path + '\grdn41w106_13'
dem_clip = 'DEM_Clip'
# Replace a layer/table view name with a path to a dataset (which can be a layer file) or create the layer/table view within the script
# The following inputs are layers or table views: "grdn41w106_13", "results.gdbAOI_image.tif"
arcpy.Clip_management(in_raster=dem, rectangle="-105.343834605788 40.1304424063456 -105.262109063624 40.2087803539345", out_raster="C:/Users/Eric Alterman/Documents/FIREBOX/data/" + dem_clip, in_template_dataset=theme, nodata_value="-3.402823e+038", clipping_geometry="NONE", maintain_clipping_extent="NO_MAINTAIN_EXTENT")

outSlope = arcpy.sa.Slope(dem_clip, "DEGREE", '1') #calculates slope of a raster in DEM
outSlope.save("SlopeRaster") #saves value  as outslope01. also generates new raster