import settings
import handlers.base_handler
import csv

class CartogramHandler(handlers.base_handler.BaseCartogramHandler):

    def get_name(self):
        return "Philippines"

    def get_gen_file(self):
        return "{}/phl_processedmap.json".format(settings.CARTOGRAM_DATA_DIR)
    
    def validate_values(self, values):

        if len(values) != 82:
            return False
        
        for v in values:
            if type(v) != float:
                return False

        return True
    
    def gen_area_data(self, values):
        return """1 {} Abra
2 {} Agusan del Norte
3 {} Agusan del Sur
4 {} Aklan
5 {} Albay
6 {} Antique
7 {} Apayao
8 {} Aurora
9 {} Basilan
10 {} Bataan
11 {} Batanes
12 {} Batangas
13 {} Benguet
14 {} Biliran
15 {} Bohol
16 {} Bukidnon
17 {} Bulacan
18 {} Cagayan
19 {} Camarines Norte
20 {} Camarines Sur
21 {} Camiguin
22 {} Capiz
23 {} Catanduanes
24 {} Cavite
25 {} Cebu
26 {} Compostela Valley
27 {} Davao del Norte
28 {} Davao del Sur
29 {} Davao Occidental
30 {} Davao Oriental
31 {} Dinagat Islands
32 {} Eastern Samar
33 {} Guimaras
34 {} Ifugao
35 {} Ilocos Norte
36 {} Ilocos Sur
37 {} Iloilo
38 {} Isabela
39 {} Kalinga
40 {} La Union
41 {} Laguna
42 {} Lanao del Norte
43 {} Lanao del Sur
44 {} Leyte
45 {} Maguindanao
46 {} Marinduque
47 {} Masbate
48 {} Metropolitan Manila
49 {} Misamis Occidental
50 {} Misamis Oriental
51 {} Mountain Province
52 {} Negros Occidental
53 {} Negros Oriental
54 {} North Cotabato
55 {} Northern Samar
56 {} Nueva Ecija
57 {} Nueva Vizcaya
58 {} Occidental Mindoro
59 {} Oriental Mindoro
60 {} Palawan
61 {} Pampanga
62 {} Pangasinan
63 {} Quezon
64 {} Quirino
65 {} Rizal
66 {} Romblon
67 {} Samar
68 {} Sarangani
69 {} Siquijor
70 {} Sorsogon
71 {} South Cotabato
72 {} Southern Leyte
73 {} Sultan Kudarat
74 {} Sulu
75 {} Surigao del Norte
76 {} Surigao del Sur
77 {} Tarlac
78 {} Tawi-Tawi
79 {} Zambales
80 {} Zamboanga del Norte
81 {} Zamboanga del Sur
82 {} Zamboanga Sibugay""".format(*values)
    
    def expect_geojson_output(self):
        return True

    def csv_to_area_string_and_colors(self, csvfile):

        return self.order_by_example(csv.reader(csvfile), "Province/Region", 0, 1, 2, 3, ["Abra","Agusan del Norte","Agusan del Sur","Aklan","Albay","Antique","Apayao","Aurora","Basilan","Bataan","Batanes","Batangas","Benguet","Biliran","Bohol","Bukidnon","Bulacan","Cagayan","Camarines Norte","Camarines Sur","Camiguin","Capiz","Catanduanes","Cavite","Cebu","Compostela Valley","Davao del Norte","Davao del Sur","Davao Occidental","Davao Oriental","Dinagat Islands","Eastern Samar","Guimaras","Ifugao","Ilocos Norte","Ilocos Sur","Iloilo","Isabela","Kalinga","La Union","Laguna","Lanao del Norte","Lanao del Sur","Leyte","Maguindanao","Marinduque","Masbate","Metropolitan Manila","Misamis Occidental","Misamis Oriental","Mountain Province","Negros Occidental","Negros Oriental","North Cotabato","Northern Samar","Nueva Ecija","Nueva Vizcaya","Occidental Mindoro","Oriental Mindoro","Palawan","Pampanga","Pangasinan","Quezon","Quirino","Rizal","Romblon","Samar","Sarangani","Siquijor","Sorsogon","South Cotabato","Southern Leyte","Sultan Kudarat","Sulu","Surigao del Norte","Surigao del Sur","Tarlac","Tawi-Tawi","Zambales","Zamboanga del Norte","Zamboanga del Sur","Zamboanga Sibugay"], [0.0 for i in range(0,82)], {"Abra":"1","Agusan del Norte":"2","Agusan del Sur":"3","Aklan":"4","Albay":"5","Antique":"6","Apayao":"7","Aurora":"8","Basilan":"9","Bataan":"10","Batanes":"11","Batangas":"12","Benguet":"13","Biliran":"14","Bohol":"15","Bukidnon":"16","Bulacan":"17","Cagayan":"18","Camarines Norte":"19","Camarines Sur":"20","Camiguin":"21","Capiz":"22","Catanduanes":"23","Cavite":"24","Cebu":"25","Compostela Valley":"26","Davao del Norte":"27","Davao del Sur":"28","Davao Occidental":"29","Davao Oriental":"30","Dinagat Islands":"31","Eastern Samar":"32","Guimaras":"33","Ifugao":"34","Ilocos Norte":"35","Ilocos Sur":"36","Iloilo":"37","Isabela":"38","Kalinga":"39","La Union":"40","Laguna":"41","Lanao del Norte":"42","Lanao del Sur":"43","Leyte":"44","Maguindanao":"45","Marinduque":"46","Masbate":"47","Metropolitan Manila":"48","Misamis Occidental":"49","Misamis Oriental":"50","Mountain Province":"51","Negros Occidental":"52","Negros Oriental":"53","North Cotabato":"54","Northern Samar":"55","Nueva Ecija":"56","Nueva Vizcaya":"57","Occidental Mindoro":"58","Oriental Mindoro":"59","Palawan":"60","Pampanga":"61","Pangasinan":"62","Quezon":"63","Quirino":"64","Rizal":"65","Romblon":"66","Samar":"67","Sarangani":"68","Siquijor":"69","Sorsogon":"70","South Cotabato":"71","Southern Leyte":"72","Sultan Kudarat":"73","Sulu":"74","Surigao del Norte":"75","Surigao del Sur":"76","Tarlac":"77","Tawi-Tawi":"78","Zambales":"79","Zamboanga del Norte":"80","Zamboanga del Sur":"81","Zamboanga Sibugay":"82"})
