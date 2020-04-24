import settings
import handlers.base_handler
import csv

class CartogramHandler(handlers.base_handler.BaseCartogramHandler):

    def get_name(self):
        return "Thailand"

    def get_gen_file(self):
        return "{}/thailand_processedmap.json".format(settings.CARTOGRAM_DATA_DIR)
    
    def validate_values(self, values):

        if len(values) != 77:
            return False
        
        for v in values:
            if type(v) != float:
                return False

        return True
    
    def gen_area_data(self, values):
        return """1 {} Amnat Charoen
2 {} Ang Thong
3 {} Bangkok Metropolis
4 {} Bueng Kan
5 {} Buri Ram
6 {} Chachoengsao
7 {} Chai Nat
8 {} Chaiyaphum
9 {} Chanthaburi
10 {} Chiang Mai
11 {} Chiang Rai
12 {} Chon Buri
13 {} Chumphon
14 {} Kalasin
15 {} Kamphaeng Phet
16 {} Kanchanaburi
17 {} Khon Kaen
18 {} Krabi
19 {} Lampang
20 {} Lamphun
21 {} Loei
22 {} Lop Buri
23 {} Mae Hong Son
24 {} Maha Sarakham
25 {} Mukdahan
26 {} Nakhon Nayok
27 {} Nakhon Pathom
28 {} Nakhon Phanom
29 {} Nakhon Ratchasima
30 {} Nakhon Sawan
31 {} Nakhon Si Thammarat
32 {} Nan
33 {} Narathiwat
34 {} Nong Bua Lam Phu
35 {} Nong Khai
36 {} Nonthaburi
37 {} Pathum Thani
38 {} Pattani
39 {} Phangnga
40 {} Phatthalung
41 {} Phayao
42 {} Phetchabun
43 {} Phetchaburi
44 {} Phichit
45 {} Phitsanulok
46 {} Phra Nakhon Si Ayutthaya
47 {} Phrae
48 {} Phuket
49 {} Prachin Buri
50 {} Prachuap Khiri Khan
51 {} Ranong
52 {} Ratchaburi
53 {} Rayong
54 {} Roi Et
55 {} Sa Kaeo
56 {} Sakon Nakhon
57 {} Samut Prakan
58 {} Samut Sakhon
59 {} Samut Songkhram
60 {} Saraburi
61 {} Satun
62 {} Si Sa Ket
63 {} Sing Buri
64 {} Songkhla
65 {} Sukhothai
66 {} Suphan Buri
67 {} Surat Thani
68 {} Surin
69 {} Tak
70 {} Trang
71 {} Trat
72 {} Ubon Ratchathani
73 {} Udon Thani
74 {} Uthai Thani
75 {} Uttaradit
76 {} Yala
77 {} Yasothon""".format(*values)
    
    def expect_geojson_output(self):
        return True

    def csv_to_area_string_and_colors(self, csvfile):

        return self.order_by_example(csv.reader(csvfile), "Province", 0, 1, 2, 3, ["Amnat Charoen","Ang Thong","Bangkok Metropolis","Bueng Kan","Buri Ram","Chachoengsao","Chai Nat","Chaiyaphum","Chanthaburi","Chiang Mai","Chiang Rai","Chon Buri","Chumphon","Kalasin","Kamphaeng Phet","Kanchanaburi","Khon Kaen","Krabi","Lampang","Lamphun","Loei","Lop Buri","Mae Hong Son","Maha Sarakham","Mukdahan","Nakhon Nayok","Nakhon Pathom","Nakhon Phanom","Nakhon Ratchasima","Nakhon Sawan","Nakhon Si Thammarat","Nan","Narathiwat","Nong Bua Lam Phu","Nong Khai","Nonthaburi","Pathum Thani","Pattani","Phangnga","Phatthalung","Phayao","Phetchabun","Phetchaburi","Phichit","Phitsanulok","Phra Nakhon Si Ayutthaya","Phrae","Phuket","Prachin Buri","Prachuap Khiri Khan","Ranong","Ratchaburi","Rayong","Roi Et","Sa Kaeo","Sakon Nakhon","Samut Prakan","Samut Sakhon","Samut Songkhram","Saraburi","Satun","Si Sa Ket","Sing Buri","Songkhla","Sukhothai","Suphan Buri","Surat Thani","Surin","Tak","Trang","Trat","Ubon Ratchathani","Udon Thani","Uthai Thani","Uttaradit","Yala","Yasothon"], [0.0 for i in range(0,77)], {"Amnat Charoen":"1","Ang Thong":"2","Bangkok Metropolis":"3","Bueng Kan":"4","Buri Ram":"5","Chachoengsao":"6","Chai Nat":"7","Chaiyaphum":"8","Chanthaburi":"9","Chiang Mai":"10","Chiang Rai":"11","Chon Buri":"12","Chumphon":"13","Kalasin":"14","Kamphaeng Phet":"15","Kanchanaburi":"16","Khon Kaen":"17","Krabi":"18","Lampang":"19","Lamphun":"20","Loei":"21","Lop Buri":"22","Mae Hong Son":"23","Maha Sarakham":"24","Mukdahan":"25","Nakhon Nayok":"26","Nakhon Pathom":"27","Nakhon Phanom":"28","Nakhon Ratchasima":"29","Nakhon Sawan":"30","Nakhon Si Thammarat":"31","Nan":"32","Narathiwat":"33","Nong Bua Lam Phu":"34","Nong Khai":"35","Nonthaburi":"36","Pathum Thani":"37","Pattani":"38","Phangnga":"39","Phatthalung":"40","Phayao":"41","Phetchabun":"42","Phetchaburi":"43","Phichit":"44","Phitsanulok":"45","Phra Nakhon Si Ayutthaya":"46","Phrae":"47","Phuket":"48","Prachin Buri":"49","Prachuap Khiri Khan":"50","Ranong":"51","Ratchaburi":"52","Rayong":"53","Roi Et":"54","Sa Kaeo":"55","Sakon Nakhon":"56","Samut Prakan":"57","Samut Sakhon":"58","Samut Songkhram":"59","Saraburi":"60","Satun":"61","Si Sa Ket":"62","Sing Buri":"63","Songkhla":"64","Sukhothai":"65","Suphan Buri":"66","Surat Thani":"67","Surin":"68","Tak":"69","Trang":"70","Trat":"71","Ubon Ratchathani":"72","Udon Thani":"73","Uthai Thani":"74","Uttaradit":"75","Yala":"76","Yasothon":"77"})
