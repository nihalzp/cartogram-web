import settings
import handlers.base_handler
import csv

class CartogramHandler(handlers.base_handler.BaseCartogramHandler):

    def get_name(self):
        return "Colombia"

    def get_gen_file(self):
        return "{}/colombia2_processedmap.json".format(settings.CARTOGRAM_DATA_DIR)
    
    def validate_values(self, values):

        if len(values) != 32:
            return False
        
        for v in values:
            if type(v) != float:
                return False

        return True
    
    def gen_area_data(self, values):
        return """1 {} Amazonas
2 {} Antioquia
3 {} Arauca
4 {} Atlantico
5 {} Bolivar
6 {} Boyaca
7 {} Caldas
8 {} Caqueta
9 {} Casanare
10 {} Cauca
11 {} Cesar
12 {} Choco
13 {} Cordoba
14 {} Cundinamarca
15 {} Guainia
16 {} Guaviare
17 {} Huila
18 {} La Guajira
19 {} Magdalena
20 {} Meta
21 {} Narino
22 {} Norte de Santander
23 {} Putumayo
24 {} Quindio
25 {} Risaralda
26 {} San Andres y Providencia  
27 {} Santander
28 {} Sucre
29 {} Tolima
30 {} Valle del Cauca
31 {} Vaupes
32 {} Vichada""".format(*values)
    
    def expect_geojson_output(self):
        return True

    def csv_to_area_string_and_colors(self, csvfile):

        return self.order_by_example(csv.reader(csvfile), "Department", 0, 1, 2, 3, ["Amazonas","Antioquia","Arauca","Atlantico","Bolivar","Boyaca","Caldas","Caqueta","Casanare","Cauca","Cesar","Choco","Cordoba","Cundinamarca","Guainia","Guaviare","Huila","La Guajira","Magdalena","Meta","Narino","Norte de Santander","Putumayo","Quindio","Risaralda","San Andres y Providencia  ","Santander","Sucre","Tolima","Valle del Cauca","Vaupes","Vichada"], [0.0 for i in range(0,32)], {"Amazonas":"1","Antioquia":"2","Arauca":"3","Atlantico":"4","Bolivar":"5","Boyaca":"6","Caldas":"7","Caqueta":"8","Casanare":"9","Cauca":"10","Cesar":"11","Choco":"12","Cordoba":"13","Cundinamarca":"14","Guainia":"15","Guaviare":"16","Huila":"17","La Guajira":"18","Magdalena":"19","Meta":"20","Narino":"21","Norte de Santander":"22","Putumayo":"23","Quindio":"24","Risaralda":"25","San Andres y Providencia  ":"26","Santander":"27","Sucre":"28","Tolima":"29","Valle del Cauca":"30","Vaupes":"31","Vichada":"32"})
