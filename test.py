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

example_sudoku3d_bool = np.asarray([[[ True,  True,  True, False, False, False,  True, False,  True],
                                     [ True,  True, False,  True,  True,  True, False,  True, False],
                                     [ True, False,  True,  True, False,  True,  True, False,  True],
                                     [ True,  True,  True,  True, False,  True, False,  True,  True],
                                     [False,  True,  True,  True,  True,  True,  True,  True, False],
                                     [ True,  True, False,  True, False,  True,  True,  True,  True],
                                     [ True, False,  True,  True, False,  True,  True, False,  True],
                                     [False,  True, False,  True,  True,  True, False,  True,  True],
                                     [ True, False,  True, False, False, False,  True,  True,  True]],
 
                                    [[False, False, False, False, False, False, False, False, False],
                                     [False, False, False, False, False, False, False, False, False],
                                     [False, False, False, False, False, False, False, False, False],
                                     [False, False, False, False, False, False, False, False, False],
                                     [False, False, False, False, False, False, False, False, False],
                                     [False, False, False, False,  True, False, False, False, False],
                                     [False, False, False, False, False, False, False,  True, False],
                                     [False, False, False, False, False, False, False, False, False],
                                     [False,  True, False, False, False, False, False, False, False]],
 
                                    [[False, False, False, False, False, False, False, False, False],
                                     [False, False, False, False, False, False,  True, False, False],
                                     [False, False, False, False, False, False, False, False, False],
                                     [False, False, False, False, False, False, False, False, False],
                                     [False, False, False, False, False, False, False, False,  True],
                                     [False, False, False, False, False, False, False, False, False],
                                     [False, False, False, False, False, False, False, False, False],
                                     [False, False, False, False, False, False, False, False, False],
                                     [False, False, False, False, False, False, False, False, False]],
 
                                    [[False, False, False, False, False, False, False, False, False],
                                     [False, False, False, False, False, False, False, False, False],
                                     [False, False, False, False, False, False, False,  True, False],
                                     [False, False, False, False, False, False,  True, False, False],
                                     [ True, False, False, False, False, False, False, False, False],
                                     [False, False, False, False, False, False, False, False, False],
                                     [False, False, False, False, False, False, False, False, False],
                                     [False, False, False, False, False, False, False, False, False],
                                     [False, False, False, False, False, False, False, False, False]],
 
                                    [[False, False, False, False,  True, False, False, False, False],
                                     [False, False, False, False, False, False, False, False, False],
                                     [False,  True, False, False, False, False, False, False, False],
                                     [False, False, False, False, False, False, False, False, False],
                                     [False, False, False, False, False, False, False, False, False],
                                     [False, False, False, False, False, False, False, False, False],
                                     [False, False, False, False, False, False, False, False, False],
                                     [False, False,  True, False, False, False, False, False, False],
                                     [False, False, False, False, False, False, False, False, False]],
 
                                    [[False, False, False, False, False, False, False,  True, False],
                                     [False, False,  True, False, False, False, False, False, False],
                                     [False, False, False, False, False, False, False, False, False],
                                     [False, False, False, False, False, False, False, False, False],
                                     [False, False, False, False, False, False, False, False, False],
                                     [False, False, False, False, False, False, False, False, False],
                                     [False,  True, False, False, False, False, False, False, False],
                                     [False, False, False, False, False, False,  True, False, False],
                                     [False, False, False, False, False,  True, False, False, False]],
 
                                    [[False, False, False, False, False, False, False, False, False],
                                     [False, False, False, False, False, False, False, False, False],
                                     [False, False, False, False,  True, False, False, False, False],
                                     [False, False, False, False, False, False, False, False, False],
                                     [False, False, False, False, False, False, False, False, False],
                                     [False, False, False, False, False, False, False, False, False],
                                     [False, False, False, False, False, False, False, False, False],
                                     [False, False, False, False, False, False, False, False, False],
                                     [False, False, False,  True, False, False, False, False, False]],
 
                                    [[False, False, False, False, False,  True, False, False, False],
                                     [False, False, False, False, False, False, False, False,  True],
                                     [False, False, False, False, False, False, False, False, False],
                                     [False, False, False, False,  True, False, False, False, False],
                                     [False, False, False, False, False, False, False, False, False],
                                     [False, False,  True, False, False, False, False, False, False],
                                     [False, False, False, False, False, False, False, False, False],
                                     [False, False, False, False, False, False, False, False, False],
                                     [False, False, False, False, False, False, False, False, False]],
 
                                    [[False, False, False,  True, False, False, False, False, False],
                                     [False, False, False, False, False, False, False, False, False],
                                     [False, False, False, False, False, False, False, False, False],
                                     [False, False, False, False, False, False, False, False, False],
                                     [False, False, False, False, False, False, False, False, False],
                                     [False, False, False, False, False, False, False, False, False],
                                     [False, False, False, False, False, False, False, False, False],
                                     [ True, False, False, False, False, False, False, False, False],
                                     [False, False, False, False,  True, False, False, False, False]],
 
                                    [[False, False, False, False, False, False, False, False, False],
                                     [False, False, False, False, False, False, False, False, False],
                                     [False, False, False, False, False, False, False, False, False],
                                     [False, False, False, False, False, False, False, False, False],
                                     [False, False, False, False, False, False, False, False, False],
                                     [False, False, False, False, False, False, False, False, False],
                                     [False, False, False, False,  True, False, False, False, False],
                                     [False, False, False, False, False, False, False, False, False],
                                     [False, False, False, False, False, False, False, False, False]]])

example_box_sudoku = ([[0, 0, 0, 0, 0, 5, 0, 4, 0],
                       [8, 4, 7, 0, 0, 0, 0, 6, 0],
                       [0, 5, 0, 2, 0, 7, 0, 3, 0],
                       [0, 0, 0, 3, 0, 0, 0, 0, 7],
                       [0, 7, 0, 0, 0, 0, 0, 1, 0],
                       [3, 0, 0, 0, 0, 2, 0, 0, 0],
                       [0, 5, 0, 8, 0, 4, 0, 1, 0],
                       [0, 9, 0, 0, 0, 0, 6, 8, 5],
                       [0, 1, 0, 5, 0, 0, 0, 0, 0]])


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
        
    def test999_end_to_end(self):
        np.testing.assert_equal(
            sud.abstract_array(sud.array_to_int(
                    sud.from_one_line(sud.load('test001_load.txt'))
                )),
            example_sudoku3d_bool
        )

        
if __name__ == '__main__':
        pdb.set_trace()
        unittest.main()
