__author__ = "Dmitrii Vialkov (nickname: icyLambda)"
__copyright__ = "Copyright 2019, The Dmitrii Vialkov Project"
__credits__ = ["Dmitrii Vialkov"]
__license__ = "GNU General Public License (GPLv3)"
__version__ = "2.0.0"
__maintainer__ = "Dmitrii Vialkov"
__email__ = "icyLambda@gmail.com"
__status__ = "Production"

print('The script will convert the temperature to the opposite format:')
print('\t(Celsius to Fahrenheit and Fahrenheit to Celsius).')
print()
print('Temperature sign:')
print('\tCelsius = C or c' + '\n' + '\tFahrenheit = F or f')
print()
print('Data entry format: \"integer-or-float_temperature-sign\"')
print()
print('Example: \"100_F\" or \"100_f\" or \"100.0_F\" or \"100.0_f\",',
      'also with a Celsius sign.')


def exit_start_restart():
    """ Function to exit or continue working. """
    data = None
    while data not in ("e", "q", "c", "n"):
        print("Exit? Enter - E or Q.", "\n",
              "Continue to work? Enter - C or N.", sep=""
              )
        print()
        print("What have you decided? -", end=" ")
        data = input().lower()
        print()
        if data == "c" or data == "n":
            print("Excellent! Let's go...")
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


def celsius_fahrenheit():
    try:
        t1, tag_1 = input('Temperature 1: ').split('_')
        t1 = float(t1)
        tag_1 = tag_1.lower()

        t2, tag_2 = input('Temperature 2: ').split('_')
        t2 = float(t2)
        tag_2 = tag_2.lower()

        print()
    except ValueError:
        print()
        print('Wrong data! Try again...')
        print()
        print('Data entry format: \"integer-or-float_temperature-sign\"')
        print()
        print('Example: \"100_F\" or \"100_f\" or \"100.0_F\" or \"100.0_f\",',
              'also with a Celsius sign.')
        print('\n')
    else:
        if tag_1 == 'f' and tag_2 == 'c':
            tc = (5 / 9) * (t1 - 32)
            tf = (9 / 5) * t2 + 32
            print('Celsius =', tc)
            print('Fahrenheit =', tf)
            print('\n')
        elif tag_1 == 'c' and tag_2 == 'f':
            tf = (9 / 5) * t1 + 32
            tc = (5 / 9) * (t2 - 32)
            print('Fahrenheit =', tf)
            print('Celsius =', tc)
            print('\n')
        elif tag_1 == 'c' and tag_2 == 'c':
            tf_1 = (9 / 5) * t1 + 32
            tf_2 = (9 / 5) * t2 + 32
            print('Fahrenheit 1 =', tf_1)
            print('Fahrenheit 2 =', tf_2)
            print('\n')
        elif tag_1 == 'f' and tag_2 == 'f':
            tc_1 = (5 / 9) * (t1 - 32)
            tc_2 = (5 / 9) * (t2 - 32)
            print('Celsius 1 =', tc_1)
            print('Celsius 2 =', tc_2)
            print('\n')


def main():
    while True:
        exit_start_restart()
        celsius_fahrenheit()


main()
