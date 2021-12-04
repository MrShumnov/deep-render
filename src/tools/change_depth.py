import numpy as np
import h5py

def open_dataset(filename):
    f = h5py.File("/raid/shumnov/hypersim/dataset/" + filename + ".hdf5", "r")

    color = f["color"][()]
    albedo = f["diffuse_reflectance"][()]
    depth = f["depth_meters"][()]
    normals = f["normal_bump_cam"][()]

    f.close()
    
    return color, albedo, depth, normals

fnames = ["ai_016_002"]

for fname in fnames:
    color, albedo, depth, normals = open_dataset("/raid/shumnov/hypersim/dataset/" + fname + ".hdf5")

    depth = depth * 2 - 1

    with h5py.File("/raid/shumnov/hypersim/dataset/" + fname + ".hdf5", "w") as f:
        f.create_dataset("color", data=color, compression='gzip')
        f.create_dataset("diffuse_reflectance", data=albedo, compression='gzip')
        f.create_dataset("depth_meters", data=depth, compression='gzip')
        f.create_dataset("normal_bump_cam", data=normals, compression='gzip')