import settings
import handlers.base_handler
import csv

class CartogramHandler(handlers.base_handler.BaseCartogramHandler):

    def get_name(self):
        return "Saudi Arabia"

    def get_gen_file(self):
        return "{}/saudiArabia_processedmap.json".format(settings.CARTOGRAM_DATA_DIR)
    
    def validate_values(self, values):

        if len(values) != 13:
            return False
        
        for v in values:
            if type(v) != float:
                return False

        return True
    
    def gen_area_data(self, values):
        return """1 {} 'Asir
2 {} Al Bahah
3 {} Al Hudud ash Shamaliyah
4 {} Al Jawf
5 {} Al Madinah
6 {} Al Quassim
7 {} Ar Riyad
8 {} Ash Sharqiyah
9 {} Ha'il
10 {} Jizan
11 {} Makkah
12 {} Najran
13 {} Tabuk""".format(*values)
    
    def expect_geojson_output(self):
        return True

    def csv_to_area_string_and_colors(self, csvfile):

        return self.order_by_example(csv.reader(csvfile), "Region", 0, 1, 2, 3, ["'Asir","Al Bahah","Al Hudud ash Shamaliyah","Al Jawf","Al Madinah","Al Quassim","Ar Riyad","Ash Sharqiyah","Ha'il","Jizan","Makkah","Najran","Tabuk"], [0.0 for i in range(0,13)], {"'Asir":"1","Al Bahah":"2","Al Hudud ash Shamaliyah":"3","Al Jawf":"4","Al Madinah":"5","Al Quassim":"6","Ar Riyad":"7","Ash Sharqiyah":"8","Ha'il":"9","Jizan":"10","Makkah":"11","Najran":"12","Tabuk":"13"})
