import settings
import handlers.base_handler
import csv

class CartogramHandler(handlers.base_handler.BaseCartogramHandler):

    def get_name(self):
        return "Arab League"

    def get_gen_file(self):
        return "{}/arab_league_processedmap.json".format(settings.CARTOGRAM_DATA_DIR)
    
    def validate_values(self, values):

        if len(values) != 22:
            return False
        
        for v in values:
            if type(v) != float:
                return False

        return True
    
    def gen_area_data(self, values):
        return """1 {} Algeria
2 {} Bahrain
3 {} Comoros
4 {} Djibouti
5 {} Egypt
6 {} Iraq
7 {} Jordan
8 {} Kuwait
9 {} Lebanon
10 {} Libya
11 {} Mauritania
12 {} Morocco
13 {} Oman
14 {} Palestine
15 {} Qatar
16 {} Saudi Arabia
17 {} Somalia
18 {} Sudan
19 {} Syria
20 {} Tunisia
21 {} United Arab Emirates
22 {} Yemen""".format(*values)
    
    def expect_geojson_output(self):
        return True

    def csv_to_area_string_and_colors(self, csvfile):

        return self.order_by_example(csv.reader(csvfile), "Country", 0, 1, 2, 3, ["Algeria","Bahrain","Comoros","Djibouti","Egypt","Iraq","Jordan","Kuwait","Lebanon","Libya","Mauritania","Morocco","Oman","Palestine","Qatar","Saudi Arabia","Somalia","Sudan","Syria","Tunisia","United Arab Emirates","Yemen"], [0.0 for i in range(0,22)], {"Algeria":"1","Bahrain":"2","Comoros":"3","Djibouti":"4","Egypt":"5","Iraq":"6","Jordan":"7","Kuwait":"8","Lebanon":"9","Libya":"10","Mauritania":"11","Morocco":"12","Oman":"13","Palestine":"14","Qatar":"15","Saudi Arabia":"16","Somalia":"17","Sudan":"18","Syria":"19","Tunisia":"20","United Arab Emirates":"21","Yemen":"22"})
