# Basic physics formulas

def speed(distance, time):
    return distance / time

def force(mass, acceleration):
    return mass * acceleration

def density(mass, volume):
    return mass / volume

if __name__ == "__main__":
    print("=== Physics Tools ===")
    d = float(input("Distance (m): "))
    t = float(input("Time (s): "))
    print("Speed:", speed(d, t), "m/s")

    m = float(input("\nMass (kg): "))
    a = float(input("Acceleration (m/s^2): "))
    print("Force:", force(m, a), "N")