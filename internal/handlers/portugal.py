import settings
import handlers.base_handler
import csv

class CartogramHandler(handlers.base_handler.BaseCartogramHandler):

    def get_name(self):
        return "Portugal"

    def get_gen_file(self):
        return "{}/prt_processedmap.json".format(settings.CARTOGRAM_DATA_DIR)
    
    def validate_values(self, values):

        if len(values) != 18:
            return False
        
        for v in values:
            if type(v) != float:
                return False

        return True
    
    def gen_area_data(self, values):
        return """cartogram_id,Region Data,Region Name,Inset
1,{},Aveiro,
2,{},Beja,
3,{},Braga,
4,{},Braganca,
5,{},Castelo Branco,
6,{},Coimbra,
7,{},Evora,
8,{},Faro,
9,{},Guarda,
10,{},Leiria,
11,{},Lisboa,
12,{},Portalegre,
13,{},Porto,
14,{},Santarem,
15,{},Setubal,
16,{},Viana do Castelo,
17,{},Vila Real,
18,{},Viseu,""".format(*values)
    
    def expect_geojson_output(self):
        return True

    def csv_to_area_string_and_colors(self, csvfile):

        return self.order_by_example(csv.reader(csvfile), "District", 0, 1, 2, 3, ["Aveiro","Beja","Braga","Braganca","Castelo Branco","Coimbra","Evora","Faro","Guarda","Leiria","Lisboa","Portalegre","Porto","Santarem","Setubal","Viana do Castelo","Vila Real","Viseu"], [0.0 for i in range(0,18)], {"Aveiro":"1","Beja":"2","Braga":"3","Braganca":"4","Castelo Branco":"5","Coimbra":"6","Evora":"7","Faro":"8","Guarda":"9","Leiria":"10","Lisboa":"11","Portalegre":"12","Porto":"13","Santarem":"14","Setubal":"15","Viana do Castelo":"16","Vila Real":"17","Viseu":"18"})
