#!/usr/bin/python3

import geopandas as gpd
import matplotlib

def main():
    print("Hello world!")
    # Set filepath
    fp = "L2_data/Europe_borders.shp"

    # Read file using gpd.read_file()
    data = gpd.read_file(fp)
    # print(type(data))

    data.plot()

main()