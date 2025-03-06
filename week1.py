import math

def main():
    # Get user input
    width = int(input("Enter the width of the tire in mm (ex 205): "))
    aspect_ratio = int(input("Enter the aspect ratio of the tire (ex 60): "))
    diameter = int(input("Enter the diameter of the wheel in inches (ex 15): "))

    # Apply the formula to calculate the volume
    volume = (math.pi * (width ** 2) * aspect_ratio * width + 2540 * diameter) / 10000000000

    # Display the result, rounded to two decimal places
    print(f"The approximate volume is {volume:.2f} liters")

# Run the program
if __name__ == "__main__":
    main()
