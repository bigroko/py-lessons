# -*- coding: UTF-8 -*-

import math
import cmath


# Coefficients, where a, b and c are real numbers and a != 0
# For two distinct real roots: a, b, c = 1, 5, 6  (x1 = -2.0, x2 = -3.0)
# For one real root: a, b, c = 1, 4, 4  (x1 = -2.0)
# For two distinct complex roots: a, b, c = 1, 4, 6
#     (x1 = (-2+1.4142135623730951j), x2 = (-2-1.4142135623730951j))
a, b, c = 1, 5, 6
# Roots
x1, x2 = None, None
# Text message
text = None
# Discriminant
d = b**2 - 4*a*c

if d > 0:
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    text = "Two real roots: x1 = {}, x2 = {}".format(x1, x2)
elif d == 0:
    x1 = -b / (2*a)
    text = "One real root: x1 = {}".format(x1)
else:
    x1 = (-b + cmath.sqrt(d)) / (2 * a)
    x2 = (-b - cmath.sqrt(d)) / (2 * a)
    text ="No real roots, two complex ones: x1 = {}, x2 = {}".format(x1, x2)

print("Quadratic equation: {}x**2 + {}x + {} = 0".format(a, b, c))
print("Discriminant = {}. {}.".format(d, text))
