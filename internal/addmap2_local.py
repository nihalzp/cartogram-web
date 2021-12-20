
from process_json import add_cart_id
from json2csv import json2csv
import sys
import os
import json
from constants import *
from shutil import rmtree

def welcome():
    
    print(f"""
                            Welcome to the Add Map Wizard!
                            
         1. Add cartogram_id and generate csv
         2. Produce SVG for coloring and labeling
         3. Add the map
         4. Delete a map
         5. See a map information
         
Input your choice (i.e. 1, 2, ...) ['exit' to quit and '?' for more info]
""")
     
def main():
    choice = input("Choice: ")
    
    if choice == '1':
        processmap();
    else:
        print("\nFor other options than 1, please run .\\addmap2.sh \n")
        sys.exit()
        
def processmap():
    map_name = input("\nInput the name of your map (without spaces): ")
    if os.path.exists(INTERNAL_DIR_LOCAL + "/handlers/{}.py".format(map_name)):
        print("Error: It looks like a map with the name '{}' already exists (I found handlers/{}.py).".format(map_name, map_name))
        return
    
    if os.path.exists(INTERNAL_DIR_LOCAL +"/static/cartdata/{}".format(map_name)):
        print("Error: It looks like a map with the name '{}' already exists (I found static/cartdata/{}).".format(map_name, map_name))
        return
    
    user_friendly_name = input("\nEnter a user friendly name for this map: ")
    
    print("Add your map's JSON/GeoJSON file inside data/addmap_data/ directory.\n")
    
    map_gen_file = input("Once you are done, enter the name of map's .json name: ")
    
    map_gen_file = ADDMAP_DATA_DIR_LOCAL + "/" + map_gen_file
    
    print("Please open the .json/.geojson file, and let me know the following information—\n")
    
    region_name_key = input("Key name that contains Region Names (usually it is NAME_1): ")
    region_abr_key = input("\nKey name that contains Region Abbreviations (usually it is GID_1): ")
    region_identifier = input("What are the regions of this map called (e.g. State, Province)? ")
    dataset_name = input("What is the name of the cartogram you want to generate (e.g. GDP)? ")
    
    print("\nI will add unique cartogram ids to each of the regions...\n")
    
    if os.path.exists(ADDMAP_DATA_DIR_LOCAL + "/{}".format(map_name)):
        rmtree(ADDMAP_DATA_DIR_LOCAL + "/{}".format(map_name))
        
    os.mkdir(ADDMAP_DATA_DIR_LOCAL + "/{}".format(map_name))
    
    add_cart_id(map_gen_file, "{}/{}/{}_processed.json".format(ADDMAP_DATA_DIR_LOCAL, map_name, map_name) ,region_name_key)
    
    print("Done adding cartogram_ids\n")
    
    print("\nI will generate csv file...\n")
    
    json2csv("{}/{}/{}_processed.json".format(ADDMAP_DATA_DIR_LOCAL, map_name, map_name), "{}/{}/{}.csv".format(ADDMAP_DATA_DIR_LOCAL, map_name, map_name) ,region_name_key, region_abr_key) 
    
    print("\nDone generating csv file\n")
    
    print("\nNow I will your map information to the local database...\n")
    with open(MAP_INFO_DIR_LOCAL, 'r') as file_object:
        map_info_file = json.load(file_object)
        map_info_file[map_name] = {
            "user_friendly_name" : user_friendly_name,
            "region_name_key" : region_name_key,
            "region_abr_key" : region_abr_key,
            "region_identifier" : region_identifier,
            "dataset_name" : dataset_name,
        }
        
    with open(MAP_INFO_DIR_LOCAL, 'w') as json_object:
        json.dump(map_info_file, json_object, indent=4, separators=(", ", ": ") )
    
    print("\nDone adding map information to the local database\n")

welcome()

main()