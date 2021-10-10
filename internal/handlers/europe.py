import settings
import handlers.base_handler
import csv

class CartogramHandler(handlers.base_handler.BaseCartogramHandler):

    def get_name(self):
        return "Europe (Eurostat members)"

    def get_gen_file(self):
        return "{}/europe_processedmap.json".format(settings.CARTOGRAM_DATA_DIR)
    
    def validate_values(self, values):

        if len(values) != 35:
            return False
        
        for v in values:
            if type(v) != float:
                return False

        return True
    
    def gen_area_data(self, values):
        return """cartogram_id,Region Data,Region Name,Inset
1,{},Austria,
2,{},Belgium,
3,{},Bosnia and Herzegovina,
4,{},Bulgaria,
5,{},Croatia,
6,{},Czech Republic,
7,{},Denmark,
8,{},Estonia,
9,{},Finland,
10,{},France,
11,{},Germany,
12,{},Greece,
13,{},Hungary,
14,{},Iceland,
15,{},Ireland,
16,{},Italy,
17,{},Latvia,
18,{},Liechtenstein,
19,{},Lithuania,
20,{},Luxembourg,
21,{},Malta,
22,{},Netherlands,
23,{},North Macedonia,
24,{},Norway,
25,{},Poland,
26,{},Portugal,
27,{},Republic of Cyprus,
28,{},Republic of Serbia,
29,{},Romania,
30,{},Slovakia,
31,{},Slovenia,
32,{},Spain,
33,{},Sweden,
34,{},Switzerland,
35,{},United Kingdom,""".format(*values)
    
    def expect_geojson_output(self):
        return True

    def csv_to_area_string_and_colors(self, csvfile):

        return self.order_by_example(csv.reader(csvfile), "Country", 0, 1, 2, 3, ["Austria","Belgium","Bosnia and Herzegovina","Bulgaria","Croatia","Czech Republic","Denmark","Estonia","Finland","France","Germany","Greece","Hungary","Iceland","Ireland","Italy","Latvia","Liechtenstein","Lithuania","Luxembourg","Malta","Netherlands","North Macedonia","Norway","Poland","Portugal","Republic of Cyprus","Republic of Serbia","Romania","Slovakia","Slovenia","Spain","Sweden","Switzerland","United Kingdom"], [0.0 for i in range(0,35)], {"Austria":"1","Belgium":"2","Bosnia and Herzegovina":"3","Bulgaria":"4","Croatia":"5","Czech Republic":"6","Denmark":"7","Estonia":"8","Finland":"9","France":"10","Germany":"11","Greece":"12","Hungary":"13","Iceland":"14","Ireland":"15","Italy":"16","Latvia":"17","Liechtenstein":"18","Lithuania":"19","Luxembourg":"20","Malta":"21","Netherlands":"22","North Macedonia":"23","Norway":"24","Poland":"25","Portugal":"26","Republic of Cyprus":"27","Republic of Serbia":"28","Romania":"29","Slovakia":"30","Slovenia":"31","Spain":"32","Sweden":"33","Switzerland":"34","United Kingdom":"35"})
