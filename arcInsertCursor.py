# arcpy cursors: search, insert, update
# SearchCursor, InsertCursor, or UpdateCursor
#arcpy.da.InsertCursor(in_table, field_names)
#arcpy.da.SearchCursor(in_table, field_names, {where_clause}, {spatial_reference}, {explode_to_points}, {sql_clause})
#arcpy.da.UpdateCursor(in_table, field_names, {where_clause}, {spatial_reference}, {explode_to_points}, {sql_clause})

import arcpy

cursor = arcpy.da.InsertCursor("D:/kgeo/kgeo.gdb/SM_Stations", ['NAME', 'TYPE'])
for i in range(0,2):
    cursor.insertRow([i, 'Fire'])
