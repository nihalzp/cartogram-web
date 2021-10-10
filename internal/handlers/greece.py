import settings
import handlers.base_handler
import csv

class CartogramHandler(handlers.base_handler.BaseCartogramHandler):

    def get_name(self):
        return "Greece"

    def get_gen_file(self):
        return "{}/grc_processedmap.json".format(settings.CARTOGRAM_DATA_DIR)
    
    def validate_values(self, values):

        if len(values) != 14:
            return False
        
        for v in values:
            if type(v) != float:
                return False

        return True
    
    def gen_area_data(self, values):
        return """cartogram_id,Region Data,Region Name,Inset
1,{},Attica,
2,{},Central Greece,
3,{},Central Macedonia,
4,{},Crete,
5,{},East Macedonia and Thrace,
6,{},Epirus,
7,{},Ionian Islands,
8,{},Mount Athos,
9,{},North Aegean,
10,{},Peloponnese,
11,{},South Aegean,
12,{},Thessaly,
13,{},West Greece,
14,{},West Macedonia,""".format(*values)
    
    def expect_geojson_output(self):
        return True

    def csv_to_area_string_and_colors(self, csvfile):

        return self.order_by_example(csv.reader(csvfile), "Region/Autonomous Region", 0, 1, 2, 3, ["Attica","Central Greece","Central Macedonia","Crete","East Macedonia and Thrace","Epirus","Ionian Islands","Mount Athos","North Aegean","Peloponnese","South Aegean","Thessaly","West Greece","West Macedonia"], [0.0 for i in range(0,14)], {"Attica":"1","Central Greece":"2","Central Macedonia":"3","Crete":"4","East Macedonia and Thrace":"5","Epirus":"6","Ionian Islands":"7","Mount Athos":"8","North Aegean":"9","Peloponnese":"10","South Aegean":"11","Thessaly":"12","West Greece":"13","West Macedonia":"14"})
