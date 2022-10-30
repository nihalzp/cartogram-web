import settings
import handlers.base_handler
import csv

class CartogramHandler(handlers.base_handler.BaseCartogramHandler):

    def get_name(self):
        return "United States (Conterminous)"

    def get_gen_file(self):
        return "{}/usa_processedmap.json".format(settings.CARTOGRAM_DATA_DIR)

    def validate_values(self, values):

        if len(values) != 49:
            return False

        for v in values:
            if type(v) != float:
                return False

        return True

    def gen_area_data(self, values):
        return """cartogram_id,Region Data,Region Name,Inset
1,{},Alabama,
2,{},Arizona,
3,{},Arkansas,
4,{},California,
5,{},Colorado,
6,{},Connecticut,
7,{},Delaware,
8,{},District of Columbia,
9,{},Florida,
10,{},Georgia,
11,{},Idaho,
12,{},Illinois,
13,{},Indiana,
14,{},Iowa,
15,{},Kansas,
16,{},Kentucky,
17,{},Louisiana,
18,{},Maine,
19,{},Maryland,
20,{},Massachusetts,
21,{},Michigan,
22,{},Minnesota,
23,{},Mississippi,
24,{},Missouri,
25,{},Montana,
26,{},Nebraska,
27,{},Nevada,
28,{},New Hampshire,
29,{},New Jersey,
30,{},New Mexico,
31,{},New York,
32,{},North Carolina,
33,{},North Dakota,
34,{},Ohio,
35,{},Oklahoma,
36,{},Oregon,
37,{},Pennsylvania,
38,{},Rhode Island,
39,{},South Carolina,
40,{},South Dakota,
41,{},Tennessee,
42,{},Texas,
43,{},Utah,
44,{},Vermont,
45,{},Virginia,
46,{},Washington,
47,{},West Virginia,
48,{},Wisconsin,
49,{},Wyoming,""".format(*values)

    def expect_geojson_output(self):
        return True

    def csv_to_area_string_and_colors(self, csvfile):

        return self.order_by_example(csv.reader(csvfile), "State", 0, 1, 2, 3, ["Alabama","Arizona","Arkansas","California","Colorado","Connecticut","Delaware","District of Columbia","Florida","Georgia","Idaho","Illinois","Indiana","Iowa","Kansas","Kentucky","Louisiana","Maine","Maryland","Massachusetts","Michigan","Minnesota","Mississippi","Missouri","Montana","Nebraska","Nevada","New Hampshire","New Jersey","New Mexico","New York","North Carolina","North Dakota","Ohio","Oklahoma","Oregon","Pennsylvania","Rhode Island","South Carolina","South Dakota","Tennessee","Texas","Utah","Vermont","Virginia","Washington","West Virginia","Wisconsin","Wyoming"], [0.0 for i in range(0,49)], {"Alabama":"1","Arizona":"2","Arkansas":"3","California":"4","Colorado":"5","Connecticut":"6","Delaware":"7","District of Columbia":"8","Florida":"9","Georgia":"10","Idaho":"11","Illinois":"12","Indiana":"13","Iowa":"14","Kansas":"15","Kentucky":"16","Louisiana":"17","Maine":"18","Maryland":"19","Massachusetts":"20","Michigan":"21","Minnesota":"22","Mississippi":"23","Missouri":"24","Montana":"25","Nebraska":"26","Nevada":"27","New Hampshire":"28","New Jersey":"29","New Mexico":"30","New York":"31","North Carolina":"32","North Dakota":"33","Ohio":"34","Oklahoma":"35","Oregon":"36","Pennsylvania":"37","Rhode Island":"38","South Carolina":"39","South Dakota":"40","Tennessee":"41","Texas":"42","Utah":"43","Vermont":"44","Virginia":"45","Washington":"46","West Virginia":"47","Wisconsin":"48","Wyoming":"49"})
