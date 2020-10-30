import settings
import handlers.base_handler
import csv

class CartogramHandler(handlers.base_handler.BaseCartogramHandler):

    def get_name(self):
        return "The Bahamas"

    def get_gen_file(self):
        return "{}/bahamas_processedmap.json".format(settings.CARTOGRAM_DATA_DIR)
    
    def validate_values(self, values):

        if len(values) != 19:
            return False
        
        for v in values:
            if type(v) != float:
                return False

        return True
    
    def gen_area_data(self, values):
        return """1 {} Abaco
2 {} Acklins
3 {} Andros
4 {} Berry Islands
5 {} Bimini
6 {} Cat Island
7 {} Crooked Island
8 {} Eleuthera
9 {} Exuma
10 {} Grand Bahama
11 {} Harbour Island
12 {} Inagua
13 {} Long Island
14 {} Mayaguana
15 {} New Providence
16 {} Ragged Islands
17 {} Rum Cay
18 {} San Salvador
19 {} Spanish Wells""".format(*values)
    
    def expect_geojson_output(self):
        return True

    def csv_to_area_string_and_colors(self, csvfile):

        return self.order_by_example(csv.reader(csvfile), "Island", 0, 1, 2, 3, ["Abaco","Acklins","Andros","Berry Islands","Bimini","Cat Island","Crooked Island","Eleuthera","Exuma","Grand Bahama","Harbour Island","Inagua","Long Island","Mayaguana","New Providence","Ragged Islands","Rum Cay","San Salvador","Spanish Wells"], [0.0 for i in range(0,19)], {"Abaco":"1","Acklins":"2","Andros":"3","Berry Islands":"4","Bimini":"5","Cat Island":"6","Crooked Island":"7","Eleuthera":"8","Exuma":"9","Grand Bahama":"10","Harbour Island":"11","Inagua":"12","Long Island":"13","Mayaguana":"14","New Providence":"15","Ragged Islands":"16","Rum Cay":"17","San Salvador":"18","Spanish Wells":"19"})
