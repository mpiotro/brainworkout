# The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a Monte Carlo method.

# Hint: The basic equation of a circle is x2 + y2 = r2.

import random


def estimate_pi(iterations: int):
    in_circle = 0

    for _ in range(iterations):
        x, y = random.uniform(-1, 1), random.uniform(-1, 1)

        distance_to_origin = x**2 + y**2
        if distance_to_origin <= 1:
            in_circle += 1

    pi_over_four = in_circle / iterations
    return pi_over_four * 4


print(estimate_pi(iterations=100000000))
