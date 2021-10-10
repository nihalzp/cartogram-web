import settings
import handlers.base_handler
import csv

class CartogramHandler(handlers.base_handler.BaseCartogramHandler):

    def get_name(self):
        return "Vietnam"

    def get_gen_file(self):
        return "{}/vietnam_processedmap.json".format(settings.CARTOGRAM_DATA_DIR)
    
    def validate_values(self, values):

        if len(values) != 63:
            return False
        
        for v in values:
            if type(v) != float:
                return False

        return True
    
    def gen_area_data(self, values):
        return """cartogram_id,Region Data,Region Name,Inset
1,{},An Giang,
2,{},Ba Ria - Vung Tau,
3,{},Bac Giang,
4,{},Bac Kan,
5,{},Bac Lieu,
6,{},Bac Ninh,
7,{},Ben Tre,
8,{},Binh Dinh,
9,{},Binh Duong,
10,{},Binh Phuoc,
11,{},Binh Thuan,
12,{},Ca Mau,
13,{},Can Tho,
14,{},Cao Bang,
15,{},Da Nang,
16,{},Dak Lak,
17,{},Dak Nong,
18,{},Dien Bien,
19,{},Dong Nai,
20,{},Dong Thap,
21,{},Gia Lai,
22,{},Ha Giang,
23,{},Ha Nam,
24,{},Ha Noi,
25,{},Ha Tinh,
26,{},Hai Duong,
27,{},Hai Phong,
28,{},Hau Giang,
29,{},Ho Chi Minh,
30,{},Hoa Binh,
31,{},Hung Yen,
32,{},Khanh Hoa,
33,{},Kien Giang,
34,{},Kon Tum,
35,{},Lai Chau,
36,{},Lam Dong,
37,{},Lang Son,
38,{},Lao Cai,
39,{},Long An,
40,{},Nam Dinh,
41,{},Nghe An,
42,{},Ninh Binh,
43,{},Ninh Thuan,
44,{},Phu Tho,
45,{},Phu Yen,
46,{},Quang Binh,
47,{},Quang Nam,
48,{},Quang Ngai,
49,{},Quang Ninh,
50,{},Quang Tri,
51,{},Soc Trang,
52,{},Son La,
53,{},Tay Ninh,
54,{},Thai Binh,
55,{},Thai Nguyen,
56,{},Thanh Hoa,
57,{},Thua Thien Hue,
58,{},Tien Giang,
59,{},Tra Vinh,
60,{},Tuyen Quang,
61,{},Vinh Long,
62,{},Vinh Phuc,
63,{},Yen Bai,""".format(*values)
    
    def expect_geojson_output(self):
        return True

    def csv_to_area_string_and_colors(self, csvfile):

        return self.order_by_example(csv.reader(csvfile), "Province/Municipality", 0, 1, 2, 3, ["An Giang","Ba Ria - Vung Tau","Bac Giang","Bac Kan","Bac Lieu","Bac Ninh","Ben Tre","Binh Dinh","Binh Duong","Binh Phuoc","Binh Thuan","Ca Mau","Can Tho","Cao Bang","Da Nang","Dak Lak","Dak Nong","Dien Bien","Dong Nai","Dong Thap","Gia Lai","Ha Giang","Ha Nam","Ha Noi","Ha Tinh","Hai Duong","Hai Phong","Hau Giang","Ho Chi Minh","Hoa Binh","Hung Yen","Khanh Hoa","Kien Giang","Kon Tum","Lai Chau","Lam Dong","Lang Son","Lao Cai","Long An","Nam Dinh","Nghe An","Ninh Binh","Ninh Thuan","Phu Tho","Phu Yen","Quang Binh","Quang Nam","Quang Ngai","Quang Ninh","Quang Tri","Soc Trang","Son La","Tay Ninh","Thai Binh","Thai Nguyen","Thanh Hoa","Thua Thien Hue","Tien Giang","Tra Vinh","Tuyen Quang","Vinh Long","Vinh Phuc","Yen Bai"], [0.0 for i in range(0,63)], {"An Giang":"1","Ba Ria - Vung Tau":"2","Bac Giang":"3","Bac Kan":"4","Bac Lieu":"5","Bac Ninh":"6","Ben Tre":"7","Binh Dinh":"8","Binh Duong":"9","Binh Phuoc":"10","Binh Thuan":"11","Ca Mau":"12","Can Tho":"13","Cao Bang":"14","Da Nang":"15","Dak Lak":"16","Dak Nong":"17","Dien Bien":"18","Dong Nai":"19","Dong Thap":"20","Gia Lai":"21","Ha Giang":"22","Ha Nam":"23","Ha Noi":"24","Ha Tinh":"25","Hai Duong":"26","Hai Phong":"27","Hau Giang":"28","Ho Chi Minh":"29","Hoa Binh":"30","Hung Yen":"31","Khanh Hoa":"32","Kien Giang":"33","Kon Tum":"34","Lai Chau":"35","Lam Dong":"36","Lang Son":"37","Lao Cai":"38","Long An":"39","Nam Dinh":"40","Nghe An":"41","Ninh Binh":"42","Ninh Thuan":"43","Phu Tho":"44","Phu Yen":"45","Quang Binh":"46","Quang Nam":"47","Quang Ngai":"48","Quang Ninh":"49","Quang Tri":"50","Soc Trang":"51","Son La":"52","Tay Ninh":"53","Thai Binh":"54","Thai Nguyen":"55","Thanh Hoa":"56","Thua Thien Hue":"57","Tien Giang":"58","Tra Vinh":"59","Tuyen Quang":"60","Vinh Long":"61","Vinh Phuc":"62","Yen Bai":"63"})
