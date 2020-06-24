import settings
import handlers.base_handler
import csv

class CartogramHandler(handlers.base_handler.BaseCartogramHandler):

    def get_name(self):
        return "world_test"

    def get_gen_file(self):
        return "{}/world_small_countries_increased_processedmap_with_key.json".format(settings.CARTOGRAM_DATA_DIR)
    
    def validate_values(self, values):

        if len(values) != 241:
            return False
        
        for v in values:
            if type(v) != float:
                return False

        return True
    
    def gen_area_data(self, values):
        return """1 {} Aland
2 {} Afghanistan
3 {} Albania
4 {} Algeria
5 {} American Samoa
6 {} Andorra
7 {} Angola
8 {} Anguilla
9 {} Antarctica
10 {} Antigua and Barb.
11 {} Argentina
12 {} Armenia
13 {} Aruba
14 {} Ashmore and Cartier Is.
15 {} Australia
16 {} Austria
17 {} Azerbaijan
18 {} Bahamas
19 {} Bahrain
20 {} Bangladesh
21 {} Barbados
22 {} Belarus
23 {} Belgium
24 {} Belize
25 {} Benin
26 {} Bermuda
27 {} Bhutan
28 {} Bolivia
29 {} Bosnia and Herz.
30 {} Botswana
31 {} Br. Indian Ocean Ter.
32 {} Brazil
33 {} British Virgin Is.
34 {} Brunei
35 {} Bulgaria
36 {} Burkina Faso
37 {} Burundi
38 {} Cote dlvoire
39 {} Cabo Verde
40 {} Cambodia
41 {} Cameroon
42 {} Canada
43 {} Cayman Is.
44 {} Central African Rep.
45 {} Chad
46 {} Chile
47 {} China
48 {} Colombia
49 {} Comoros
50 {} Congo
51 {} Cook Is.
52 {} Costa Rica
53 {} Croatia
54 {} Cuba
55 {} Curacao
56 {} Cyprus
57 {} Czechia
58 {} Dem. Rep. Congo
59 {} Denmark
60 {} Djibouti
61 {} Dominica
62 {} Dominican Rep.
63 {} Ecuador
64 {} Egypt
65 {} El Salvador
66 {} Eq. Guinea
67 {} Eritrea
68 {} Estonia
69 {} eSwatini
70 {} Ethiopia
71 {} Faeroe Is.
72 {} Falkland Is.
73 {} Fiji
74 {} Finland
75 {} Fr. Polynesia
76 {} Fr. S. Antarctic Lands
77 {} France
78 {} Gabon
79 {} Gambia
80 {} Georgia
81 {} Germany
82 {} Ghana
83 {} Greece
84 {} Greenland
85 {} Grenada
86 {} Guam
87 {} Guatemala
88 {} Guernsey
89 {} Guinea
90 {} Guinea-Bissau
91 {} Guyana
92 {} Haiti
93 {} Heard I. and McDonald Is.
94 {} Honduras
95 {} Hong Kong
96 {} Hungary
97 {} Iceland
98 {} India
99 {} Indian Ocean Ter.
100 {} Indonesia
101 {} Iran
102 {} Iraq
103 {} Ireland
104 {} Isle of Man
105 {} Israel
106 {} Italy
107 {} Jamaica
108 {} Japan
109 {} Jersey
110 {} Jordan
111 {} Kazakhstan
112 {} Kenya
113 {} Kiribati
114 {} Kosovo
115 {} Kuwait
116 {} Kyrgyzstan
117 {} Laos
118 {} Latvia
119 {} Lebanon
120 {} Lesotho
121 {} Liberia
122 {} Libya
123 {} Liechtenstein
124 {} Lithuania
125 {} Luxembourg
126 {} Macao
127 {} Macedonia
128 {} Madagascar
129 {} Malawi
130 {} Malaysia
131 {} Maldives
132 {} Mali
133 {} Malta
134 {} Marshall Is.
135 {} Mauritania
136 {} Mauritius
137 {} Mexico
138 {} Micronesia
139 {} Moldova
140 {} Monaco
141 {} Mongolia
142 {} Montenegro
143 {} Montserrat
144 {} Morocco
145 {} Mozambique
146 {} Myanmar
147 {} N. Cyprus
148 {} N. Mariana Is.
149 {} Namibia
150 {} Nauru
151 {} Nepal
152 {} Netherlands
153 {} New Caledonia
154 {} New Zealand
155 {} Nicaragua
156 {} Niger
157 {} Nigeria
158 {} Niue
159 {} Norfolk Island
160 {} North Korea
161 {} Norway
162 {} Oman
163 {} Pakistan
164 {} Palau
165 {} Palestine
166 {} Panama
167 {} Papua New Guinea
168 {} Paraguay
169 {} Peru
170 {} Philippines
171 {} Pitcairn Is.
172 {} Poland
173 {} Portugal
174 {} Puerto Rico
175 {} Qatar
176 {} Romania
177 {} Russia
178 {} Rwanda
179 {} S. Geo. and the Is.
180 {} S. Sudan
181 {} Sao Tome and Principe
182 {} Saint Helena
183 {} Saint Lucia
184 {} Samoa
185 {} San Marino
186 {} Saudi Arabia
187 {} Senegal
188 {} Serbia
189 {} Seychelles
190 {} Siachen Glacier
191 {} Sierra Leone
192 {} Singapore
193 {} Sint Maarten
194 {} Slovakia
195 {} Slovenia
196 {} Solomon Is.
197 {} Somalia
198 {} Somaliland
199 {} South Africa
200 {} South Korea
201 {} Spain
202 {} Sri Lanka
203 {} St Barthelemy
204 {} St-Martin
205 {} St. Kitts and Nevis
206 {} St. Pierre and Miquelon
207 {} St. Vin. and Gren.
208 {} Sudan
209 {} Suriname
210 {} Sweden
211 {} Switzerland
212 {} Syria
213 {} Taiwan
214 {} Tajikistan
215 {} Tanzania
216 {} Thailand
217 {} Timor-Leste
218 {} Togo
219 {} Tonga
220 {} Trinidad and Tobago
221 {} Tunisia
222 {} Turkey
223 {} Turkmenistan
224 {} Turks and Caicos Is.
225 {} U.S. Virgin Is.
226 {} Uganda
227 {} Ukraine
228 {} United Arab Emirates
229 {} United Kingdom
230 {} United States of America
231 {} Uruguay
232 {} Uzbekistan
233 {} Vanuatu
234 {} Vatican
235 {} Venezuela
236 {} Vietnam
237 {} W. Sahara
238 {} Wallis and Futuna Is.
239 {} Yemen
240 {} Zambia
241 {} Zimbabwe""".format(*values)
    
    def expect_geojson_output(self):
        return True

    def csv_to_area_string_and_colors(self, csvfile):

        return self.order_by_example(csv.reader(csvfile), "Country", 0, 1, 2, 3, ["Aland","Afghanistan","Albania","Algeria","American Samoa","Andorra","Angola","Anguilla","Antarctica","Antigua and Barb.","Argentina","Armenia","Aruba","Ashmore and Cartier Is.","Australia","Austria","Azerbaijan","Bahamas","Bahrain","Bangladesh","Barbados","Belarus","Belgium","Belize","Benin","Bermuda","Bhutan","Bolivia","Bosnia and Herz.","Botswana","Br. Indian Ocean Ter.","Brazil","British Virgin Is.","Brunei","Bulgaria","Burkina Faso","Burundi","Cote dlvoire","Cabo Verde","Cambodia","Cameroon","Canada","Cayman Is.","Central African Rep.","Chad","Chile","China","Colombia","Comoros","Congo","Cook Is.","Costa Rica","Croatia","Cuba","Curacao","Cyprus","Czechia","Dem. Rep. Congo","Denmark","Djibouti","Dominica","Dominican Rep.","Ecuador","Egypt","El Salvador","Eq. Guinea","Eritrea","Estonia","eSwatini","Ethiopia","Faeroe Is.","Falkland Is.","Fiji","Finland","Fr. Polynesia","Fr. S. Antarctic Lands","France","Gabon","Gambia","Georgia","Germany","Ghana","Greece","Greenland","Grenada","Guam","Guatemala","Guernsey","Guinea","Guinea-Bissau","Guyana","Haiti","Heard I. and McDonald Is.","Honduras","Hong Kong","Hungary","Iceland","India","Indian Ocean Ter.","Indonesia","Iran","Iraq","Ireland","Isle of Man","Israel","Italy","Jamaica","Japan","Jersey","Jordan","Kazakhstan","Kenya","Kiribati","Kosovo","Kuwait","Kyrgyzstan","Laos","Latvia","Lebanon","Lesotho","Liberia","Libya","Liechtenstein","Lithuania","Luxembourg","Macao","Macedonia","Madagascar","Malawi","Malaysia","Maldives","Mali","Malta","Marshall Is.","Mauritania","Mauritius","Mexico","Micronesia","Moldova","Monaco","Mongolia","Montenegro","Montserrat","Morocco","Mozambique","Myanmar","N. Cyprus","N. Mariana Is.","Namibia","Nauru","Nepal","Netherlands","New Caledonia","New Zealand","Nicaragua","Niger","Nigeria","Niue","Norfolk Island","North Korea","Norway","Oman","Pakistan","Palau","Palestine","Panama","Papua New Guinea","Paraguay","Peru","Philippines","Pitcairn Is.","Poland","Portugal","Puerto Rico","Qatar","Romania","Russia","Rwanda","S. Geo. and the Is.","S. Sudan","Sao Tome and Principe","Saint Helena","Saint Lucia","Samoa","San Marino","Saudi Arabia","Senegal","Serbia","Seychelles","Siachen Glacier","Sierra Leone","Singapore","Sint Maarten","Slovakia","Slovenia","Solomon Is.","Somalia","Somaliland","South Africa","South Korea","Spain","Sri Lanka","St Barthelemy","St-Martin","St. Kitts and Nevis","St. Pierre and Miquelon","St. Vin. and Gren.","Sudan","Suriname","Sweden","Switzerland","Syria","Taiwan","Tajikistan","Tanzania","Thailand","Timor-Leste","Togo","Tonga","Trinidad and Tobago","Tunisia","Turkey","Turkmenistan","Turks and Caicos Is.","U.S. Virgin Is.","Uganda","Ukraine","United Arab Emirates","United Kingdom","United States of America","Uruguay","Uzbekistan","Vanuatu","Vatican","Venezuela","Vietnam","W. Sahara","Wallis and Futuna Is.","Yemen","Zambia","Zimbabwe"], [0.0 for i in range(0,241)], {"Aland":"1","Afghanistan":"2","Albania":"3","Algeria":"4","American Samoa":"5","Andorra":"6","Angola":"7","Anguilla":"8","Antarctica":"9","Antigua and Barb.":"10","Argentina":"11","Armenia":"12","Aruba":"13","Ashmore and Cartier Is.":"14","Australia":"15","Austria":"16","Azerbaijan":"17","Bahamas":"18","Bahrain":"19","Bangladesh":"20","Barbados":"21","Belarus":"22","Belgium":"23","Belize":"24","Benin":"25","Bermuda":"26","Bhutan":"27","Bolivia":"28","Bosnia and Herz.":"29","Botswana":"30","Br. Indian Ocean Ter.":"31","Brazil":"32","British Virgin Is.":"33","Brunei":"34","Bulgaria":"35","Burkina Faso":"36","Burundi":"37","Cote dlvoire":"38","Cabo Verde":"39","Cambodia":"40","Cameroon":"41","Canada":"42","Cayman Is.":"43","Central African Rep.":"44","Chad":"45","Chile":"46","China":"47","Colombia":"48","Comoros":"49","Congo":"50","Cook Is.":"51","Costa Rica":"52","Croatia":"53","Cuba":"54","Curacao":"55","Cyprus":"56","Czechia":"57","Dem. Rep. Congo":"58","Denmark":"59","Djibouti":"60","Dominica":"61","Dominican Rep.":"62","Ecuador":"63","Egypt":"64","El Salvador":"65","Eq. Guinea":"66","Eritrea":"67","Estonia":"68","eSwatini":"69","Ethiopia":"70","Faeroe Is.":"71","Falkland Is.":"72","Fiji":"73","Finland":"74","Fr. Polynesia":"75","Fr. S. Antarctic Lands":"76","France":"77","Gabon":"78","Gambia":"79","Georgia":"80","Germany":"81","Ghana":"82","Greece":"83","Greenland":"84","Grenada":"85","Guam":"86","Guatemala":"87","Guernsey":"88","Guinea":"89","Guinea-Bissau":"90","Guyana":"91","Haiti":"92","Heard I. and McDonald Is.":"93","Honduras":"94","Hong Kong":"95","Hungary":"96","Iceland":"97","India":"98","Indian Ocean Ter.":"99","Indonesia":"100","Iran":"101","Iraq":"102","Ireland":"103","Isle of Man":"104","Israel":"105","Italy":"106","Jamaica":"107","Japan":"108","Jersey":"109","Jordan":"110","Kazakhstan":"111","Kenya":"112","Kiribati":"113","Kosovo":"114","Kuwait":"115","Kyrgyzstan":"116","Laos":"117","Latvia":"118","Lebanon":"119","Lesotho":"120","Liberia":"121","Libya":"122","Liechtenstein":"123","Lithuania":"124","Luxembourg":"125","Macao":"126","Macedonia":"127","Madagascar":"128","Malawi":"129","Malaysia":"130","Maldives":"131","Mali":"132","Malta":"133","Marshall Is.":"134","Mauritania":"135","Mauritius":"136","Mexico":"137","Micronesia":"138","Moldova":"139","Monaco":"140","Mongolia":"141","Montenegro":"142","Montserrat":"143","Morocco":"144","Mozambique":"145","Myanmar":"146","N. Cyprus":"147","N. Mariana Is.":"148","Namibia":"149","Nauru":"150","Nepal":"151","Netherlands":"152","New Caledonia":"153","New Zealand":"154","Nicaragua":"155","Niger":"156","Nigeria":"157","Niue":"158","Norfolk Island":"159","North Korea":"160","Norway":"161","Oman":"162","Pakistan":"163","Palau":"164","Palestine":"165","Panama":"166","Papua New Guinea":"167","Paraguay":"168","Peru":"169","Philippines":"170","Pitcairn Is.":"171","Poland":"172","Portugal":"173","Puerto Rico":"174","Qatar":"175","Romania":"176","Russia":"177","Rwanda":"178","S. Geo. and the Is.":"179","S. Sudan":"180","Sao Tome and Principe":"181","Saint Helena":"182","Saint Lucia":"183","Samoa":"184","San Marino":"185","Saudi Arabia":"186","Senegal":"187","Serbia":"188","Seychelles":"189","Siachen Glacier":"190","Sierra Leone":"191","Singapore":"192","Sint Maarten":"193","Slovakia":"194","Slovenia":"195","Solomon Is.":"196","Somalia":"197","Somaliland":"198","South Africa":"199","South Korea":"200","Spain":"201","Sri Lanka":"202","St Barthelemy":"203","St-Martin":"204","St. Kitts and Nevis":"205","St. Pierre and Miquelon":"206","St. Vin. and Gren.":"207","Sudan":"208","Suriname":"209","Sweden":"210","Switzerland":"211","Syria":"212","Taiwan":"213","Tajikistan":"214","Tanzania":"215","Thailand":"216","Timor-Leste":"217","Togo":"218","Tonga":"219","Trinidad and Tobago":"220","Tunisia":"221","Turkey":"222","Turkmenistan":"223","Turks and Caicos Is.":"224","U.S. Virgin Is.":"225","Uganda":"226","Ukraine":"227","United Arab Emirates":"228","United Kingdom":"229","United States of America":"230","Uruguay":"231","Uzbekistan":"232","Vanuatu":"233","Vatican":"234","Venezuela":"235","Vietnam":"236","W. Sahara":"237","Wallis and Futuna Is.":"238","Yemen":"239","Zambia":"240","Zimbabwe":"241"})
