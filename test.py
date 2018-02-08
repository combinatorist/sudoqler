import unittest
import sudoqler as sud
import numpy as np
import pdb

example_one_line = '...847.5...5...2.7.4..6..3.....7.3..3.......2..7.1.....5..9..1.8.4...5...1.685...\n'

example_sudoku2d = np.asarray([['.', '.', '.', '8', '4', '7', '.', '5', '.'],
                               ['.', '.', '5', '.', '.', '.', '2', '.', '7'],
                               ['.', '4', '.', '.', '6', '.', '.', '3', '.'],
                               ['.', '.', '.', '.', '7', '.', '3', '.', '.'],
                               ['3', '.', '.', '.', '.', '.', '.', '.', '2'],
                               ['.', '.', '7', '.', '1', '.', '.', '.', '.'],
                               ['.', '5', '.', '.', '9', '.', '.', '1', '.'],
                               ['8', '.', '4', '.', '.', '.', '5', '.', '.'],
                               ['.', '1', '.', '6', '8', '5', '.', '.', '.']])

example_sudoku2d_int = np.asarray([[0, 0, 0, 8, 4, 7, 0, 5, 0],
                                   [0, 0, 5, 0, 0, 0, 2, 0, 7],
                                   [0, 4, 0, 0, 6, 0, 0, 3, 0],
                                   [0, 0, 0, 0, 7, 0, 3, 0, 0],
                                   [3, 0, 0, 0, 0, 0, 0, 0, 2],
                                   [0, 0, 7, 0, 1, 0, 0, 0, 0],
                                   [0, 5, 0, 0, 9, 0, 0, 1, 0],
                                   [8, 0, 4, 0, 0, 0, 5, 0, 0],
                                   [0, 1, 0, 6, 8, 5, 0, 0, 0]])

example_sudoku3d_bool = np.asarray([
    [[None, None, None, None, None, None, None, None, None],
     [None, None, None, None, None, None, None, None, None],
     [None, None, None, None, None, None, None, None, None],
     [None, None, None, None, None, None, None, None, None],
     [None, None, None, None, None, None, None, None, None],
     [None, None, None, None, True, None, None, None, None],
     [None, None, None, None, None, None, None, True, None],
     [None, None, None, None, None, None, None, None, None],
     [None, True, None, None, None, None, None, None, None]],

    [[None, None, None, None, None, None, None, None, None],
     [None, None, None, None, None, None, True, None, None],
     [None, None, None, None, None, None, None, None, None],
     [None, None, None, None, None, None, None, None, None],
     [None, None, None, None, None, None, None, None, True],
     [None, None, None, None, None, None, None, None, None],
     [None, None, None, None, None, None, None, None, None],
     [None, None, None, None, None, None, None, None, None],
     [None, None, None, None, None, None, None, None, None]],

    [[None, None, None, None, None, None, None, None, None],
     [None, None, None, None, None, None, None, None, None],
     [None, None, None, None, None, None, None, True, None],
     [None, None, None, None, None, None, True, None, None],
     [True, None, None, None, None, None, None, None, None],
     [None, None, None, None, None, None, None, None, None],
     [None, None, None, None, None, None, None, None, None],
     [None, None, None, None, None, None, None, None, None],
     [None, None, None, None, None, None, None, None, None]],

    [[None, None, None, None, True, None, None, None, None],
     [None, None, None, None, None, None, None, None, None],
     [None, True, None, None, None, None, None, None, None],
     [None, None, None, None, None, None, None, None, None],
     [None, None, None, None, None, None, None, None, None],
     [None, None, None, None, None, None, None, None, None],
     [None, None, None, None, None, None, None, None, None],
     [None, None, True, None, None, None, None, None, None],
     [None, None, None, None, None, None, None, None, None]],

    [[None, None, None, None, None, None, None, True, None],
     [None, None, True, None, None, None, None, None, None],
     [None, None, None, None, None, None, None, None, None],
     [None, None, None, None, None, None, None, None, None],
     [None, None, None, None, None, None, None, None, None],
     [None, None, None, None, None, None, None, None, None],
     [None, True, None, None, None, None, None, None, None],
     [None, None, None, None, None, None, True, None, None],
     [None, None, None, None, None, True, None, None, None]],

    [[None, None, None, None, None, None, None, None, None],
     [None, None, None, None, None, None, None, None, None],
     [None, None, None, None, True, None, None, None, None],
     [None, None, None, None, None, None, None, None, None],
     [None, None, None, None, None, None, None, None, None],
     [None, None, None, None, None, None, None, None, None],
     [None, None, None, None, None, None, None, None, None],
     [None, None, None, None, None, None, None, None, None],
     [None, None, None, True, None, None, None, None, None]],

    [[None, None, None, None, None, True, None, None, None],
     [None, None, None, None, None, None, None, None, True],
     [None, None, None, None, None, None, None, None, None],
     [None, None, None, None, True, None, None, None, None],
     [None, None, None, None, None, None, None, None, None],
     [None, None, True, None, None, None, None, None, None],
     [None, None, None, None, None, None, None, None, None],
     [None, None, None, None, None, None, None, None, None],
     [None, None, None, None, None, None, None, None, None]],

    [[None, None, None, True, None, None, None, None, None],
     [None, None, None, None, None, None, None, None, None],
     [None, None, None, None, None, None, None, None, None],
     [None, None, None, None, None, None, None, None, None],
     [None, None, None, None, None, None, None, None, None],
     [None, None, None, None, None, None, None, None, None],
     [None, None, None, None, None, None, None, None, None],
     [True, None, None, None, None, None, None, None, None],
     [None, None, None, None, True, None, None, None, None]],

    [[None, None, None, None, None, None, None, None, None],
     [None, None, None, None, None, None, None, None, None],
     [None, None, None, None, None, None, None, None, None],
     [None, None, None, None, None, None, None, None, None],
     [None, None, None, None, None, None, None, None, None],
     [None, None, None, None, None, None, None, None, None],
     [None, None, None, None, True, None, None, None, None],
     [None, None, None, None, None, None, None, None, None],
     [None, None, None, None, None, None, None, None, None]]])

