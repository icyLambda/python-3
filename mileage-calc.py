"""
    The program calculates the average mileage of the car depending
    on the year of production and the state of the vehicle.
"""

__author__ = "Dmitrii Vialkov"
__copyright__ = "Copyright 2018, The Dmitrii Vialkov Project"
__credits__ = ["Dmitrii Vialkov", "Anton Vialkov"]
__license__ = "GNU General Public License (GPLv3)"
__version__ = "3.0.0"
__maintainer__ = "Dmitrii Vialkov"
__email__ = "vdv87@hotmail.com"
__status__ = "Production"

# The mileage of the car is calculated using the date of manufacture of the vehicle,
# so we import the "DateTime" module.
import datetime

now_date = datetime.date.today()
cur_year = now_date.year
cur_month = now_date.month
cur_day = now_date.day

welcome_calc_1 = ("=================================="
                  "\n" + "\t" + "I\'m a calculator!" + "\n"
                  "==================================")

welcome_calc_2 = ("I calculate the average mileage of cars "
                  "\n"
                  "depending on the year of production and the state of the vehicle."
                  )

print(welcome_calc_1.title() + "\n\n\n" + welcome_calc_2.title())
print(".........." * 9)
print("\n")


def exit_start_restart():
    """ Function to exit the calculator or continue working in it. """
    data = None
    while data not in ("e", "q", "c", "n"):
        print("Exit the calc? Enter - E or Q.", "\n",
              "Continue to work with the calc? Enter - C or N.", sep=""
              )
        print()
        print("What have you decided? -", end=" ")
        data = input().lower()
        print()
        if data == "c" or data == "n":
            print("Excellent! Let's calculate the mileage...")
            print("\n")
        elif data == "e" or data == "q":
            exit()
        else:
            print("Incorrect answer!!!".upper(),
                  "(Enter only English letters!!!)".upper(), "\n",
                  "Enter for exit - \"E\" or \"Q\".".title(), "\n",
                  "Enter for continue - \"C\" or \"N\"".title(), "\n", sep=""
                  )
            print()
    return data


"""
    Excellent condition of the car (Average mileage 4970 mi or 8000 km / year)!
    Good condition of the car (Average mileage 9320 mi or 15000 km / year)!
    Average condition of the car (Average mileage 13670 mi or 22000 km / year)!
    Bad condition of the car (Average mileage of 18640 mi or 30000 km / year)!
"""

date_list = ["year", "month", "day"]
text_list = [
    "Mileage:",
    "Wow! Well, you invented the",
    "of manufacture of the car! Try again.",
    "An example of the correct spelling of the",
    ": 1995, 2010, 1895, etc...",
    ": 11, 9, 09 etc...",
    ": 3, 03, 21 etc.",
    "of manufacture of the car:"
]
excellent_condition = "Excellent condition of the car!"
good_condition = "Good condition of the car!"
average_condition = "Average condition of the car!"
bad_condition = "Bad condition of the car!"


