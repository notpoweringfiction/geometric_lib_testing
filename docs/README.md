__**Table of contents:**__
1. [Description](#overall-description)
2. [Files](#files)
    * [circle.py](#circlepy)
    * [rectangle.py](#rectanglepy)
    * [square.py](#squarepy)
    * [triangle.py](#trianglepy)
    
3. [Commits Logs](#commits-logs)\
<br>
# Description
This geometric library's main goal is to provide functions and tools to get certain values of geometric figures, including circles, triangles and rectangles. For more detailed description of each, check the [**Files**](#files) section.

## Files
- ### circle.py
    Consists of 2 functions: `area(radius : float)` and `perimeter(radius : float)`.
    First returns area of a circle depending on given radius as argument, second one returns perimeter of circle with given radius as argument.
    #### Example:
    ```
    area(5)
    # returns 25 * pi

    perimeter(5)
    # returns 10 * pi
    ```
- ### rectangle.py
    Consists of 2 functions: `area(a : float, b : float)` and `perimeter(a : float, b : float)`.
    First returns area of a rectangle depending on given sides as argument, second one returns perimeter of a rectangle with given adjacent sides as argument.

    #### Example:
    ```
    area(5, 2)
    # returns 10

    perimeter(10, 2)
    # returns 24
    ```
- ### square.py
    Consists of 2 functions: `area(a : float)` and `perimeter(a : float)`.
    First returns area of a square depending on given side as argument, second one returns perimeter of a square with given side as argument.
    #### Example:
    ```
    area(3)
    # returns 9

    perimeter(7)
    # returns 28
    ```
- ### triangle.py
    Consists of 2 functions: `area(a : float, h : float)` and `perimeter(a : float, b : float, c : float)`.
    First returns area of a right triangle depending on given cathetus and hypotenuse as arguments, second one returns perimeter of a right triangle with given sides as arguments.
    #### Example:
    ```
    area(2, 5)
    # returns 5

    perimeter(1, 2, 5)
    # returns 8
    ```

## Commits Logs

### Commit 9fab72e2a38a531483476b4131c8db47c2132a93 
(HEAD -> new_features_356089) <br>
Author: LamaDevGuy <86229883+LamaDevGuy@users.noreply.github.com> <br>
Date:   Fri Sep 19 14:10:39 2025 +0300
```
    Fixed perimeter calculation in 'rectangle.py' file.
```
    
### Commit 859fa1b88fc4afa29c0f9b884fbfd95f4f64cf3e
Author: LamaDevGuy <86229883+LamaDevGuy@users.noreply.github.com> <br>
Date:   Fri Sep 19 14:07:43 2025 +0300
```
    Added new 'rectangle.py' file.
```