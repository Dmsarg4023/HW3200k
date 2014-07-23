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

## EXE. 8 Challenge #2
import arcpy
from arcpy import env
env.workspace = "f:/Python/Homework/Data/Exercise08"
fc = "Hawaii.shp"
cursor = arcpy.da.SearchCursor(fc, ["SHAPE@"])
length = 0

for row in cursor:
    partnum = 0
    length = 0
    for part in row[0]:
        poly = arcpy.Polygon(part)
        print("Part {0} area: {1}".format(partnum, poly.area))
        print("Part {0} perimeter: {1}".format(partnum, poly.length))
        
        partnum += 1

## EXE. 8 Challenge # 3

import arcpy
from arcpy import env
env.workspace = "f:/Python/Homework/Data/Exercise08"
fc = "Hawaii.shp"
cursor = arcpy.da.SearchCursor(fc, ["OID@", "SHAPE@"])
xlist = []
ylist = []
for row in cursor:
  for part in row[1]:
    for point in part:
      xlist.append(point.X)
      ylist.append(point.Y)
xlist.sort()
ylist.sort()
max_x = xlist[-1]
min_x = xlist[0]
max_y = ylist[-1]
min_y = ylist[0]

coordlist = [(min_x,min_y),(max_x,min_y),(max_x,max_y),(min_x,max_y),(min_x,min_y)]
             
arcpy.CreateFeatureclass_management("f:/Python/Homework/Data/Exercise08", "Results/envelope1.shp", "Polygon")
cursor = arcpy.da.InsertCursor("Results/envelope1.shp", ["SHAPE@"])
array = arcpy.Array()
ident = 0
for coord in coordlist:
   ID, X, Y = ident, coord[0],coord[1]
   array.add(arcpy.Point(X, Y))
   ident += 1
cursor.insertRow([arcpy.Polygon(array)])
del cursor



if __name__== '__main__':
    import doctest
    doctest.testmod()

##EXE 10 Challenge 1
import arcpy
mxd = arcpy.mapping.MapDocument("f:/python/Homework/Data/Exercise10/Austin_TX.mxd")
dfs = arcpy.mapping.ListDataFrames(mxd)
addLayer = arcpy.mapping.ListLayers(mxd, "parks")[0]
for df in dfs:
  print df, df.name
  if df.name != "Parks":
     df2 = arcpy.mapping.ListDataFrames(mxd, df.name)[0]
     print df2
mxd.saveACopy("f:/python/Homework/Data/Exercise10/Austin_TX_2.mxd")


