from pipeline import Pipeline

# BEGIN YOUR IMPORTS
from recognition import resize_image, binarize, crop_image, get_sudoku_cells, is_empty, get_digit_correlations, show_correlations, recognize_digits
from const import SUDOKU_SIZE, NUM_CELLS, CELL_SIZE
from utils import read_image
from frontalization import rescale_image, gaussian_blur, find_edges, highlight_edges, find_contours, get_max_contour, find_corners, frontalize_image
# END YOUR IMPORTS

# BEGIN YOUR CODE

"""
create dict of cell coordinates like in this example

CELL_COORDINATES = {"image_0.jpg": {1: (0, 0),
                                    2: (1, 1)},
                    "image_2.jpg": {1: (2, 3),
                                    3: [(2, 1), (0, 4)],
                                    9: (5, 6)}}
"""
"""
In the train dataset we have sudokus from two diffrent sources and thereby two diffrent font for the digits.
Because of that we sample templates from both sources.
"""

CELL_COORDINATES = {"image_1.jpg": {1: (6,1),
                                    3: (1,1),
                                    5: (1,4),
                                    7: (4,1),
                                    8: (1,0)},
                    "image_2.jpg": {2: (7,7),
                                    4: (7,5),
                                    6: (4,4),
                                    9: (0,2)},
                    "image_5.jpg": {1: (7,7),
                                    3: (1,7),
                                    5: (1,1),
                                    6: (1,4),
                                    7: (7,4),
                                    8: (4,1)},
                    "image_6.jpg": {2: (1,6),
                                    4: (4,6),
                                    9: (1,2)}}

# END YOUR CODE


# BEGIN YOUR FUNCTIONS



# END YOUR FUNCTIONS


def get_template_pipeline():
    # BEGIN YOUR CODE

    functions = [
        gaussian_blur,
        find_edges,
        highlight_edges,
        find_contours,
        get_max_contour,
        find_corners,
        frontalize_image,
        resize_image,
        get_sudoku_cells
    ]
    parameters = {
        "rescale_image": {"scale": 0.6},
        "gaussian_blur": {"sigma": 0.9},
        "find_corners": {"epsilon": 0.9},
        "resize_image": {"size": SUDOKU_SIZE},
        "crop_image": {"crop_factor": 0.9},
        "get_sudoku_cells": {"crop_factor": 0.75, "binarization_kwargs": {}},
        "get_digit_correlations": {"templates_dict": CELL_COORDINATES}
    }
    pipeline = Pipeline(functions=functions, parameters=parameters)

    return pipeline

    # END YOUR CODE
"""
    functions = [
        resize_image,
        binarize,
        crop_image,
        get_sudoku_cells,
        is_empty,
        get_digit_correlations,
        show_correlations,
        recognize_digits
    ]
    parameters = {
        "resize_image": {"size": (512, 512)},
        "crop_image": {"crop_factor": 0.1},
        "extract_sudoku_cells": {"cell_size": 64},
        "is_empty": {"threshold": 0.5},
        "get_digit_correlations": {"templates_dict": CELL_COORDINATES}  # templates_dict hinzugefügt
    }
"""
