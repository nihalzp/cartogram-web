from constants import *

def createhandler(map_name, csv_data, user_friendly_name, region_identifier):
    handler_py_template = '''import settings
import handlers.base_handler
import csv
import types

class CartogramHandler(handlers.base_handler.BaseCartogramHandler):

    def get_name(self):
        return "{0}"

    def get_gen_file(self):
        return "{{}}/{1}".format(settings.CARTOGRAM_DATA_DIR)
    
    def validate_values(self, values):

        if len(values) != {2}:
            return False
        
        for v in values:
            if type(v) != float:
                return False

        return True
    
    def gen_area_data(self, values):
        return """cartogram_id,Region Data,Region Name,Inset
{3}""".format(*values)
    
    def expect_geojson_output(self):
        return True

    def csv_to_area_string_and_colors(self, csvfile):
        if(isinstance(csvfile, types.GeneratorType)):
            csvfile = csv.reader(csvfile)
        return self.order_by_example(csv.reader(csvfile), "{4}", 0, 1, 2, 3, [{5}], [0.0 for i in range(0,{2})], {{{6}}})
'''
    
    area_data_template = "\n".join(list(map(lambda region: "{},{{}},{},{}".format(region["id"], region["name"], region["inset"]), csv_data)))
    region_names = ",".join(list(map(lambda region: '"{}"'.format(region["name"]), csv_data)))
    region_name_id_dict = ",".join(list(map(lambda region: '"{}":"{}"'.format(region["name"], region["id"]), csv_data)))

    handler_py = handler_py_template.format(user_friendly_name, "addmap_data/{0}/{0}_processed.json".format(map_name), len(csv_data), area_data_template, region_identifier, region_names, region_name_id_dict)

    with open(INTERNAL_DIR + "/handlers/{}.py".format(map_name), "w") as handler_file:

        handler_file.write(handler_py)
    
    return