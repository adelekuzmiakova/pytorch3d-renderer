#!/usr/bin/env python
# coding: utf-8

import json
from utils import Params


def create_2d_mesh(orig_filename, new_filename, z_coord):
    """
    Creates a new obj file by copying the contents from the original obj file and 
    replacing the z-coordinate values with a constant (0 in this case).

    Args:
        orig_filename: str, path to the original obj filename
        new_filename: str, path to the new obj filename
        z_coord: list, new z-coordinate which will replace old z-values 
    """
    with open(orig_filename) as orig_file, open(new_filename, 'w') as new_file: 
        # Read through lines in the original obj file
        for line in orig_file:
            # Look for vertex coordinates: do not match "vt" or "vn"
            if 'v' == line[0] and line[1].isspace(): 
                partial_coord = line.split(' ')[0:-1]
                # Use previous x- and y-coordinates and append the new z-coordinate
                line = partial_coord + z_coord
                line = ' '.join([str(elem) for elem in line])
                new_file.write(str(line) + '\n')
            else:
                new_file.write(str(line))
    orig_file.close()
    new_file.close()         


def main():
    orig_filename = "data/rooster/rooster_1.0.1.obj"
    added_string = "_copy.obj"
    # Generate a new obj filename 
    new_filename = orig_filename.split('.obj')[0] + added_string
    params = Params("params.json")
    z_coord = [params.z_coord]
    create_2d_mesh(orig_filename, new_filename, z_coord)
    print("Done. Created a new mesh " + str(new_filename))


if __name__ == "__main__":
    main()
