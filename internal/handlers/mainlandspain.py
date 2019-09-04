import settings
import handlers.base_handler
import csv

class CartogramHandler(handlers.base_handler.BaseCartogramHandler):

    def get_name(self):
        return "Mainland Spain and Balearic Islands"

    def get_gen_file(self):
        return "{}/esp_processedmap.json".format(settings.CARTOGRAM_DATA_DIR)
    
    def validate_values(self, values):

        if len(values) != 17:
            return False
        
        for v in values:
            if type(v) != float:
                return False

        return True
    
    def gen_area_data(self, values):
        return """1 {} Andalusia
2 {} Aragon
3 {} Cantabria
4 {} Castile and Leon
5 {} Castile-La Mancha
6 {} Catalonia
7 {} Ceuta y Melilla
8 {} Community of Madrid
9 {} Chartered Community of Navarre
10 {} Valencian Community
11 {} Extremadura
12 {} Galicia
13 {} Balearic Islands
14 {} La Rioja
15 {} Basque Autonomous Community
16 {} Principality of Asturias
17 {} Region of Murcia""".format(*values)
    
    def expect_geojson_output(self):
        return True

    def csv_to_area_string_and_colors(self, csvfile):

        return self.order_by_example(csv.reader(csvfile), "Region", 0, 1, 2, 3, ["Andalusia","Aragon","Cantabria","Castile and Leon","Castile-La Mancha","Catalonia","Ceuta y Melilla","Community of Madrid","Chartered Community of Navarre","Valencian Community","Extremadura","Galicia","Balearic Islands","La Rioja","Basque Autonomous Community","Principality of Asturias","Region of Murcia"], [0.0 for i in range(0,17)], {"Andalusia":"1","Aragon":"2","Cantabria":"3","Castile and Leon":"4","Castile-La Mancha":"5","Catalonia":"6","Ceuta y Melilla":"7","Community of Madrid":"8","Chartered Community of Navarre":"9","Valencian Community":"10","Extremadura":"11","Galicia":"12","Balearic Islands":"13","La Rioja":"14","Basque Autonomous Community":"15","Principality of Asturias":"16","Region of Murcia":"17"})
