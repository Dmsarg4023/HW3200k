## EXE 7 Challenge 1:

import arcpy
from arcpy import env
env.workspace = "E:/Python/Homework/Data/Exercise07"
fc = "airports.shp"
airport = arcpy.CreateAirport("Results/buffer.shp")
seaplane = arcpy.CreateSeaplane("Results/buffer.shp")
arcpy.Buffer_analysis(fc, airport, "15000 METERS", )
arcpy.Buffer_analysis(fc, seaplane, "7500 METERS", )
print fc

## Challenge 2:

import arcpy
from arcpy import env
env.workspace = 'E:/Python/Homework/Data/Exercise07/Roads.shp"
fc = "Results/Roads.shp"
newfield = "FERRY"
fieldtype = "TEXT"
fieldfeature = arcpy.ValidateFieldName(newfield)
arcpy.AddField_management(fc, fieldfeature, fieldtype, "Yes", "No", 12)
