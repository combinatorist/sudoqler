import numpy as np
from tribool import Tribool
import warnings

box_shape    = (3, 3)
box_size     = box_shape[0] * box_shape[1]
puzzle_shape = (box_size,) * 2
puzzle_size  = box_size ** 2

def load(file):
    """
    loads file
    """
    with open(file) as f:
        contents = f.read()
    return contents


def from_one_line(one_line_sudoku):
    """
    creates a 2d array view from sudoku in "one line" format
    """
    length = len(one_line_sudoku)
    if length > puzzle_size:
        warning_body = ["Too many values: Needed {}, but received {}",
                        "Ignored values: {} ..."]
        warnings.warn('\n'.join(warning_body).format(puzzle_size, length,
            one_line_sudoku[puzzle_size:puzzle_size + 7]
            .encode('string_escape')))
    sudoku1d = np.array([char for char in one_line_sudoku[:puzzle_size]])
    sudoku2d = sudoku1d.copy().reshape(puzzle_shape)
    return sudoku2d


def array_to_int(array, find='.', replace=0):
    """
    converts array to int dtype
    default replaces '.' with 0 (helpful for simple sudoku format: .ss)
    """
    array[array == find] = replace
    int_array = np.asarray(array, dtype=int)
    return int_array


def abstract_array(array, value_list = range(1, box_size + 1)):
    """
    creates boolean array with additional dimension representing values
    """
    array_list = []
    for i in value_list:
        array_list.append(array == i)
    boolean_array = np.stack(array_list)
    three_valued_array = np.asarray(boolean_array, dtype=Tribool)
    three_valued_array[three_valued_array == False] = None
    return three_valued_array

def box_sudoku(sudoku2d):
    """
    creates a view that indicates the boxes
    """
    # First converts shape from 9 rows by 9 columns to (3, 3, 3, 3) [unit_rows]
    unit_row_sudoku = sudoku2d.reshape(box_shape * 2)
    # Then, swaps middle 2 axes and converts to new (9, 9) [9 boxes by 9 cells]
    return np.swapaxes(unit_row_sudoku, -3, -2).reshape(puzzle_shape)

def rotate(array):
    """
    rotates axes once by pushing first axis to the last position
    """
    return np.moveaxis(array, 0, -1)

def eliminate(array):
    """
    marks unknowns false where they would conflict with known values
    """
    array = array.copy()
    for axis in range(3):
        groups = array.reshape((puzzle_size, box_size))
        for group in groups:
            occupied = max(group)
            if occupied == True:
                group[group != True] = False

        array = groups.reshape((box_size,) * 3)
        array = rotate(array)
    return array


if __name__ == '__main__':
  main()
