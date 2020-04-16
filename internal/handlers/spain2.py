import settings
import handlers.base_handler
import csv

class CartogramHandler(handlers.base_handler.BaseCartogramHandler):

    def get_name(self):
        return "Spain"

    def get_gen_file(self):
        return "{}/spain2_processedmap.json".format(settings.CARTOGRAM_DATA_DIR)
    
    def validate_values(self, values):

        if len(values) != 17:
            return False
        
        for v in values:
            if type(v) != float:
                return False

        return True
    
    def gen_area_data(self, values):
        return """7 {} Ceuta y Melilla
14 {} La Rioja
3 {} Cantabria
11 {} Extremadura
9 {} Comunidad Foral de Navarra
16 {} Principado de Asturias
17 {} Region de Murcia
13 {} Islas Baleares
2 {} Aragon
5 {} Castilla-La Mancha
4 {} Castilla y Leon
12 {} Galicia
15 {} Pais Vasco
10 {} Comunidad Valenciana
1 {} Andalucia
6 {} Cataluna
8 {} Comunidad de Madrid""".format(*values)
    
    def expect_geojson_output(self):
        return True

    def csv_to_area_string_and_colors(self, csvfile):

        return self.order_by_example(csv.reader(csvfile), "Autonomous Community/City", 0, 1, 2, 3, ["Ceuta y Melilla","La Rioja","Cantabria","Extremadura","Comunidad Foral de Navarra","Principado de Asturias","Region de Murcia","Islas Baleares","Aragon","Castilla-La Mancha","Castilla y Leon","Galicia","Pais Vasco","Comunidad Valenciana","Andalucia","Cataluna","Comunidad de Madrid"], [0.0 for i in range(0,17)], {"Ceuta y Melilla":"7","La Rioja":"14","Cantabria":"3","Extremadura":"11","Comunidad Foral de Navarra":"9","Principado de Asturias":"16","Region de Murcia":"17","Islas Baleares":"13","Aragon":"2","Castilla-La Mancha":"5","Castilla y Leon":"4","Galicia":"12","Pais Vasco":"15","Comunidad Valenciana":"10","Andalucia":"1","Cataluna":"6","Comunidad de Madrid":"8"})
