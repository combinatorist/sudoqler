# soduqler
> ... because a 2D sudoku puzzle is really just a 3D boolean array (with a view).

As far as I know, I'm the only person to come up with this alternate data structure. Of course, there may be other independent discoveries of it, but mine wasn't based on anyone else's work.

## Abstract Data Stucture
The regular 2 dimensions are rows and columns, with a number in each field. Now imagine, stacking 9 layers (one for each number) on top of each other to get a 9 x 9 x 9. Then, in each layer, mark True where the number represented by that layer appeared in the original 2D puzzle and leave the rest undetermined. Now, for any row and column position, you could "look down" through the layers and see at most one True and it should be in the layer corresponding to the original number.

In addition, the boxes in the puzzle act like a pseudo 4th dimension, but since they are determined by row and column, we handle them as a view. In other words, we evaluate the same rules on the box view as we do a row, column, or number, but the updates are applied to the 3 dimensional array, not duplicated per box. Also, for curiosity, notice that when you rearrange cells into boxes (as rows in the view), then the positions in those boxes (columns in the view) become another, unused dimension. They are rare, but you can play a [version of sudoku][Colour Sudoku] where the positions in the box must also be unique by number.

Hence:
```
                      +----- column (7)
                      |
                      v
+---------+---------+---------+
| _  _  _ | 8  4  7 | _  5  _ |
| _  _  5 | _  3  _ | 2  _  7 |
| _  4  _ | _  6  _ | _  3  _ |
+---------+---------+---------+
| _  _  _ | _  7  _ | 3  _  _ |
| 3  _  _ | _  5  _ | _  _  2 |
| _  _  7 | _  1  _ | _  _  _ |
+---------+---------+---------+
| _  5  _ | _  9  _ | _  1  _ |
| 8  _  4 | _  2  _ | 5  _  _ | <- row (2)
| _  1  _ | 6  8  5 | _  _  _ |
+---------+---------+---------+
                         |
                         *     +---------+
                          \    | _  1  _ |
                           *-> | 5  _  _ |  <- "box" (9)
                               | _  _  _ |
                               +---------+

1 2 3 4 5 6 7 8 9
        ^
        |
        +----- number (5)
```
becomes:
```
        +---- row
        |     +------- number
        |     |
        v     v
True @ [8, 7, 5, 9] in a 4 dimensional array (hard to visualize)
           ^     ^
           |     |
           |     +-----------box
           +--- column
```

## Rules

When you look at it this way, you can do a lot with just two rules:
- `deduce`: Mark undetermined fields False if they are in line with a True (in any dimension).
- `eliminate`: Mark an undetermined field True if the rest of the fields in one of their dimensions are all False.

### "Deduce"
A single True drives multiple Falses.
```
(Only visualising 2 dimensions of the boolean array: rows and columns for the number 5)
+---------+---------+---------+
| _  _  _ | _  _  _ | 0  1  _ |
| _  _  1 | _  _  _ | 0  _  _ |
| _  _  _ | _  _  _ | 0  _  _ |
+---------+---------+---------+
| _  _  _ | _  _  _ | 0  _  _ |
| _  _  _ | _  1  _ | 0  _  _ |
| _  _  _ | _  _  _ | 0  _  _ |
+---------+---------+---------+
| _  1  _ | _  _  _ | 0  _  _ |
| 0  0  0 | 0  0  0 | 1  0  0 | <- a True (1) makes rest of row False (0)
| _  _  _ | _  _  1 | 0  _  _ |
+---------+---------+---------+
                      ^
                      |
                      +------ a True (1) makes rest of column False (0)
```
In other words, the since the 7th column and 8th row is a 5, there can be no other 5's in that row or column.

### "Eliminate"
This is similar to Deduce, but it takes multiple Falses to get a single True.
```
(Boolean array of rows and columns for the number 6)
+---------+---------+---------+
| 0  0  0 | 0  0  0 | _  0  0 | <- the only position in the row that wasn't False, must be True
| _  _  _ | _  _  _ | _  _  _ |
| _  _  _ | _  _  _ | _  _  _ |
+---------+---------+---------+
| _  _  _ | _  _  _ | _  _  _ |
| _  _  _ | _  _  _ | _  _  _ |
| _  _  _ | _  _  _ | _  _  _ |
+---------+---------+---------+
| _  _  _ | _  _  _ | _  _  _ |
| _  _  _ | _  _  _ | _  _  _ |
| _  _  _ | _  _  _ | _  _  _ |
+---------+---------+---------+
```
In other words, of the entire 1st row, only the 7th column could be a 6, so it must be.

[Colour Sudoku]: http://www.sudokuwiki.org/A_Perfect_Sudoku
