import settings
import handlers.base_handler
import csv

class CartogramHandler(handlers.base_handler.BaseCartogramHandler):

    def get_name(self):
        return "Algeria"

    def get_gen_file(self):
        return "{}/dza_processedmap.json".format(settings.CARTOGRAM_DATA_DIR)
    
    def validate_values(self, values):

        if len(values) != 48:
            return False
        
        for v in values:
            if type(v) != float:
                return False

        return True
    
    def gen_area_data(self, values):
        return """cartogram_id,Region Data,Region Name,Inset
1,{},Adrar,
2,{},Ain Defla,
3,{},Ain Temouchent,
4,{},Alger,
5,{},Annaba,
6,{},Batna,
7,{},Bechar,
8,{},Bejaia,
9,{},Biskra,
10,{},Blida,
11,{},Bordj Bou Arreridj,
12,{},Bouira,
13,{},Boumerdes,
14,{},Chlef,
15,{},Constantine,
16,{},Djelfa,
17,{},El Bayadh,
18,{},El Oued,
19,{},El Tarf,
20,{},Ghardaia,
21,{},Guelma,
22,{},Illizi,
23,{},Jijel,
24,{},Khenchela,
25,{},Laghouat,
26,{},M'Sila,
27,{},Mascara,
28,{},Medea,
29,{},Mila,
30,{},Mostaganem,
31,{},Naama,
32,{},Oran,
33,{},Ouargla,
34,{},Oum el Bouaghi,
35,{},Relizane,
36,{},Saida,
37,{},Setif,
38,{},Sidi Bel Abbes,
39,{},Skikda,
40,{},Souk Ahras,
41,{},Tamanghasset,
42,{},Tebessa,
43,{},Tiaret,
44,{},Tindouf,
45,{},Tipaza,
46,{},Tissemsilt,
47,{},Tizi Ouzou,
48,{},Tlemcen,""".format(*values)
    
    def expect_geojson_output(self):
        return True

    def csv_to_area_string_and_colors(self, csvfile):

        return self.order_by_example(csv.reader(csvfile), "Province", 0, 1, 2, 3, ["Adrar","Ain Defla","Ain Temouchent","Alger","Annaba","Batna","Bechar","Bejaia","Biskra","Blida","Bordj Bou Arreridj","Bouira","Boumerdes","Chlef","Constantine","Djelfa","El Bayadh","El Oued","El Tarf","Ghardaia","Guelma","Illizi","Jijel","Khenchela","Laghouat","M'Sila","Mascara","Medea","Mila","Mostaganem","Naama","Oran","Ouargla","Oum el Bouaghi","Relizane","Saida","Setif","Sidi Bel Abbes","Skikda","Souk Ahras","Tamanghasset","Tebessa","Tiaret","Tindouf","Tipaza","Tissemsilt","Tizi Ouzou","Tlemcen"], [0.0 for i in range(0,48)], {"Adrar":"1","Ain Defla":"2","Ain Temouchent":"3","Alger":"4","Annaba":"5","Batna":"6","Bechar":"7","Bejaia":"8","Biskra":"9","Blida":"10","Bordj Bou Arreridj":"11","Bouira":"12","Boumerdes":"13","Chlef":"14","Constantine":"15","Djelfa":"16","El Bayadh":"17","El Oued":"18","El Tarf":"19","Ghardaia":"20","Guelma":"21","Illizi":"22","Jijel":"23","Khenchela":"24","Laghouat":"25","M'Sila":"26","Mascara":"27","Medea":"28","Mila":"29","Mostaganem":"30","Naama":"31","Oran":"32","Ouargla":"33","Oum el Bouaghi":"34","Relizane":"35","Saida":"36","Setif":"37","Sidi Bel Abbes":"38","Skikda":"39","Souk Ahras":"40","Tamanghasset":"41","Tebessa":"42","Tiaret":"43","Tindouf":"44","Tipaza":"45","Tissemsilt":"46","Tizi Ouzou":"47","Tlemcen":"48"})
