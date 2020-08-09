import settings
import handlers.base_handler
import csv

class CartogramHandler(handlers.base_handler.BaseCartogramHandler):

    def get_name(self):
        return "Guyana"

    def get_gen_file(self):
        return "{}/guyana_processedmap.json".format(settings.CARTOGRAM_DATA_DIR)
    
    def validate_values(self, values):

        if len(values) != 10:
            return False
        
        for v in values:
            if type(v) != float:
                return False

        return True
    
    def gen_area_data(self, values):
        return """1 {} Barima-Waini
2 {} Cuyuni-Mazaruni
3 {} Demerara-Mahaica
4 {} East Berbice-Corentyne
5 {} Essequibo Islands-West Demerara
6 {} Mahaica-Berbice
7 {} Pomeroon-Supenaam
8 {} Potaro-Siparuni
9 {} Upper Demerara-Berbice
10 {} Upper Takutu-Upper Essequibo""".format(*values)
    
    def expect_geojson_output(self):
        return True

    def csv_to_area_string_and_colors(self, csvfile):

        return self.order_by_example(csv.reader(csvfile), "Region", 0, 1, 2, 3, ["Barima-Waini","Cuyuni-Mazaruni","Demerara-Mahaica","East Berbice-Corentyne","Essequibo Islands-West Demerara","Mahaica-Berbice","Pomeroon-Supenaam","Potaro-Siparuni","Upper Demerara-Berbice","Upper Takutu-Upper Essequibo"], [0.0 for i in range(0,10)], {"Barima-Waini":"1","Cuyuni-Mazaruni":"2","Demerara-Mahaica":"3","East Berbice-Corentyne":"4","Essequibo Islands-West Demerara":"5","Mahaica-Berbice":"6","Pomeroon-Supenaam":"7","Potaro-Siparuni":"8","Upper Demerara-Berbice":"9","Upper Takutu-Upper Essequibo":"10"})
