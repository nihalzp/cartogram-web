import sys
import os
import json
import csv
import re
from constants import *
import importlib
import settings
import shutil
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
    elif choice == '4':
        delete_map()
    elif choice == '5':
        show_map_info_database()
    elif choice == 'exit':
        sys.exit(1)
    else:
        print("\nUnknown choice option given. Please input either 1, 2, 3, 4, 5, 'exit', or '?'\n")
        main()
    return
        
def produce_svg():
    print()
    print("Enter the name of the map (not the user friendly name) below. This name should be exactly the same name you entered to generate the csv in Choice 1.")
    print()
    map_name = input("Enter map name: ")
    print()
    if not os.path.exists(ADDMAP_DATA_DIR +"/{}".format(map_name)):
        print("Error: It looks like the map with the name '{}' doesn't exist inside data/addmap_data.".format(map_name))
        print("Please add your map using Choice 1 first.\n")
        sys.exit(1)
    
    try:
        with open(MAP_INFO_DIR, 'r') as file_object:
            map_info_file = json.load(file_object)

            if map_name not in map_info_file:
                print("You map information does not exist in our map database. Please add your map again using Choice 1.\n")
                sys.exit(1)
    except Exception as e:
        print("Problem opening the local map database map_data.json.")
        print(repr(e))
        sys.exit(1)
            
        
    print("I will now create {0}.svg inside data/addmap_data/{0}. You should edit this file to specify the default color and add labels for each region.".format(map_name))
    print("DO NOT RESIZE OR RESCALE THE CONTENTS OF THIS FILE! Accurate label placement depends on the scale calculated by this wizard.")
    print()
    
    map_gen_file = "{}/{}/{}_processed.json".format(ADDMAP_DATA_DIR, map_name, map_name)
    
    map_csv_file = "{}/{}/{}.csv".format(ADDMAP_DATA_DIR, map_name, map_name)
    
    print("Writing {}.svg...\n".format(map_name))
    
    try:
        scale = json2svg(map_gen_file, "{}/{}/{}.svg".format(ADDMAP_DATA_DIR, map_name, map_name), map_csv_file)
    except Exception as e:
        print("Problem writing the svg file.")
        print(repr(e))
        sys.exit(1)
    
    print("Done writing {}.svg\n".format(map_name))
    
    #Add scale in our map_info_database
    try:
        with open(MAP_INFO_DIR, 'r') as file_object:
            map_info_file = json.load(file_object)
            map_info_file[map_name]["svg_geojson_scale"] = scale
    except Exception as e:
        print("Problem opening the local map database map_data.json.")
        print(repr(e))
        sys.exit(1)
    
    try:
        with open(MAP_INFO_DIR, 'w') as json_object:
            json.dump(map_info_file, json_object, indent=4, separators=(", ", ": "))
    except Exception as e:
        print("Problem writing to the local map database map_data.json.")
        print(repr(e))
        sys.exit(1)
    
    print("A {0}.svg file has been generated inside data/addmap_data/{0}. Please modify the svg to change color and add labels to your map.".format(map_name))

