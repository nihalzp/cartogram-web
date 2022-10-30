import settings
import handlers.base_handler
import csv

class CartogramHandler(handlers.base_handler.BaseCartogramHandler):

    def get_name(self):
        return "Turkey"

    def get_gen_file(self):
        return "{}/tur_processedmap.json".format(settings.CARTOGRAM_DATA_DIR)
    
    def validate_values(self, values):

        if len(values) != 81:
            return False
        
        for v in values:
            if type(v) != float:
                return False

        return True
    
    def gen_area_data(self, values):
        return """cartogram_id,Region Data,Region Name,Inset
1,{},Adana,
2,{},Adiyaman,
3,{},Afyon,
4,{},Agri,
5,{},Aksaray,
6,{},Amasya,
7,{},Ankara,
8,{},Antalya,
9,{},Ardahan,
10,{},Artvin,
11,{},Aydin,
12,{},Balikesir,
13,{},Bartin,
14,{},Batman,
15,{},Bayburt,
16,{},Bilecik,
17,{},Bingol,
18,{},Bitlis,
19,{},Bolu,
20,{},Burdur,
21,{},Bursa,
22,{},Canakkale,
23,{},Cankiri,
24,{},Corum,
25,{},Denizli,
26,{},Diyarbakir,
27,{},Duzce,
28,{},Edirne,
29,{},Elazig,
30,{},Erzincan,
31,{},Erzurum,
32,{},Eskisehir,
33,{},Gaziantep,
34,{},Giresun,
35,{},Gumushane,
36,{},Hakkari,
37,{},Hatay,
38,{},Igdir,
39,{},Isparta,
40,{},Istanbul,
41,{},Izmir,
42,{},Kahramanmaras,
43,{},Karabuk,
44,{},Karaman,
45,{},Kars,
46,{},Kastamonu,
47,{},Kayseri,
48,{},Kilis,
49,{},Kinkkale,
50,{},Kirklareli,
51,{},Kirsehir,
52,{},Kocaeli,
53,{},Konya,
54,{},Kutahya,
55,{},Malatya,
56,{},Manisa,
57,{},Mardin,
58,{},Mersin,
59,{},Mugla,
60,{},Mus,
61,{},Nevsehir,
62,{},Nigde,
63,{},Ordu,
64,{},Osmaniye,
65,{},Rize,
66,{},Sakarya,
67,{},Samsun,
68,{},Sanliurfa,
69,{},Siirt,
70,{},Sinop,
71,{},Sirnak,
72,{},Sivas,
73,{},Tekirdag,
74,{},Tokat,
75,{},Trabzon,
76,{},Tunceli,
77,{},Usak,
78,{},Van,
79,{},Yalova,
80,{},Yozgat,
81,{},Zonguldak,""".format(*values)
    
    def expect_geojson_output(self):
        return True

    def csv_to_area_string_and_colors(self, csvfile):

        return self.order_by_example(csv.reader(csvfile), "Province", 0, 1, 2, 3, ["Adana","Adiyaman","Afyon","Agri","Aksaray","Amasya","Ankara","Antalya","Ardahan","Artvin","Aydin","Balikesir","Bartin","Batman","Bayburt","Bilecik","Bingol","Bitlis","Bolu","Burdur","Bursa","Canakkale","Cankiri","Corum","Denizli","Diyarbakir","Duzce","Edirne","Elazig","Erzincan","Erzurum","Eskisehir","Gaziantep","Giresun","Gumushane","Hakkari","Hatay","Igdir","Isparta","Istanbul","Izmir","Kahramanmaras","Karabuk","Karaman","Kars","Kastamonu","Kayseri","Kilis","Kinkkale","Kirklareli","Kirsehir","Kocaeli","Konya","Kutahya","Malatya","Manisa","Mardin","Mersin","Mugla","Mus","Nevsehir","Nigde","Ordu","Osmaniye","Rize","Sakarya","Samsun","Sanliurfa","Siirt","Sinop","Sirnak","Sivas","Tekirdag","Tokat","Trabzon","Tunceli","Usak","Van","Yalova","Yozgat","Zonguldak"], [0.0 for i in range(0,81)], {"Adana":"1","Adiyaman":"2","Afyon":"3","Agri":"4","Aksaray":"5","Amasya":"6","Ankara":"7","Antalya":"8","Ardahan":"9","Artvin":"10","Aydin":"11","Balikesir":"12","Bartin":"13","Batman":"14","Bayburt":"15","Bilecik":"16","Bingol":"17","Bitlis":"18","Bolu":"19","Burdur":"20","Bursa":"21","Canakkale":"22","Cankiri":"23","Corum":"24","Denizli":"25","Diyarbakir":"26","Duzce":"27","Edirne":"28","Elazig":"29","Erzincan":"30","Erzurum":"31","Eskisehir":"32","Gaziantep":"33","Giresun":"34","Gumushane":"35","Hakkari":"36","Hatay":"37","Igdir":"38","Isparta":"39","Istanbul":"40","Izmir":"41","Kahramanmaras":"42","Karabuk":"43","Karaman":"44","Kars":"45","Kastamonu":"46","Kayseri":"47","Kilis":"48","Kinkkale":"49","Kirklareli":"50","Kirsehir":"51","Kocaeli":"52","Konya":"53","Kutahya":"54","Malatya":"55","Manisa":"56","Mardin":"57","Mersin":"58","Mugla":"59","Mus":"60","Nevsehir":"61","Nigde":"62","Ordu":"63","Osmaniye":"64","Rize":"65","Sakarya":"66","Samsun":"67","Sanliurfa":"68","Siirt":"69","Sinop":"70","Sirnak":"71","Sivas":"72","Tekirdag":"73","Tokat":"74","Trabzon":"75","Tunceli":"76","Usak":"77","Van":"78","Yalova":"79","Yozgat":"80","Zonguldak":"81"})