example_box_sudoku = ([[0, 0, 0, 0, 0, 5, 0, 4, 0],
                       [8, 4, 7, 0, 0, 0, 0, 6, 0],
                       [0, 5, 0, 2, 0, 7, 0, 3, 0],
                       [0, 0, 0, 3, 0, 0, 0, 0, 7],
                       [0, 7, 0, 0, 0, 0, 0, 1, 0],
                       [3, 0, 0, 0, 0, 2, 0, 0, 0],
                       [0, 5, 0, 8, 0, 4, 0, 1, 0],
                       [0, 9, 0, 0, 0, 0, 6, 8, 5],
                       [0, 1, 0, 5, 0, 0, 0, 0, 0]])

example_partial_elimination = np.asarray(
    [[ None, False,  None, False, False, False,  None, False,  None],
     [ None, False, False,  None, False,  None, False, False, False],
     [ None, False,  None,  None, False,  None,  None, False,  None],
     [ None, False,  None,  None, False,  None, False, False,  None],
     [False, False,  None,  None, False,  None,  None, False, False],
     [False, False, False, False,  True, False, False, False, False],
     [False, False, False, False, False, False, False,  True, False],
     [False, False, False,  None, False,  None, False, False,  None],
     [False,  True, False, False, False, False, False, False, False]]
)

class bq_tests(unittest.TestCase):
    def test001_load(self):
        content = sud.load('test001_load.txt')
        self.assertEqual(
            content,
            example_one_line
        )

    def test002_from_one_line(self):
        sudoku2d = sud.from_one_line(example_one_line)
        self.assertEqual(
            sudoku2d.shape,
            (9,)*2
        )
        np.testing.assert_equal(
            sudoku2d,
            example_sudoku2d
        )

    def test003_array_to_int(self):
        int_array = sud.array_to_int(example_sudoku2d)
        np.testing.assert_equal(
            int_array,
            example_sudoku2d_int
        )

    def test004_abstract_array(self):
        np.testing.assert_equal(
          sud.abstract_array(example_sudoku2d_int),
          example_sudoku3d_bool
        )

    def test005_box_sudoku(self):
        np.testing.assert_equal(
          sud.box_sudoku(example_sudoku2d_int),
          example_box_sudoku
        )

    def test005_rotate(self):
        positional_3d_array = np.asarray(range(1, 9 ** 3 + 1)).reshape((9,) * 3)
        result = sud.rotate(sud.rotate(sud.rotate(positional_3d_array)))
        np.testing.assert_equal(
            result,
            positional_3d_array
        )

    def test006_group_ungroup(self):
        # demonstrates logic used inside eliminate function
        test_array = np.arange(27).reshape((3, 3, 3))
        grouped = test_array.reshape((9, 3))
        ungrouped = grouped.reshape((3, 3, 3))

        np.testing.assert_equal(
            ungrouped,
            test_array
        )

    def test007_eliminate(self):
        result = sud.eliminate(example_sudoku3d_bool)
        np.testing.assert_equal(
            result[0],
            example_partial_elimination
        )

    def test999_end_to_end(self):
        np.testing.assert_equal(
            sud.abstract_array(sud.array_to_int(
                    sud.from_one_line(sud.load('test001_load.txt'))
                )),
            example_sudoku3d_bool
        )


if __name__ == '__main__':
        unittest.main()
