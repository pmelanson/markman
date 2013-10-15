markman
=======

This program takes an input of a properly-formatted *.csv file that contains
student marks, then appends a course average and total average to each student record.

Format
------

```
[anything]
Type,[header],[O.Ax],[Sx],[Ex]
[data],[data],[level],[level],[level]
[data],[data],[level],[level],[level]
[nothing should come after the table of records]
```

`[anything]`: the beginning of the spreadsheet, precedes the header row. Can
include anything *but* a row whose first cell is "Type", like the header row.

`Type`: case-insensitive and whitespace padding-insensitive. This cell marks
the beginning of the header row.
 
`[header]`: any headers that do not begin with `O.A`, `S` or `E`. Data in
these columns will be ignored.

`[O.Ax]`: a header cell that shows which column contains a mark for a unit.
The `x` denotes which unit. For example, `O.A2` means this column contains
marks for unit 2.

`[Sx]`: like O.A, but for summatives.

`[Ex]`: like O.A, but for exams.

`[data]`: can be anything, this is ignored.

`[level]`: this is a level for the unit, exam, or summative. The levels use
the following conversions to percentage points:

    A: [no mark],
    [nothing]: [no mark]
    R-: 25, R: 35, R+: 45,
    1-: 52, 1: 55, 1+: 58,
    2-: 62, 2: 65, 2+: 68,
    3-: 72, 3: 75, 3+: 78,
    4--: 80, 4-: 85, 4: 90, 4+: 95, 4++: 100,
    5: 100

The reverse of any mark is also valid. For example, `--4` and `4--` are equivalent.

Calculation
-----------

### Exam mark substitution

If the exam mark for a unit is higher than the course mark for a unit, the
average calculations will use the exam mark for that unit instead of the
course mark. The reverse is not true. For example, if a student has

    O.A1,   E2
    2-,     5

The course mark will be replaced by a `5`, giving:

    O.A1,   E2, "Course Ave",   "Total Ave"
    2-,     5,  100,            100

However, the exam mark cannot be replaced by a course mark. For example, if a
student has

    O.A1,   E2
    5,      1-

The result will be:

    O.A1,   E2, "Course Ave",   "Total Ave"
    4++,    1-, 100,            76

### Summative and Exam

The summative and exam must both have at least one mark each to be counted.
For example:

    O.A1,   S1, E1, "Course Ave",   "Total Ave"
    3+      5,  A,  78,             78

Notice how the summative mark was not counted in calculating the total average,
since the exam had no mark (an `A`). If we were to give the exam a mark, this
would be the result:

    O.A1,   S1, E1, "Course Ave",   "Total Ave"
    3+      5,  5,  100,             100

Note that the summative mark now counts, in addition to the new exam mark. Also
note how the mark in `O.A1` was replaced by the mark in `E1`, as explained in
the **Exam mark substitution**.

Attribution
===========

Created by Patrick Melanson, 2013

Contact: patrick.melanstone@gmail.com

Licensed under the MIT license. See accompanying LICENSE file
