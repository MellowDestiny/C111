import math
from datetime import datetime

def main():
    # Get user input for tire dimensions
    width = int(input("Enter the width of the tire in mm (ex 205): "))
    aspect_ratio = int(input("Enter the aspect ratio of the tire (ex 60): "))
    diameter = int(input("Enter the diameter of the wheel in inches (ex 15): "))

    # Calculate the tire volume
    volume = (math.pi * (width ** 2) * aspect_ratio * width + 2540 * diameter) / 10000000000

    # Display the volume to the user
    print(f"The approximate volume is {volume:.2f} liters")

    # Get the current date in YYYY-MM-DD format
    current_date = datetime.now().strftime("%Y-%m-%d")

    # Open the volumes.txt file in append mode and write the data
    with open("volumes.txt", "at") as file:
        # Append the current date, tire dimensions, and volume to the file
        file.write(f"{current_date}, {width}, {aspect_ratio}, {diameter}, {volume:.2f}\n")

# Run the program
if __name__ == "__main__":
    main()
