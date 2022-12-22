import csv
import json
import geopandas as gpd
from mapclassify import greedy

def convert_id_to_hex(id):
    if id == 0:
        return '#1b9e77'
    elif id == 1:
        return '#d95f02'
    elif id == 2:
        return '#7570b3'
    elif id == 3:
        return '#e7298a'
    elif id == 4:
        return '#66a61e'
    elif id == 5:
        return '#e6ab02'
    elif id == 6:
        return '#a6761d'

def json2csv(json_file, out_file, name_key, abr_key):
    try:
        gjson_df = gpd.read_file(open(json_file))
    except Exception as e:
        raise e

    gjson_df['color_id'] = greedy(gjson_df, min_colors=6)

    gjson_df = gjson_df[[name_key,'color_id']]
    
    color_dict = dict(zip(gjson_df[name_key], gjson_df['color_id']))
    
    try:
        with open(json_file) as map_gen_file:
            geo_json = json.load(map_gen_file)
            csv_data = []
            for i in geo_json["features"]:
                csv_data.append({'Region Id': int(i["properties"]["cartogram_id"]),
                                    'Landarea Data': '',
                                    'Population Data': '',
                                    'Cart Data': '',
                                    'Region Name': i["properties"][name_key],
                                    'Abbreviation': i["properties"][abr_key],
                                    'Inset': '',
                                    'Color': convert_id_to_hex(color_dict[i["properties"][name_key]])})

            
            csv_data_sorted = sorted(csv_data, key=lambda d: d['Region Id']) 

            with open(out_file, 'w', newline='') as csvfile:
                columnnames = ['Region Id','Landarea Data','Population Data','Cart Data','Region Name','Abbreviation','Inset','Color']
                writer = csv.DictWriter(csvfile, fieldnames=columnnames)
                writer.writeheader()
                writer.writerows(csv_data_sorted)
            
    except Exception as e:
        raise e
    