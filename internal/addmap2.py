import sys
import os
import json
import csv
from constants import *
import importlib
import settings
from svg2color import svg2color
from svg2labels import svg2labels
from svg2config import svg2config
from json2svg import json2svg
from updatewebpy import updatewebpy
from createhandler import createhandler
from generatecartogram import serverless_generate, self_generate
import settings
import json
import geojson_extrema
from mappackify import mappackify


 
def welcome():

    print(f"""
                            Welcome to the Add Map Wizard!
                            
         1. Add cartogram_id and generate csv
         2. Produce SVG for coloring and labeling
         3. Add your map to the local website
         4. Delete a map
         5. See your map information
         
Input your choice (i.e. 1, 2, ...) ['exit' to quit and '?' for more info]
""")
     
def main():
    choice = input("Choice: ")
    
    if choice == '1':
        print("\nTo add cartogram id and generate csv, please run ./addmap2_local.sh \n")
        sys.exit()
    elif choice == '2':
        produce_svg()
    elif choice == '3':
        add_map_files()
    elif choice == '5':
        show_map_info_database()
    elif choice == 'exit':
        sys.exit(1)
    else:
        print("\nUnknown choice option given. Please input either 1, 2, 3, 4, 5, 'exit', or '?'\n")
        main()
        
def produce_svg():
    print()
    print("Enter the name of the map below. This name should be exactly the same name you entered to generate the csv in Choice 1.")
    print()
    map_name = input("Enter map name: ")
    print()
    if os.path.exists(ADDMAP_DATA_DIR +"/{}".format(map_name)) == False:
        print("Error: It looks like the map with the name '{}' doesn't exist inside data/addmap_data.".format(map_name))
        print("Please add your map using Choice 1 first.\n")
        sys.exit(1)
        
    with open(MAP_INFO_DIR, 'r') as file_object:
        map_info_file = json.load(file_object)

        if (map_name in map_info_file) == False:
            print("You map information doesn't exist in our map database. Please add your map again using Choice 1.\n")
            sys.exit(1)
            
        
    print("I will now create {0}.svg inside data/addmap_data/{0}. You should edit this file to specify the default color and add labels for each region.".format(map_name))
    print("DO NOT RESIZE OR RESCALE THE CONTENTS OF THIS FILE! Accurate label placement depends on the scale calculated by this wizard.")
    print()
    
    map_gen_file = "{}/{}/{}_processed.json".format(ADDMAP_DATA_DIR, map_name, map_name)
    
    map_csv_file = "{}/{}/{}.csv".format(ADDMAP_DATA_DIR, map_name, map_name)
    
    print("Writing {}.svg...\n".format(map_name))
    scale = json2svg(map_gen_file, "{}/{}/{}.svg".format(ADDMAP_DATA_DIR, map_name, map_name), map_csv_file)
    
    print("Done writing {}.svg\n".format(map_name))
    
    #Add scale in our map_info_database
    with open(MAP_INFO_DIR, 'r') as file_object:
        map_info_file = json.load(file_object)
        map_info_file[map_name]["svg_geojson_scale"] = scale
        
    with open(MAP_INFO_DIR, 'w') as json_object:
        json.dump(map_info_file, json_object, indent=4, separators=(", ", ": "))
    
    print("A {0}.svg file has been generated inside data/addmap_data/{0}. Please modify the svg to change color and add labels to your map.".format(map_name))

def add_map_files():
    print()
    print("Enter the name of the map below. This name should be exactly the same name you entered to generate the csv in Choice 1.")
    print()
    map_name = input("Enter map name: ")
    print()
    if os.path.exists(ADDMAP_DATA_DIR +"/{}".format(map_name)) == False:
        print("Error: It looks like the map with the name '{}' doesn't exist inside data/addmap_data.".format(map_name))
        print("Please add your map using Choice 1 first.\n")
        sys.exit(1)
        
    with open(MAP_INFO_DIR, 'r') as file_object:
        map_info_file = json.load(file_object)

        if (map_name in map_info_file) == False:
            print("You map information doesn't exist in our map database. Please add your map again using Choice 1.\n")
            sys.exit(1)
    print()
    
    print("I will parse the csv")
    
    regions = []
    
    with open("{}/{}/{}.csv".format(ADDMAP_DATA_DIR, map_name, map_name ), newline='') as dat_file:

        reader = csv.DictReader(dat_file)
