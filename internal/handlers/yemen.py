import settings
import handlers.base_handler
import csv

class CartogramHandler(handlers.base_handler.BaseCartogramHandler):

    def get_name(self):
        return "Yemen"

    def get_gen_file(self):
        return "{}/yem_processedmap.json".format(settings.CARTOGRAM_DATA_DIR)
    
    def validate_values(self, values):

        if len(values) != 22:
            return False
        
        for v in values:
            if type(v) != float:
                return False

        return True
    
    def gen_area_data(self, values):
        return """1 {} Aden
2 {} Abyan
3 {} Al Bayda'
4 {} Ad Dali
5 {} Al Hudaydah
6 {} Al Jawf
7 {} Al Mahrah
8 {} Al Mahwit
9 {} Amanat Al Asimah
10 {} 'Amran
11 {} Dhamar
12 {} Hadramawt
13 {} Hajjah
14 {} Ibb
15 {} Lahij
16 {} Ma'rib
17 {} Raymah
18 {} Sa'dah
19 {} Sana'a
20 {} Shabwah
21 {} Socotra
22 {} Ta'izz""".format(*values)
    
    def expect_geojson_output(self):
        return True

    def csv_to_area_string_and_colors(self, csvfile):

        return self.order_by_example(csv.reader(csvfile), "Governorate", 0, 1, 2, 3, ["Aden","Abyan","Al Bayda'","Ad Dali","Al Hudaydah","Al Jawf","Al Mahrah","Al Mahwit","Amanat Al Asimah","'Amran","Dhamar","Hadramawt","Hajjah","Ibb","Lahij","Ma'rib","Raymah","Sa'dah","Sana'a","Shabwah","Socotra","Ta'izz"], [0.0 for i in range(0,22)], {"Aden":"1","Abyan":"2","Al Bayda'":"3","Ad Dali":"4","Al Hudaydah":"5","Al Jawf":"6","Al Mahrah":"7","Al Mahwit":"8","Amanat Al Asimah":"9","'Amran":"10","Dhamar":"11","Hadramawt":"12","Hajjah":"13","Ibb":"14","Lahij":"15","Ma'rib":"16","Raymah":"17","Sa'dah":"18","Sana'a":"19","Shabwah":"20","Socotra":"21","Ta'izz":"22"})
