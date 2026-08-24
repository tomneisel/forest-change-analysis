import numpy as np

def calculate_ndvi(nir, red):
    return (nir - red) / (nir + red)