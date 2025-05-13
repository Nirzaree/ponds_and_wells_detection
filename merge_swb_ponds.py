import geopandas as gpd
import pandas as pd
import numpy as np
import ee


def merge_swb_ponds(swb_layer_path,
                    ponds_layer_path,
                    mws_layer_path
                    ):
    '''
    module to merge swb and ponds layer
    '''

    #Load swb layer
    swb_gdf = gpd.read_file(swb_layer_path)

    #Load ponds layer
    ponds_gdf= gpd.read_file(ponds_layer_path)

    # #change their crs
    # swb_gdf.to_crs('epsg:7755',inplace=True)
    # ponds_gdf.to_crs('epsg:7755',inplace=True)

    # #compute area of geometries
    # swb_gdf['area_m2'] = swb_gdf['geometry'].area
    # ponds_gdf['area_m2'] = ponds_gdf['geometry'].area

    # create merged_gdf
    intersecting_UIDs = swb_gdf.sjoin(ponds_gdf)['UID'].tolist()

    # 1. Add standalone SWBs
    standalone_swb_gdf = swb_gdf[~swb_gdf['UID'].isin(intersecting_UIDs)]
    merged_gdf = standalone_swb_gdf

    # 2. Add standalone ponds
    intersecting_FIDs = ponds_gdf.sjoin(standalone_swb_gdf)['FID'].tolist()
    standalone_ponds_gdf = ponds_gdf[~ponds_gdf['FID'].isin(intersecting_FIDs)]
    merged_gdf = pd.concat([merged_gdf,standalone_ponds_gdf])

    # 3. Intersection cases : 
    # case 1: 1 pond intersecting with 1 swb 