def add_map_files():
    print(("""\nREMINDER: If you want to use custom color for regions and add labels, please edit the svg file in
           data/addmap_data/mapname/mapname.svg first with custom coloring and labels/arrows before this step.\n"""))
    print("\nEnter the name of the map (not the user friendly name) below. This name should be exactly the same name you entered to generate the csv in Choice 1.")
    map_name = input("\nEnter map name: ")
    if not os.path.exists(ADDMAP_DATA_DIR +"/{}".format(map_name)):
        print("\nError: It looks like the map with the name '{}' doesn't exist inside data/addmap_data.".format(map_name))
        print("Please add your map using Choice 1 first.\n")
        sys.exit(1)
        
    with open(MAP_INFO_DIR, 'r') as file_object:
        map_info_file = json.load(file_object)

        if map_name not in map_info_file:
            print("\nYou map information doesn't exist in our map database. Please add your map again using Choice 1.\n")
            sys.exit(1)
    
    print("\nI will parse the csv now...\n")
    
    regions = []
    
    csv_filename = "{}/{}/{}.csv".format(ADDMAP_DATA_DIR, map_name, map_name)
    try:
        with open(csv_filename, newline='') as dat_file:

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
    except Exception as e:
        print("Problem reading the csv file: {}.".format(csv_filename))
        print(repr(e))
        sys.exit(1)
        
    print(regions)
        
    print("\nI will create necessary files to add your map to the local website.\n")
    
    print("Creating directory internal/static/cartdata/{}...".format(map_name))
    # if directory doesn't exist, create it
    if not os.path.exists("static/cartdata/{}".format(map_name)):
        os.mkdir("static/cartdata/{}".format(map_name))
        print("Done.\n")
    else:
        print("Directory already exists. Skipping.\n")
        
    print("Creating internal/static/cardata/{}/colors.json...".format(map_name))
    
    try:    
        with open("{}/{}/colors.json".format(CARTDATA_DIR,map_name), "w") as colors_json_file:
            colors_json_file.write("{\n")
            colors_json_file.write(",\n".join(list(map(lambda region: '"id_{}":"{}"'.format(region["id"], region["color"]), regions))))
            colors_json_file.write("\n}")
    except Exception as e:
        print("Problem writing to the colors.json file: {}/{}/colors.json.".format(CARTDATA_DIR,map_name))
        print(repr(e))
        sys.exit(1)
    
    print("\nDone.")
    
    print("\nI will now parse {}.svg to learn each map region's default color.".format(map_name))

    print("\nUpdating color information from SVG...\n")
    try:
        # the colors.json file is updated inside the svg2color function
        new_colors, colors_by_name = svg2color(ADDMAP_DATA_DIR + "/{0}/{0}.svg".format(map_name), CARTDATA_DIR + "/{0}/colors.json".format(map_name))
        print(new_colors)
        print(regions)
    except Exception as e:
        print("Problem parsing the svg file: {}/{}/{}.svg.".format(ADDMAP_DATA_DIR, map_name, map_name))
        print(repr(e))
        sys.exit(1)
        
    # Update color information from new_colors to regions
    for id in new_colors:
        cart_id = int(id.replace("id_", ""))    
        regions[cart_id - 1]["color"] = new_colors[id]
        
    print(repr(colors_by_name))
    print("\nDone.\n")
        
    print("Creating labels.json file: {}/{}/labels.json...".format(CARTDATA_DIR,map_name))
    
    try:
        with open("{}/{}/labels.json".format(CARTDATA_DIR,map_name), "w") as labels_json_file:
            labels_json_file.write('{{"scale_x": {0}, "scale_y": {0}, "labels": [], "lines": []}}'.format(map_info_file[map_name]["svg_geojson_scale"]))
    except Exception as e:
        print("Problem writing to the labels.json file: {}/{}/labels.json.".format(CARTDATA_DIR,map_name))
        print(repr(e))
        sys.exit(1)
    
    print("\nDone.\n")
    
    print("Updating label.json from label information from SVG...")
    try:
        svg2labels(ADDMAP_DATA_DIR + "/{0}/{0}.svg".format(map_name), CARTDATA_DIR + "/{0}/labels.json".format(map_name), map_info_file[map_name]["svg_geojson_scale"], map_info_file[map_name]["svg_geojson_scale"])
    except Exception as e:
        print("Problem parsing the svg file: {}/{}/{}.svg.".format(ADDMAP_DATA_DIR, map_name, map_name))
        print(repr(e))
        sys.exit(1)
    
    print("\nDone.\n")
        
    print("Creating config.json: {}/{}/config.json...".format(CARTDATA_DIR,map_name))
    
    try:
        with open("{}/{}/config.json".format(CARTDATA_DIR,map_name), "w") as config_json_file:
            
            config_json_file.write("""{
        "dont_draw": [],
        "elevate": []
    }""")
    except Exception as e:
        print("Problem writing to the config.json file: {}/{}/config.json.".format(CARTDATA_DIR,map_name))
        print(repr(e))
        sys.exit(1)
        
    print("\nDone.\n")
    
    print("Updating config information from SVG...")
    
    try:
        svg2config(ADDMAP_DATA_DIR + "/{0}/{0}.svg".format(map_name), CARTDATA_DIR + "/{0}/config.json".format(map_name))
    except Exception as e:
        print("Problem parsing the svg file: {}/{}/{}.svg.".format(ADDMAP_DATA_DIR, map_name, map_name))
        print(repr(e))
        sys.exit(1)
        
    print("\nDone.\n")
    
    print("Creating abbreviations.json: {}/{}/abbreviations.json...".format(CARTDATA_DIR,map_name))
    
    try:
        with open("{}/{}/abbreviations.json".format(CARTDATA_DIR,map_name), "w") as abbreviations_json_file:
            abbreviations_json_file.write("{\n")
            abbreviations_json_file.write(",\n".join(list(map(lambda region: '"{}":"{}"'.format(region["name"], region["abbreviation"]), regions))))
            abbreviations_json_file.write("\n}")
    except Exception as e:
        print("Problem writing to the abbreviations.json file: {}/{}/abbreviations.json.".format(CARTDATA_DIR,map_name))
        print(repr(e))
        sys.exit(1)
        
    print("\nDone.\n")
    
    print("Creating template.csv...")
    
    try:
        with open("{}/{}/template.csv".format(CARTDATA_DIR,map_name), "w") as template_csv_file:
            template_csv_file.write('"{}","Population","{}","Colour"\n'.format(map_info_file[map_name]["region_identifier"], map_info_file[map_name]["dataset_name"]))
            template_csv_file.write("\n".join(list(map(lambda region: '"{}","{}","{}","{}"'.format(region["name"], region["population"], region["cartdata"], region["color"]), regions))))
    except Exception as e:
        print("Problem writing to the template.csv file: {}/{}/template.csv.".format(CARTDATA_DIR,map_name))
        print(repr(e))
        sys.exit(1)
        
    print("\nDone.\n")
    
    print("Creating internal/handlers/{}.py...".format(map_name))
    
    try:
        createhandler(map_name, regions, map_info_file[map_name]["user_friendly_name"], map_info_file[map_name]["region_identifier"])
    except Exception as e:
        print("Problem creating the internal/handlers/{}.py file.".format(map_name))
        print(repr(e))
        sys.exit(1)
    
    print("\nDone.\n")
    
    
    print("Updating internal/static/web.py...")
    
    try:
        updatewebpy(map_name)
    except Exception as e:
        print("Problem updating the internal/static/web.py file.")
        print(repr(e))
        sys.exit(1)
    
    print("\nDone.\n")
    
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
    
    print("\nDone.\n")
    
    if "bbox" not in population_json:
        print("Adding bbox to population map...")
        population_json["bbox"] = geojson_extrema.get_extrema_from_geojson(population_json)
        print("Done.\n")
    
    print("Creating population.json: {}/{}/population.json...".format(CARTDATA_DIR,map_name))
    
    try:
        with open("static/cartdata/{}/population.json".format(map_name), "w") as original_json_file:
            population_json["tooltip"] = population_cartogramui[2]
            json.dump(population_json, original_json_file)
    except Exception as e:
        print("Problem writing to the population.json file: {}/{}/population.json.".format(CARTDATA_DIR,map_name))
        print(repr(e))
        sys.exit(1)
    
    print("\nDone.\n")
    
    print("Creating original.json: {}/{}/original.json...".format(CARTDATA_DIR,map_name))
    try:
        with open(map_handler.get_gen_file(), "r") as map_gen_file:
            original_json = json.load(map_gen_file)
            original_tooltip = landarea_cartogramui[2]
            original_json['tooltip'] = original_tooltip
    except Exception as e:
        print(repr(e))
        sys.exit(1)
        
    try:
        with open("static/cartdata/{}/original.json".format(map_name), "w") as original_json_file:
            json.dump(original_json, original_json_file)
    except Exception as e:
        print("Problem writing to the original.json file: {}/{}/original.json.".format(CARTDATA_DIR,map_name))
        print(repr(e))
        sys.exit(1)
            
    print("\nDone.\n")
    
    print("Creating griddocument.json: {}/{}/griddocument.json...".format(CARTDATA_DIR,map_name))
    
    try:
        with open("static/cartdata/{}/griddocument.json".format(map_name), "w") as griddocument_json_file:
            json.dump(cartogramui[3], griddocument_json_file)
    except Exception as e:
        print("Problem writing to the griddocument.json file: {}/{}/griddocument.json.".format(CARTDATA_DIR,map_name))
        print(repr(e))
        sys.exit(1)
    
    print("\nDone.\n")
    
    print("Generating map pack in static/cartdata/{}/mappack.json...".format(map_name))
    
    try:
        mappackify(map_name)
    except Exception as e:
        print("Problem generating the mappack.json file.")
        print(repr(e))
        sys.exit(1)
    
    print("\nDone.\n")
    
    return

