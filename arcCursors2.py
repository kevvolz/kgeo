# arcpy cursors: search, insert, update
# SearchCursor, InsertCursor, or UpdateCursor
#arcpy.da.InsertCursor(in_table, field_names)
#arcpy.da.SearchCursor(in_table, field_names, {where_clause}, {spatial_reference}, {explode_to_points}, {sql_clause})
#arcpy.da.UpdateCursor(in_table, field_names, {where_clause}, {spatial_reference}, {explode_to_points}, {sql_clause})

import arcpy

fc = "D:/kgeo/kgeo.gdb/SM_Stations"

cursor = arcpy.da.SearchCursor(fc, ['NAME', 'TYPE'])
for row in cursor:
    print(row)
