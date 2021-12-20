import settings
import handlers.base_handler
import csv

class CartogramHandler(handlers.base_handler.BaseCartogramHandler):

    def get_name(self):
        return "USA Test 2"

    def get_gen_file(self):
        return "{}/uspr_processedmap.json".format(settings.CARTOGRAM_DATA_DIR)
    
    def validate_values(self, values):

        if len(values) != 52:
            return False
        
        for v in values:
            if type(v) != float:
                return False

        return True
    
    def gen_area_data(self, values):
        return """cartogram_id,Region Data,Region Name,Inset
1,{},Alabama,
2,{},Alaska,
3,{},Arizona,
4,{},Arkansas,
5,{},California,
6,{},Colorado,
7,{},Connecticut,
8,{},Delaware,
9,{},District of Columbia,
10,{},Florida,
11,{},Georgia,
12,{},Hawaii,
13,{},Idaho,
14,{},Illinois,
15,{},Indiana,
16,{},Iowa,
17,{},Kansas,
18,{},Kentucky,
19,{},Louisiana,
20,{},Maine,
21,{},Maryland,
22,{},Massachusetts,
23,{},Michigan,
24,{},Minnesota,
25,{},Mississippi,
26,{},Missouri,
27,{},Montana,
28,{},Nebraska,
29,{},Nevada,
30,{},New Hampshire,
31,{},New Jersey,
32,{},New Mexico,
33,{},New York,
34,{},North Carolina,
35,{},North Dakota,
36,{},Ohio,
37,{},Oklahoma,
38,{},Oregon,
39,{},Pennsylvania,
40,{},Puerto Rico,
41,{},Rhode Island,
42,{},South Carolina,
43,{},South Dakota,
44,{},Tennessee,
45,{},Texas,
46,{},Utah,
47,{},Vermont,
48,{},Virginia,
49,{},Washington,
50,{},West Virginia,
51,{},Wisconsin,
52,{},Wyoming,""".format(*values)
    
    def expect_geojson_output(self):
        return True

    def csv_to_area_string_and_colors(self, csvfile):

        return self.order_by_example(csv.reader(csvfile), "State", 0, 1, 2, 3, ["Alabama","Alaska","Arizona","Arkansas","California","Colorado","Connecticut","Delaware","District of Columbia","Florida","Georgia","Hawaii","Idaho","Illinois","Indiana","Iowa","Kansas","Kentucky","Louisiana","Maine","Maryland","Massachusetts","Michigan","Minnesota","Mississippi","Missouri","Montana","Nebraska","Nevada","New Hampshire","New Jersey","New Mexico","New York","North Carolina","North Dakota","Ohio","Oklahoma","Oregon","Pennsylvania","Puerto Rico","Rhode Island","South Carolina","South Dakota","Tennessee","Texas","Utah","Vermont","Virginia","Washington","West Virginia","Wisconsin","Wyoming"], [0.0 for i in range(0,52)], {"Alabama":"1","Alaska":"2","Arizona":"3","Arkansas":"4","California":"5","Colorado":"6","Connecticut":"7","Delaware":"8","District of Columbia":"9","Florida":"10","Georgia":"11","Hawaii":"12","Idaho":"13","Illinois":"14","Indiana":"15","Iowa":"16","Kansas":"17","Kentucky":"18","Louisiana":"19","Maine":"20","Maryland":"21","Massachusetts":"22","Michigan":"23","Minnesota":"24","Mississippi":"25","Missouri":"26","Montana":"27","Nebraska":"28","Nevada":"29","New Hampshire":"30","New Jersey":"31","New Mexico":"32","New York":"33","North Carolina":"34","North Dakota":"35","Ohio":"36","Oklahoma":"37","Oregon":"38","Pennsylvania":"39","Puerto Rico":"40","Rhode Island":"41","South Carolina":"42","South Dakota":"43","Tennessee":"44","Texas":"45","Utah":"46","Vermont":"47","Virginia":"48","Washington":"49","West Virginia":"50","Wisconsin":"51","Wyoming":"52"})
