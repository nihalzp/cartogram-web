import json

def get_bbox(geojson):
    
    min_x = None
    max_x = None
    min_y = None
    max_y = None
    
    for feature in geojson["features"]:
        if feature["geometry"]["type"] == "Polygon":
            for path in feature["geometry"]["coordinates"]:
                for coord in path:
                    if max_x == None or coord[0] > max_x:
                        max_x = coord[0]
                    if min_x == None or coord[0] < min_x:
                        min_x = coord[0]
                    if max_y == None or coord[1] > max_y:
                        max_y = coord[1]
                    if min_y == None or coord[1] < min_y:
                        min_y = coord[1]
        
        elif feature["geometry"]["type"] == "MultiPolygon":
            for polygon in feature["geometry"]["coordinates"]:
                for path in polygon:
                    for coord in path:
                        if max_x == None or coord[0] > max_x:
                            max_x = coord[0]
                        if min_x == None or coord[0] < min_x:
                            min_x = coord[0]
                        if max_y == None or coord[1] > max_y:
                            max_y = coord[1]
                        if min_y == None or coord[1] < min_y:
                            min_y = coord[1]
        
        else:
            raise Exception("Unsupported feature type {}".format(feature["geometry"]["type"]))
    
    return [
        min_x,
        min_y,
        max_x,
        max_y
    ]
    
def add_cart_id(json_file, out_file, name_key):
    try:
        with open(json_file, "r") as map_gen_file:
            geo_json = json.load(map_gen_file)
            names = []
            for regions in geo_json["features"]:
                names.append(regions["properties"][name_key])
            sorted_names_with_ids = {}
            names = sorted(names)
            for id in range(len(names)):
                sorted_names_with_ids[names[id]] = id + 1
            for regions in geo_json["features"]:
                regions["properties"]["cartogram_id"] = str(sorted_names_with_ids[regions["properties"][name_key]])
                
            if "bbox" not in geo_json:
                print("\nGeoJSON doesn't have a bbox information. \n")
                print("\nAdding bbox...")
                geo_json["bbox"] = get_bbox(geo_json)
                
            with open(out_file, 'w') as f:
                f.write(json.dumps(geo_json))
    except Exception as e:
        raise e




