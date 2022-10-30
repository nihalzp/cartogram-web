import settings
import handlers.base_handler
import csv

class CartogramHandler(handlers.base_handler.BaseCartogramHandler):

    def get_name(self):
        return "Taiwan (Mainland China and Taiwan)"

    def get_gen_file(self):
        return "{}/china_processedmap.json".format(settings.CARTOGRAM_DATA_DIR)
    
    def validate_values(self, values):

        if len(values) != 34:
            return False
        
        for v in values:
            if type(v) != float:
                return False

        return True
    
    def gen_area_data(self, values):
        return """cartogram_id,Region Data,Region Name,Inset
1,{},Anhui,
2,{},Beijing,
3,{},Chongqing,
4,{},Fujian,
5,{},Gansu,
6,{},Guangdong,
7,{},Guangxi,
8,{},Guizhou,
9,{},Hainan,
10,{},Hebei,
11,{},Heilongjiang,
12,{},Henan,
13,{},Hong Kong,
14,{},Hubei,
15,{},Hunan,
16,{},Inner Mongolia,
17,{},Jiangsu,
18,{},Jiangxi,
19,{},Jilin,
20,{},Liaoning,
21,{},Macau,
22,{},Ningxia,
23,{},Qinghai,
24,{},Shaanxi,
25,{},Shandong,
26,{},Shanghai,
27,{},Shanxi,
28,{},Sichuan,
29,{},Taiwan,
30,{},Tianjin,
31,{},Tibet,
32,{},Xinjiang,
33,{},Yunnan,
34,{},Zhejiang,""".format(*values)
    
    def expect_geojson_output(self):
        return True

    def csv_to_area_string_and_colors(self, csvfile):

        return self.order_by_example(csv.reader(csvfile), "Province", 0, 1, 2, 3, ["Anhui","Beijing","Chongqing","Fujian","Gansu","Guangdong","Guangxi","Guizhou","Hainan","Hebei","Heilongjiang","Henan","Hong Kong","Hubei","Hunan","Inner Mongolia","Jiangsu","Jiangxi","Jilin","Liaoning","Macau","Ningxia","Qinghai","Shaanxi","Shandong","Shanghai","Shanxi","Sichuan","Taiwan","Tianjin","Tibet","Xinjiang","Yunnan","Zhejiang"], [0.0 for i in range(0,34)], {"Anhui":"1","Beijing":"2","Chongqing":"3","Fujian":"4","Gansu":"5","Guangdong":"6","Guangxi":"7","Guizhou":"8","Hainan":"9","Hebei":"10","Heilongjiang":"11","Henan":"12","Hong Kong":"13","Hubei":"14","Hunan":"15","Inner Mongolia":"16","Jiangsu":"17","Jiangxi":"18","Jilin":"19","Liaoning":"20","Macau":"21","Ningxia":"22","Qinghai":"23","Shaanxi":"24","Shandong":"25","Shanghai":"26","Shanxi":"27","Sichuan":"28","Taiwan":"29","Tianjin":"30","Tibet":"31","Xinjiang":"32","Yunnan":"33","Zhejiang":"34"})
