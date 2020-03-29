import settings
import handlers.base_handler
import csv

class CartogramHandler(handlers.base_handler.BaseCartogramHandler):

    def get_name(self):
        return "Indonesia"

    def get_gen_file(self):
        return "{}/idn_processedmap.json".format(settings.CARTOGRAM_DATA_DIR)
    
    def validate_values(self, values):

        if len(values) != 33:
            return False
        
        for v in values:
            if type(v) != float:
                return False

        return True
    
    def gen_area_data(self, values):
        return """1 {} Aceh
2 {} Bali
3 {} Bangka Belitung
4 {} Banten
5 {} Bengkulu
6 {} Gorontalo
7 {} Jakarta Raya
8 {} Jambi
9 {} Jawa Barat
10 {} Jawa Tengah
11 {} Jawa Timur
12 {} Kalimantan Barat
13 {} Kalimantan Selatan
14 {} Kalimantan Tengah
15 {} Kalimantan Timur
16 {} Kepulauan Riau
17 {} Lampung
18 {} Maluku
19 {} Maluku Utara
20 {} Nusa Tenggara Barat
21 {} Nusa Tenggara Timur
22 {} Papua
23 {} Papua Barat
24 {} Riau
25 {} Sulawesi Barat
26 {} Sulawesi Selatan
27 {} Sulawesi Tengah
28 {} Sulawesi Tenggara
29 {} Sulawesi Utara
30 {} Sumatera Barat
31 {} Sumatera Selatan
32 {} Sumatera Utara
33 {} Yogyakarta""".format(*values)
    
    def expect_geojson_output(self):
        return True

    def csv_to_area_string_and_colors(self, csvfile):

        return self.order_by_example(csv.reader(csvfile), "Region", 0, 1, 2, 3, ["Aceh","Bali","Bangka Belitung","Banten","Bengkulu","Gorontalo","Jakarta Raya","Jambi","Jawa Barat","Jawa Tengah","Jawa Timur","Kalimantan Barat","Kalimantan Selatan","Kalimantan Tengah","Kalimantan Timur","Kepulauan Riau","Lampung","Maluku","Maluku Utara","Nusa Tenggara Barat","Nusa Tenggara Timur","Papua","Papua Barat","Riau","Sulawesi Barat","Sulawesi Selatan","Sulawesi Tengah","Sulawesi Tenggara","Sulawesi Utara","Sumatera Barat","Sumatera Selatan","Sumatera Utara","Yogyakarta"], [0.0 for i in range(0,33)], {"Aceh":"1","Bali":"2","Bangka Belitung":"3","Banten":"4","Bengkulu":"5","Gorontalo":"6","Jakarta Raya":"7","Jambi":"8","Jawa Barat":"9","Jawa Tengah":"10","Jawa Timur":"11","Kalimantan Barat":"12","Kalimantan Selatan":"13","Kalimantan Tengah":"14","Kalimantan Timur":"15","Kepulauan Riau":"16","Lampung":"17","Maluku":"18","Maluku Utara":"19","Nusa Tenggara Barat":"20","Nusa Tenggara Timur":"21","Papua":"22","Papua Barat":"23","Riau":"24","Sulawesi Barat":"25","Sulawesi Selatan":"26","Sulawesi Tengah":"27","Sulawesi Tenggara":"28","Sulawesi Utara":"29","Sumatera Barat":"30","Sumatera Selatan":"31","Sumatera Utara":"32","Yogyakarta":"33"})