class MileageCalculator:
    """ The function «mileage_calculator_mi» calculates the mileage of the car in miles. """

    @staticmethod
    def mileage_calc_km():
        """ The function «mileage_calculator_km» calculates the mileage of the car in kilometers. """
        while True:
            print("==========" * 7)
            print()
            year = input("Year of manufacture of the car (Example: 1989, 2005, 1975 etc...): ".upper())
            age_y = int(cur_year) - int(year)
            if not year.isnumeric():
                print()
                print(text_list[3], date_list[0] + text_list[4])
                print("\n\n")
            elif int(year) < 1000 or int(year) > int(cur_year):
                print()
                print(text_list[1], date_list[0], text_list[2])
                print("\n\n")
            elif 1000 < int(year) < int(cur_year):
                print("\n")
                print("Answer... ".upper() * 5)
                print()
                print(excellent_condition, text_list[0], age_y * 8000, "km.")
                print()
                print(good_condition, text_list[0], age_y * 15000, "km.")
                print()
                print(average_condition, text_list[0], age_y * 22000, "km.")
                print()
                print(bad_condition, text_list[0], age_y * 30000, "km.")
                print()
                print("==========" * 7)
                print("\n\n")
                break
            elif int(year) == int(cur_year):
                print()
                month = input("Month of manufacturing a car (Enter number from 1 to 12): ".upper())
                age_m = int(cur_month) - int(month)
                if not month.isnumeric():
                    print()
                    print(text_list[3], date_list[1] + text_list[5])
                    print("\n\n")
                elif int(month) < 1 or int(month) > int(cur_month):
                    print()
                    print(text_list[1], date_list[1], text_list[2])
                    print("\n\n")
                elif 0 < int(month) < int(cur_month):
                    print("\n")
                    print("Answer... ".upper() * 5)
                    print()
                    print(excellent_condition, text_list[0], age_m * 666, "km.")
                    print()
                    print(good_condition, text_list[0], age_m * 1250, "km.")
                    print()
                    print(average_condition, text_list[0], age_m * 1833, "km.")
                    print()
                    print(bad_condition, text_list[0], age_m * 2500, "km.")
                    print()
                    print("==========" * 7)
                    print("\n\n")
                    break
                elif int(month) == int(cur_month):
                    print()
                    day = input("Day of manufacturing a car (Enter number from 1 to 31): ".upper())
                    age_d = int(cur_day) - int(day)
                    if not day.isnumeric():
                        print()
                        print(text_list[3], date_list[2] + text_list[6])
                        print("\n\n")
                    elif int(day) < 1 or int(day) > int(cur_day):
                        print()
                        print(text_list[1], date_list[2], text_list[2])
                        print("\n\n")
                    elif 0 < int(day) < int(cur_day):
                        print("\n")
                        print("Answer... ".upper() * 5)
                        print()
                        print(excellent_condition, text_list[0], age_d * 22, "km.")
                        print()
                        print(good_condition, text_list[0], age_d * 42, "km.")
                        print()
                        print(average_condition, text_list[0], age_d * 61, "km.")
                        print()
                        print(bad_condition, text_list[0], age_d * 83, "km.")
                        print()
                        print("==========" * 7)
                        print("\n\n")
                        break
                    elif int(day) == int(cur_day):
                        print("\n")
                        print("Answer... ".upper() * 5)
                        print()
                        print("New Car! Mileage: 0 km.")
                        print()
                        print("==========" * 7)
                        print("\n\n")
                        break

    @staticmethod
    def mileage_calc_mi():
        """ The function «mileage_calculator_mi» calculates the mileage of the car in miles. """
        while True:
            print("==========" * 7)
            print()
            year = input("Year of manufacture of the car (Example: 1989, 2005, 1975 etc...): ".upper())
            age_y = int(cur_year) - int(year)
            if not year.isnumeric():
                print()
                print(text_list[3], date_list[0] + text_list[4])
                print("\n\n")
            elif int(year) < 1000 or int(year) > int(cur_year):
                print()
                print(text_list[1], date_list[0], text_list[2])
                print("\n\n")
            elif 1000 < int(year) < int(cur_year):
                print("\n")
                print("Answer... ".upper() * 5)
                print()
                print(excellent_condition, text_list[0], age_y * 4970, "mi.")
                print()
                print(good_condition, text_list[0], age_y * 9320, "mi.")
                print()
                print(average_condition, text_list[0], age_y * 13670, "mi.")
                print()
                print(bad_condition, text_list[0], age_y * 18640, "mi.")
                print()
                print("==========" * 7)
                print("\n\n")
                break
            elif int(year) == int(cur_year):
                print()
                month = input("Month of manufacturing a car (Enter number from 1 to 12): ".upper())
                age_m = int(cur_month) - int(month)
                if not month.isnumeric():
                    print()
                    print(text_list[3], date_list[1] + text_list[5])
                    print("\n\n")
                elif int(month) < 1 or int(month) > int(cur_month):
                    print()
                    print(text_list[1], date_list[1], text_list[2])
                    print("\n\n")
                elif 0 < int(month) < int(cur_month):
                    print("\n")
                    print("Answer... ".upper() * 5)
                    print()
                    print(excellent_condition, text_list[0], age_m * 414, "mi.")
                    print()
                    print(good_condition, text_list[0], age_m * 777, "mi.")
                    print()
                    print(average_condition, text_list[0], age_m * 1139, "mi.")
                    print()
                    print(bad_condition, text_list[0], age_m * 1553, "mi.")
                    print()
                    print("==========" * 7)
                    print("\n\n")
                    break
                elif int(month) == int(cur_month):
                    print()
                    day = input("Day of manufacturing a car (Enter number from 1 to 31): ".upper())
                    age_d = int(cur_day) - int(day)
                    if not day.isnumeric():
                        print()
                        print(text_list[3], date_list[2] + text_list[6])
                        print("\n\n")
                    elif int(day) < 1 or int(day) > int(cur_day):
                        print()
                        print(text_list[1], date_list[2], text_list[2])
                        print("\n\n")
                    elif 0 < int(day) < int(cur_day):
                        print("\n")
                        print("Answer... ".upper() * 5)
                        print()
                        print(excellent_condition, text_list[0], age_d * 14, "mi.")
                        print()
                        print(good_condition, text_list[0], age_d * 26, "mi.")
                        print()
                        print(average_condition, text_list[0], age_d * 38, "mi.")
                        print()
                        print(bad_condition, text_list[0], age_d * 52, "mi.")
                        print()
                        print("==========" * 7)
                        print("\n\n")
                        break
                    elif int(day) == int(cur_day):
                        print("\n")
                        print("Answer... ".upper() * 5)
                        print()
                        print("New Car! Mileage: 0 mi.")
                        print()
                        print("==========" * 7)
                        print("\n\n")
                        break


mc = MileageCalculator()


def mi_km():
    """ The function «Mi_Km» calculates the mileage of the car. """
    while True:
        print("The mileage of the car in miles? Enter - M.")
        print("The mileage of the car in kilometers? Enter - K.")
        print("Exit the calculator? Enter - E or Q.")
        print()
        data = input("What do you choose? - ")
        print()
        if data.lower() == "m":
            mc.mileage_calc_mi()
        elif data.lower() == "k":
            mc.mileage_calc_km()
        elif data.lower() == "e" or data.lower() == "q":
            exit()
        elif data.lower() != "e" or "q" or "k" or "m":
            print("Incorrect answer!!! Enter - \"M\" or \"K\" or \"E\" or \"Q\"".upper(),
                  "(Enter only English letters!!!)".upper())
            print("\n")
            continue


def main():
    while True:
        exit_start_restart()
        mi_km()


main()

input("Enter Please")
