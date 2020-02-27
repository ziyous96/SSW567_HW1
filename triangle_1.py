"""
author: Ziyou Shang
This is a program that takes the length of sides of triangles and
classify the triangles as equilateral triangles, isosceles triangles, scalene triangles,
and right triangles
"""


def classify_triangle(i_1, i_2, i_3):
    """ This is the function that classifies triangles """

    try:      # check invalid input
        s_1 = float(i_1)
        s_2 = float(i_2)
        s_3 = float(i_3)
    except ValueError as e_1:
        print(e_1)
        return "Error"

    if s_1 <= 0 or s_2 <= 0 or s_3 <= 0:     # check for invalid length
        raise ValueError("Invalid side length.")

    if s_1 + s_2 <= s_3 or s_1 + s_3 <= s_2 or s_2 + s_3 <= s_1:    # check for valid triangle
        raise ValueError("Invalid triangle")

    result = "scalene"
    if s_1 == s_2 == s_3:
        result = "equilateral"      # classify triangles by length of sides
    elif s_1 == s_2 or s_2 == s_3 or s_1 == s_3:
        result = "isosceles"

    if round((s_1 ** 2) + (s_2 ** 2), 2) == round((s_3 ** 2), 2) or \
            round((s_1 ** 2) + (s_3 ** 2), 2) == round((s_2 ** 2), 2) or \
            round((s_2 ** 2) + (s_3 ** 2), 2) == round((s_1 ** 2), 2):
        result += " right triangle"     # check for right triangles
    else:
        result += " triangle"

    return result
