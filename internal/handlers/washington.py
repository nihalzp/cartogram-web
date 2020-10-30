import settings
import handlers.base_handler
import csv

class CartogramHandler(handlers.base_handler.BaseCartogramHandler):

    def get_name(self):
        return "Washington (U.S. State)"

    def get_gen_file(self):
        return "{}/washington_processedmap.json".format(settings.CARTOGRAM_DATA_DIR)
    
    def validate_values(self, values):

        if len(values) != 39:
            return False
        
        for v in values:
            if type(v) != float:
                return False

        return True
    
    def gen_area_data(self, values):
        return """1 {} Adams
2 {} Asotin
3 {} Benton
4 {} Chelan
5 {} Clallam
6 {} Clark
7 {} Columbia
8 {} Cowlitz
9 {} Douglas
10 {} Ferry
11 {} Franklin
12 {} Garfield
13 {} Grant
14 {} Grays Harbor
15 {} Island
16 {} Jefferson
17 {} King
18 {} Kitsap
19 {} Kittitas
20 {} Klickitat
21 {} Lewis
22 {} Lincoln
23 {} Mason
24 {} Okanogan
25 {} Pacific
26 {} Pend Oreille
27 {} Pierce
28 {} San Juan
29 {} Skagit
30 {} Skamania
31 {} Snohomish
32 {} Spokane
33 {} Stevens
34 {} Thurston
35 {} Wahkiakum
36 {} Walla Walla
37 {} Whatcom
38 {} Whitman
39 {} Yakima""".format(*values)
    
    def expect_geojson_output(self):
        return True

    def csv_to_area_string_and_colors(self, csvfile):

        return self.order_by_example(csv.reader(csvfile), "County", 0, 1, 2, 3, ["Adams","Asotin","Benton","Chelan","Clallam","Clark","Columbia","Cowlitz","Douglas","Ferry","Franklin","Garfield","Grant","Grays Harbor","Island","Jefferson","King","Kitsap","Kittitas","Klickitat","Lewis","Lincoln","Mason","Okanogan","Pacific","Pend Oreille","Pierce","San Juan","Skagit","Skamania","Snohomish","Spokane","Stevens","Thurston","Wahkiakum","Walla Walla","Whatcom","Whitman","Yakima"], [0.0 for i in range(0,39)], {"Adams":"1","Asotin":"2","Benton":"3","Chelan":"4","Clallam":"5","Clark":"6","Columbia":"7","Cowlitz":"8","Douglas":"9","Ferry":"10","Franklin":"11","Garfield":"12","Grant":"13","Grays Harbor":"14","Island":"15","Jefferson":"16","King":"17","Kitsap":"18","Kittitas":"19","Klickitat":"20","Lewis":"21","Lincoln":"22","Mason":"23","Okanogan":"24","Pacific":"25","Pend Oreille":"26","Pierce":"27","San Juan":"28","Skagit":"29","Skamania":"30","Snohomish":"31","Spokane":"32","Stevens":"33","Thurston":"34","Wahkiakum":"35","Walla Walla":"36","Whatcom":"37","Whitman":"38","Yakima":"39"})
