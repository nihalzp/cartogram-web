import json
import csv

# TODO: Use a Python package to write SVG files instead of writing the SVG by hand
def json2svg(json_file, out_file, csv_file):
    
    try:
        with open(json_file, "r") as map_gen_file:
            geo_json = json.load(map_gen_file)
    except Exception as e:
        raise e
    
    try:
        with open(csv_file, 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            regions = []
    
            for row in reader:
                regions.append({
                    "id": row["Region Id"],
                    "name": row["Region Name"],
                    "color": row["Color"]
                })
    except Exception as e:
        raise e
        
    def find_region_by_id(i):
        for region in regions:
            if region["id"] == str(i):
                return region
        
        return None


    with open("{}".format(out_file), "w") as svg_file:

        max_x = geo_json["bbox"][2]
        min_x = geo_json["bbox"][0]
        max_y = geo_json["bbox"][3]
        min_y = geo_json["bbox"][1]

        width = max_x - min_x
        height = max_y - min_y

        if width >= height:
            scale = 450.0/width
        else:
            scale = 450.0/height
        
        width *= scale
        height *= scale
        
        def x_transform(x):

            return (x - min_x)*scale
        
        def y_transform(y):

            return (max_y - y)*scale
        
        svg_file.write("""<svg version="1.1"
baseProfile="full"
width="{}" height="{}"
xmlns="http://www.w3.org/2000/svg"
xmlns:gocart="https://go-cart.io">
""".format(round(width,2), round(height, 2)))

        next_polygon_id = 1

        for feature in geo_json["features"]:

            if feature["geometry"]["type"] == "Polygon":

                polygon_path = None
                hole_paths = []
                polygon_id = next_polygon_id

                for path in feature["geometry"]["coordinates"]:

                    next_polygon_id += 1

                    if polygon_path == None:

                        polygon_path = " ".join(list(map(lambda coord: "{} {}".format(round(x_transform(coord[0]), 3), round(y_transform(coord[1]), 3)), path)))
                        
                    else:

                        hole_path = " ".join(list(map(lambda coord: "{} {}".format(round(x_transform(coord[0]), 3), round(y_transform(coord[1]), 3)), path)))

                        hole_paths.append("M {} z".format(hole_path))
                
                path = "M {} z {}".format(polygon_path, " ".join(hole_paths))

                region = find_region_by_id(feature["properties"]["cartogram_id"])
                svg_file.write(
                    '<path gocart:regionname="{}" d="{}" id="polygon-{}" class="region-{}" fill="{}" stroke="#000000" stroke-width="1"/>\n'.format(
                        region["name"], path, polygon_id, feature["properties"]["cartogram_id"], region["color"]))
            elif feature["geometry"]["type"] == "MultiPolygon":

                for polygon in feature["geometry"]["coordinates"]:

                    polygon_path = None
                    hole_paths = []
                    polygon_id = next_polygon_id

                    for path in polygon:

                        next_polygon_id += 1

                        if polygon_path == None:

                            polygon_path = " ".join(list(map(lambda coord: "{} {}".format(round(x_transform(coord[0]), 3), round(y_transform(coord[1]), 3)), path)))
                            
                        else:

                            hole_path = " ".join(list(map(lambda coord: "{} {}".format(round(x_transform(coord[0]), 3), round(y_transform(coord[1]), 3)), path)))

                            hole_paths.append("M {} z".format(hole_path))
                    
                    path = "M {} z {}".format(polygon_path, " ".join(hole_paths))

                    #print(feature["properties"]["cartogram_id"])

                    region = find_region_by_id(feature["properties"]["cartogram_id"])

                    #print(repr(region))

                    svg_file.write('<path gocart:regionname="{}" d="{}" id="polygon-{}" class="region-{}" fill="{}" stroke="#000000" stroke-width="1"/>\n'.format(region["name"], path, polygon_id, feature["properties"]["cartogram_id"],region["color"]))
            else:
                raise Exception("Unsupported feature type {}.".format(feature["geometry"]["type"]))
        
        svg_file.write("</svg>")
        return scale