# Region Id,Landarea Data,Population Data,Cart Data,Region Name,Abbreviation,Inset,Color
        for row in reader:

            regions.append({
                "id": row["Region Id"],
                "landarea": row["Landarea Data"],
                "population": row["Population Data"],
                "cartdata": row["Cart Data"],
                "name": row["Region Name"],
                "abbreviation": row["Abbreviation"],
                "inset": row["Inset"],
                "color": row["Color"]
            })
    print(regions)
    
    print("I will create necessary files to add your map to the local website.\n")
    
    print("Creating directory internal/static/cartdata/{}...".format(map_name))
    # if directory doesn't exist, create it
    if not os.path.exists("static/cartdata/{}".format(map_name)):
        os.mkdir("static/cartdata/{}".format(map_name))
    print("Done.\n")
    print("Creating colors.json...")
    
    with open("{}/{}/colors.json".format(CARTDATA_DIR,map_name), "w") as colors_json_file:
        
        colors_json_file.write("{\n")
        colors_json_file.write(",\n".join(list(map(lambda region: '"id_{}":"{}"'.format(region["id"], region["color"]), regions))))
        colors_json_file.write("\n}")

    print("Done.\n")
    print("I will now parse {}.svg to learn each map region's default color.".format(map_name))
    print()

    print("Updating color information from SVG...")
    new_colors, colors_by_name = svg2color(ADDMAP_DATA_DIR + "/{0}/{0}.svg".format(map_name), CARTDATA_DIR + "/{0}/colors.json".format(map_name))
    print(new_colors)
    print(regions)
    # Update color information from new_colors to regions
    for id in new_colors:
        cart_id = int(id.replace("id_", ""))    
        regions[cart_id - 1]["color"] = new_colors[id]
        
        
        
    print(repr(colors_by_name))
    print("Done.\n")
    
    print("Creating labels.json...")
    
    with open("{}/{}/labels.json".format(CARTDATA_DIR,map_name), "w") as labels_json_file:
        
        labels_json_file.write('{{"scale_x": {0}, "scale_y": {0}, "labels": [], "lines": []}}'.format(map_info_file[map_name]["svg_geojson_scale"]))
    
    print("Done.\n")
    
    print("Updating label information from SVG...")
    svg2labels(ADDMAP_DATA_DIR + "/{0}/{0}.svg".format(map_name), CARTDATA_DIR + "/{0}/labels.json".format(map_name), map_info_file[map_name]["svg_geojson_scale"], map_info_file[map_name]["svg_geojson_scale"])
    
    print("Done.\n")
    
    print("Creating config.json...")
    
    with open("{}/{}/config.json".format(CARTDATA_DIR,map_name), "w") as config_json_file:
        
        config_json_file.write("""{
    "dont_draw": [],
    "elevate": []
}""")
    print("Done.\n")
    
    print("Updating config information from SVG...")
    svg2config(ADDMAP_DATA_DIR + "/{0}/{0}.svg".format(map_name), CARTDATA_DIR + "/{0}/config.json".format(map_name))
    print("Done.\n")
    
    print("Creating abbreviations.json...")
    with open("{}/{}/abbreviations.json".format(CARTDATA_DIR,map_name), "w") as abbreviations_json_file:

        abbreviations_json_file.write("{\n")
        abbreviations_json_file.write(",\n".join(list(map(lambda region: '"{}":"{}"'.format(region["name"], region["abbreviation"]), regions))))
        abbreviations_json_file.write("\n}")
        
    print("Done.\n")
    
    print("Creating template.csv...")
    
    with open("{}/{}/template.csv".format(CARTDATA_DIR,map_name), "w") as template_csv_file:
        
        template_csv_file.write('"{}","Population","{}","Colour"\n'.format(map_info_file[map_name]["region_identifier"], map_info_file[map_name]["dataset_name"]))
        template_csv_file.write("\n".join(list(map(lambda region: '"{}","{}","{}","{}"'.format(region["name"], region["population"], region["cartdata"], region["color"]), regions))))
    
    print("Done.\n")
    
    
    print("Creating handlers/{}.py...".format(map_name))
    
    createhandler(map_name, regions, map_info_file[map_name]["user_friendly_name"], map_info_file[map_name]["region_identifier"])
    
    print("Done.\n")
    
    print("Updating web.py...")
    
    updatewebpy(map_name)
    
    print("Done.\n")
    
    
    landarea_csv = [[map_info_file[map_name]["region_identifier"], "", "Land Area", "Color"]]
    population_csv = [[map_info_file[map_name]["region_identifier"], "", "Population", "Color"]]
    cart_csv = [[map_info_file[map_name]["region_identifier"], "Population",map_info_file[map_name]["dataset_name"] , "Color"]]
    
    for region in regions:
        landarea_csv.append([region["name"], "" ,region["landarea"],region["color"]])
        population_csv.append([region["name"], "" ,region["population"],region["color"]])
        cart_csv.append([region["name"], region["population"] ,region["cartdata"],region["color"]])    
    
    map_module = importlib.import_module('handlers.{}'.format(map_name))

    map_handler = map_module.CartogramHandler()
    
    landarea_cartogramui = map_handler.csv_to_area_string_and_colors(landarea_csv)
    population_cartogramui = map_handler.csv_to_area_string_and_colors(population_csv)
    cartogramui = map_handler.csv_to_area_string_and_colors(cart_csv)
    
    landarea_cartogramui[2]["unit"] = 'km sq.'
    population_cartogramui[2]["unit"] = "people"
    
    print("Generating population map...")
    
    area_data = population_cartogramui[0].split(";")
    population_json = serverless_generate(area_data, map_handler) if settings.CARTOGRAM_LOCAL_DOCKERIZED else self_generate(area_data, map_handler)
    
    print("Done.\n")
    
    if "bbox" not in population_json:
        print("Adding bbox to population map...")
        population_json["bbox"] = geojson_extrema.get_extrema_from_geojson(population_json)
        print("Done.\n")
    
    print("Creating population.json...")
    
    with open("static/cartdata/{}/population.json".format(map_name), "w") as original_json_file:
        population_json["tooltip"] = population_cartogramui[2]
        json.dump(population_json, original_json_file)
    
    print("Done.\n")
    
    print("Creating original.json...")
    with open(map_handler.get_gen_file(), "r") as map_gen_file:
        original_json = json.load(map_gen_file)
        original_tooltip = landarea_cartogramui[2]
        original_json['tooltip'] = original_tooltip
        
    with open("static/cartdata/{}/original.json".format(map_name), "w") as original_json_file:
        json.dump(original_json, original_json_file)
            
    print("Done.\n")
    
    print("Creating griddocument.json...")
    with open("static/cartdata/{}/griddocument.json".format(map_name), "w") as griddocument_json_file:
        json.dump(cartogramui[3], griddocument_json_file)
    
    print("Done.\n")
    
    print("Generating map pack in static/cartdata/{}/mappack.json...".format(map_name))
        
    mappackify(map_name)
    
    print("Done.\n")
    
    return
    
def show_map_info_database():
    with open(MAP_INFO_DIR, 'r') as file_object:
        map_info_file = json.load(file_object)
    
    print("\nWe have following map info in our Add Map Database: \n")
    for map_info in map_info_file:
        print("*",map_info,)
    map_name = input("\nEnter your map name: ")
    print()
    print("map_name : " + map_name)
    if map_name in map_info_file.keys():
        for info in map_info_file[map_name]:
            print(info, ":", map_info_file[map_name][info])
    else:
        print("Unknown map name. Please provide map name from the following list. If not here, please add your map first using Choice 1")
        for map_info in map_info_file:
            print("*",map_info,)
    return

welcome()

main()