import settings
import handlers.base_handler
import csv

class CartogramHandler(handlers.base_handler.BaseCartogramHandler):

    def get_name(self):
        return "Spain"

    def get_gen_file(self):
        return "{}/spain4_processedmap.json".format(settings.CARTOGRAM_DATA_DIR)
    
    def validate_values(self, values):

        if len(values) != 18:
            return False
        
        for v in values:
            if type(v) != float:
                return False

        return True
    
    def gen_area_data(self, values):
        return """1 {} Andalucia
2 {} Aragon
3 {} Cantabria
4 {} Castilla y Leon
5 {} Castilla-La Mancha
6 {} Cataluna
7 {} Ceuta
8 {} Comunidad de Madrid
9 {} Comunidad Foral de Navarra
10 {} Comunidad Valenciana
11 {} Extremadura
12 {} Galicia
13 {} Islas Baleares
14 {} La Rioja
15 {} Melilla
16 {} Pais Vasco
17 {} Principado de Asturias
18 {} Region de Murcia""".format(*values)
    
    def expect_geojson_output(self):
        return True

    def csv_to_area_string_and_colors(self, csvfile):

        return self.order_by_example(csv.reader(csvfile), "Autonomous Community/City", 0, 1, 2, 3, ["Andalucia","Aragon","Cantabria","Castilla y Leon","Castilla-La Mancha","Cataluna","Ceuta","Comunidad de Madrid","Comunidad Foral de Navarra","Comunidad Valenciana","Extremadura","Galicia","Islas Baleares","La Rioja","Melilla","Pais Vasco","Principado de Asturias","Region de Murcia"], [0.0 for i in range(0,18)], {"Andalucia":"1","Aragon":"2","Cantabria":"3","Castilla y Leon":"4","Castilla-La Mancha":"5","Cataluna":"6","Ceuta":"7","Comunidad de Madrid":"8","Comunidad Foral de Navarra":"9","Comunidad Valenciana":"10","Extremadura":"11","Galicia":"12","Islas Baleares":"13","La Rioja":"14","Melilla":"15","Pais Vasco":"16","Principado de Asturias":"17","Region de Murcia":"18"})
