import settings
import handlers.base_handler
import csv

class CartogramHandler(handlers.base_handler.BaseCartogramHandler):

    def get_name(self):
        return "Mexico"

    def get_gen_file(self):
        return "{}/mex_processedmap.json".format(settings.CARTOGRAM_DATA_DIR)
    
    def validate_values(self, values):

        if len(values) != 32:
            return False
        
        for v in values:
            if type(v) != float:
                return False

        return True
    
    def gen_area_data(self, values):
        return """1 {} Aguascalientes
2 {} Baja California
3 {} Baja California Sur
4 {} Campeche
5 {} Chiapas
6 {} Chihuahua
7 {} Coahuila
8 {} Colima
9 {} Mexico City
10 {} Durango
11 {} Guanajuato
12 {} Guerrero
13 {} Hidalgo
14 {} Jalisco
15 {} Mexico State
16 {} Michoacan
17 {} Morelos
18 {} Nayarit
19 {} Nuevo Leon
20 {} Oaxaca
21 {} Puebla
22 {} Queretaro
23 {} Quintana Roo
24 {} San Luis Potosi
25 {} Sinaloa
26 {} Sonora
27 {} Tabasco
28 {} Tamaulipas
29 {} Tlaxcala
30 {} Veracruz
31 {} Yucatan
32 {} Zacatecas""".format(*values)
    
    def expect_geojson_output(self):
        return True

    def csv_to_area_string_and_colors(self, csvfile):

        return self.order_by_example(csv.reader(csvfile), "State", 0, 1, 2, 3, ["Aguascalientes","Baja California","Baja California Sur","Campeche","Chiapas","Chihuahua","Coahuila","Colima","Mexico City","Durango","Guanajuato","Guerrero","Hidalgo","Jalisco","Mexico State","Michoacan","Morelos","Nayarit","Nuevo Leon","Oaxaca","Puebla","Queretaro","Quintana Roo","San Luis Potosi","Sinaloa","Sonora","Tabasco","Tamaulipas","Tlaxcala","Veracruz","Yucatan","Zacatecas"], [0.0 for i in range(0,32)], {"Aguascalientes":"1","Baja California":"2","Baja California Sur":"3","Campeche":"4","Chiapas":"5","Chihuahua":"6","Coahuila":"7","Colima":"8","Mexico City":"9","Durango":"10","Guanajuato":"11","Guerrero":"12","Hidalgo":"13","Jalisco":"14","Mexico State":"15","Michoacan":"16","Morelos":"17","Nayarit":"18","Nuevo Leon":"19","Oaxaca":"20","Puebla":"21","Queretaro":"22","Quintana Roo":"23","San Luis Potosi":"24","Sinaloa":"25","Sonora":"26","Tabasco":"27","Tamaulipas":"28","Tlaxcala":"29","Veracruz":"30","Yucatan":"31","Zacatecas":"32"})
