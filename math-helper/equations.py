# Solves common mathematics equations

import math

def quadratic(a, b, c):
    """Returns solutions to ax^2 + bx + c = 0"""
    discriminant = b**2 - 4*a*c

    if discriminant < 0:
        return "No real roots"
    
    x1 = (-b + math.sqrt(discriminant)) / (2*a)
    x2 = (-b - math.sqrt(discriminant)) / (2*a)
      
    return x1, x2

if __name__ == "__main__":
    print("=== Quadratic Solver ===")
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))

    print("Solutions:", quadratic(a, b, c))