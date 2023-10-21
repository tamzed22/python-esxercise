"""
#1.Write a program that asks your name and then greets you by your name
# Get the user's name as input
name = input("Please enter your name: ")

# Print the greeting
print("Hello, " + name + "!")


#2.Write a program that asks the user for the radius of a circle and the prints out the area of the circle.
import math

# Ask the user for the radius
radius = float(input("Please enter the radius of the circle: "))

# Calculate the area of the circle
area = math.pi * radius**2

# Print the result
print("The area of the circle with a radius of", radius, "is", area)

#3.Write a program that asks the user for the length and width of a rectangle. The program then prints out the perimeter and area of the rectangle. The perimeter of a rectangle is the sum of the lengths of each four sides.

# Ask the user for the length and width of the rectangle
length = float(input("Please enter the length of the rectangle: "))
width = float(input("Please enter the width of the rectangle: "))

# Calculate the perimeter and area of the rectangle
perimeter = 2 * (length + width)
area = length * width

# Print the results
print("The perimeter of the rectangle is:", perimeter)
print("The area of the rectangle is:", area)

#4.Write a program that asks the user for three integer numbers. The program prints out the sum, product, and average of the numbers.
# Ask the user for three integer numbers
num1 = int(input("Please enter the first integer number: "))
num2 = int(input("Please enter the second integer number: "))
num3 = int(input("Please enter the third integer number: "))

# Calculate the sum, product, and average
sum_numbers = num1 + num2 + num3
product_numbers = num1 * num2 * num3
average = sum_numbers / 3

# Print the results
print("The sum of the numbers is:", sum_numbers)
print("The product of the numbers is:", product_numbers)
print("The average of the numbers is:", average)

#5.Write a program that asks the user to enter a mass in medieval units: talents (leiviskä), pounds (naula), and lots (luoti). The program converts the input to full kilograms and grams and outputs the result to the user:

# Constants for conversion
POUNDS_PER_TALENT = 20
LOTS_PER_POUND = 32
GRAMS_PER_LOT = 13.3

# Ask the user to enter mass in medieval units
talents = float(input("Enter the number of talents: "))
pounds = float(input("Enter the number of pounds: "))
lots = float(input("Enter the number of lots: "))

# Calculate the total mass in grams
total_grams = (talents * POUNDS_PER_TALENT * LOTS_PER_POUND * GRAMS_PER_LOT) + (pounds * LOTS_PER_POUND * GRAMS_PER_LOT) + (lots * GRAMS_PER_LOT)

# Convert to kilograms and grams
kilograms = int(total_grams // 1000)
grams = total_grams % 1000

# Print the result
print(f"The mass is {kilograms} kilograms and {grams} grams.")

# 6.Write a program that draws two random combinations of numbers for a combination lock:
#a 3-digit code where each number is between 0 and 9.
#a 4-digit code where each number is between 1 and 6.
import random

# Generate a random 3-digit combination
combination_3_digit = ""
for _ in range(3):
    digit = random.randint(0, 9)
    combination_3_digit += str(digit)

# Generate a random 4-digit combination
combination_4_digit = ""
for _ in range(4):
    digit = random.randint(1, 6)
    combination_4_digit += str(digit)

# Print the combinations
print("Random 3-digit combination:", combination_3_digit)
print("Random 4-digit combination:", combination_4_digit)

#module 3
#1.Write a program that asks a fisher the length of a zander in centimeters. If the zander does not fulfill the size limit, the program instructs to release the fish back into the lake and notifies the user of how many centimeters below the size limit the caught fish was. A zander must be 42 centimeters or longer to meet the size limit.
# Size limit for a zander
size_limit = 42

# Ask the fisher for the length of the zander
zander_length = float(input("Enter the length of the zander in centimeters: "))

# Check if the zander meets the size limit
if zander_length >= size_limit:
    print("Congratulations! You can keep the zander.")
else:
    difference = size_limit - zander_length
    print(f"The zander is {difference} centimeters below the size limit.")
    print("Please release the fish back into the lake.")

#2.Write a program that asks the user to enter the cabin class of a cruise ship and then prints out a written description according to the list below. You must use an if/elif/else structure in your solution.

#LUX: upper-deck cabin with a balcony.
#A: above the car deck, equipped with a window.
#B: windowless cabin above the car deck.
#C: windowless cabin below the car deck.
# Ask the user to enter the cabin class
cabin_class = input("Enter the cabin class (LUX, A, B, or C): ")

# Determine the description based on the cabin class
if cabin_class == "LUX":
    description = "Upper-deck cabin with a balcony."
elif cabin_class == "A":
    description = "Above the car deck, equipped with a window."
elif cabin_class == "B":
    description = "Windowless cabin above the car deck."
elif cabin_class == "C":
    description = "Windowless cabin below the car deck."
else:
    description = "Invalid cabin class."

# Print the description
print(description)

#3.Write a program that asks for the biological gender and hemoglobin value (g/l). The program the notifies the user if the hemoglobin value is low, normal or high.

#A normal hemoglobin value for adult females is between 117-155 g/l.
#A normal hemoglobin value for adult males is between 134-167 g/l.

# Ask the user for biological gender and hemoglobin value
gender = input("Enter your biological gender (male or female): ").lower()
hemoglobin_value = float(input("Enter your hemoglobin value (g/l): "))

# Define the normal hemoglobin ranges for males and females
normal_ranges = {
    "male": (134, 167),
    "female": (117, 155)
}

# Check if the entered gender is valid
if gender not in normal_ranges:
    print("Invalid gender.")
else:
    # Get the normal range for the entered gender
    min_range, max_range = normal_ranges[gender]

    # Determine if the hemoglobin value is low, normal, or high
    if hemoglobin_value < min_range:
        print("Hemoglobin is low.")
    elif min_range <= hemoglobin_value <= max_range:
        print("Hemoglobin is normal.")
    else:
        print("Hemoglobin is high.")


#4.Write a program that asks the user to enter a year and notifies the user whether the input year is a leap year. A year is a leap year if it is divisible by four. However, years divisible by 100 are leap years only if they are also divisible by 400.
# Ask the user to enter a year
year = int(input("Enter a year: "))

# Check if it's a leap year
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")

#Module 4
#1.Write a program that uses a while loop to print out all numbers divisible by three in the range of 1-1000.
# Initialize a variable to start from 1
number = 1

# Use a while loop to iterate through numbers
while number <= 1000:
    if number % 3 == 0:
        print(number)
    number += 1

#2.Write a program that converts inches to centimeters until the user inputs a negative value. Then the program ends.
# Conversion factor from inches to centimeters
INCH_TO_CM = 2.54

while True:
    # Ask the user for inches
    inches = float(input("Enter a length in inches (or a negative value to quit): "))

    # Check if the input is negative to end the program
    if inches < 0:
        print("Program ended.")
        break

    # Convert inches to centimeters
    centimeters = inches * INCH_TO_CM

    # Print the result
    print(f"{inches} inches is equal to {centimeters} centimeters")

#3.Write a program that asks the user to enter numbers until they enter an empty string to quit. Finally, the program prints out the smallest and largest number from the numbers it received.
# Initialize variables for smallest and largest numbers
smallest = None
largest = None

# Loop to receive input from the user
while True:
    user_input = input("Enter a number (or press Enter to quit): ")

    # Check if the input is an empty string to quit the loop
    if user_input == "":
        break

    try:
        number = float(user_input)
        # Update smallest and largest numbers
        if smallest is None or number < smallest:
            smallest = number
        if largest is None or number > largest:
            largest = number
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Print the smallest and largest numbers
if smallest is not None and largest is not None:
    print("Smallest number entered:", smallest)
    print("Largest number entered:", largest)
else:
    print("No valid numbers were entered.")

#4.Write a game where the computer draws a random integer between 1 and 10. The user tries to guess the number until they guess the right number. After each guess the program prints out a text: Too high, Too low or Correct. Notice that the computer must not change the number between guesses.
import random

# Generate a random number between 1 and 10
target_number = random.randint(1, 10)

# Initialize the user's guess
user_guess = None

# Main game loop
while user_guess != target_number:
    # Ask the user to enter a guess
    try:
        user_guess = int(input("Guess the number (between 1 and 10): "))
        if user_guess < 1 or user_guess > 10:
            print("Please enter a valid number between 1 and 10.")
            continue
    except ValueError:
        print("Please enter a valid number.")
        continue

    # Check if the guess is correct
    if user_guess < target_number:
        print("Too low")
    elif user_guess > target_number:
        print("Too high")
    else:
        print("Correct! You guessed the number:", target_number)

#5.Write a program that asks the user for a username and password. If either or both are incorrect, the program ask the user to enter the username and password again. This continues until the login information is correct or wrong credentials have been entered five times. If the information is correct, the program prints out Welcome. After five failed attempts the program prints out Access denied. The correct username is python and password rules.


# Define the correct username and password
correct_username = "python"
correct_password = "rules"

# Initialize variables for login attempts and logged in status
attempts = 0
logged_in = False

# Loop for login attempts
while attempts < 5 and not logged_in:
    # Ask the user for username and password
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Check if the username and password are correct
    if username == correct_username and password == correct_password:
        print("Welcome")
        logged_in = True
    else:
        print("Incorrect username or password. Please try again.")
        attempts += 1

# After the loop, check if the user is not logged in
if not logged_in:
    print("Access denied")

#6.
import random

# Ask the user for the number of random points to generate
num_points = int(input("Enter the number of random points to generate: "))

# Initialize a counter for points inside the circle
points_inside_circle = 0

# Generate random points and check if they are inside the circle
for _ in range(num_points):
    x = random.uniform(-1, 1)  # Random x-coordinate between -1 and 1
    y = random.uniform(-1, 1)  # Random y-coordinate between -1 and 1

    if x**2 + y**2 < 1:  # Check if the point is inside the circle
        points_inside_circle += 1

# Calculate the approximate value of pi
approx_pi = 4 * points_inside_circle / num_points

# Print the approximation of pi
print(f"Approximation of pi: {approx_pi}")

#Module 5
#1.Write a program that asks the user how many dice to roll. The program rolls all the dice once and prints out the sum of the numbers. Use a for loop.


import random

# Ask the user for the number of dice to roll
num_dice = int(input("Enter the number of dice to roll: "))

# Initialize a variable to store the sum
total_sum = 0

# Roll the dice using a for loop
for _ in range(num_dice):
    # Generate a random number between 1 and 6 (simulating a dice roll)
    dice_roll = random.randint(1, 6)
    print(f"Die {_ + 1}: {dice_roll}")
    total_sum += dice_roll

# Print the sum of the dice rolls
print(f"Total sum: {total_sum}")

#2.
# Initialize an empty list to store the numbers
numbers = []

# Loop to receive input from the user
while True:
    user_input = input("Enter a number (or press Enter to quit): ")

    # Check if the input is an empty string to quit the loop
    if user_input == "":
        break

    try:
        number = float(user_input)
        numbers.append(number)
    except ValueError:
        print("Please enter a valid number.")

# Sort the list of numbers in descending order
numbers.sort(reverse=True)

# Print the five greatest numbers
if len(numbers) > 0:
    print("The five greatest numbers (in descending order):")
    for i, num in enumerate(numbers[:5]):
        print(f"{i + 1}: {num}")
else:
    print("No valid numbers were entered.")

#3.
# Ask the user for an integer
num = int(input("Enter an integer: "))

# Check if the number is less than 2
if num < 2:
    is_prime = False
else:
    is_prime = True
    # Check for factors from 2 to the square root of the number
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

# Print the result
if is_prime:
    print(num, "is a prime number.")
else:
    print(num, "is not a prime number.")

#4.
# Initialize an empty list to store city names
cities = []

# Use a for loop to ask the user for city names
for i in range(5):
    city = input(f"Enter the name of city {i+1}: ")
    cities.append(city)

# Use a for/in loop to iterate through the list and print the city names
print("City names:")
for city in cities:
    print(city)

#Module 6
#1.
import random

# Define a function to simulate a dice roll
def roll_dice():
    return random.randint(1, 6)

# Main program to roll the dice until the result is 6
while True:
    result = roll_dice()
    print("Dice roll:", result)
    if result == 6:
        break


#2.
import random

# Define a function to simulate a dice roll with a specified number of sides
def roll_dice(num_sides):
    return random.randint(1, num_sides)

# Ask the user for the maximum number on the dice
max_number = int(input("Enter the maximum number on the dice: "))

# Main program to roll the dice until the maximum number is rolled
while True:
    result = roll_dice(max_number)
    print("Dice roll:", result)
    if result == max_number:
        break

#3.
# Define a function to convert gallons to liters
def gallons_to_liters(gallons):
    liters = gallons * 3.78541  # Conversion factor
    return liters


# Main program to convert gallons to liters
while True:
    # Ask the user for a volume in gallons
    gallons = float(input("Enter a volume in American gallons (or a negative value to quit): "))

    # Check if the input is negative to quit the program
    if gallons < 0:
        break

    # Convert the volume to liters using the function
    liters = gallons_to_liters(gallons)

    # Print the result
    print(f"{gallons} American gallons is equal to {liters} liters")

#4.
# Define a function to calculate the sum of a list of integers
def sum_of_list(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

# Main program to test the function
if __name__ == "__main__":
    # Create a list of integers
    integer_list = [3, 5, 7, 9, 11]

    # Call the function to calculate the sum
    result = sum_of_list(integer_list)

    # Print the result
    print("Sum of the list:", result)
#5.
# Define a function to remove odd numbers from a list of integers
def remove_odd_numbers(input_list):
    # Use list comprehension to create a new list without odd numbers
    filtered_list = [num for num in input_list if num % 2 == 0]
    return filtered_list

# Main program to test the function
if __name__ == "__main__":
    # Create a list of integers
    integer_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Call the function to remove odd numbers from the list
    filtered_list = remove_odd_numbers(integer_list)

    # Print the original list
    print("Original list:", integer_list)

    # Print the modified list with odd numbers removed
    print("List with odd numbers removed:", filtered_list)

#6.
# Define a function to calculate unit price per square meter
def calculate_unit_price(diameter, price):
    radius = diameter / 2
    area = 3.14159 * (radius ** 2)  # Calculate area of the pizza in square centimeters
    unit_price = price / area * 10000  # Convert unit price to euros per square meter
    return unit_price

# Main program
if __name__ == "__main__":
    # Ask the user for the diameter and price of the first pizza
    diameter1 = float(input("Enter the diameter of the first pizza (in cm): "))
    price1 = float(input("Enter the price of the first pizza (in euros): "))

    # Ask the user for the diameter and price of the second pizza
    diameter2 = float(input("Enter the diameter of the second pizza (in cm): "))
    price2 = float(input("Enter the price of the second pizza (in euros): "))

    # Calculate unit prices using the function
    unit_price1 = calculate_unit_price(diameter1, price1)
    unit_price2 = calculate_unit_price(diameter2, price2)

    # Determine and print which pizza provides better value for money
    if unit_price1 < unit_price2:
        print("The first pizza provides better value for money.")
    elif unit_price1 > unit_price2:
        print("The second pizza provides better value for money.")
    else:
        print("Both pizzas have the same unit price.")

#module 7
#1
def get_season(month_number):
    # Define the seasons as three-month intervals
    seasons = ('talvi', 'kevät', 'kesä', 'syksy')

    # Map months to seasons based on the index
    season_index = (month_number - 1) // 3
    season = seasons[season_index]

    return season

def main():
    try:
        month_number = int(input("Enter the number of the month (1-12): "))
        if 1 <= month_number <= 12:
            season = get_season(month_number)
            print(f"The corresponding season is {season}.")
        else:
            print("Invalid input. Please enter a number between 1 and 12.")
    except ValueError:
        print("Invalid input. Please enter a valid number between 1 and 12.")

if __name__ == "__main__":
    main()

#2.
def main():
    names = []

    while True:
        name = input("Enter a name (or press Enter to finish): ")

        if name == "":
            break  # Exit the loop if an empty string is entered

        if name in names:
            print("Aiemmin syötetty nimi")
        else:
            print("Uusi nimi")

        names.append(name)

    print("Entered names:")
    for name in names:
        print(name)

if __name__ == "__main__":
    main()

#3.
# Dictionary to store airport information (ICAO code as the key and airport name as the value)
airport_info = {}


def add_airport():
    icao_code = input("Enter the ICAO code of the airport: ")
    airport_name = input("Enter the name of the airport: ")
    airport_info[icao_code] = airport_name
    print(f"Airport information for {icao_code} ({airport_name}) has been added.")


def retrieve_airport():
    icao_code = input("Enter the ICAO code of the airport you want to retrieve: ")
    if icao_code in airport_info:
        print(f"The name of the airport with ICAO code {icao_code} is {airport_info[icao_code]}.")
    else:
        print(f"No information found for ICAO code {icao_code}.")


def main():
    while True:
        print("Options:")
        print("1. Add a new airport")
        print("2. Retrieve airport information")
        print("3. Stop")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            add_airport()
        elif choice == "2":
            retrieve_airport()
        elif choice == "3":
            print("Program is stopping.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()

#Module 8
#1.
import sqlite3

# Connect to the SQLite database containing airport information
conn = sqlite3.connect("airport_database.db")
cursor = conn.cursor()


def search_airport(icao_code):
    # Define the SQL query to retrieve airport information based on ICAO code
    query = "SELECT name, location FROM airport WHERE ident = ?"

    # Execute the query with the given ICAO code
    cursor.execute(query, (icao_code,))

    # Fetch the result
    result = cursor.fetchone()

    if result:
        name, location = result
        print(f"Airport Name: {name}")
        print(f"Location: {location}")
    else:
        print("Airport not found for the given ICAO code.")


def main():
    while True:
        icao_code = input("Enter the ICAO code of the airport (or 'q' to quit): ")

        if icao_code.lower() == 'q':
            break

        search_airport(icao_code)


if __name__ == "__main__":
    main()

# Close the database connection
conn.close()

#2.
import sqlite3

# Connect to the SQLite database containing airport information
conn = sqlite3.connect("airport_database.db")
cursor = conn.cursor()


def count_airports_by_type(country_code):
    # Define the SQL query to count airports by type for the given country code
    query = """
    SELECT type, COUNT(*) FROM airport 
    WHERE iso_country = ? 
    GROUP BY type 
    ORDER BY type
    """

    # Execute the query with the given country code
    cursor.execute(query, (country_code,))

    results = cursor.fetchall()

    if results:
        print(f"Airports in {country_code}:")
        for row in results:
            airport_type, count = row
            print(f"{count} {airport_type} airports")
    else:
        print(f"No airports found for the country code {country_code}.")


def main():
    country_code = input("Enter a country code (e.g., FI): ")

    count_airports_by_type(country_code)


if __name__ == "__main__":
    main()

# Close the database connection
conn.close()

#3.
pip install geopy
from geopy.distance import geodesic
import sqlite3

# Connect to the SQLite database containing airport information
conn = sqlite3.connect("airport_coordinates.db")
cursor = conn.cursor()


def get_airport_coordinates(icao_code):
    # Define the SQL query to retrieve airport coordinates based on ICAO code
    query = "SELECT latitude_deg, longitude_deg FROM airport WHERE ident = ?"

    # Execute the query with the given ICAO code
    cursor.execute(query, (icao_code,))

    result = cursor.fetchone()

    if result:
        latitude, longitude = result
        return (latitude, longitude)
    else:
        print(f"No information found for ICAO code {icao_code}.")
        return None


def calculate_distance_between_airports(icao_code1, icao_code2):
    coords1 = get_airport_coordinates(icao_code1)
    coords2 = get_airport_coordinates(icao_code2)

    if coords1 is not None and coords2 is not None:
        distance = geodesic(coords1, coords2).kilometers
        return distance
    else:
        return None


def main():
    icao_code1 = input("Enter the ICAO code of the first airport: ")
    icao_code2 = input("Enter the ICAO code of the second airport: ")

    distance = calculate_distance_between_airports(icao_code1, icao_code2)

    if distance is not None:
        print(f"The distance between {icao_code1} and {icao_code2} is approximately {distance:.2f} kilometers.")
    else:
        print("Unable to calculate the distance.")


if __name__ == "__main__":
    main()

# Close the database connection
conn.close()
"""