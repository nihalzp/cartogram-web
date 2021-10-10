import settings
import handlers.base_handler
import csv

class CartogramHandler(handlers.base_handler.BaseCartogramHandler):

    def get_name(self):
        return "Romania"

    def get_gen_file(self):
        return "{}/romania_processedmap.json".format(settings.CARTOGRAM_DATA_DIR)
    
    def validate_values(self, values):

        if len(values) != 42:
            return False
        
        for v in values:
            if type(v) != float:
                return False

        return True
    
    def gen_area_data(self, values):
        return """cartogram_id,Region Data,Region Name,Inset
1,{},Alba,
2,{},Arad,
3,{},Arges,
4,{},Bacau,
5,{},Bihor,
6,{},Bistrita-Nasaud,
7,{},Botosani,
8,{},Braila,
9,{},Brasov,
10,{},Bucharest,
11,{},Buzau,
12,{},Calarasi,
13,{},Caras-Severin,
14,{},Cluj,
15,{},Constanta,
16,{},Covasna,
17,{},Dambovita,
18,{},Dolj,
19,{},Galati,
20,{},Giurgiu,
21,{},Gorj,
22,{},Harghita,
23,{},Hunedoara,
24,{},Ialomita,
25,{},Iasi,
26,{},Ilfov,
27,{},Maramures,
28,{},Mehedinti,
29,{},Mures,
30,{},Neamt,
31,{},Olt,
32,{},Prahova,
33,{},Salaj,
34,{},Satu Mare,
35,{},Sibiu,
36,{},Suceava,
37,{},Teleorman,
38,{},Timis,
39,{},Tulcea,
40,{},Valcea,
41,{},Vaslui,
42,{},Vrancea,""".format(*values)
    
    def expect_geojson_output(self):
        return True

    def csv_to_area_string_and_colors(self, csvfile):

        return self.order_by_example(csv.reader(csvfile), "County", 0, 1, 2, 3, ["Alba","Arad","Arges","Bacau","Bihor","Bistrita-Nasaud","Botosani","Braila","Brasov","Bucharest","Buzau","Calarasi","Caras-Severin","Cluj","Constanta","Covasna","Dambovita","Dolj","Galati","Giurgiu","Gorj","Harghita","Hunedoara","Ialomita","Iasi","Ilfov","Maramures","Mehedinti","Mures","Neamt","Olt","Prahova","Salaj","Satu Mare","Sibiu","Suceava","Teleorman","Timis","Tulcea","Valcea","Vaslui","Vrancea"], [0.0 for i in range(0,42)], {"Alba":"1","Arad":"2","Arges":"3","Bacau":"4","Bihor":"5","Bistrita-Nasaud":"6","Botosani":"7","Braila":"8","Brasov":"9","Bucharest":"10","Buzau":"11","Calarasi":"12","Caras-Severin":"13","Cluj":"14","Constanta":"15","Covasna":"16","Dambovita":"17","Dolj":"18","Galati":"19","Giurgiu":"20","Gorj":"21","Harghita":"22","Hunedoara":"23","Ialomita":"24","Iasi":"25","Ilfov":"26","Maramures":"27","Mehedinti":"28","Mures":"29","Neamt":"30","Olt":"31","Prahova":"32","Salaj":"33","Satu Mare":"34","Sibiu":"35","Suceava":"36","Teleorman":"37","Timis":"38","Tulcea":"39","Valcea":"40","Vaslui":"41","Vrancea":"42"})
