import settings
import handlers.base_handler
import csv
class CartogramHandler(handlers.base_handler.BaseCartogramHandler):
    def get_name(self):
        return "Paraguay"
    def get_gen_file(self):
        return "{}/pry_processedmap.json".format(settings.CARTOGRAM_DATA_DIR)
    
    def validate_values(self, values):
        if len(values) != 18:
            return False
        
        for v in values:
            if type(v) != float:
                return False
        return True
    
    def gen_area_data(self, values):
        return """cartogram_id,Region Data,Region Name,Inset
1,{},Alto Paraguay,
2,{},Alto Parana,
3,{},Amambay,
4,{},Asuncion,
5,{},Boqueron,
6,{},Caaguazu,
7,{},Caazapa,
8,{},Canindeyu,
9,{},Central,
10,{},Concepcion,
11,{},Cordillera,
12,{},Guaira,
13,{},Itapua,
14,{},Misiones,
15,{},Neembucu,
16,{},Paraguari,
17,{},Presidente Hayes,
18,{},San Pedro,""".format(*values)
    
    def expect_geojson_output(self):
        return True
    def csv_to_area_string_and_colors(self, csvfile):
        return self.order_by_example(csv.reader(csvfile), "Department", 0, 1, 2, 3, ["Alto Paraguay","Alto Parana","Amambay","Asuncion","Boqueron","Caaguazu","Caazapa","Canindeyu","Central","Concepcion","Cordillera","Guaira","Itapua","Misiones","Neembucu","Paraguari","Presidente Hayes","San Pedro"], [0.0 for i in range(0,18)], {"Alto Paraguay":"1","Alto Parana":"2","Amambay":"3","Asuncion":"4","Boqueron":"5","Caaguazu":"6","Caazapa":"7","Canindeyu":"8","Central":"9","Concepcion":"10","Cordillera":"11","Guaira":"12","Itapua":"13","Misiones":"14","Neembucu":"15","Paraguari":"16","Presidente Hayes":"17","San Pedro":"18"})
