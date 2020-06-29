import settings
import handlers.base_handler
import csv
class CartogramHandler(handlers.base_handler.BaseCartogramHandler):
    def get_name(self):
        return "Dominican Republic"
    def get_gen_file(self):
        return "{}/dom_processedmap.json".format(settings.CARTOGRAM_DATA_DIR)
    
    def validate_values(self, values):
        if len(values) != 32:
            return False
        
        for v in values:
            if type(v) != float:
                return False
        return True
    
    def gen_area_data(self, values):
        return """1 {} Azua
2 {} Bahoruco
3 {} Barahona
4 {} Dajabon
5 {} Distrito Nacional
6 {} Duarte
7 {} El Seibo
8 {} Espaillat
9 {} Hato Mayor
10 {} Hermanas Mirabal
11 {} Independencia
12 {} La Altagracia
13 {} Elias Pina
14 {} La Romana
15 {} La Vega
16 {} Maria Trinidad Sanchez
17 {} Monsenor Nouel
18 {} Monte Cristi
19 {} Monte Plata
20 {} Pedernales
21 {} Peravia
22 {} Puerto Plata
23 {} Samana
24 {} San Cristobal
25 {} San Jose de Ocoa
26 {} San Juan
27 {} San Pedro de Macoris
28 {} Sanchez Ramirez
29 {} Santiago
30 {} Santiago Rodriguez
31 {} Santo Domingo
32 {} Valverde""".format(*values)
    
    def expect_geojson_output(self):
        return True
    def csv_to_area_string_and_colors(self, csvfile):
        return self.order_by_example(csv.reader(csvfile), "Province", 0, 1, 2, 3, ["Azua","Bahoruco","Barahona","Dajabon","Distrito Nacional","Duarte","El Seibo","Espaillat","Hato Mayor","Hermanas Mirabal","Independencia","La Altagracia","Elias Pina","La Romana","La Vega","Maria Trinidad Sanchez","Monsenor Nouel","Monte Cristi","Monte Plata","Pedernales","Peravia","Puerto Plata","Samana","San Cristobal","San Jose de Ocoa","San Juan","San Pedro de Macoris","Sanchez Ramirez","Santiago","Santiago Rodriguez","Santo Domingo","Valverde"], [0.0 for i in range(0,32)], {"Azua":"1","Bahoruco":"2","Barahona":"3","Dajabon":"4","Distrito Nacional":"5","Duarte":"6","El Seibo":"7","Espaillat":"8","Hato Mayor":"9","Hermanas Mirabal":"10","Independencia":"11","La Altagracia":"12","Elias Pina":"13","La Romana":"14","La Vega":"15","Maria Trinidad Sanchez":"16","Monsenor Nouel":"17","Monte Cristi":"18","Monte Plata":"19","Pedernales":"20","Peravia":"21","Puerto Plata":"22","Samana":"23","San Cristobal":"24","San Jose de Ocoa":"25","San Juan":"26","San Pedro de Macoris":"27","Sanchez Ramirez":"28","Santiago":"29","Santiago Rodriguez":"30","Santo Domingo":"31","Valverde":"32"})
