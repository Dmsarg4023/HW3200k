## EXE 6
## Challenge Question 1:

import arcpy
from arcpy import env
env.workspace = "C:/Data"
fieldlist = arcpy.ListFields()
for fields in FieldList:
    print field.name + field.shapeType + " " + str(field.length)

## Challenge Question 2
    
import arcpy
from arcpy import env
env.workspace = "C:/Data"
polylist = arcpy.ListRasters("", "polygon")
for poly in polylist:
    arcpy.BuildPyramids_managment(polygon)
    print polylist
