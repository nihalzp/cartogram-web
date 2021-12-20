from xml.dom import minidom
import pandas as pd
import geojson 

# Create dictionary for regions to abbreviations.
def get_abr_dict(csv_file, region_name='Region Name', region_abbrev='Region Abbreviation'):
    df = pd.read_csv(csv_file)
    df.loc[:, region_abbrev] = df.loc[:, region_abbrev].fillna('NA')

    region_abr = dict()
    for region, abr in zip(df.loc[:, region_name], df.loc[:, region_abbrev]):
        region_abr[region] = abr 
    
    return region_abr

# Get centroid of polygon.
def get_cent(coords):
    sum_x = 0
    sum_y = 0
    for i in range (len(coords) - 1): # until n-1
        x = coords[i][0]
        y = coords[i][1]
        x_n = coords[i+1][0]
        y_n = coords[i+1][1]

        sum_x += (x + x_n) * ((x * y_n) - (x_n * y))
        sum_y += (y + y_n) * ((x * y_n) - (x_n * y))
    
    centroid_x = (1 / (6 * get_area(coords))) * sum_x
    centroid_y = (1/ (6 * get_area(coords))) * sum_y
    return (centroid_x, centroid_y)

# Get area of polygon.
def get_area(coords):
    sum_area = 0
    for i in range (len(coords) - 1): # until n-1
        x = coords[i][0]
        y = coords[i][1]
        x_n = coords[i+1][0]
        y_n = coords[i+1][1]

        sum_area += (x * y_n) - (x_n * y)

    return (1/2) * sum_area

# Main function for labelling polygons' centroids
def label_centroid(svg_file, abr_dict):
    print('Preparing to label the centroid of each polygon')

    svg = minidom.parse(svg_file)
    paths = svg.getElementsByTagName('path')

    all_coords = [] # for geojson
    # Create dictionary of region abr and coords. {'AB':[(), (), ()], 'CD':[(), (), ()], 'EF':[(), (), ()]}
    abr_to_coords = dict()
    for count, path in enumerate(paths): # iterates through each "path" in the svg
       
        # Need to add code to handle enclaves
        # Create list of path values.
        try:
            num_list = path.getAttribute('d').strip().split(' ')[1:][:-1] # remove M and z
            num_list = [float(x.strip()) for x in num_list] # remove any remaining whitespace
        except:
            continue


        # Create a list of tuples containing the coords of a region. [(), (), (), ()]
        coords = []
        for i in range(0, len(num_list), 2):
            coords.append((num_list[i], num_list[i + 1]))

        # Get value (abbreviation) from abr_dict based on current polygon's region name.
        abbrev = abr_dict[path.getAttribute('gocart:regionname')] 
        if abbrev == 'NA': continue # Skip over regions which have no abbrevation available
        
        # If abr_to_coords dictionary already contains current polygon's abbrevation.
        if abbrev in abr_to_coords.keys():
            curr_p_area = get_area(coords) # current polygon's area 
            dict_p_area = get_area(abr_to_coords[abbrev]) # dictionary polygon's area

            # If the current polygon has a smaller area than the one already in the dictionary, move to next polygon.
            if curr_p_area < dict_p_area: continue

        # If everything checks out, assign value (coords) to key (abbrevation).
        abr_to_coords[abbrev] = coords
        

        ## Included some code below to export a geojson to visualise it which isn't actually necessary in the final code. ##

        centroid = get_cent(coords) # Add centroid to visualise.
        coords_gjson = coords + [(centroid[0], centroid[1])]

        # flip y-coord for geojson file
        for i in range(len(coords_gjson)):
            coords_gjson[i] = (coords_gjson[i][0], -1 * coords_gjson[i][1]) 

        all_coords.append(coords_gjson) # Add coords to all_coords list.

    gjson = geojson.MultiPolygon([all_coords]) 


    # Construct xml text (label) elements and add them to .svg file.
    svg = minidom.parse(svg_file)
    for key in abr_to_coords:
        cent_x = get_cent(abr_to_coords[key])[0] 
        cent_y = get_cent(abr_to_coords[key])[1] 

        # Create label elements.
        label = svg.createElement('text')
        label.setAttribute('y', str(cent_y)) # setAttribute y coord
        label.setAttribute('xml:space', 'preserve')
        label.setAttribute('x', str(cent_x)) # setAttribute x coord
        label.setAttribute('style', 'font-size:18.6667px;line-height:1.25;font-family:sans-serif')
        label.setAttribute('inkscape:label', 'gocartlabel')
        label.setAttribute('id', 'text101')

        # Create tspan elements.
        tspan = svg.createElement('tspan')
        tspan.setAttribute('y', str(cent_y)) # set y coord
        tspan.setAttribute('x', str(cent_x)) # set x coord
        tspan.setAttribute('sodipodi:roll', 'line')
        tspan.setAttribute('id', 'tspan101')
        tspan.appendChild(svg.createTextNode(key))

        # Append tspan as a subelement of label.
        label.appendChild(tspan)

        # Append label element to svg (inside svg tags)
        svg.childNodes[0].appendChild(label)
        
        # Add inkscape attributes to svg element.
        svg_el = svg.getElementsByTagName('svg')[0]
        svg_el.setAttribute('xmlns:dc', 'http://purl.org/dc/elements/1.1/')
        svg_el.setAttribute('xmlns:cc', 'http://creativecommons.org/ns#')
        svg_el.setAttribute('xmlns:rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')
        svg_el.setAttribute('xmlns:svg', 'http://www.w3.org/2000/svg')
        svg_el.setAttribute('xmlns:sodipodi', 'http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd')
        svg_el.setAttribute('xmlns:inkscape', 'http://www.inkscape.org/namespaces/inkscape')
        svg_el.setAttribute('inkscape:version', '1.0beta2 (2b71d25, 2019-12-03)')
        svg_el.setAttribute('sodipodi:docname', svg_file)
        svg_el.setAttribute('id', 'svg337') # not sure if can hardcode this

    # Write to new _labelled.svg file
    with open(svg_file.split('.')[0] + '_labelled.svg', 'w') as f:
        f.write(svg.toxml())

    print('Completed labelling the centroid of each polygon')
    print()

    # Create geojson file or visualisation.
    #with open(svg_file.split('.')[0] + '.json', 'w') as f:
     #   f.write(str(gjson))
