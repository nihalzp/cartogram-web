import settings
import handlers.base_handler
import csv

class CartogramHandler(handlers.base_handler.BaseCartogramHandler):

    def get_name(self):
        return "Croatia"

    def get_gen_file(self):
        return "{}/hrv_processedmap.json".format(settings.CARTOGRAM_DATA_DIR)
    
    def validate_values(self, values):

        if len(values) != 21:
            return False
        
        for v in values:
            if type(v) != float:
                return False

        return True
    
    def gen_area_data(self, values):
        return """cartogram_id,Region Data,Region Name,Inset
1,{},Bjelovar-Bilogora,
2,{},Brod-Posavina,
3,{},Dubrovnik-Neretva,
4,{},City of Zagreb,
5,{},Istria,
6,{},Karlovac,
7,{},Koprivnica-Krizevci,
8,{},Krapina-Zagorje,
9,{},Lika-Senj,
10,{},Medimurje,
11,{},Osijek-Baranja,
12,{},Pozega-Slavonia,
13,{},Primorje-Gorski Kotar,
14,{},Sibenik-Knin,
15,{},Sisak-Moslavina,
16,{},Split-Dalmatia,
17,{},Varazdin,
18,{},Virovitica-Podravina,
19,{},Vukovar-Srijem,
20,{},Zadar,
21,{},Zagreb County,""".format(*values)
    
    def expect_geojson_output(self):
        return True

    def csv_to_area_string_and_colors(self, csvfile):

        return self.order_by_example(csv.reader(csvfile), "Region", 0, 1, 2, 3, ["Bjelovar-Bilogora","Brod-Posavina","Dubrovnik-Neretva","City of Zagreb","Istria","Karlovac","Koprivnica-Krizevci","Krapina-Zagorje","Lika-Senj","Medimurje","Osijek-Baranja","Pozega-Slavonia","Primorje-Gorski Kotar","Sibenik-Knin","Sisak-Moslavina","Split-Dalmatia","Varazdin","Virovitica-Podravina","Vukovar-Srijem","Zadar","Zagreb County"], [0.0 for i in range(0,21)], {"Bjelovar-Bilogora":"1","Brod-Posavina":"2","Dubrovnik-Neretva":"3","City of Zagreb":"4","Istria":"5","Karlovac":"6","Koprivnica-Krizevci":"7","Krapina-Zagorje":"8","Lika-Senj":"9","Medimurje":"10","Osijek-Baranja":"11","Pozega-Slavonia":"12","Primorje-Gorski Kotar":"13","Sibenik-Knin":"14","Sisak-Moslavina":"15","Split-Dalmatia":"16","Varazdin":"17","Virovitica-Podravina":"18","Vukovar-Srijem":"19","Zadar":"20","Zagreb County":"21"})
