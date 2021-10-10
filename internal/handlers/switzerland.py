import settings
import handlers.base_handler
import csv

class CartogramHandler(handlers.base_handler.BaseCartogramHandler):

    def get_name(self):
        return "Switzerland"

    def get_gen_file(self):
        return "{}/che_processedmap.json".format(settings.CARTOGRAM_DATA_DIR)
    
    def validate_values(self, values):

        if len(values) != 26:
            return False
        
        for v in values:
            if type(v) != float:
                return False

        return True
    
    def gen_area_data(self, values):
        return """cartogram_id,Region Data,Region Name,Inset
1,{},Aargau,
2,{},Appenzell Ausserrhoden,
3,{},Appenzell Innerrhoden,
4,{},Basel-Landschaft,
5,{},Basel-Stadt,
6,{},Bern,
7,{},Fribourg,
8,{},Geneva,
9,{},Glarus,
10,{},Graubunden,
11,{},Jura,
12,{},Lucerne,
13,{},Neuchatel,
14,{},Nidwalden,
15,{},Obwalden,
16,{},Sankt Gallen,
17,{},Schaffhausen,
18,{},Schwyz,
19,{},Solothurn,
20,{},Thurgau,
21,{},Ticino,
22,{},Uri,
23,{},Valais,
24,{},Vaud,
25,{},Zug,
26,{},Zurich,""".format(*values)
    
    def expect_geojson_output(self):
        return True

    def csv_to_area_string_and_colors(self, csvfile):

        return self.order_by_example(csv.reader(csvfile), "Region", 0, 1, 2, 3, ["Aargau","Appenzell Ausserrhoden","Appenzell Innerrhoden","Basel-Landschaft","Basel-Stadt","Bern","Fribourg","Geneva","Glarus","Graubunden","Jura","Lucerne","Neuchatel","Nidwalden","Obwalden","Sankt Gallen","Schaffhausen","Schwyz","Solothurn","Thurgau","Ticino","Uri","Valais","Vaud","Zug","Zurich"], [0.0 for i in range(0,26)], {"Aargau":"1","Appenzell Ausserrhoden":"2","Appenzell Innerrhoden":"3","Basel-Landschaft":"4","Basel-Stadt":"5","Bern":"6","Fribourg":"7","Geneva":"8","Glarus":"9","Graubunden":"10","Jura":"11","Lucerne":"12","Neuchatel":"13","Nidwalden":"14","Obwalden":"15","Sankt Gallen":"16","Schaffhausen":"17","Schwyz":"18","Solothurn":"19","Thurgau":"20","Ticino":"21","Uri":"22","Valais":"23","Vaud":"24","Zug":"25","Zurich":"26"})
