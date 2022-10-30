import settings
import handlers.base_handler
import csv

class CartogramHandler(handlers.base_handler.BaseCartogramHandler):

    def get_name(self):
        return "India"

    def get_gen_file(self):
        return "{}/india_processedmap.json".format(settings.CARTOGRAM_DATA_DIR)
    
    def validate_values(self, values):

        if len(values) != 35:
            return False
        
        for v in values:
            if type(v) != float:
                return False

        return True
    
    def gen_area_data(self, values):
        return """cartogram_id,Region Data,Region Name,Inset
1,{},Andaman and Nicobar Islands,
2,{},Andhra Pradesh,
3,{},Arunachal Pradesh,
4,{},Assam,
5,{},Bihar,
6,{},Chandigarh,
7,{},Chhattisgarh,
8,{},Dadra and Nagar Haveli,
9,{},Daman and Diu,
10,{},Delhi,
11,{},Goa,
12,{},Gujarat,
13,{},Haryana,
14,{},Himachal Pradesh,
15,{},Jammu and Kashmir,
16,{},Jharkhand,
17,{},Karnataka,
18,{},Kerala,
19,{},Madhya Pradesh,
20,{},Maharashtra,
21,{},Manipur,
22,{},Meghalaya,
23,{},Mizoram,
24,{},Nagaland,
25,{},Odisha,
26,{},Puducherry,
27,{},Punjab,
28,{},Rajasthan,
29,{},Sikkim,
30,{},Tamil Nadu,
31,{},Telangana,
32,{},Tripura,
33,{},Uttar Pradesh,
34,{},Uttarakhand,
35,{},West Bengal,""".format(*values)
    
    def expect_geojson_output(self):
        return True

    def csv_to_area_string_and_colors(self, csvfile):

        return self.order_by_example(csv.reader(csvfile), "State", 0, 1, 2, 3, ["Andaman and Nicobar Islands","Andhra Pradesh","Arunachal Pradesh","Assam","Bihar","Chandigarh","Chhattisgarh","Dadra and Nagar Haveli","Daman and Diu","Delhi","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Puducherry","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal"], [0.0 for i in range(0,35)], {"Andaman and Nicobar Islands":"1","Andhra Pradesh":"2","Arunachal Pradesh":"3","Assam":"4","Bihar":"5","Chandigarh":"6","Chhattisgarh":"7","Dadra and Nagar Haveli":"8","Daman and Diu":"9","Delhi":"10","Goa":"11","Gujarat":"12","Haryana":"13","Himachal Pradesh":"14","Jammu and Kashmir":"15","Jharkhand":"16","Karnataka":"17","Kerala":"18","Madhya Pradesh":"19","Maharashtra":"20","Manipur":"21","Meghalaya":"22","Mizoram":"23","Nagaland":"24","Odisha":"25","Puducherry":"26","Punjab":"27","Rajasthan":"28","Sikkim":"29","Tamil Nadu":"30","Telangana":"31","Tripura":"32","Uttar Pradesh":"33","Uttarakhand":"34","West Bengal":"35"})