def delete_map():
    print("""WARNING: This action is irreversible. If you delete a map, you will not be able to recover it. If you are sure you want to delete a map, enter the name of the map below. If you do not want to delete a map, enter 'exit'.""")
    print()
    print("Enter the name of the map (not the user friendly name) below. This name should be exactly the same name you see inside cartdata.")
    map_name = input("\nEnter map name to delete: ")
    if map_name == 'exit':
        return
    friendly_name = "Not Found"
    try:
        with open("handlers/{}.py".format(map_name), "r") as handler_file:
            handler_file_content = handler_file.read()
            handler_file_lines = handler_file_content.split("\n")
            friendly_name_found = False
            for line in handler_file_lines:
                if friendly_name_found:
                    friendly_name = re.findall('"([^"]*)"', line)[0]
                    break
                elif line.strip() == "def get_name(self):":
                    friendly_name_found = True
                
    except Exception as e:
        print("\nSeems like your map doesn't exist (I couldn't find it in handlers directory). Please input accurate map name or else type 'exit' get out of Add Map Wizard")
        print(repr(e))
        return
    
    print("Add Map Wizard is going to delete all the files related to the map named: \n \t\t\t " + friendly_name)
    print()
    proceed = input("Enter 'Yes' to confirm or anything else to exit: ")
    print()
    if proceed != "Yes":
        return    

    print()
    print("I will now modify web.py to remove your new map. Before I do this, I will back up the current version of web.py to web.py.bak.")
    print()

    print("Backing up web.py...")
    try:
        shutil.copy("web.py", "web.py.bak")
    except Exception as e:
        print("Backing up failed. Try again: ")
        print(repr(e))
        return
    
    print("\nDone.")

    print("\nEditing web.py...")

    try:
        with open("web.py", "r") as web_py_file:

            try:
                web_py_contents = web_py_file.read()
                web_py_lines = web_py_contents.split("\n")
            except Exception as e:
                print("Cannot read web.py. Try again.")
                print(repr(e))
                return
            
        web_py_new_lines = []
        found_header = False
        found_body = False
        
        for line in web_py_lines:
            if line.strip() == "from handlers import {}".format(map_name):
                found_header = True
            elif line.strip() == "'{0}': {0}.CartogramHandler(),".format(map_name):
                found_body = True
            else:
                web_py_new_lines.append(line)
            
        if not found_header or not found_body:
            print()
            print("I was not able to find your map's handler information in web.py file.")
            print()
            print("Do you still want to continue deleting other files?")
            print()
            proceed = input("Enter 'Yes' to continue: ")
            if proceed == "Yes":
                pass
            else:
                return
        else:
            with open("web.py", "w") as web_py_file:
                try:
                    web_py_file.write("\n".join(web_py_new_lines))
                except Exception as e:
                    print("An error occured while trying to write changes to web.py.")
                    print(repr(e))
                    return
        
    except Exception as e:
        print("Cannot open web.py. Try again.")
        print(repr(e))
        return
    
    print("\nDone.\n")
        
    print("Removing handlers/{}.py...".format(map_name))
    try:
        os.remove("handlers/{}.py".format(map_name))
    except FileNotFoundError:
        pass
    except Exception as e:
        print("Problem removing {}.py file. Please check if the file exists.".format(map_name))
        print(repr(e))
        return
    
    print("\nDone.\n")
    
    print("Removing static/cartdata/{}...".format(map_name))
    
    shutil.rmtree("static/cartdata/{}".format(map_name), ignore_errors=True)
    
    print("\nDone.\n")
    
def show_map_info_database():
    try:
        with open(MAP_INFO_DIR, 'r') as file_object:
            map_info_file = json.load(file_object)
    except Exception as e:
        print("Problem reading {}. Please check if the file exists and is in the correct format.".format(MAP_INFO_DIR))
        print(repr(e))
        sys.exit(1)
    
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