#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      kvolz
#
# Created:     03/11/2017
# Copyright:   (c) kvolz 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import arcpy
import csv

# For each field in the Hospitals feature class, print
#  the field name, type, and length.
arcpy.env.workspace = "C:\Users\kvolz\AppData\Roaming\ESRI\Desktop10.3\ArcCatalog\SDE CONNECTION..."

features = arcpy.ListFeatureClasses()

#open file for output
fh = open('C:/Users/kvolz/Documents/output.txt', 'wb')


fields = arcpy.ListFields(feature)

for field in fields:
    print("{0}, {1}/{2}, domain:{3}"
          .format(field.name, field.type, field.length, field.domain))

for i in features:
##    print i
    fh.write(str(i) + "\r\n")
    array = []
    fields = arcpy.ListFields(i)
    for field in fields:
        array.append("{0}, {1}/{2}, {3}"
          .format(field.name, field.type, field.length, field.domain))
    array.sort()
##    print array
    for item in array:
##        print item
        fh.write(str(item) + "\r\n")
    fh.write("\r\n")

fh.close()

