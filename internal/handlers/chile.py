import settings
import handlers.base_handler
import csv

class CartogramHandler(handlers.base_handler.BaseCartogramHandler):

    def get_name(self):
        return "Chile"

    def get_gen_file(self):
        return "{}/chl_processedmap.json".format(settings.CARTOGRAM_DATA_DIR)
    
    def validate_values(self, values):

        if len(values) != 16:
            return False
        
        for v in values:
            if type(v) != float:
                return False

        return True
    
    def gen_area_data(self, values):
        return """cartogram_id,Region Data,Region Name,Inset
1,{},Aisen del General Carlos Ibanez del Campo,
2,{},Antofagasta,
3,{},Araucania,
4,{},Arica y Parinacota,
5,{},Atacama,
6,{},Biobio,
7,{},Coquimbo,
8,{},Libertador General Bernardo O'Higgins,
9,{},Los Lagos,
10,{},Los Rios,
11,{},Magallanes y Antartica Chilena,
12,{},Maule,
13,{},Nuble,
14,{},Region Metropolitana de Santiago,
15,{},Tarapaca,
16,{},Valparaiso,""".format(*values)
    
    def expect_geojson_output(self):
        return True

    def csv_to_area_string_and_colors(self, csvfile):

        return self.order_by_example(csv.reader(csvfile), "Region", 0, 1, 2, 3, ["Aisen del General Carlos Ibanez del Campo","Antofagasta","Araucania","Arica y Parinacota","Atacama","Biobio","Coquimbo","Libertador General Bernardo O'Higgins","Los Lagos","Los Rios","Magallanes y Antartica Chilena","Maule","Nuble","Region Metropolitana de Santiago","Tarapaca","Valparaiso"], [0.0 for i in range(0,16)], {"Aisen del General Carlos Ibanez del Campo":"1","Antofagasta":"2","Araucania":"3","Arica y Parinacota":"4","Atacama":"5","Biobio":"6","Coquimbo":"7","Libertador General Bernardo O'Higgins":"8","Los Lagos":"9","Los Rios":"10","Magallanes y Antartica Chilena":"11","Maule":"12","Nuble":"13","Region Metropolitana de Santiago":"14","Tarapaca":"15","Valparaiso":"16"})
