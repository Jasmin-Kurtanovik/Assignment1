from pipeline import Pipeline

# BEGIN YOUR IMPORTS
from recognition import resize_image, binarize, crop_image, get_sudoku_cells, is_empty, get_digit_correlations, show_correlations, recognize_digits
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
CELL_COORDINATES = {"image_1.jpg": {1: (1,6),
                                    3: (1,1),
                                    5: (4,1),
                                    7: (1,4),
                                    8: (0,1)},
                    "image_2.jpg": {2: (7,7),
                                    4: (5,7),
                                    6: (4,4),
                                    9: (2,0)},
                    "image_5.jpg": {1: (7,7),
                                    3: (7,1),
                                    5: (1,1),
                                    6: (4,1),
                                    7: (4,7),
                                    8: (1,4)},
                    "image_6.jpg": {2: (6,1),
                                    4: (6,4),
                                    9: (2,1)}}

# END YOUR CODE


# BEGIN YOUR FUNCTIONS



# END YOUR FUNCTIONS


def get_template_pipeline():
    # BEGIN YOUR CODE
    # Give all the functions of the file recognition.py to the pipeline
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

    pipeline = Pipeline(functions= functions)
    
    return pipeline

    # END YOUR CODE

