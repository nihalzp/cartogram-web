from xml.dom import minidom
import json
import sys
import re
import copy
import os

polygon_id_re = re.compile(r'polygon-([0-9]+)')

def svg2config(svg_filepath, config_filepath):

    config = {
        'dont_draw': [],
        'elevate': []
    }
    svg_map = minidom.parse(svg_filepath)

    for path in svg_map.getElementsByTagName("path"):

        # First, see if we have a valid polygon
        polygon_id_match = polygon_id_re.match(path.getAttribute("id"))

        if polygon_id_match == None:
            continue
        
        polygon_id = int(polygon_id_match.group(1))

        if not path.hasAttribute("inkscape:label"):
            continue
        
        if path.getAttribute("inkscape:label") != "gocartelevate":
            continue
        
        print("Elevating polygon {}.".format(polygon_id))
        
        config['elevate'].append(polygon_id)
        
    with open(config_filepath, 'w') as config_json_file:
        json.dump(config, config_json_file, indent=4)
    
    return

    




