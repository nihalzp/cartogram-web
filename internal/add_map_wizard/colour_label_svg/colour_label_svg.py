from topo_colour import topo_colour
from set_svg_colours import get_colour_dict, set_style
from label_centroid import get_abr_dict, label_centroid

json_file = input('Enter the name of the .json file: ')
csv_file = input('Enter the name of the .csv file: ')
svg_file = input('Enter the name of the .svg file: ')

'''
region_col_name = input("Please enter the column name of the regions: ")
region_abr_name= input("Please enter the column name of the region abbrevations: ")

csv_file = 'world_97_data_ogists.csv'
json_file =  'world_97_processedmap.json'
svg_file = 'world_97.svg' 
'''

region_col_name = 'Region Name'
region_abr_name= 'Region Abbreviation'

# Run topo_colour.py
print('1. Running topo_colour.py...')
topo_colour('data/' + csv_file,'data/' + json_file)

# Run set_svg_colours.py
print('2. Running set_svg_colours.py...')
csv_top_filename = 'data/' + csv_file.split('.')[0] + '_top.csv'
region_colour_dict = get_colour_dict(csv_top_filename, region_col_name)
set_style('data/' + svg_file, region_colour_dict)

# Run label_centroid.py
print('3. Running label_centroid.py...')
region_abr_dict = get_abr_dict('data/' + csv_file, region_col_name)
coloured_filename = 'data/' + svg_file.split('.')[0] + '_coloured.svg'
label_centroid(coloured_filename, region_abr_dict)
