import pandas as pd
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

def topo_colour(csv_file, json_file):
    print('Preparing csv file with \'Colour\' column')
    
    csv_df = pd.read_csv(csv_file)
    gjson_df = gpd.read_file(open(json_file))

    gjson_df['colour_id'] = greedy(gjson_df, min_colors=6)

    gjson_df = gjson_df[['NAME', 'STUSPS', 'colour_id']]

    for i, row1 in csv_df.iterrows():
        for j, row2 in gjson_df.iterrows():
            if csv_df.loc[i, 'Region Abbreviation'] == gjson_df.loc[j, 'STUSPS']:
                csv_df.loc[i, 'Colour'] = convert_id_to_hex(gjson_df.loc[j, 'colour_id'])
                break

    csv_df.to_csv(csv_file.split('.')[0] + '_top.csv', index=False)

    print('Completed csv file with \'Colour\' column')
    print()
