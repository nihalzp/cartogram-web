import pandas as pd 
from xml.dom import minidom

def get_colour_dict(csv_file_name, region_name='NAME'):
    # read in csv as dataframe object
    df = pd.read_csv(csv_file_name)

    # fill empty colour cells
    df.loc[:, 'Colour'] = df.loc[:, 'Colour'].fillna("#aaaaaa")

    region_colour = dict()

    for region, colour in zip(df.loc[:, region_name], df.loc[:, 'Colour']):
        region_colour[region] = colour
    
    return region_colour

def set_style(svg_file_path, colour_dict):
    # read in svg as minidom object
    svg = minidom.parse(svg_file_path)
    # get path elements
    paths = svg.getElementsByTagName('path')

    # iterate through path elements
    print('Replacing the style attributes with the colours provided...')
    for path in paths:
        
        # set style
        fill = 'fill:' + colour_dict.get(path.getAttribute('gocart:regionname'), '#aaaaaa')
        path.setAttribute('style', fill)

        # remove 'fill' as it has less priority compared to 'style'
        try:
            path.removeAttribute('fill')
        except:
            pass
        
    with open(svg_file_path.split('.')[0] + "_coloured.svg", 'w') as f:
        f.write(svg.toxml())

    print('Completed replacing the style attributes!')
    print()


#csv = input("Enter csv file: ")
#svg = input("Enter svg file: ")

#colour_dict = get_colour_dict('data/world_97_data_ogists_top.csv', 'Region Name')
#set_style('data/world_97.svg', colour_dict)
