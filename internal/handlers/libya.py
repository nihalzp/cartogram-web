import settings
import handlers.base_handler
import csv

class CartogramHandler(handlers.base_handler.BaseCartogramHandler):

    def get_name(self):
        return "Libya"

    def get_gen_file(self):
        return "{}/lby_processedmap.json".format(settings.CARTOGRAM_DATA_DIR)
    
    def validate_values(self, values):

        if len(values) != 22:
            return False
        
        for v in values:
            if type(v) != float:
                return False

        return True
    
    def gen_area_data(self, values):
        return """1 {} Al Butnan
2 {} Al Jabal al Akhdar
3 {} Al Jabal al Gharbi
4 {} Al Jifarah
5 {} Al Jufrah
6 {} Al Kufrah
7 {} Al Marj
8 {} Al Marqab
9 {} Al Wahat
10 {} An Nuqat al Khams
11 {} Az Zawiyah
12 {} Benghazi
13 {} Darnah
14 {} Ghat
15 {} Misratah
16 {} Murzuq
17 {} Nalut
18 {} Sabha
19 {} Surt
20 {} Tripoli
21 {} Wadi al Hayat
22 {} Wadi ash Shati'""".format(*values)
    
    def expect_geojson_output(self):
        return True

    def csv_to_area_string_and_colors(self, csvfile):

        return self.order_by_example(csv.reader(csvfile), "District", 0, 1, 2, 3, ["Al Butnan","Al Jabal al Akhdar","Al Jabal al Gharbi","Al Jifarah","Al Jufrah","Al Kufrah","Al Marj","Al Marqab","Al Wahat","An Nuqat al Khams","Az Zawiyah","Benghazi","Darnah","Ghat","Misratah","Murzuq","Nalut","Sabha","Surt","Tripoli","Wadi al Hayat","Wadi ash Shati'"], [0.0 for i in range(0,22)], {"Al Butnan":"1","Al Jabal al Akhdar":"2","Al Jabal al Gharbi":"3","Al Jifarah":"4","Al Jufrah":"5","Al Kufrah":"6","Al Marj":"7","Al Marqab":"8","Al Wahat":"9","An Nuqat al Khams":"10","Az Zawiyah":"11","Benghazi":"12","Darnah":"13","Ghat":"14","Misratah":"15","Murzuq":"16","Nalut":"17","Sabha":"18","Surt":"19","Tripoli":"20","Wadi al Hayat":"21","Wadi ash Shati'":"22"})
