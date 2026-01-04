## function to integrate: x^3, boundaries a=0, b=2; theoretical value = 4

import random

def f(x):
    return x*x*x

def is_inside(x, y, a, b, f):
    """
    check if point is inside area of interest
    """
    return (a <= x <= b) and (y <= f(x))

def monte_carlo_simulation(a, b, f, num_experiments: int):
    """
    making a series of experiments using Monte-Carlo method
    """
    integral_value_average = 0

    for _ in range(num_experiments):
        # Generate random points
        points = [(random.uniform(a, b), random.uniform(f(a), f(b))) for _ in range(15000)]
        # Select points that are inside the area of interest
        inside_points = [point for point in points if is_inside(point[0], point[1], a, b, f)]

        # Calculate value:
        m = len(inside_points)
        n = len(points)
        integral_value = (m / n) * ((b-a) * (f(b)-f(a)))

        # Adding to average value
        integral_value_average += integral_value

    # Обчислення середньої площі
    integral_value_average /= num_experiments
    return integral_value_average

# Integration boundaries
a = 0
b = 2
theoretical_value = (b**4) / 4 - (a**4) / 4

# Кількість експериментів
num_experiments = 100

# Виконання симуляції
monte_carlo_value = monte_carlo_simulation(a, b, f, num_experiments)
monte_carlo_value_2 = monte_carlo_simulation(a, b, f, 100*num_experiments)
print(f"Theoretical value: {theoretical_value}")
print(f"Average value for {num_experiments} experiments: {monte_carlo_value}")
print(f"Average value for {100*num_experiments} experiments: {monte_carlo_value_2}")
