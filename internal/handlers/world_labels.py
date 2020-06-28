import settings
import handlers.base_handler
import csv

class CartogramHandler(handlers.base_handler.BaseCartogramHandler):

    def get_name(self):
        return "World (labels)"

    def get_gen_file(self):
        return "{}/world_ci_processedmap.json".format(settings.CARTOGRAM_DATA_DIR)
    
    def validate_values(self, values):

        if len(values) != 242:
            return False
        
        for v in values:
            if type(v) != float:
                return False

        return True
    
    def gen_area_data(self, values):
        return """1 {} Afghanistan
2 {} Aland
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
14 {} Australia
15 {} Austria
16 {} Azerbaijan
17 {} Bahamas
18 {} Bahrain
19 {} Bangladesh
20 {} Barbados
21 {} Belarus
22 {} Belgium
23 {} Belize
24 {} Benin
25 {} Bermuda
26 {} Bhutan
27 {} Bolivia
28 {} Bosnia and Herz.
29 {} Botswana
30 {} Br. Indian Ocean Ter.
31 {} Brazil
32 {} British Virgin Is.
33 {} Brunei
34 {} Bulgaria
35 {} Burkina Faso
36 {} Burundi
37 {} Cabo Verde
38 {} Cambodia
39 {} Cameroon
40 {} Canada
41 {} Cayman Is.
42 {} Central African Rep.
43 {} Chad
44 {} Chile
45 {} China
46 {} Colombia
47 {} Comoros
48 {} Congo
49 {} Cook Is.
50 {} Costa Rica
51 {} Cote d'Ivoire
52 {} Croatia
53 {} Cuba
54 {} Curacao
55 {} Cyprus
56 {} Czechia
57 {} Dem. Rep. Congo
58 {} Denmark
59 {} Djibouti
60 {} Dominica
61 {} Dominican Rep.
62 {} Ecuador
63 {} Egypt
64 {} El Salvador
65 {} Eq. Guinea
66 {} Eritrea
67 {} Estonia
68 {} eSwatini
69 {} Ethiopia
70 {} Faeroe Is.
71 {} Falkland Is.
72 {} Fiji
73 {} Finland
74 {} Fr. Polynesia
75 {} Fr. S. Antarctic Lands
76 {} France
77 {} Gabon
78 {} Gambia
79 {} Georgia
80 {} Germany
81 {} Ghana
82 {} Gibraltar
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
99 {} Indonesia
100 {} Iran
101 {} Iraq
102 {} Ireland
103 {} Isle of Man
104 {} Israel
105 {} Italy
106 {} Jamaica
107 {} Japan
108 {} Jersey
109 {} Jordan
110 {} Kazakhstan
111 {} Kenya
112 {} Kiribati
113 {} Kosovo
114 {} Kuwait
115 {} Kyrgyzstan
116 {} Laos
117 {} Latvia
118 {} Lebanon
119 {} Lesotho
120 {} Liberia
121 {} Libya
122 {} Liechtenstein
123 {} Lithuania
124 {} Luxembourg
125 {} Macao
126 {} Macedonia
127 {} Madagascar
128 {} Malawi
129 {} Malaysia
130 {} Maldives
131 {} Mali
132 {} Malta
133 {} Marshall Is.
134 {} Mauritania
135 {} Mauritius
136 {} Mexico
137 {} Micronesia
138 {} Moldova
139 {} Monaco
140 {} Mongolia
141 {} Montenegro
142 {} Montserrat
143 {} Morocco
144 {} Mozambique
145 {} Myanmar
146 {} N. Cyprus
147 {} N. Mariana Is.
148 {} Namibia
149 {} Nauru
150 {} Nepal
151 {} Netherlands
152 {} New Caledonia
153 {} New Zealand
154 {} Nicaragua
155 {} Niger
156 {} Nigeria
157 {} Niue
158 {} Norfolk Island
159 {} North Korea
160 {} Norway
161 {} Oman
162 {} Pakistan
163 {} Palau
164 {} Palestine
165 {} Panama
166 {} Papua New Guinea
167 {} Paraguay
168 {} Peru
169 {} Philippines
170 {} Pitcairn Is.
171 {} Poland
172 {} Portugal
173 {} Puerto Rico
174 {} Qatar
175 {} Romania
176 {} Russia
177 {} Rwanda
178 {} S. Geo. and the Is.
179 {} S. Sudan
180 {} Saint Helena
181 {} Saint Lucia
182 {} Samoa
183 {} San Marino
184 {} Sao Tome and Principe
185 {} Saudi Arabia
186 {} Senegal
187 {} Serbia
188 {} Seychelles
189 {} Siachen Glacier
190 {} Sierra Leone
191 {} Singapore
192 {} Sint Maarten
193 {} Slovakia
194 {} Slovenia
195 {} Solomon Is.
196 {} Somalia
197 {} Somaliland
198 {} South Africa
199 {} South Korea
200 {} Spain
201 {} Sri Lanka
202 {} St-Barthelemy
203 {} St-Martin
204 {} St. Kitts and Nevis
205 {} St. Pierre and Miquelon
206 {} St. Vin. and Gren.
207 {} Sudan
208 {} Suriname
209 {} Sweden
210 {} Switzerland
211 {} Syria
212 {} Taiwan
213 {} Tajikistan
214 {} Tanzania
215 {} Thailand
216 {} Timor-Leste
217 {} Togo
218 {} Tonga
219 {} Trinidad and Tobago
220 {} Tunisia
221 {} Turkey
222 {} Turkmenistan
223 {} Turks and Caicos Is.
224 {} Tuvalu
225 {} U.S. Minor Outlying Is.
226 {} U.S. Virgin Is.
227 {} Uganda
228 {} Ukraine
229 {} United Arab Emirates
230 {} United Kingdom
231 {} United States of America
232 {} Uruguay
233 {} Uzbekistan
234 {} Vanuatu
235 {} Vatican
236 {} Venezuela
237 {} Vietnam
238 {} W. Sahara
239 {} Wallis and Futuna Is.
240 {} Yemen
241 {} Zambia
242 {} Zimbabwe""".format(*values)
    
    def expect_geojson_output(self):
        return True

    def csv_to_area_string_and_colors(self, csvfile):

        return self.order_by_example(csv.reader(csvfile), "Country", 0, 1, 2, 3, ["Afghanistan","Aland","Albania","Algeria","American Samoa","Andorra","Angola","Anguilla","Antarctica","Antigua and Barb.","Argentina","Armenia","Aruba","Australia","Austria","Azerbaijan","Bahamas","Bahrain","Bangladesh","Barbados","Belarus","Belgium","Belize","Benin","Bermuda","Bhutan","Bolivia","Bosnia and Herz.","Botswana","Br. Indian Ocean Ter.","Brazil","British Virgin Is.","Brunei","Bulgaria","Burkina Faso","Burundi","Cabo Verde","Cambodia","Cameroon","Canada","Cayman Is.","Central African Rep.","Chad","Chile","China","Colombia","Comoros","Congo","Cook Is.","Costa Rica","Cote d'Ivoire","Croatia","Cuba","Curacao","Cyprus","Czechia","Dem. Rep. Congo","Denmark","Djibouti","Dominica","Dominican Rep.","Ecuador","Egypt","El Salvador","Eq. Guinea","Eritrea","Estonia","eSwatini","Ethiopia","Faeroe Is.","Falkland Is.","Fiji","Finland","Fr. Polynesia","Fr. S. Antarctic Lands","France","Gabon","Gambia","Georgia","Germany","Ghana","Gibraltar","Greece","Greenland","Grenada","Guam","Guatemala","Guernsey","Guinea","Guinea-Bissau","Guyana","Haiti","Heard I. and McDonald Is.","Honduras","Hong Kong","Hungary","Iceland","India","Indonesia","Iran","Iraq","Ireland","Isle of Man","Israel","Italy","Jamaica","Japan","Jersey","Jordan","Kazakhstan","Kenya","Kiribati","Kosovo","Kuwait","Kyrgyzstan","Laos","Latvia","Lebanon","Lesotho","Liberia","Libya","Liechtenstein","Lithuania","Luxembourg","Macao","Macedonia","Madagascar","Malawi","Malaysia","Maldives","Mali","Malta","Marshall Is.","Mauritania","Mauritius","Mexico","Micronesia","Moldova","Monaco","Mongolia","Montenegro","Montserrat","Morocco","Mozambique","Myanmar","N. Cyprus","N. Mariana Is.","Namibia","Nauru","Nepal","Netherlands","New Caledonia","New Zealand","Nicaragua","Niger","Nigeria","Niue","Norfolk Island","North Korea","Norway","Oman","Pakistan","Palau","Palestine","Panama","Papua New Guinea","Paraguay","Peru","Philippines","Pitcairn Is.","Poland","Portugal","Puerto Rico","Qatar","Romania","Russia","Rwanda","S. Geo. and the Is.","S. Sudan","Saint Helena","Saint Lucia","Samoa","San Marino","Sao Tome and Principe","Saudi Arabia","Senegal","Serbia","Seychelles","Siachen Glacier","Sierra Leone","Singapore","Sint Maarten","Slovakia","Slovenia","Solomon Is.","Somalia","Somaliland","South Africa","South Korea","Spain","Sri Lanka","St-Barthelemy","St-Martin","St. Kitts and Nevis","St. Pierre and Miquelon","St. Vin. and Gren.","Sudan","Suriname","Sweden","Switzerland","Syria","Taiwan","Tajikistan","Tanzania","Thailand","Timor-Leste","Togo","Tonga","Trinidad and Tobago","Tunisia","Turkey","Turkmenistan","Turks and Caicos Is.","Tuvalu","U.S. Minor Outlying Is.","U.S. Virgin Is.","Uganda","Ukraine","United Arab Emirates","United Kingdom","United States of America","Uruguay","Uzbekistan","Vanuatu","Vatican","Venezuela","Vietnam","W. Sahara","Wallis and Futuna Is.","Yemen","Zambia","Zimbabwe"], [0.0 for i in range(0,242)], {"Afghanistan":"1","Aland":"2","Albania":"3","Algeria":"4","American Samoa":"5","Andorra":"6","Angola":"7","Anguilla":"8","Antarctica":"9","Antigua and Barb.":"10","Argentina":"11","Armenia":"12","Aruba":"13","Australia":"14","Austria":"15","Azerbaijan":"16","Bahamas":"17","Bahrain":"18","Bangladesh":"19","Barbados":"20","Belarus":"21","Belgium":"22","Belize":"23","Benin":"24","Bermuda":"25","Bhutan":"26","Bolivia":"27","Bosnia and Herz.":"28","Botswana":"29","Br. Indian Ocean Ter.":"30","Brazil":"31","British Virgin Is.":"32","Brunei":"33","Bulgaria":"34","Burkina Faso":"35","Burundi":"36","Cabo Verde":"37","Cambodia":"38","Cameroon":"39","Canada":"40","Cayman Is.":"41","Central African Rep.":"42","Chad":"43","Chile":"44","China":"45","Colombia":"46","Comoros":"47","Congo":"48","Cook Is.":"49","Costa Rica":"50","Cote d'Ivoire":"51","Croatia":"52","Cuba":"53","Curacao":"54","Cyprus":"55","Czechia":"56","Dem. Rep. Congo":"57","Denmark":"58","Djibouti":"59","Dominica":"60","Dominican Rep.":"61","Ecuador":"62","Egypt":"63","El Salvador":"64","Eq. Guinea":"65","Eritrea":"66","Estonia":"67","eSwatini":"68","Ethiopia":"69","Faeroe Is.":"70","Falkland Is.":"71","Fiji":"72","Finland":"73","Fr. Polynesia":"74","Fr. S. Antarctic Lands":"75","France":"76","Gabon":"77","Gambia":"78","Georgia":"79","Germany":"80","Ghana":"81","Gibraltar":"82","Greece":"83","Greenland":"84","Grenada":"85","Guam":"86","Guatemala":"87","Guernsey":"88","Guinea":"89","Guinea-Bissau":"90","Guyana":"91","Haiti":"92","Heard I. and McDonald Is.":"93","Honduras":"94","Hong Kong":"95","Hungary":"96","Iceland":"97","India":"98","Indonesia":"99","Iran":"100","Iraq":"101","Ireland":"102","Isle of Man":"103","Israel":"104","Italy":"105","Jamaica":"106","Japan":"107","Jersey":"108","Jordan":"109","Kazakhstan":"110","Kenya":"111","Kiribati":"112","Kosovo":"113","Kuwait":"114","Kyrgyzstan":"115","Laos":"116","Latvia":"117","Lebanon":"118","Lesotho":"119","Liberia":"120","Libya":"121","Liechtenstein":"122","Lithuania":"123","Luxembourg":"124","Macao":"125","Macedonia":"126","Madagascar":"127","Malawi":"128","Malaysia":"129","Maldives":"130","Mali":"131","Malta":"132","Marshall Is.":"133","Mauritania":"134","Mauritius":"135","Mexico":"136","Micronesia":"137","Moldova":"138","Monaco":"139","Mongolia":"140","Montenegro":"141","Montserrat":"142","Morocco":"143","Mozambique":"144","Myanmar":"145","N. Cyprus":"146","N. Mariana Is.":"147","Namibia":"148","Nauru":"149","Nepal":"150","Netherlands":"151","New Caledonia":"152","New Zealand":"153","Nicaragua":"154","Niger":"155","Nigeria":"156","Niue":"157","Norfolk Island":"158","North Korea":"159","Norway":"160","Oman":"161","Pakistan":"162","Palau":"163","Palestine":"164","Panama":"165","Papua New Guinea":"166","Paraguay":"167","Peru":"168","Philippines":"169","Pitcairn Is.":"170","Poland":"171","Portugal":"172","Puerto Rico":"173","Qatar":"174","Romania":"175","Russia":"176","Rwanda":"177","S. Geo. and the Is.":"178","S. Sudan":"179","Saint Helena":"180","Saint Lucia":"181","Samoa":"182","San Marino":"183","Sao Tome and Principe":"184","Saudi Arabia":"185","Senegal":"186","Serbia":"187","Seychelles":"188","Siachen Glacier":"189","Sierra Leone":"190","Singapore":"191","Sint Maarten":"192","Slovakia":"193","Slovenia":"194","Solomon Is.":"195","Somalia":"196","Somaliland":"197","South Africa":"198","South Korea":"199","Spain":"200","Sri Lanka":"201","St-Barthelemy":"202","St-Martin":"203","St. Kitts and Nevis":"204","St. Pierre and Miquelon":"205","St. Vin. and Gren.":"206","Sudan":"207","Suriname":"208","Sweden":"209","Switzerland":"210","Syria":"211","Taiwan":"212","Tajikistan":"213","Tanzania":"214","Thailand":"215","Timor-Leste":"216","Togo":"217","Tonga":"218","Trinidad and Tobago":"219","Tunisia":"220","Turkey":"221","Turkmenistan":"222","Turks and Caicos Is.":"223","Tuvalu":"224","U.S. Minor Outlying Is.":"225","U.S. Virgin Is.":"226","Uganda":"227","Ukraine":"228","United Arab Emirates":"229","United Kingdom":"230","United States of America":"231","Uruguay":"232","Uzbekistan":"233","Vanuatu":"234","Vatican":"235","Venezuela":"236","Vietnam":"237","W. Sahara":"238","Wallis and Futuna Is.":"239","Yemen":"240","Zambia":"241","Zimbabwe":"242"})
