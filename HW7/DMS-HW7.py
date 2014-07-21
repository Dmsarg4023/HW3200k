## EXE: 8 Challenge #1

import arcpy
from arcpy import env
env.workspace = "f:/python/Homework/Data/Exercise08"
env.overwriteOutput = True
outpath = "f:/Python/Homework/Data/Exercise08"
newfc = "Results/square.shp"
arcpy.CreateFeatureclass_management(outpath, newfc, "Polygon")
infile = "f:/Python/Homework/Data/Exercise08/Results/square.txt"
cursor = arcpy.da.InsertCursor(newfc, ["SHAPE@"])
array = arcpy.Array()
for line in fileinput.input(infile):
    ID, X, Y = string.split(line, " ")
    array.add(arcpy.Point(X, Y))
cursor.insertRow([arcpy.Polygon(array)])
fileinput.close()
del cursor
