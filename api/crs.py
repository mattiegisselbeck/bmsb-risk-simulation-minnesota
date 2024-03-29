# -*- coding: utf-8 -*-

import pyproj

__author__ = "Mattie Gisselbeck"
__status__ = "Production"

class CoordinateTransformer:
    def __init__(self, current_epsg: int = 32615, target_epsg: int = 4326):
        self.current_crs = pyproj.CRS.from_epsg(current_epsg)
        self.target_crs = pyproj.CRS.from_epsg(target_epsg)
        self.transformer = pyproj.Transformer.from_crs(
            self.current_crs, self.target_crs, always_xy=True
        )

    def transform_coordinates(self, results):
        # Convert Coordinates in Each Feature to WGS84
        for feature in results['features']:
            coords = feature['geometry']['coordinates']
            transformed_coords = self.transformer.transform(coords[0], coords[1])
            feature['geometry']['coordinates'] = [transformed_coords[0], transformed_coords[1]]

        # Return
        return results

