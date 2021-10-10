import settings
import handlers.base_handler
import csv

class CartogramHandler(handlers.base_handler.BaseCartogramHandler):

    def get_name(self):
        return "Peru"

    def get_gen_file(self):
        return "{}/per_processedmap.json".format(settings.CARTOGRAM_DATA_DIR)
    
    def validate_values(self, values):

        if len(values) != 26:
            return False
        
        for v in values:
            if type(v) != float:
                return False

        return True
    
    def gen_area_data(self, values):
        return """cartogram_id,Region Data,Region Name,Inset
1,{},Amazonas,
2,{},Ancash,
3,{},Apurimac,
4,{},Arequipa,
5,{},Ayacucho,
6,{},Cajamarca,
7,{},Callao,
8,{},Cusco,
9,{},Huancavelica,
10,{},Huanuco,
11,{},Ica,
12,{},Junin,
13,{},La Libertad,
14,{},Lambayeque,
15,{},Lima,
16,{},Lima Province,
17,{},Loreto,
18,{},Madre de Dios,
19,{},Moquegua,
20,{},Pasco,
21,{},Piura,
22,{},Puno,
23,{},San Martin,
24,{},Tacna,
25,{},Tumbes,
26,{},Ucayali,""".format(*values)
    
    def expect_geojson_output(self):
        return True

    def csv_to_area_string_and_colors(self, csvfile):

        return self.order_by_example(csv.reader(csvfile), "Region/Province", 0, 1, 2, 3, ["Amazonas","Ancash","Apurimac","Arequipa","Ayacucho","Cajamarca","Callao","Cusco","Huancavelica","Huanuco","Ica","Junin","La Libertad","Lambayeque","Lima","Lima Province","Loreto","Madre de Dios","Moquegua","Pasco","Piura","Puno","San Martin","Tacna","Tumbes","Ucayali"], [0.0 for i in range(0,26)], {"Amazonas":"1","Ancash":"2","Apurimac":"3","Arequipa":"4","Ayacucho":"5","Cajamarca":"6","Callao":"7","Cusco":"8","Huancavelica":"9","Huanuco":"10","Ica":"11","Junin":"12","La Libertad":"13","Lambayeque":"14","Lima":"15","Lima Province":"16","Loreto":"17","Madre de Dios":"18","Moquegua":"19","Pasco":"20","Piura":"21","Puno":"22","San Martin":"23","Tacna":"24","Tumbes":"25","Ucayali":"26"})
