import math

"""
    Calculates the volume of a sphere given its radius

    Parameters:
    radius (float): The radius of the sphere

    Returns:
    float: The volume of the sphere
"""
def calculate_volume(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return (4/3) * math.pi * (radius ** 3)



if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Calculate the volume of a sphere")
    parser.add_argument("radius", type=float, help="The radius of the sphere")
    args = parser.parse_args()

    try:
        volume = calculate_volume(args.radius)
        print(f"The volume of the sphere with radius {args.radius} is {volume}")
    except ValueError as e:
        print(e)
