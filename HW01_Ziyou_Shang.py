"""
author: Ziyou Shang
This is a program that takes the length of sides of triangles and
classify the triangles as equilateral triangles, isosceles triangles, scalene triangles,
and right triangles
"""


def classify_triangle(a, b, c):
    """ This is the function that classifies triangles """

    try:      # check invalid input
        s1 = float(a)
        s2 = float(b)
        s3 = float(c)
    except ValueError as e:
        print(e)
        return "Error"

    if s1 <= 0 or s2 <= 0 or s3 <= 0:     # check for invalid length
        raise ValueError("Invalid side length.")

    result = "scalene"
    if s1 == s2 == s3:
        result = "equilateral"      # classify triangles by length of sides
    elif s1 == s2 or s2 == s3 or s1 == s3:
        result = "isosceles"

    if round((s1 ** 2) + (s2 ** 2), 2) == round((s3 ** 2), 2) or \
            round((s1 ** 2) + (s3 ** 2), 2) == round((s2 ** 2), 2) or \
            round((s2 ** 2) + (s3 ** 2), 2) == round((s1 ** 2), 2):
        result += " right triangle"     # check for right triangles
    else:
        result += " triangle"

    return result


def main():
    """ The main function (basically to get the input) """

    a = input("Length of side1: ")
    b = input("length of side2: ")
    c = input("length of side3: ")
    result = classify_triangle(a, b, c)
    print(f"The triangle is {result}.")

if __name__ == '__main__':
    main()